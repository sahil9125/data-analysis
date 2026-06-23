# ek hi function ko different trh se use karne 
# 1 complte time polymorphism
# 2 run time polymorphism

# print(len("pninfosys"))
# print(len([1,2,3,4,5]))
# print(len({1:"a",2:"b",3:"c"}))

# overriding
# class animal:
#     def sound(self):
#         print("animal makes sound")
# class dog(animal):
#     def sound(self):
#         print("dog braks")
# a = animal()
# b = dog()
# a.sound()
# b.sound()     
# 
# 
# class bird :
#     def fly(self):
#         print("bird flies")
# class eagle(bird):
#     def fly (self):
#         print("eagle flies high")
# b = bird()               
# e =eagle()
# b.fly()
# e.fly()


#overloading
# pyhton me overloading nhi hota

class calclucator:
#    # def add(self, a, b):
#     #    return a + b

#     def add(self, a, b, c):
#         return a + b + c
    def add (self, a, b, c, d):
        return a + b + c +d
calc = calclucator()
# print(calc.add(1,2))
# print(calc.add(1,2,3))
print(calc.add(1,2,3,4))
#Python does not support method overloading directly.
#  Multiple methods with same name overwrite each other.