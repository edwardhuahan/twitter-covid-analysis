""" CSC110 Final Project

This file is Copyright (c) 2021 Edward Han, Zekun Liu, Arvin Gingoyon
"""

import plotly.graph_objects as go


def reverse_dict(original: dict[any, any]) -> dict[any, any]:
    """ Returns dictionary that is the original but with the key and value
    swapped

    >>> a = {'a': 1, 'c': 4, 'b': 2}
    >>> reverse_dict(a)
    {1: 'a', 4: 'c', 2: 'b'}
    """
    return {original[key]: key for key in original}


def find_top_10(emotions: dict[str, float], smallest: bool) -> dict[str, float]:
    """ Given a dictionary, returns a dictionary with the top 10 most
    positive or negative words (specified by 'smallest' argument) in that dictionary"""

    sorted_emotions = sorted(reverse_dict(emotions), reverse=True)  # sorts keys in descending order
    if smallest:
        sorted_emotions = sorted(reverse_dict(emotions))  # sorts keys in ascending order

    # sorted_emotions is a list
    top_10_emotions_so_far = {}

    for sent_score_key in sorted_emotions:
        top_10_emotions_so_far[reverse_dict(emotions)[sent_score_key]] = sent_score_key
        if len(top_10_emotions_so_far) == 10:
            return top_10_emotions_so_far
    return top_10_emotions_so_far


def graph_2(emotional_words: dict[str, float]) -> None:
    """ Creates relative bar graph of most emotional words to their average emotional score"""

    most_negative = find_top_10(emotional_words, True)
    neg_key = []
    for word in most_negative:
        neg_key.append(word)

    most_positive = find_top_10(emotional_words, False)
    pos_key = []
    for word in most_positive:
        pos_key.append(word)

    x = []
    y = []

    for i in range(10):
        x.append(pos_key[i])
        x.append(neg_key[i])
        y.append(most_positive[pos_key[i]])
        y.append(most_negative[neg_key[i]])

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=x, y=y))

    fig2.update_layout(title_text='Top 10 Most Emotional Words')
    fig2.show()
    # fig2.write_html('graph2.html')


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    python_ta.check_all(config={
        'extra-imports': ['plotly.graph_objects', 'nltk'],
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
