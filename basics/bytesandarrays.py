lst = [20,30,40,234]
print(type(lst)) # <class 'list'>

# converting a list into bytes
b=bytes(lst)
print(type(b)) # <class 'bytes'>
#b[3] = 22 # ERROR: 'bytes' object does not support item assignment

# converting a list into bytearray
b1=bytearray(lst)
print(type(b1)) # <class 'bytearray'>
b1[2] = 33 # No error