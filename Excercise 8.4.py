fileName = input('Enter file name: ')
fileHandle = open(fileName)
lst = list()
for line in fileHandle:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)


