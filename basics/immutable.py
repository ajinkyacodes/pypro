a = 20
b = 20
print(a is b)  # True
print(id(a))  # 140728068621832
print(id(b))  # 140728068621832

a = True
b = True
print(a is b)  # True
print(id(a))  # 140728069833136
print(id(b))  # 140728069833136

a = True
b = False
print(a is b)  # False
print(id(a))  # 140728069833136
print(id(b))  # 140728069833168

a = "David"
b = "David"
print(a is b)  # True
print(id(a))  # 1813940012736
print(id(b))  # 1813940012736
