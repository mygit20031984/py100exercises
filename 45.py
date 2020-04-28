import string, os

if not os.path.exists("Letters"):
    os.makedirs("Letters")

for letter in string.ascii_lowercase:
    f = open("Letters/" + letter+".txt", "w")
    f.write(letter)
    f.close()
    #print(letter)