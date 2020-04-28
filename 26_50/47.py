import glob
st1 = "python"
st2 = []
st1 = list(st1)

file_list = glob.glob("Letters/*.txt")

for filename in file_list:
    with open(filename, "r") as file:
        f = file.read()
        if f in st1:
            st2.append(f)

print(st2)


