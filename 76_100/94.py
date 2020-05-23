

with open("../url.txt", 'r') as file:
    content = file.readlines()

with open("../url_corrected.txt", 'w') as file:
    for i in content:
        i = i.replace("s", "", 1)
        i = i[:6] + "/" + i[6:]
        file.write(i)