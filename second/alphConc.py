import re

dict = {}
result = []
filePath = input()
with open(filePath) as file:
    text = file.readlines()
counter = 1
for line in text:
    words = list(set(re.split("\W+", line)))
    for word in words:
        if word != "":
            if word not in dict:
                dict[word] = []
            dict[word].append(counter)
    counter += 1


for word in sorted(dict.keys()):
    print(f"{word} : {dict[word]}")
