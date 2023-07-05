# Preinstalled packages
import requests # 2.24.0

# Default packages
import json
import time

# URL of our News API
base_url = "https://api.newscatcherapi.com/v2/search"

# Your API key
X_API_KEY = 'YibMPpKlVCKx_8TQnZi0Pj8A82sAby1Avaacu90DNEM'

# Define your desired parameters
params = {
    "q": "\"Elon Musk\"",
    "from": "13 days ago",
    "countries": "IN,GB",
    "page_size": 100,
    "page": 1
}

# Put your API key to headers in order to be authorized to perform a call
headers = {"x-api-key": X_API_KEY}


# Variable to store all found news articles
all_news_articles = {}

# Ensure that we start from page 1
params['page'] = 1

# Infinite loop which ends when all articles are extracted
while True:

    # Wait for 1 second between each call
    time.sleep(1)

    # GET Call
    response = requests.get(base_url, headers=headers, params=params)
    results = json.loads(response.text.encode())
    if response.status_code == 200:
        print(f'Done for page number => {params["page"]}/{results["total_pages"]}')


        # Storing all found articles
        if not all_news_articles:
            all_news_articles = results
        else:
            all_news_articles['articles'].extend(results['articles'])

        # Ensuring to cover all pages by incrementing "page" value at each iteration
        params['page'] += 1
        if params['page'] > results['total_pages']:
            print("All articles have been extracted")
            break
        else:
            print(f'Proceed extracting page number => {params["page"]}')
    else:
        print(results)
        print(f'ERROR: API call failed for page number => {params["page"]}')
        break

print(f'Number of extracted articles => {str(len(all_news_articles))}')
