"""
Tuple

Immutable in nature
Cannot be modified
Insertion Order
Duplicates Allowed
Different Types Allowed

Example:
    t1 = (1,2,3,4)
    t2 = 1,2,3,,4
    t3 = 1,
"""

tpl = (20,30,40,20,50,"xyz")
print(tpl) # (20, 30, 40, 20, 50, 'xyz')

tpl2 = 1,
print(tpl2)

# Repeat values multiple
print(tpl*3) # (20, 30, 40, 20, 50, 'xyz', 20, 30, 40, 20, 50, 'xyz', 20, 30, 40, 20, 50, 'xyz')

# count value
print(tpl.count(20)) # 2

# Index
print(tpl.index("xyz")) # 5

# convert a list to tuple
lst = [67,34,"xyz"]
print(type(lst)) # <class 'list'>
tpl2 = tuple(lst)
print(type(tpl2)) # <class 'tuple'>
print(tpl2) # (67, 34, 'xyz')

"""
List vs Tuple

List: 
1. Uses square brackets
2. Mutable. We can change values
3. Changing
4. Cannot use as a key to Dictionary

Tuple: 
1. Uses Round brackets or no brackets with comma
2. Immutable. We cannot change values
3. Not Changing
4. Can be used as key to dictionary
"""