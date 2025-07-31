student_info = {"name": "Larry", "age": 51, "major": "Computer Science"}
print(student_info)  # {'name': 'Larry', 'age': 51, 'major': 'Computer Science'}

# Print name and age
print(student_info["name"], student_info["age"])  # Larry 51

# Add new key email
student_info["email"] = "lary@gmail.com"
print(student_info)  # {'name': 'Larry', 'age': 51, 'major': 'Computer Science', 'email': 'lary@gmail.com'}

# Update the age
student_info["age"] = 52
print(student_info)  # {'name': 'Larry', 'age': 52, 'major': 'Computer Science', 'email': 'lary@gmail.com'}

# Remove the key major
del (student_info["major"])
print(student_info)  # {'name': 'Larry', 'age': 52, 'email': 'lary@gmail.com'}
