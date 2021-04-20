from django.shortcuts import render
from django.views import View
import json

# Create your views here.
class NewsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html", context={})

class ArticleView(View):
    def get(self, request, post_id, *args, **kwargs):

        # pass in link as parameter and only pull context for that link?
        with open("hypernews/news.json", "r") as json_file:
            articles = json.load(json_file)
            for article in articles:
                link = article.get("link")
                if link == post_id:
                    title = article.get("title")
                    created = article.get("created")
                    text = article.get("text")

        context = {
            "link": link,
            "title": title,
            "created": created,
            "text": text,
        }

        return render(request, "article.html", context= context)
