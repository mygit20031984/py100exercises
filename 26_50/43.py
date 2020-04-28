import string
a = []
i=0
j=1

with open("43_o.txt", "w") as file:
    for letter in string.ascii_lowercase:
        a.append(letter)

    while i <= 25:
        for p, q in zip(a[i], a[j]):
            file.write(p + q + "\n")
            i += 2
            j += 2


