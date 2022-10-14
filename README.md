# DataScience-in-Social-Media
To understand the impact of COVID-19, it is important to collect data. Data helps to
identifying the most vulnerable demographic group and to recognize which treatments are
effective and which are not. Therefore, collecting data is a vital process to understand
further possibilities regarding COVID-19 (R. Tang,2021). In this study we only consider the
citizen perspective of German people. (Lafaro 2020).

The COVID-19 disease has attracted the attention on social media. People start to inform
and exchange information on these platforms when an event happens. Twitter provides a
great possibility to track the dynamics of the Coronavirus (Aguilar-Gallegos et al. 2020)

The aim of the study is to build a good dataset to represent the Querdenker in the German
population. We focus on the Pro-Querdenker as representation of the freedom restriction
protests to achieve our dataset. The Querdenker protests suggest that there is a link
between the government measures and Querdenker protests, that means the Querdenker
protests results from the government measures. From this connection a research question
can be derived: Is there a relationship between the announcement of Corona measures by
the German government (freedom reduction) and the Querdenker protests from March
2020 until March 2021

# Approach
In our approach, we have used an open-source Python Library named Twint for gathering
data from selected Twitter accounts and we also have used nest_asyncio for loop patching.
Twint is an advance tool for Twitter scrapping and this allows data scraping from Tweeter
accounts and profiles in relatively easier way. Twint utilizes Twitter’s search operators to let
us scrape Tweets from specific users, scrape Tweets relating to certain topics, hashtags &
trends, or sort out sensitive information from Tweets.

# Algorithm
STEP 1: Import necessary packages (twint, nest_asyncio etc.) <br>
STEP 1.1: Search data with respect to the pro-Querdenken usernames and make a
loop so that we can collect the data from all the usernames in one shot <br>
STEP 1.2: From our collected hashtags, define the searchlist<br>
STEP 1.3: Select the language in which it will collect data <br>
STEP 1.4: Mention the timeline and the format of storing the data (.csv, .xlsx etc.) <br>
STEP 2: Classification of Data <br>
STEP 2.1: Based on Features <br>
STEP 2.2: Based on Pro-Querdenken twitter accounts <br>
STEP 3: Data Cleaning <br>
STEP 3.1: Removal of punctuations <br>
STEP 3.2: Removal of retweets ‘RT’ <br>
STEP 3.3: Removal of stop words <br>
STEP 3.4: Removal of tweet repetitions <br>
STEP 3.5: Removal of non-related tweets and based on that, further classification<br>
STEP 3.6: Identify Hashtags which are associated with anti-Querdenker (e. g.
#covidiots,…) <br>
STEP 3.7: Create new columns which count the words supportive of pro-Querdenker
(positive words) and words which are not supportive of pro-Querdenker (negative
words) <br>
STEP 3.8: Manually delete Tweets which are not supportive of Querdenken and
couldn‘t be identified through 3.6 and 3.7. <br>
STEP 4: Data Pre-processing<br>
STEP 4.1: Simplification of the data<br>
STEP 4.2: Extract fact-checkable tweets<br>
STEP 4.3: Inclusion of new columns (where required)<br>
STEP 4.4: Inclusion of class and ranks to prioritize which tweets are relevant to our
research question<br>
STEP 4.5: Ranking of tweets based on: (a) Numbers and Quantity, (b) Location, (c)
Organiation Names, (d) Resources Present, (e) Contact Information<br>

# Twint
Data Collection Using Twint <br>
We used an open-source Python Library named Twint for gathering data from selected
Twitter accounts. Twint is an advance tool for Twitter scrapping. It allows data scraping
from Tweeter accounts and profiles. Twint utilizes Twitter’s search operators to allow us
for scraping Tweets from specific users, scrape Tweets referring to certain topics,
hashtags & trends, or sort out sensitive information from Tweets like e-mail and phone
numbers.
