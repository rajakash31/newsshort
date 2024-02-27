from newsapi import NewsApiClient
from datetime import datetime
import pandas as pd

# Init
newsapi = NewsApiClient(api_key='4f7a2da18c2a441da4b0bb13f3e4cce5')

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='',
#                                           sources='abc-news',
#                                           category='business',
#                                           language='en',
#                                           country='US')
# /v2/top-headlines/sources
# sources = newsapi.get_sources()


# /v2/everything - extract all article in a specific time range
all_articles = newsapi.get_everything(q='',
                                      sources='abc-news',
                                      domains='abcnews.go.com',
                                      from_param='2024-02-05',
                                      to='2024-02-20',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)


articles = all_articles['articles']
df_articles = pd.json_normalize(articles)
print(df_articles.head(2))