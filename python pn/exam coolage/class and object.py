# class Add:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def sum(self):
#         print(self.a + self.b)

# obj = Add(5, 3)
# obj.sum()

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)

# # Creating object
# s1 = Student("Shiv", 85)

# # Calling method
# s1.display()

class A:
    def __init__(self, age, name, address):
        self.age = age
        self.name = name
        self.address = address

obj = A(10, "manpreet", "punjab")
print(obj.age, obj.name, obj.address)  
# a=10
# b=0
# try:
#    c=a/b
#    print(c)
# except:   
#     # print("a number can not divide by zero(0)")
#      print("hello python")     

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Cannot divide by zero")


student = {"name": "Shiv", "age": 20, "marks": 85}
student["class"] = 7

print(student)
del student["class"]
print(student)
  

for key, value in student.items():
    print(key, ":", value)
