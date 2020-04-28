from pprint import pprint
d = dict(a=list(range(1, 11)), b=list(range(11, 21)), c=list(range(21, 31)))

#pprint("b has value" + str(d['b']))
#pprint("c has value" + str(d['c']))
#pprint("a has value" + str(d['a']))


for key, value in d.items():
    print(key , ' has value ',  value)