
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.rcParams['figure.figsize'] = (10, 5)

complaints = pd.read_csv('data/311_Service_Requests_from_2011.csv')


#При печати большого dataframe, будет показаны только первые строки
#для первых 5

print(complaints[:5])


#Выбор строк и столбцов
print(complaints['Complaint Type'][:5])

#Не важно в каком порядке(взять первые 5 срок у столбца или столбец у первых 5 строк)
print(complaints[:5]['Complaint Type'])

#Выбор нескольких столбцов
print(complaints[['Complaint Type', 'Borough']])


#Посмотрим первые 10 строк
print(complaints[['Complaint Type', 'Borough']][:10])


#Какой самый частый тип жалоб
print(complaints['Complaint Type'].value_counts())

#10 Наиболее частых типов
complaints_counts = complaints['Complaint Type'].value_counts()
print(complaints_counts[:10])

#Относительно них построить график
complaints_counts[:10].plot(kind = 'bar')
plt.show()
