dict = {'key1':'value1', 'key2':'value2'}

dict.pop('key2')
print(dict)

#safer option

dict.pop('key3', None)
print(dict)