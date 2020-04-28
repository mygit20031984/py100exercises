import string

with open("41_o.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")


