
import matplotlib

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')         #Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)    #Размер картинок


"""
Изменят разделитель на ;

Изменят кодировку на 'latin1' (по умолчанию считается 'utf8')

Обработают даты в колонке 'Date'

Скажут, что сначала идёт день, а потом месяц (формат YYYY-DD-MM)

Изменят индекс на значения в колонке 'Date'
"""

fixed_df = pd.read_csv('data/bikes.csv', sep =';',
                       encoding = 'latin1',
                       parse_dates = ['Date'],
                       dayfirst = True,
                       index_col = 'Date')

print(fixed_df[:3])
print(fixed_df['Berri 1'][:10])
fixed_df['Berri 1'].plot()
plt.show()

fixed_df.plot(figsize = (15, 10))
plt.show()