def count_words(string):
    string_list = string.split()
    return len(string_list)

f = open('original.txt','r')
print(count_words(f.read()))