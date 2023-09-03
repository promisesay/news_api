import requests
import send_email


topic = "tesla"
api_key = "8e4d4260180540b89dc8626a17358572"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=2023-07-30&sortBy=publishedAt&" \
      "apiKey=8e4d4260180540b89dc8626a17358572"

# get the api from the address
requests = requests.get(url)

# make a jason dict
content = requests.json()

message = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        message = "Subject: today's news"\
                + "\n" + message + "\n" \
                + article["title"] + "\n" + article["description"] +\
                  "\n" + "more in the link:"\
                  + article["url"] + 2*"\n"

message = message.encode("utf-8")
send_email.send_email(message)
