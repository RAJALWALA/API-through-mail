import requests

api = "1650ea878dc64a3dbf02e703bd0380da"
url ="https://newsapi.org/v2/everything?q=tesla&" \
     "from=2024-03-16&sortBy=publishedAt&apiKey=1650ea878dc64a3dbf02e703bd0380da"
# make a request
request = requests.get(url)
# Get dictionary with data
content = request.json()

# Access the title & description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
