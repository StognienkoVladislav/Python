import pickle, glob
for filename in glob.glob('*.pkl'):     #для 'bob', 'sue', 'tom'
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>', record)

suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])