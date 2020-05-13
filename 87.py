
checklist = ["Portugal", "Germany", "Spain"]
checklist = [i + "\n" for i in checklist]

with open("countries_missing.txt",'r') as file:
    content = file.readlines()

updated_list = sorted(checklist + content)

with open("countries_missing_new.txt",'w') as file:
    for i in updated_list:
        file.write(i)