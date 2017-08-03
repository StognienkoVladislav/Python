
import pandas as pd
import sqlite3


con = sqlite3.connect("data/weather_2012.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)
print(df)


df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con, index_col = 'id')
print(df)


#для индексирования несколькими столбцами
#можно указать их в список в index_col

df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con, index_col = ['id', 'date_time'])

print(df)


#Запись в базу
#Записывается с помошью метода to_sql(по аналогии с CSV)

weather_df = pd.read_csv('data/weather_2012.csv')
con = sqlite3.connect("data/test_db.sqlite")
con.execute("DROP TABLE IF EXISTS weather_2012")
weather_df.to_sql("weather_2012", con)

#Можно загрузить получ данные
con = sqlite3.connect("data/test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)

print(df)


#Можно юзать SQL запросы напрямую к базе
con = sqlite3.connect("data/test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 ORDER BY Weather LIMIT 3", con)
print(df)

