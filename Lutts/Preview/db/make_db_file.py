dbfilename = 'people-file'
ENDDB = 'enddb'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename = dbfilename):
    'сохраняет базу данных в файл'
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for(name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file = dbfile)
    dbfile.close()

def loadDbase(dbfilename = dbfilename):
    "Востановление данных"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db={}
    key = input()
    while key != ENDDB:
        rec ={}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db

if __name__ == '__main__':
    from db.initdata import db
    storeDbase(db)