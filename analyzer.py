""" CSC110 Final Project

This file is Copyright (c) 2021 Edward Han, Zekun Liu, Arvin Gingoyon
"""
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer
from tweet import Tweet

STOPWORDS = ['', "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
             "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself",
             "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
             "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
             "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has",
             "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if",
             "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about",
             "against", "between", "into", "through", "during", "before", "after", "above",
             "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
             "again", "further", "then", "once", "here", "there", "when", "where", "why", "how",
             "all", "any", "both", "each", "few", "more", "most", "other", "some", "such",
             "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s",
             "t", "can", "will", "just", "don", "should", "now"]

MAP_TOPICS = {'conspiracy': {'hoax', 'lie', 'conspiraci', 'trump', 'fake', 'chip'},
              'masks': {'antimask', 'mrna', 'n95', 'kn94', 'facemask', 'mask', 'cloth'},
              'quarantine': {'quarantin', 'lockdown', 'shutdown'},
              'vaccine': {'antivax', 'mrna', 'vaccin', 'needl', 'vax', 'booster', 'unvax'},
              'covid': {'covid-19', 'covid19', 'covid', 'viru', 'pandem', 'epidem'}}
TOPIC_KEYWORDS = {'hoax', 'lie', 'conspiraci', 'trump', 'fake', 'chip', 'antimask',
                  'mrna', 'n95', 'kn94', 'facemask', 'mask', 'cloth', 'quarantin',
                  'lockdown', 'shutdown', 'antivax', 'mrna', 'vaccin', 'needl',
                  'vax', 'booster', 'covid-19', 'covid19', 'covid', 'viru', 'pandem',
                  'epidem'}


def analyze_tweets(tweets: list[Tweet]) -> list[tuple[Tweet, dict[str, float], set[str]]]:
    """ Given a list of tweets, return a list containing tuples with the tweets and their
    sentiment scores and category.

    >>> import datetime
    >>> example = [Tweet(1, datetime.datetime(2021, 12, 1), 'vaccines are good')]
    >>> example_analysis = analyze_tweets(example)
    >>> example_analysis[0][0].content
    'vaccines are good'
    >>> example_analysis[0][1]
    {'neg': 0.0, 'neu': 0.408, 'pos': 0.592, 'compound': 0.4404}
    >>> example_analysis[0][2]
    {'vaccine'}
    """

    sentiment_score = analyze_sentiment(tweets)
    clean = clean_input(tweets)
    stems = split_into_stems(clean)

    # Analyze each sentence
    analyzed_tweets_so_far = []
    for i in range(len(tweets)):
        categories = calc_sentence_topic(stems[i])
        analyzed_tweets_so_far.append((tweets[i], sentiment_score[i], categories))

    return analyzed_tweets_so_far


def analyze_sentiment(msgs: list[Tweet]) -> list[dict[str, float]]:
    """ Return the emotional score in order of the tweets given using the VADER lexicon.
    The return type is a list of dictionaries with compound, neutral, positive and negative
    emotional scores which can be accessed using 'compound', 'neu', 'pos' or 'neg'

    Preconditions:
        - all(len(msg.content) > 0 for msg in msgs)
        - len(msgs) > 0

    >>> import datetime
    >>> example_pos_tweet = Tweet(1, datetime.datetime(2021, 12, 1), 'vaccines are good')
    >>> analysis = analyze_sentiment([example_pos_tweet])
    >>> analysis[0]['compound']
    0.4404

    >>> example_neg_tweet = Tweet(1, datetime.datetime(2021, 12, 1), 'i hate vaccines')
    >>> analysis = analyze_sentiment([example_neg_tweet])
    >>> analysis[0]['compound']
    -0.5719

    """

    analyzer = SentimentIntensityAnalyzer()
    scores_so_far = []
    for msg in msgs:
        vs = analyzer.polarity_scores(msg.content)
        scores_so_far.append(vs)

    return scores_so_far


def calc_word_emotions(scores: list[dict[str, float]], roots: list[list[str]]) -> dict[str, float]:
    """ Return each word with its average emotional score,
    given a list of a list of stems and a list of sentiment dictionaries.

    >>> import datetime
    >>> list_of_tweets = [Tweet(1, datetime.datetime(2021, 12, 1), 'vaccines are good')]
    >>> scores = analyze_sentiment(list_of_tweets)
    >>> clean = clean_input(list_of_tweets)
    >>> roots = split_into_stems(clean)
    >>> emotions = calc_word_emotions(scores, roots)
    >>> emotions['vaccin']
    0.4404
    """

    dict_so_far = {}
    count_so_far = calc_word_count(roots)

    for i in range(len(scores)):
        # Get the emotional score of a sentence and add it to the sum
        # for every root found in the sentence
        stems = roots[i]
        score = scores[i]

        for stem in stems:
            sum_topic_words(stem, dict_so_far, score)

    for root in dict_so_far:
        emotional_score = dict_so_far[root] / count_so_far[root]
        dict_so_far[root] = round(emotional_score, 5)

    return dict_so_far


def sum_topic_words(stem: str, sum_dict: dict[str, float], score: dict[str, float]) -> None:
    """ Checks if a word is a topic keyword. If so, add the sum of its emotional score
    to the sum dictionary.

    >>> stem = 'vaccin'
    >>> sum_dict = {}
    >>> score = {'compound': -1.0}
    >>> sum_topic_words(stem, sum_dict, score)
    >>> sum_dict
    {'vaccin': -1.0}
    """
    if stem in TOPIC_KEYWORDS:
        if stem not in sum_dict:
            sum_dict[stem] = 0
        sum_dict[stem] = sum_dict[stem] + score['compound']


def calc_word_count(stems_list: list[list[str]]) -> dict[str, int]:
    """ For a given list of list of stems, return a dictionary with each stem as a key
    and how many times a stem was counted as the value.

    >>> example_list = [['test', 'one', 'two', 'three'], ['three', 'test']]
    >>> count = calc_word_count(example_list)
    >>> count == {'test': 2, 'one': 1, 'two': 1, 'three': 2}
    True
    """

    count_so_far = {}

    for stems in stems_list:
        for stem in stems:
            if stem not in count_so_far:
                count_so_far[stem] = 0
            count_so_far[stem] = count_so_far[stem] + 1

    return count_so_far


def calc_sentence_topic(sentence: list[str]) -> set[str]:
    """Checks which category a sentence belongs to
    If word is in keyword then check which topic it's in and return the topic as str
    Else return _

    Preconditions:
        - all(len(msg) > 0 for msg in sentence)
        - len(sentence) > 0

    >>> example_sentence = ['vaccines are a hoax']
    >>> example_stems = split_into_stems(example_sentence)
    >>> calc_sentence_topic(example_stems[0]) == {'conspiracy', 'vaccine'}
    True
    """

    category_so_far = set()
    for word in sentence:
        category = calc_word_topic(word)
        if category != '_':
            category_so_far.add(category)

    return category_so_far


def calc_word_topic(word: str) -> str:
    """Checks which category a word belongs to
    If word is in keyword then check which topic it's in and return the topic as str
    Else return _

    Preconditions:
        - len(word) > 0

    >>> calc_word_topic('vaccin')
    'vaccine'
    >>> calc_word_topic('test')
    '_'
    """

    if word in TOPIC_KEYWORDS:
        for tpc in MAP_TOPICS:
            if word in MAP_TOPICS[tpc]:  # this actually won't work unless you convert word to stem
                return tpc

    return '_'


def split_into_stems(msgs: list[str]) -> list[list[str]]:
    """ Takes a list of cleaned input and splits it into word stems.
    Also removes all stopwords, which are words typically ignored in linguistic analysis.

    Preconditions:
        - all(len(msg) > 0 for msg in msgs)
        - len(msgs) > 0

    >>> example_list = ['vaccines are good']
    >>> split_into_stems(example_list)
    [['vaccin', 'good']]
    """
    porter = PorterStemmer()

    stem_lists_so_far = []
    for msg in msgs:
        word_list = msg.split(' ')
        topic_list = [porter.stem(word) for word in word_list if word not in STOPWORDS]
        stem_lists_so_far.append(topic_list)

    return stem_lists_so_far


def clean_input(msgs: list[Tweet]) -> list[str]:
    """ Takes a list of strings and returns a new list of strings that converts all tweet contents
    into lowercase and also removes all punctuation. Removes hyperlinks and new lines.

    Preconditions:
        - all(len(msg.content) > 0 for msg in msgs)
        - len(msgs) > 0

    >>> import datetime
    >>> example_tweet = Tweet(1, datetime.datetime(2021, 12, 1), 'Vaccines, are good!??')
    >>> clean_input([example_tweet])
    ['vaccines are good']
    """

    output = []
    for msg in msgs:

        # Set to lowercase and remove all new lines for better processing.
        lower_msg = msg.content.lower()
        lower_msg = lower_msg.replace('\n', ' ')
        clean_msg = ''
        for word in lower_msg.split(' '):
            clean_word = ''

            # Ignore all word snippets that are hyperlinks or include the @ character
            if '@' not in word and 'http' not in word:
                # Only add characters that are not punctuation
                clean_word = ''.join(char for char in word if char not in string.punctuation)
                clean_word = clean_word + ' '

            clean_msg = clean_msg + clean_word

        output.append(clean_msg.strip())

    return output


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    python_ta.check_all(config={
        'extra-imports': ['string', 'nltk.sentiment.vader', 'nltk.stem', 'tweet'],
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
