import requests
import json
from newscatcherapi import NewsCatcherApiClient


# # Worldnews API - test api with filter
# response = requests.get(url="https://api.worldnewsapi.com/search-news?api-key=36d231b0056346e7adf29dd6bbd8d89d&text=tesla")
# info = (response.json())
# #print(info)
# with open('learning_code/3. Intermediate projects/news.htm', 'w', encoding="utf-8") as f:
#     f.write(str(info))

# # Worldnews API - get news from usa, mentioning russia
# response = requests.get(url="https://api.worldnewsapi.com/search-news?api-key=36d231b0056346e7adf29dd6bbd8d89d&source-countries=us&entities=LOC:Russia ")
# with open('learning_code/3. Intermediate projects/russia.htm', 'w', encoding="utf-8") as f:
#     f.write(str(response.json()))

# # Worldnews API - select very negative sentiment (usa mentioning russia)
# requests.get(url="https://api.worldnewsapi.com/search-news?api-key=36d231b0056346e7adf29dd6bbd8d89d&source-countries=us&entities=LOC:Russia&min-sentiment=-1max-sentiment=-0.6")



# # newscatcher API
# API_KEY = 'YibMPpKlVCKx_8TQnZi0Pj8A82sAby1Avaacu90DNEM'
# newscatcherapi = NewsCatcherApiClient(x_api_key=API_KEY)
# news_articles = newscatcherapi.get_search(q="Ukraine", countries='US,GB')
# #print(news_articles)
# with open('learning_code/3. Intermediate projects/newscatcher.htm', 'w', encoding="utf-8") as f:
#     f.write(str(news_articles))


#news API
url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2023-07-04&'
       'sortBy=popularity&'
       'apiKey=e1461d8b08d54d9bb539c00fb844a056')

response = requests.get(url)
results = json.loads(response.text.encode())
#print(results)
with open('learning_code/3. Intermediate projects/newsapi.json', 'w', encoding="utf-8") as f:
    f.write(str(results))