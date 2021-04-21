from django.shortcuts import render
from django.views import View
import json


# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        with open("hypernews/news.json", "r") as json_file:
            articles = sorted(json.load(json_file), key=lambda i: i['created'], reverse=True)
            for article in articles:
                article["date"] = article.get("created")[0:10]

        return render(request, "home.html", context={"articles": articles})


class ArticleView(View):
    def get(self, request, post_id, *args, **kwargs):
        with open("hypernews/news.json", "r") as json_file:
            articles = json.load(json_file)
            for article in articles:
                art_id = article.get("link")
                if art_id == post_id:
                    title = article.get("title")
                    created = article.get("created")
                    text = article.get("text")
                    link = art_id

        context = {
            "link": link,
            "title": title,
            "created": created,
            "text": text,
        }

        return render(request, "article.html", context=context)


class CreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "create.html", context={})
