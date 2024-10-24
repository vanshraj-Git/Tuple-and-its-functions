# Dictionary
students3 = { "Alice": 85, "Bob":78, "Charlie": 92, "David": 88, "Eva": 76}
print(type(students3))
max3=max(students3,key=students3.get)
print(f"The student with the highest marks is {max3} with {students3[max3]} marks.")


# list
students2 = [("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 88), ("Eva", 76)]
print(type(students2))
max2=max(students2,key=lambda x:x[1])
print(max2)

# Set
students1 = {("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 88), ("Eva", 76)}
print(type(students1))
max1=max(students1,key=lambda x:x[1])
print(max1)

# tuple
students = (("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 88), ("Eva", 76))
print(type(students))
max=max(students,key=lambda x:x[1])
print(max)


# list ,set and tuple all 3 uses same function (max, min, count, etc.)
# list and set are mutable or changeable
# tuple is immutable so function like sort(),reverse() does not work
