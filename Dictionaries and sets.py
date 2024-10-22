my_dict = {}

student = {"name":"Alice", "age": 20, "courses": ["Math", "CS"]}

print(student)  
print(student.get("courses"))
print(student.get("Alice"))

student["address"] = "New York"
student["age"] = 21
print(student) 