
d = {1: 'two', 3: 'four', 4: 'three', 2: 'one', 0: 'zero', 0:'zero'}
result = {}

for key,value in d.items():
    if value not in result.values():
        result[key] = value

print(result)