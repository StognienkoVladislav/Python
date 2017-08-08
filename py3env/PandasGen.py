

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')                     #Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)    #Размер картинок


fixed_df = pd.read_csv('imdb.csv',  # Это то, куда вы скачали файл
                       sep=',', names = ["title", "certificate", "runtime", "genre",
                                          "imdb", "metascore", "director",
                                          "stars", "votes", "gross"])

#fixed_df.loc[0] = ['title', 'certificate', 'runtime', 'genre', 'imdb_rating', 'metascore',
                   #'director', 'stars', 'votes', 'gross']
#fixed_df.to_csv(r'imdb.csv', mode = 'a', header =  None, index = False)


#print(fixed_df[:])

print(fixed_df["certificate"].value_counts())

#Режисер с найбольшим кол-во
print(fixed_df["director"].value_counts())


#Визуализация
#fixed_df["certificate"].value_counts().plot(kind = 'bar')
#plt.show()


#Минимальное / Максимальное / среднее значения
print("IMDB : ")
print(fixed_df['imdb'].min())
print(fixed_df['imdb'].max())
print(fixed_df['imdb'].mean())

#Топ IMDB
print(fixed_df.sort_values(['imdb'])[-10:])

#Топ Metascore
print(fixed_df.sort_values(['metascore'])[-10:])

print("#########################################################")

starS = fixed_df['stars']
SS = {}


#Кол-во оскоров у 1 актера
for s in starS:
    for j in s.split(","):

        if j not in SS:
            SS[j] = 1

        else:
            SS[j] = SS[j] + 1

for x, y in SS.items():
    print(x, y)

print("\nTop of stars:")
for k, v in SS.items():
    if v >= 2:
        print(k + " " + str(v))



#Аналог по жанрам

genre = fixed_df['genre']
genreBest = {}
for g in genre:
    for j in g.split(","):

        if j not in genreBest:
            genreBest[j] = 1

        else:
            genreBest[j] = genreBest[j] + 1


#Top of genre
for x, y in genreBest.items():
    if y >= 10:
        print(x + " " +  str(y))
