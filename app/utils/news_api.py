import requests


class NewsAPI:
    def __init__(self, api_key):
        self.base_url = "https://newsapi.org/v2/"
        self.api_key = api_key

    # def get_news_from_source(self, source):
    #     data = requests.get(self.base_url)

    def get_top_headlines(self):
        slack_text = ""
        url = self.base_url + "top-headlines?country=us" + "&apikey=" + self.api_key
        data = requests.get(url)
        if data.status_code == 200:
            news_json = data.json()
            articles = news_json["articles"]
            for article in articles:
                author = article['author']
                title = article['title']
                description = article['description']
                url = article['url']
                image_url = article["urlToImage"]
                published_at = article["publishedAt"]

                slack_text += self.get_slack_text(author, title, description, url, image_url, published_at) + "\n"
            return slack_text
        else:
            return "An error occurred"

    @staticmethod
    def get_slack_text(author, title, description, url, image_url, published_at):
        return "*Author:* {} \n " \
               "*Title:* {} \n " \
               "*Description:* {} \n" \
               "*Date:* {} \n" \
               "{} \n" \
               "{} \n".format(author, title, description, published_at, image_url, url)
