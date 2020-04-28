#a = ["1", 1, "1", 2]
#s = set(a)
#b = list(s)
#print(b)
#------Solution2-----------------------
#from collections import OrderedDict
#a = ["1", 1, "1", 2]
#a = list(OrderedDict.fromkeys(a))
#print(a)
#------Solution3-----------------------

a = ["1", 1, "1", 2]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)
