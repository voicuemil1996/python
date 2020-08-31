
#Ex. 1 (sorting by value)
mport operator

d = {1: 'two', 3: 'four', 4: 'three', 2: 'one', 0: 'zero'}

print('Original dictionary : ',d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1)))

print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))

print('Dictionary in descending order by value : ',sorted_d)


#Ex. 2(adding)
dict = {'key1':'value1', 'key2':'value2'}
print('Current dict: ', dict)

dict['new_key'] = 'new_value'
print('New dict: ', dict)

#also, it can be used the update function

dict1 = {'other_key1':'other_value1', 'other_key2':'other_value2'}
dict.update(dict1)
print('Newest dict: ', dict)


#Ex. 4 (checking existance)
dict = {'key1':'value1', 'key2':'value2'}

if 'key1' in dict:

    print('it exists')

else:

    print("it doesn't exist")

#Ex. 5 (iterating)
dict = {'key1':'value1', 'key2':'value2'}

for key in dict:

    print(key, ':', dict[key])

print('\n')
for key, value in dict.items():

    print(key, ':', value)


#Ex. 6
n = 4
dict = {}

for i in range(1, n + 1):

    dict[i] = i * i


print(dict)


#Ex.12(removing)
dict = {'key1':'value1', 'key2':'value2'}

dict.pop('key2')
print(dict)

#safer option
dict.pop('key3', None)
print(dict)


#Ex.14(sorting by key)
import operator

d = {1: 'two', 3: 'four', 4: 'three', 2: 'one', 0: 'zero'}

print('Original dictionary : ',d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(0)))

print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(0),reverse=True))

print('Dictionary in descending order by value : ',sorted_d)


#Ex.17(removing duplicates)
d = {1: 'two', 3: 'four', 4: 'three', 2: 'one', 0: 'zero', 0:'zero'}
result = {}

for key,value in d.items():
    if value not in result.values():
        result[key] = value

print(result)


#Ex.18 (Checking emptiness)
d = {1: 'two', 3: 'four', 4: 'three', 2: 'one', 0: 'zero', 0:'zero'}
result = not bool(d)

print(f'Is dictionary empty? {result}')

d= {}
result = not bool(d)

print(f'Is dictionary empty? {result}')


#Ex.19
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}

for key1 in d1:

    for key2 in d2:

        if key1 not in d3 and key2 not in d3:
            if key1 == key2:

                d3[key1] = d1[key1] + d2[key2]
                break

            else:

                d3[key1] = d1[key1]
                d3[key2] = d2[key2]

print(d3)

#better solution
from collections import Counter
d = Counter(d1) + Counter(d2)
print(d)


#Ex. 21

#best option
import itertools

d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))

#Ex. 24
string = "w3resource"
dict = {}

for i in string:

    if i not in dict:

        dict[i] = string.count(i)

print(dict)