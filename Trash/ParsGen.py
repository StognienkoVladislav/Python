#!/usr/bin/env python3

import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
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

        writer.writerow((data['title'],
                         data['certificate'],
                         data['runtime'],
                         data['genre'],
                         data['imdb'],
                         data['metascore'],
                         data['director'],
                         data['stars'],
                         data['votes'],
                         data['gross']))


def get_page_data(html):

    soup = BeautifulSoup(html, "lxml")

    ads = soup.find("div", class_ = 'lister-list').find_all('div', class_ = 'lister-item')

    for ad in ads:

        #Title of movie
        try:
            title = ad.find("div", class_ = "lister-item-content").find("h3", class_ = 'lister-item-header').find("a").text.strip()

        except:
            title = ""


        #Certificate
        try:
            certificate = ad.find("div", class_ = "lister-item-content").find("p", class_ = "text-muted").find("span", class_ = "certificate").text.strip()

        except:
            certificate = ""


        #Runtime
        try:
            runtime = ad.find("div", class_ = "lister-item-content").find("p", class_ = "text-muted").find("span", class_="runtime").text.strip()

        except:
            runtime = ""


        #Genre
        try:
            genre =ad.find("div", class_ = "lister-item-content").find("p", class_ = "text-muted").find("span", class_="genre").text.strip()

        except:
            genre = ""


        ##Rating
        #IMDB
        try:
            imdb = ad.find("div", class_ = "lister-item-content").find("div", class_ = "rating-bar").find("div", class_ = "ratings-imdb-rating").find("strong").text.strip()

        except:
            imdb = 0


        #Metascore
        try:
            metascore = ad.find("div", class_ = "lister-item-content").find("div", class_ = "rating-bar").find("div", class_ = "ratings-metascore").find("span").text.strip()

        except:
            metascore = 0


        ##Director&Stars
        #Director
        try:
            director = ad.find("div", class_ = "lister-item-content").find("p", class_ = "").find("a")[0].text.strip()
        except:
            director = ""


        #Stars:
        try:
            stars = ad.find("div", class_ = "lister-item-content").find("p", class_ = "").find("a")[1:].text.strip()
        except:
            stars = ""


        ##Votes&Gross
        #Votes
        try:
            votes = ad.find("div", class_ = "lister-item-content").find("p", class_ = "sort-num_votes-visible").find("span", name_ = "nv")[0].text.strip()

        except:
            votes = 0


        #Gross:
        try:
            gross = ad.find("div", class_ = "lister-item-content").find("p", class_ = "sort-num_votes-visible").find("span", name_ = "nv")[1].text.strip()
        except:
            gross = 0

        data = {'title'      : title,
                'certificate': certificate,
                'runtime'    : runtime,
                'genre'      : genre,
                'imdb' : imdb,
                'metascore'  : metascore,
                'director'   : director,
                'stars'      : stars,
                'votes'      : votes,
                'gross'      : gross}

        write_csv(data)







def main():
    url = "http://www.imdb.com/search/title?count=100&groups=oscar_best_picture_winners&sort=year,desc&ref_=nv_ch_osc_2"

#    total_pages = get_total_pages(get_html(url))

    #Парс всех страниц total_pages
    html = get_html(url)
    get_page_data(html)


if __name__ == '__main__':
    main()
