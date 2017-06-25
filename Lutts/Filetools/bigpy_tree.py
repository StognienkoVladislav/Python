#отыскивает наибольший файл с исходным программным кодом в дереве каталогов

import sys, os, pprint

trace = False
if sys.platform.startswith('win'):
    dirname = r'E:\Python\Python\Lib'       #Windows

else:
    dirname = '/usr/lib/python'             #Unix, Linux, Cygwin

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullzise = os.path.getsize(fullname)
            allsizes.append((fullzise, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])