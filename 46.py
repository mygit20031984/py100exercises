import string

a = []
for letter in string.ascii_lowercase:
    f = open("Letters/" + letter+".txt", "r")
    a.append(f.read())
    f.close()

print(a)