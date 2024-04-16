import requests
from send_email import Send_email

api = "1650ea878dc64a3dbf02e703bd0380da"
url ="https://newsapi.org/v2/everything?q=tesla&" \
     "from=2024-03-16&sortBy=publishedAt&apiKey=1650ea878dc64a3dbf02e703bd0380da"
# make a request
request = requests.get(url)
# Get dictionary with data
content = request.json()

# Access the title and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + (article["title"]) + "\n" + (article["description"]) + 2*"\n"

body = body.encode("utf-8")
Send_email(message=body)

