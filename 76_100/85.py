
with open("../countries.txt", 'r') as file:
    content = file.readlines()
#print(content)

content = [i.strip("\n") for i in content if "\n" in i]
content = [i for i in content if i != ""]
content = [i for i in content if i != "Top of Page"]
content = [i for i in content if len(i) != 1]

f = open("../countries_new.txt", 'w')

for i in content:
    f.write(i + "\n")

