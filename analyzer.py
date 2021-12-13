""" CSC110 Final Project

Edward Han, Zekun Liu, Arvin Gingoyon
"""
import string
from tweet import Tweet
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer

stopwords = ['', "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
             "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
             "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
             "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
             "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
             "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
             "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
             "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
             "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
             "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


def analyze_sentiment(msgs: list[Tweet]) -> list[dict[str, float]]:
    """ Return the compound normalized score in order of the tweets given"""

    analyzer = SentimentIntensityAnalyzer()
    scores_so_far = []
    for msg in msgs:
        vs = analyzer.polarity_scores(msg.content)
        scores_so_far.append(vs)

    return scores_so_far


def clean_input(msgs: list[Tweet]) -> list[str]:
    """ Takes a list of strings and converts it into lowercase and also removes
        all punctuation
    """

    output = []
    for msg in msgs:

        lower_msg = msg.content.lower()
        lower_msg = lower_msg.replace('\n', ' ')
        clean_msg = ''
        for word in lower_msg.split(' '):
            clean_word = ''
            if '@' not in word and 'http' not in word:
                clean_word = ''.join(char for char in word if char not in string.punctuation)
                clean_word = clean_word + ' '

            clean_msg = clean_msg + clean_word

        output.append(clean_msg)

    return output


def split_into_stems(msgs: list[str]) -> list[list[str]]:
    """ Takes a list of cleaned input and splits it into word stems.
        Also removes all stopwords
    """
    porter = PorterStemmer()

    stem_lists_so_far = []
    for msg in msgs:
        word_list = msg.split(' ')
        topic_list = [porter.stem(word) for word in word_list if word not in stopwords]
        stem_lists_so_far.append(topic_list)

    return stem_lists_so_far


def calculate_word_count(stems_list: list[list[str]]) -> dict[str, int]:
    """ Return how many times a certain stem ending occurs
    """

    count_so_far = {}

    for stems in stems_list:
        for stem in stems:
            if stem not in count_so_far:
                count_so_far[stem] = 0
            count_so_far[stem] = count_so_far[stem] + 1

    return count_so_far


def calculate_word_emotion(scores: list[dict[str, int]], roots: list[list[str]]) -> dict[str, float]:
    """ Return each word with its average emotional score

        >>> import reader
        >>> a = reader.read_tweet_data('scraper-output/scrapes.csv')
        >>> scores = analyze_sentiment(a)
        >>> clean = clean_input(a)
        >>> roots = split_into_stems(clean)
        >>> calculate_word_emotion(scores, roots)
    """

    dict_so_far = {}
    count_so_far = calculate_word_count(roots)

    for i in range(len(scores)):
        # Get the emotional score of a sentence and add it to the sum for every root found in the sentence
        stems = roots[i]
        score = scores[i]
        for stem in stems:
            if stem not in dict_so_far:
                dict_so_far[stem] = 0
            dict_so_far[stem] = dict_so_far[stem] + score['compound']

    for root in dict_so_far:
        dict_so_far[root] = dict_so_far[root] / count_so_far[root]

    return dict_so_far
