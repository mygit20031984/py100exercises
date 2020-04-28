def count_words(string):
    string_list1 = string.replace(',', " ")
    string_list = string_list1.split()
    print(string_list)
    return len(string_list)

f = open('words2.txt','r')
print(count_words(f.read()))