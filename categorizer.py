"""
DEC 10 2021

This script is used to categorize each tweet into a certain category by its contents.

"""
import pandas as pd

tweets_df = pd.read_csv('scraper-output/pd-test.csv')

for i in tweets_df.index:
    print(tweets_df.loc[i, 'col2'])
