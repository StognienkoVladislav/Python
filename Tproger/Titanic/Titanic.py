

import numpy as np
import pandas as pd

#Алгоритм машинного обучения
from sklearn.ensemble import RandomForestClassifier

#Импорт функции для тестов
from sklearn.cross_validation import train_test_split

#Отключение предупреждени Pandas
pd.options.mode.chained_assignment = None

#Используется для записи модели в файл
from sklearn.externals import joblib


data = pd.read_csv("titanic_train.csv")
print(data.head())


#Используем медиану для определения возраста

mediana_age = data['age'].median()
print("\nMedian age is {}".format(mediana_age))


#Замена пустых значений в колонке age на 29

data['age'].fillna(mediana_age, inplace = True)
print(data['age'].head())


#Достанем класс, возраст, пол

data_inputs = data[["pclass", "age", "sex"]]
print(data_inputs.head())


#Ожидаемые выходные данные:
expected_output = data[["survived"]]
print(expected_output.head())

#Замена для алгоритма Scikit

data_inputs["pclass"].replace("3rd", 3, inplace=True)

data_inputs["pclass"].replace("2nd", 2, inplace=True)

data_inputs["pclass"].replace("1st", 1, inplace=True)

print(data_inputs.head())


#Замена female на 0, male на 1
data_inputs["sex"] = np.where(data_inputs["sex"] == "female", 0, 1)
print(data_inputs.head())

