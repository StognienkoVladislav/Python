

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')                     #Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)    #Размер картинок

#Вытаскиваем csv и добавляем названия колонкам
fixed_df = pd.read_csv('imdb.csv',  # Это то, куда вы скачали файл
                       sep=',', names = ["title", "certificate", "runtime", "genre",
                                          "imdb", "metascore", "director",
                                          "stars", "votes", "gross"])

#Вывести всю инфу
#print(fixed_df[:])

#Вывести кол-во mpaa-рейтинг
print(fixed_df["certificate"].value_counts())

#Кол-во оскаров у режисера
print(fixed_df["director"].value_counts())


#Визуализация, 1 из примеров
#fixed_df["certificate"].value_counts().plot(kind = 'bar')
#plt.show()


#Минимальное / Максимальное / среднее значения IMDB по всем фильмам
print("IMDB : ")
print(fixed_df['imdb'].min())
print(fixed_df['imdb'].max())
print(fixed_df['imdb'].mean())

#Топ IMDB  топ 10 фильмов по рейтингу imdb
print(fixed_df.sort_values(['imdb'])[-10:])

#Топ Metascore то 10 по metascore
print(fixed_df.sort_values(['metascore'])[-10:])

#просто черточки для отделения вывода
print("#########################################################")



#Среднее кол-во финансов
grs = fixed_df["gross"]
grsAv = []
sumG = 0
#проходимся по всем строчкам и вытаскиваем ячейку с бюджетом
for g in grs:
    if len(g) > 2:
        grsAv.append((g[1:-1]))
        sumG += float(g[1:-1])


print("AV sum fin : " + str(float(sumG) / len(grsAv)) + 'M')



#Кол-во оскоров у 1 актера

starS = fixed_df['stars']
SS = {}

for s in starS:
    for j in s.split(","):
        #Проходимся по всем актерам
        #Если актера нет в списке - добавляем его и прирав кол-во оскаров к 1
        if j not in SS:
            SS[j] = 1
        #Если есть, то кол-во +1
        else:
            SS[j] += 1

#for x, y in SS.items():
#    print(x, y)

#Выводим актеров , у которых больше или равно 2 оскара
print("\nTop of stars:")
for k, v in SS.items():
    if v >= 2:
        print(k + " " + str(v))



#Аналог по жанрам

genre = fixed_df['genre']
genreBest = {}
for g in genre:
    for j in g.split(","):
        #То же самое по жанрам
        if j not in genreBest:
            genreBest[j] = 1

        else:
            genreBest[j] = genreBest[j] + 1

print("\n####################################################\n")
#Top of genre
for x, y in genreBest.items():
    if y >= 10:
        print(x + " " +  str(y))

