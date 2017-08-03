
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.rcParams['figure.figsize'] = (10, 5)


bikes = pd.read_csv('data/bikes.csv', sep = ';', encoding = 'latin1',
                    parse_dates = ['Date'], dayfirst = True, index_col = 'Date')


bikes['Berri 1'].plot()
plt.show()


#Посмотрим на велодорожку Berri
#Создадим dataframe только с ней

berri_bikes = bikes[['Berri 1']].copy()

print(berri_bikes[:5])

#Индексы
print(berri_bikes.index)


#Для получения дней месяца каждой строки
print(berri_bikes.index.day)


#День недели
print(berri_bikes.index.weekday)


#Можно добавить дни недели как столбец
berri_bikes.loc[:, 'weekday'] = berri_bikes.index.weekday
print(berri_bikes[:5])


###Добавляем велосипедистов
#Сгрупировать строки по дню недели и затем сложить все знач с одинак днем

weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
#weekday_counts = berri_bikes.groupby('weekday').sum() - можно и так(даже проще)

print(weekday_counts)


#Переименуем 0, 1, 2, 3, 4, 5, 6 ,чтобы понимать, что они означают
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekday_counts)

weekday_counts.plot(kind = 'bar')



#Соединим все вместе
#Add the weekday column
berri_bikes = bikes[['Berri 1']].copy()
berri_bikes.loc[:, 'weekday'] = berri_bikes.index.weekday

#Add up the number of cyclists by weekday, and plot!
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts.plot(kind = 'bar')