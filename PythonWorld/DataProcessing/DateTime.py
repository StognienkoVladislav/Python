

#Unix timestamps

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)    #Размер картинки

#Read it, and remove the last row
popcon = pd.read_csv('data/popularity-contest.txt', sep = ' ')[:-1]
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']

print(popcon[:5])

#Все, что нам нужно сделать - это сказать pandas, что целые числа в колонках это datetimes

popcon['atime'] = popcon['atime'].astype(int)
popcon['ctime'] = popcon['ctime'].astype(int)

popcon['atime'] = pd.to_datetime(popcon['atime'], unit = 's')
popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit = 's')

print(popcon[:5])

#Посмотрим на все с timestamp 0
#С помощью pandas мы можем использовать строку для сравнения

popcon = popcon[popcon['atime'] > '1970-01-01']

#Можно использовать pandas, чтобы посмотреть, где имя пакета не содержит 'lib'

nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]
print(nonlibraries.sort_values('ctime', ascending = False)[:10])