
import urllib2
#для работы с протоколам HTTP, высокоуровневый

import urllib
from Queue import Queue
import threading
import re
#модуль для работы с регулярными выражениями
import time

queue = Queue()
PROXY = "10.10.31.103:3128"

HEADERS = {"User-Agent" : "Opera/9.64 (Windows NT 5.1; U; en) Presto/2.1.1",
           "Accept" : "text/html, application/xml;q=0.9, application/xhtml+xml, image/ png, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1",
           "Accept-Language" : "ru,uk-UA;q=0.9,uk;q=0.8,en;q=0.7",
           "Accept-Charset" : "iso-8859-1, utf-8, utf-16, *;q=0.1",
           "Accept-Encoding" : "identity, *;q=0",
           "Connection" : "Keep-Alive"}

THREADS_COUNT = 10
DEEP = 30
ENCODING = "UTF-8"

LOCK = threading.RLock()           


def worker():
    global queue
    while True:
        try:
            target_link = queue.get_nowait()
            #получение задачи из списка

        except Exception, error:
            return

        parsed_data = get_and_parse_page(target_link)

        if parsed_data != "ERROR":
            write_to_file(parsed_data)
            #запись данных в файл

        else:
            queue.put(target_link)
            #Если страница не была получена, то забрасываем ее обратно в queue


def write_to_file(parsed_data):
    global LOCK
    global ENCODING
    LOCK.acquire()
    #выполн только 1 потоком в 1 момент времени

    with open("parsed_data.txt", "a") as out:
        for site in parsed_data:
            link, title = site[0], site[1]
            title = title.replace("<em>", "").replace("</em>","").replace("<b>","").replace("</b>","")
            #замена тегов, которые нам не нужны в title
            out.write(u"{link}|{title}\n").format(link = link, title = title).encode("cp1251")
    LOCK.release()                            


def get_and_parse_page(target_link):
    global PROXY
    global HEADERS

    if PROXY is not None:
        proxy_handler = urllib2.ProxyHandlr({"http":"" + PROXY + "/"})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)

    page_request = urllib2.Request(url = target_link, headers = HEADERS)

    try:
        page = urllib2.urlopen(url = page_request).read().decode("UTF-8", "replace")

    except Exception, error:
        print(str(error))
        return "ERROR"
    
    harvested_data = re.findall(r'''\<li\ class\=g\>\<h3\ class\=r\>\<a\ href\=\"(.*?)".*?>(.*?)\<\/a\>\<\/h3\>''', page)                
    #Сбор со страницы поиска ссылок и title найденных страниц
    #Очистка данных от результатов поиска по блогам, картинкам и др. сервисам гугла

    for data in harvested_data:
        if data[0].startwith("/"):
            harvested_data.remove(data)

        if ".google.com" in data[0]:
            harvested_data.remove(data)
    
    return harvested_data     


def main():
    print ("STARTED")

    global THREADS_COUNT
    global DEEP
    global ENCODING

    with open("requests.txt") as requests:
        for request in requests:
            request = request.translate(None, "\r\n").decode(ENCODING, "replace")

            empty_link = "www.google.com/search?hl=ru&client=opera&rls=ru&hs=67v&q={request}&start={N}&sa=N"

            for i in range(0, DEEP, 10):
                queue.put(empty_link.format(request = request.encode("UTF-8"), N = i))

        for _ in range(THREADS_COUNT):
            
            thread_ = threading.Thread(target = worker)
            thread_.start()

        while threading.active_count() > 1:
            time.sleep(1)

        print("FINISHED")
                        