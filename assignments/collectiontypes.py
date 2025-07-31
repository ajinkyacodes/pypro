lst = ["India", "Nepal", "USA", "China"]

# Add a country at the end
lst.append("Russia")
print(lst) # ['India', 'Nepal', 'USA', 'China', 'Russia']

# Remove a country by index
del(lst[1])
print(lst) # ['India', 'USA', 'China', 'Russia']

# Add a country in the middle
length = len(lst)
middle = length/2
lst.insert(int(middle), "England")
print(lst) # ['India', 'USA', 'England', 'China', 'Russia']