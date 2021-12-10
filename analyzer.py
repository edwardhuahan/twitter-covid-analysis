""" CSC110 Final Project

Edward Han, Zekun Liu, Arvin Gingoyon
"""
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer

stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
             "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
             "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
             "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
             "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
             "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
             "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
             "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
             "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
             "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


def analyze_sentiment(msgs: list[str]) -> list[int]:
    """ Return the compound normalized score in order of the tweets given"""

    analyzer = SentimentIntensityAnalyzer()
    scores_so_far = []
    for msg in msgs:
        vs = analyzer.polarity_scores(msg)
        scores_so_far.append(vs['compound'])

    return scores_so_far


def clean_input(msgs: list[str]) -> list[str]:
    """ Takes a list of strings and converts it into lowercase and also removes
        all punctuation
    """

    output = []
    for msg in msgs:
        lower_str = msg.lower()
        clean_str = ''.join([char for char in lower_str
                             if char not in string.punctuation])

        output.append(clean_str)

    return output


def split_into_stems(msgs: list[str]) -> list[set[str]]:
    """ Takes a list of cleaned input and splits it into word stems.
        Also removes all stopwords
    """
    porter = PorterStemmer()

    stem_lists_so_far = []
    for msg in msgs:
        word_list = msg.split(' ')
        topic_list = {porter.stem(word) for word in word_list if word not in stopwords}
        stem_lists_so_far.append(topic_list)

    return stem_lists_so_far
