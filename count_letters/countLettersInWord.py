text = input("Enter a word: ")
dict = {}

for i in range(len(text)):
    dict[text[i]] = text.count(text[i])

print(dict)
