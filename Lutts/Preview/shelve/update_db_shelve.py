from db.initdata import tom
import shelve
db = shelve.open('people-shelve')
sue = db['sue']         #Извлекает обьект sue
sue['pay'] *= 1.50
db['sue'] = sue         #Изменяет обьект sue
db['tom'] = tom         #Добавляет новую запись
db.close()