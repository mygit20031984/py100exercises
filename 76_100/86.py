
checklist = ["Portugal", "Germany", "India", "Munster", "Spain"]

with open("../countries_clean.txt", 'r') as file:
    content = file.read()
    for i in checklist:
        if i not in content:
            checklist.remove(i)

print(checklist)

#--------------------
checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("../countries_clean.txt", "r") as file:
    content = file.readlines()

content = [i.rstrip('\n') for i in content]
checked = [i for i in content if i in checklist]

print(checked)