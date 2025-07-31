students = {"John": ["Python", "DJango", "DRF"], "Bob": ["Java", "Spring"], "Jim": ["JS", "Node", "React"]}
keys = students.keys()
for eachKey in keys:
    print("Courses taken by ", eachKey, " are: ")
    for eachCourse in students[eachKey]:
        print(eachCourse)

"""
OUTPUT:

Courses taken by  John  are: 
Python
DJango
DRF
Courses taken by  Bob  are: 
Java
Spring
Courses taken by  Jim  are: 
JS
Node
React
"""