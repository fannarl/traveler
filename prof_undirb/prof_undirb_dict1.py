import operator
# Write a Python script to sort (ascending and descending) a dictionary by value.

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print('Original dictionary: {0}'.format(d))
sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by value: {}'.format(sorted_d))
sorted_d = sorted(d.items(), key=operator.itemgetter(0), reverse = True)
print('Dictionary in descending order by value: {}'.format(sorted_d))