dict1 = {1: "John", 2: "Bob", 3: "Bill"}
print(dict1)  # {1: 'John', 2: 'Bob', 3: 'Bill'}

# Access keys and values
print(dict1.items())  # dict_items([(1, 'John'), (2, 'Bob'), (3, 'Bill')])
print(dict1.keys())  # dict_keys([1, 2, 3])

k = dict1.keys()
for i in k: print(i)
"""
OUTPUT:
1
2
3
"""

v = dict1.values()
for i in v: print(i)
"""
OUTPUT:
John
Bob
Bill
"""

print(dict1[3])  # Bill

# Delete element
del dict1[3]
print(dict1)  # {1: 'John', 2: 'Bob'}
