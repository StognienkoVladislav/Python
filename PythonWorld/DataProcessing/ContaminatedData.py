

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



pd.options.display.max_rows = 7
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

requests = pd.read_csv('data/311_Service_Requests_from_2011.csv')

###Как понять, что данные загрязнены
#Некоторые значения - строки, некоторые - числа

#Есть nan

#Некоторые значение 29616-0759 или 83

#Некоторые неопределенные значения, которые pandas Не смог распознать, такие как 'N/A' и 'NO CLUE'



###Как можно фиксить
#Преобразовать 'N/A' и 'NO CLUE' в обычные nan

#Посмотреть, что такое 83, и решить, что же делать

#Сделать все строками


print(requests['Incident Zip'].unique())


###Исправление ошибок с NAN и различий строки/числа
#Можно передать na_values в pd.read_csv , чтобы немного очистить данные,
#также явно указать тип для Incident Zip

na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('data/311_Service_Requests_from_2011.csv', na_values = na_values, dtype = {'Incident Zip': str})

print(requests['Incident Zip'].unique())



#Что с дефисами
rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
print(len(requests[rows_with_dashes]))

print(requests[rows_with_dashes]['Incident Zip'])


#обрежем слишком длинный код
long_zip_codes = requests['Incident Zip'].str.len() > 5
print(requests['Incident Zip'][long_zip_codes].unique())

requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)

#Посмотрим кого код  00000
print(requests[requests['Incident Zip'] == '00000'])

#Заменим на nan
zero_zips = requests['Incident Zip'] == '00000'
requests.loc[zero_zips, 'Incident Zip'] = np.nan

unique_zips = requests['Incident Zip'].unique()
print(unique_zips)

print(requests['City'].str.upper().value_counts())
