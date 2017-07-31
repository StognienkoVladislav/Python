
def enquote1(in_str):
    "quotes input string with single-quote"
    in_str = in_str.replace("'", r"\'")
    return "'%s" % in_str

def enquote2(in_str):
    "double - quoute"
    in_str = in_str.replace('"', r'\"')
    return '"%s"' % in_str

def gen_insert(table, **kwargs):
    "Generate DB insert statement"

    cols = []
    vals = []

    for col, val in kwargs.items():
        cols.append(enquote2(col))
        vals.append(enquote1(str(val)))
    cols = ", ".join(cols)
    vals = ", ".join(vals)

    return 'INSERT INTO "%s"(%s) VALUES(%s);' % (table, cols, vals)

def logging(func, *args, **kwargs):
    res = func(*args, **kwargs)
    print('calling %s, returned %r' % (func.__name__, res))
    return res

def double(x):
    "Doubles a number"
    return 2 * x

if __name__ == '__main__':
    print (gen_insert("workers", name = "John", age = 21, salary = 1500.0))
    params = {"name" : "Mary", "age" : 19, "salary" : 1200.0}
    print (gen_insert("workers", **params))
    print (logging(double, 155))