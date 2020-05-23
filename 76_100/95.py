
st1 = input("Enter values:")
st2 = st1.split(",")

with open("../user_data.txt", 'a+') as file:
    for i in st2:
        file.write(i + '\n')
