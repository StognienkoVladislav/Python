import shelve
fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ') # ключ или пустая строка, возбуждает исключение

    if not key: break
    else:
        try:
            record = db[key] # извлечь запись по ключу и вывести
            for field in fieldnames:
                print(field.ljust(maxfield), '=>', getattr(record, field))
        except:
            print('No such key “%s”!' % key)

