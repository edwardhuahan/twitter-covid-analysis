""" CSC110 Final Project

This file is Copyright (c) 2021 Edward Han, Zekun Liu, Arvin Gingoyon
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
    """ Return the emotional score in order of the tweets given using the VADER lexicon.
    The return type is a list of dictionaries with compound, neutral, positive and negative
    emotional scores which can be accessed using 'compound', 'neu', 'pos' or 'neg'

    >>> import datetime
    >>> example_tweet = Tweet(1, datetime.datetime(2021, 12, 1), 'vaccines are good')
    >>> analysis = analyze_sentiment([example_tweet])
    >>> analysis[0]['compound']
    0.4404

    """

    analyzer = SentimentIntensityAnalyzer()
    scores_so_far = []
    for msg in msgs:
        vs = analyzer.polarity_scores(msg.content)
        scores_so_far.append(vs)

    return scores_so_far


def clean_input(msgs: list[Tweet]) -> list[str]:
    """ Takes a list of strings and returns a new list of strings that converts all tweet contents
    into lowercase and also removes all punctuation. Removes hyperlinks and new lines.

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


def split_into_stems(msgs: list[str]) -> list[list[str]]:
    """ Takes a list of cleaned input and splits it into word stems.
    Also removes all stopwords, which are words typically ignored in linguistic analysis.

    >>> example_list = ['vaccines are good']
    >>> split_into_stems(example_list)
    [['vaccin', 'good']]

    """
    porter = PorterStemmer()

    stem_lists_so_far = []
    for msg in msgs:
        word_list = msg.split(' ')
        topic_list = [porter.stem(word) for word in word_list if word not in stopwords]
        stem_lists_so_far.append(topic_list)

    return stem_lists_so_far


def calculate_word_count(stems_list: list[list[str]]) -> dict[str, int]:
    """ For a given list of list of stems, return a dictionary with each stem as a key
    and how many times a stem was counted as the value.

    >>> example_list = [['test', 'one', 'two', 'three'], ['three', 'test']]
    >>> count = calculate_word_count(example_list)
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


def calculate_word_emotion(scores: list[dict[str, int]], roots: list[list[str]]) -> dict[str, float]:
    """ Return each word with its average emotional score.

    >>> import reader
    >>> list_of_tweets = reader.read_tweet_data('scraper-output/scrapes.csv')
    >>> scores = analyze_sentiment(list_of_tweets)
    >>> clean = clean_input(list_of_tweets)
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
