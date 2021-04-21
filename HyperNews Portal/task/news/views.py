from django.shortcuts import render, redirect
from django.views import View
import json
from datetime import datetime
import random


with open("hypernews/news.json", "r") as json_file:
    articles = sorted(json.load(json_file), key=lambda i: i['created'], reverse=True)
    links = []
    for article in articles:
        links.append(article.get("link"))


class HomeView(View):
    def get(self, request, *args, **kwargs):
        for article in articles:
            article["date"] = article.get("created")[0:10]
        q = request.GET.get("q", None)
        if q:
            searched_articles = [article for article in articles if q in article.get("title")]
        else:
            searched_articles = articles
        return render(request, "home.html", context={"articles": searched_articles})


class ArticleView(View):
    def get(self, request, post_id, *args, **kwargs):
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

    def post(self, request, *args, **kwargs):
        global articles, links

        title = request.POST.get("title")
        text = request.POST.get("text")
        created = str(datetime.now())

        # generate random number for link, making sure it doesn't match any existing link
        link_found = False
        while not link_found:
            link = random.randint(1, 2000)
            if link not in links:
                link_found = True

        articles.append({
            "created": created,
            "text": text,
            "title": title,
            "link": link
        })

        articles = sorted(articles, key=lambda i: i['created'], reverse=True)

        return redirect('/news')
