
i = ""
lst = []

while i != "CLOSE":
    i = input("Enter Value:")
    if i == "CLOSE":
        break;
    else:
        lst.append(i)

with open("user_data_till_close.txt", 'a+') as file:
    for i in lst:
        file.write(i + '\n')
