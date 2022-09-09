# Twitter Sentiment Analysis Tool
Since the start of the pandemic back in March 2020, discussion surrounding COVID-19 has given rise to false information online. One of the main sources of this is social media, which gives people an easily accessible platform to spread misinformation. Twitter stands out as one of the major social media applications that has contributed to this issue. Like other social media platforms, users are able to share media, photos, articles, and messages in the form of tweets. With tweets, users have the freedom to share any piece of information they desire, allowing information to spread rapidly across a large amount of people.

On Twitter, sensationalist discussions surrounding the virus contribute to fits of hysteria in response to the pandemic. This was first seen during the toilet paper and hand sanitizer shortage at the beginning of the pandemic, a prime example of individuals losing their rationality due to misinformation.

Detecting and quickly identifying sensationalism is critical in ensuring Twitter users, and those who use social media in general, are able to discern the truth from various sources. If the population is more educated on legitimate information surrounding the virus, the process of tackling the pandemic would become more efficient as a whole.

For social media analysis, it’s important to understand what sources are trustworthy and which ones are not. For twitter and social media especially, it can be incredibly useful to have an understanding of what themes/topics that are more or less trustworthy, unbiased and otherwise free of manipulation. This will help researchers deploy more or less filtering techniques to gather better data in the future.

For this project, we aim to answer the questions: Which aspects/topics/themes around COVID have been subject to the most sensationalism and fear mongering? Are there any observable patterns in fear mongering associated with major events during the pandemic?

# Dataset Description
The dataset we used was collected using a module that we developed ourselves that is dependent on snscraper

# Computations
For the aggregation and transformation of data, we will create a Twitter Scraper to create a collection of tweets, filtering out non-covid related tweets, based on keywords found in the entire tweet or in the hashtags. We find that snscrape or Twitter APIs are appropriate for this kind of aggregation, and more than adequate for our purposes to generate a CSV file.

The scraper collects the total number of tweets to bescraped and a start date in the form YYYY/MM/DD as inputs. Then, it collects the current date using datetime.now and makes the start date a datetime object using strpdate(). Then, the it find the time delta in days between the two dates and converts that value to an integer to perform an integer division to figure out how many tweets are to be scraped per day.

Following this, the program opens a csv file named scrapes, or will create a new file with that name if it doesn't exist and loads it with the correct header.

Following this, the program goes into a while loop in which the start date is the loop variable and is increased every iteration using timedelta(), the loop stops once the start date is the current date. Within the loop, it creates 2 string dates using strftime() named dt (date) and dtn (date next) to create a search term in an f string expression that constrains snscraper to only pick up tweets from that day. Following this, an enumerate loop begins which passes the search term into snscraper.TwitterSearchScraper() to collect the tweets, the loop breaks once the loop runs for a number of times dictated by the number of tweets per day as calculated earlier. Each tweet is appended into the csv file opened earlier.

Once all loops finishes running, the module closes the csv file.

# Install requirements

https://www.nltk.org/data.html

install vader_lexicon using this package manager 
