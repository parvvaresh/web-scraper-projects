from bs4 import BeautifulSoup
import os, fnmatch
import urllib.request, urllib.error, urllib.parse
from urllib.request import urlopen
import requests
import pandas as pd
import glob
import os


class load_pages:
    def __init__(self, start, finish):
        self.samples = {
            "politics": "https://www.farsnews.ir/politics?p=",
            "sports": "https://www.farsnews.ir/sports?p=",
            "social": "https://www.farsnews.ir/social?p=",
            "economy": "https://www.farsnews.ir/economy?p=",
            "culture": "https://www.farsnews.ir/culture?p=",
            "arts-media": "https://www.farsnews.ir/arts-media?p=",
        }
        self.start = start
        self.finish = finish
        self._generate_page()
        self._get_pages()
        print("all pages loaded !")

    def _generate_page(self):
        self.links_generated = dict()
        for name, url in self.samples.items():
            temp_generated = []
            for day in range(self.start, self.finish + 1):
                temp_generated.append(url + str(day))
            self.links_generated[name] = temp_generated

    def _get_pages(self):
        for name, urls in self.links_generated.items():
            print(f"start --- get page of {name} in farsnews")
            page = open(f"{name}_news.html", "a")
            for url in urls:
                response = urllib.request.urlopen(url)
                webContent = response.read().decode("UTF-8")
                page.write(webContent)
                page.close
            print(f"finish --- get page of {name} in farsnews")


class get_news:
    def __init__(self):
        self.files = os.path.join("*.html")
        self.files = glob.glob(self.files)
        self.urls = dict()
        self.df = pd.DataFrame(
            {"title": None, "text": None, "label": None, "date": None}, index=[0]
        )

        print("start  extraxt links")
        self._get_urls_news()
        print("finish  extraxt links")

        print("start  extraxt data")
        self.get_data()
        print("finish  extraxt data")

        print("save  all data ----- csv file -----")
        self.df.to_csv("farsnews.csv")
        for file in self.files:
            os.remove(file)

    def _get_urls_news(self):
        for file in self.files:
            self._extraxt_links(file)

    def _extraxt_links(self, file):
        links = []
        data = open(file, "r")
        soup = BeautifulSoup(data, "html.parser")
        for element in soup.find_all("a"):
            link = element.get("href")
            if ("1401" in link) or ("1402" in link):
                links.append("https://www.farsnews.ir/news/" + link)

        links = list(set(links))
        self.urls[file.split("_")[0]] = links

        print(f"all news for {file.split('_')[0]} category {len(links)}")

    def get_data(self):
        for label, urls in self.urls.items():
            print(f"    start get data {label}")
            for index, url in enumerate(urls):
                self._get_data(url, label)
            print(f"    finish get data {label}")
            print(f"save  {label} data ----- csv file -----")
            self.df.to_csv("farsnews.csv")

    def _get_data(self, link, label):
        reqs = requests.get(link)
        soup = BeautifulSoup(reqs.content, "html.parser")

        date = soup.find("div", "publish-time d-flex justify-content-center")
        if date != None:
            date = date.text
            date = date.lstrip()
            date = date.rstrip()
        else:
            date = None

        text = soup.find("div", "nt-body text-right mt-4")
        if text != None:
            text = text.text
        else:
            text = None

        title = soup.find("h1", "title mb-2 d-block text-justify")
        if title != None:
            title = title.text
        else:
            title = None

        temp_data = {"title": title, "text": text, "label": label, "date": date}
        self.df = self.df._append(temp_data, ignore_index=True)


start = int(input("What page should we start to get information from? "))
finish = int(input("What page should we go to for information?"))
lg = load_pages(start, finish)
gn = get_news()
