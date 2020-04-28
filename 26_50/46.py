#import string

#a = []
#for letter in string.ascii_lowercase:
    #f = open("Letters/" + letter+".txt", "r")
    #a.append(f.read())
    #    f.close()

#print(a)

import glob

letters= []
file_list = glob.glob("Letters/*.txt")

for filename in file_list:
    with open(filename, "r") as file:
        letters.append(file.read().strip("\n"))


print(letters)