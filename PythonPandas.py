
#Получить данные с сайта, который не предоставляет API

import pandas as pd

calls_df, = pd.read_html("http://apps.sandiego.gov/sdfiredispatch/", header = 0, parse_dates=["Call Date"])

print(calls_df)


print(calls_df.to_json(orient = "records", date_format = "iso"))
#calls_df.to_csv('calls.csv', index = False)

print("\n##################################\n")

#Статистика запроса:
print(calls_df.describe())

#Группировка
print(calls_df.groupby("Call Type").count())

#Обработка данных
print(calls_df["Unit"].unique())