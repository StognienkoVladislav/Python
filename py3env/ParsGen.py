#!/usr/bin/env python3

#Импортируем нужные нам библиотеки для проекта
import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    #Вытягиваем html
    r = requests.get(url)
    return r.text

#def get_total_pages(html):
#    soup = BeautifulSoup(html, 'lxml')
#
#    pages = soup.find("div", class_="pagination-pages").find_all('a', class_ = "pagination-page")[-1].get("href")
#    total_pages = pages.split("=")[1].split("&")[0]

#    return int(total_pages)


def write_csv(data):
    with open('imdb.csv', 'a') as f:
        writer = csv.writer(f)
        #Записываем в csv относительно наших ключей
        writer.writerow((data['title'],
                         data['certificate'],
                         data['runtime'],
                         data['genre'],
                         data['imdb'],
                         data['metascore'],
                         data['director'],
                         #data['description'],
                         data['stars'],
                         data['votes'],
                         data['gross']))


def get_page_data(html):
    #Библиотека для парсинга
    soup = BeautifulSoup(html, "lxml")

    ads = soup.find("div", class_ = 'lister-list').find_all('div', class_ = 'lister-item')
    #Парсим по кускам, потом ,в конце for, будем собирать
    for ad in ads:

        #Title of movie
        try:
            title = ad.find("div", class_ = "lister-item-content").find("h3", class_ = 'lister-item-header').find("a").text.strip()

        except:
            title = ""


        #Certificate
        try:
            certificate = ad.find("div", class_ = "lister-item-content").find_all("p", class_ = "text-muted")[0].find("span", class_="certificate").text.strip()

        except:
            certificate = ""

        #Runtime
        try:
            runtime = ad.find("div", class_ = "lister-item-content").find_all("p", class_ = "text-muted")[0].find("span", class_="runtime").text.strip()

        except:
            runtime = ""


        #Genre
        try:
            genre =ad.find("div", class_ = "lister-item-content").find_all("p", class_ = "text-muted")[0].find("span", class_="genre").text.strip()

        except:
            genre = ""


        ##Rating
        #IMDB
        try:
            imdb = ad.find("div", class_ = "lister-item-content").find("div", class_ = "ratings-bar").find("div", class_ = "ratings-imdb-rating").find("strong").text.strip()

        except:
            imdb = 0


        #Metascore
        try:
            metascore = ad.find("div", class_ = "lister-item-content").find("div", class_ = "ratings-bar").find("div", class_ = "ratings-metascore").find("span").text.strip()

        except:
            metascore = 0


        #Description(Описание фильма, вытянуть то конечно можно, но для анализа нам не нужно)
        #try:
        #    descr = ad.find("div", class_ = "lister-item-content").find_all("p", class_ = "text-muted")[1].text.strip()

        #except:
        #    descr = ""

        ##Director&Stars
        #Director
        try:
            director = ad.find("div", class_ = "lister-item-content").find_all("p")[2].find_all("a")[0].text.strip()
        except:
            director = ""


        #Stars:
        stars = ""
        for i in range(ad.find("div", class_ = "lister-item-content").find_all("p")[2].find_all("a").__len__()-2):
            try:
                stars += ad.find("div", class_ = "lister-item-content").find_all("p")[2].find_all("a")[i+1].text.strip() + ", "#Захавать несколько
            except:
                stars = ""


        ##Votes&Gross
        #Votes
        try:
            votes = ad.find("div", class_ = "lister-item-content").find("p", class_ = "sort-num_votes-visible").find_all("span", attrs = {'name' : 'nv'})[0].text.strip()

        except:
            votes = 0


        #Gross:
        try:
            gross = ad.find("div", class_ = "lister-item-content").find("p", class_ = "sort-num_votes-visible").find_all("span", attrs = {'name' : 'nv'})[1].text.strip()
        except:
            gross = 0

        #Записываем в словарь и передаем его дальне на запись в csv

        data = {'title'      : title,
                'certificate': certificate,
                'runtime'    : runtime,
                'genre'      : genre,
                'imdb' : imdb,
                'metascore'  : metascore,
                #'description': descr,
                'director'   : director,
                'stars'      : stars,
                'votes'      : votes,
                'gross'      : gross}

        write_csv(data)







def main():
    #Урл из которого мы парсим всю нужную нам информацию
    url = "http://www.imdb.com/search/title?count=100&groups=oscar_best_picture_winners&sort=year,desc&ref_=nv_ch_osc_2"

    #total_pages = get_total_pages(get_html(url))

    #Парс всех страниц total_pages(если бы было больше страниц)
    html = get_html(url)
    get_page_data(html)


if __name__ == '__main__':
    #Просто вызов main()
    main()
