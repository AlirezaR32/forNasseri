with open('file.txt' ,'r') as file:
    data = file.readlines()

i = 0
for line in data:
    print(line)
    i += 1


print (i)