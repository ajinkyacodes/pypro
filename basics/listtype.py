lst=[10,20,"Ajinkya",-10,30.5]
print(lst) # [10, 20, 'Ajinkya', -10, 30.5]

# indexing
print(lst[3]) # -10

# slicing
print(lst[3:5]) # [-10, 30.5]

# Repeat values in multiple
print(lst*4)  # [10, 20, 'Ajinkya', -10, 30.5, 10, 20, 'Ajinkya', -10, 30.5, 10, 20, 'Ajinkya', -10, 30.5, 10, 20, 'Ajinkya', -10, 30.5]

# length
print(len(lst)) # 5

# Adding or removing values
lst.append(40)
lst.remove("Ajinkya")
del(lst[1])
print(lst) # [10, -10, 30.5, 40]

# maximum and minimum element
print(max(lst)) # 40
print(min(lst)) # -10

# insert value at index
lst.insert(3,99) # [10, -10, 30.5, 99, 40]
print(lst)

# sorting the list
lst.sort()
print(lst) # [-10, 10, 30.5, 40, 99]
lst.sort(reverse=True)
print(lst) # [99, 40, 30.5, 10, -10]

# clear
lst.clear()
print(lst) # []

