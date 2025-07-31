# Single line string
from itertools import count

s = "You are awesome"
print(s)

# Multiline string
s1 = """You are
the creator
of your destiny."""
print(s1)

# Printing the character of the string
print(s[0])

# Repeat string multiple times
print(s * 2)

# Length of string
print(len(s))

# Slicing of string
print(s[0:5])
print(s[0:])
print(s[:8])
print(s[-3:-1])

# Slicing of string with steps
print(s[0:9:2])

# Reverse the string
print(s[15::-1])
print(s[::-1])

# stripping the spaces
str = "    You are awesome    "
print(str.strip())
print(str.lstrip())
print(str.rstrip())

# Locate
print(str.find("awe",0,len(s)))
print(str.find("awe",0,8))

# count character
print(str.count("a"))

# replace
print(str.replace("awesome", "super"))

# text transformation
print(str.upper())
print(str.lower())
print(str.title())