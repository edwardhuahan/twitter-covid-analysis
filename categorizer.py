"""
DEC 10 2021

This script is used to categorize each tweet into a certain category by its contents.

"""
import pandas as pd
import csv

tweets_df = pd.read_csv('scraper-output/pd-test.csv')

map_topics = {'vaccine': {'vaccin', 'needle', 'vax', 'vaccina'}}
keywords = {'vaccine', 'needle', 'vax', 'vaccina'}
key_list = list(map_topics.keys())
val_list = list(map_topics.values())  # this is a list of sets


def check_word(wd: str) -> str:
    """
    Checks which category a word belongs to

    If word is in keyword then check which topic it's in and return the topic as str
    Else return _
    """
    # CHANGE THIS BY CONVERTING THE WORD TO STEM AND THEN CHECKING
    # EFFICIENCY BABY
    if wd in keywords:
        for tpc in map_topics:
            if wd in map_topics[tpc]:
                return tpc
    else:
        return '_'


for i in tweets_df.index:
    contents = tweets_df.loc[i, 'col2']  # column name should be 'contents'
    categories = []
    #  list of categories because we're going to append tweet to several csv files if needed
    for word in contents:
        topic = check_word(word)
        if topic != '_':
            categories.append(topic)
    for category in categories:
        csvFile = open('scraper-output/' + category + '.csv',
                       mode='a', newline='', encoding='utf8')
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow([tweets_df.loc[i, 'col1']])
