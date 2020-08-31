import operator

d = {1: 'two', 3: 'four', 4: 'three', 2: 'one', 0: 'zero'}

print('Original dictionary : ',d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(0)))

print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(0),reverse=True))

print('Dictionary in descending order by value : ',sorted_d)