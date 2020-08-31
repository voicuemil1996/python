
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
