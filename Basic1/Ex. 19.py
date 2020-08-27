
def creatingNewString(string):

    if(string.startswith('Is')):

        return string

    else:

        return 'Is' + string

print(creatingNewString('Isomorphic'))
print(creatingNewString('somorphic'))