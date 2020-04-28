def count_words(string):
    string_list = string.split()
    return len(string_list)

print(count_words(input("Please enter your string")))