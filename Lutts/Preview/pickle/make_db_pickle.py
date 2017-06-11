import pickle

from db.initdata import db

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)  # Сохранение всей БД
dbfile.close()
