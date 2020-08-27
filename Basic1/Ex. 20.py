
def creatingNewString(string, n):

    newString = string

    for i in range(n - 1):
        newString += string

    return  newString

n = int(input('n = '))
string = input('string = ')

print(creatingNewString(string, n))