import requests, json


class NewsAPI:
    def __init__(self, api_key):
        self.base_url = "https://newsapi.org/v2/"
        self.api_key = api_key

    def get_top_headlines(self):
        url = self.base_url + "top-headlines?country=us" + "&apikey=" + self.api_key
        data = requests.get(url)
        if data.status_code == 200:
            return self.get_slack_message_attachment(data.json())
        else:
            return "An error occurred"

    def get_sports_news(self):
        url = self.base_url + "top-headlines?country=us" + "&category=sports" + "&apikey=" + self.api_key
        data = requests.get(url)
        if data.status_code == 200:
            return self.get_slack_message_attachment(data.json())
        else:
            return "An error occurred"

    def get_slack_message_attachment(self, news_json):
        slack_msg = []
        articles = news_json["articles"]
        for article in articles:
            author = article['author']
            title = article['title']
            description = article['description']
            url = article['url']
            image_url = article["urlToImage"]
            published_at = article["publishedAt"]
            source = article['source']

            slack_msg.append(self.get_slack_text(author, title, description, url, image_url, published_at, source))
        return slack_msg

    @staticmethod
    def get_slack_text(author, title, description, url, image_url, published_at, source):
        return {
            "fallback": title,
            "color": "#2eb886",
            "pretext": title,
            "author_name": author,
            "title": title,
            "title_link": url,
            "text": description,
            "fields": [
                {
                    "title": "Source",
                    "value": source['name'],
                    "short": False
                }
            ],
            "image_url": image_url,
            "footer": "Lit Bot",
            "ts": 123456789
        }
