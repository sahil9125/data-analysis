#self refer to the insatnce of the class
# it is automatically passed with a function call
#from an object.
class employee:
    company="pninfsys"
    def getsalary(self,a):
        print("salary is 100k")       
        print(f"salary is {self.salary}")
        print(f"salary is {self.salary}")
        print("salary is this employee working")
        print(f"salary is this employee woking {self.company} is {self.salary}")
rohit = employee()
rohit.salary = 10000
rohit.getsalary(3000) #employee.getsalary(rohit)