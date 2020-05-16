i = []

while True:
    line = input("Enter Value:")
    file = open("user_data_append.txt", 'a+')
    if line == "CLOSE":
        for e in i:
            file.write(e + '\n')
        file.close()
        break
    elif line == "SAVE":
        for e in i:
            file.write(e + '\n')
        file.close()
        i = []
        pass
        print("You are here")
    else:
        i.append(line)
        print(i)

print("GAME OVER")

