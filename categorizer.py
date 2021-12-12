"""
DEC 10 2021

This script is used to categorize each tweet into a certain category by its contents.

Requires csv file of tweets with a header named 'contents'
Outputs csv file in the following format: <date>, <score>
"""
import pandas as pd
import csv

tweets_df = pd.read_csv('scraper-output/pd-keyword-test.csv')

map_topics = {'vaccine': {'vaccine'}, 'mask': {'mask'}}
keywords = {'vaccine', 'mask'}
# key_list = list(map_topics.keys())
# val_list = list(map_topics.values())  # this is a list of sets


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
            if wd in map_topics[tpc]:  # this actually won't work unless you convert word to stem
                return tpc
    else:
        return '_'


for i in tweets_df.index:
    print(f'Current iteration:{i}')
    contents = tweets_df.loc[i, 'contents']  # column name should be 'contents'
    contents = contents.split(' ')  # because contents starts off as a string
    categories = []
    #  list of categories because we're going to append tweet to several csv files if needed
    print(f'Current Tweet Contents: {contents}')  # print test

    # checks each word in contents
    for word in contents:
        topic = check_word(word)
        print(f'Current word:{word} Topic of word:{topic}')  # print test
        if topic != '_':
            categories.append(topic)
    print(f'Categories:{categories}')  # print test

    # appends tweet to csv file of topic
    for category in categories:
        csvFile = open('scraper-output/' + category + '.csv',
                       mode='a', newline='', encoding='utf8')
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow([tweets_df.loc[i, 'contents']])  # check columns when using for reals
        #  in the actual implementation csvWriter will write [tweets_df.loc[i, 'date'], score]
        csvFile.close()
