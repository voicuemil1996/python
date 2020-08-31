
string = "w3resource"
dict = {}

for i in string:

    if i not in dict:

        dict[i] = string.count(i)

print(dict)