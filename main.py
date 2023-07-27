import requests

api_key = "8e4d4260180540b89dc8626a17358572"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-06-27&sortBy=publishedAt&apiKey=" \
      "8e4d4260180540b89dc8626a17358572"

requests = requests.get(url)
content = requests.json()

for article in content["articles"]:
      print(article["title"])
      print(article["description"])

