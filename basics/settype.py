s = {10, 20, 30, "xyz"}
print(s)  # {10, 20, 30, 'xyz'}
print(type(s))  # <class 'set'>

# Set doesn't allow duplicate values
s = {10, 20, 30, "xyz", 20, 10}
print(s) # {10, 20, 30, 'xyz'}

# Update values
s.update([88,99])
print(s) # {'xyz', 99, 10, 20, 88, 30} Set doesn't guaranty any order

# Few operations are not supported using sets
#print(s[0]) # ERROR: set' object is not subscriptable : Indexing: Not supported in sets
#print(s[0:5]) # ERROR: set' object is not subscriptable. Slicing is not supported
#print(s*3) # ERROR: unsupported operand type(s) for *: 'set' and 'int' : Repeatation Not supported

# Removing element
s.remove(30)
print(s) # {99, 10, 20, 88, 'xyz'}

# Convert Set into Frozen Set : After that we cannot use update, remove operations

f=frozenset(s)
#f.update([20]) # 'frozenset' object has no attribute 'update'
#f.remove(20) # 'frozenset' object has no attribute 'remove'