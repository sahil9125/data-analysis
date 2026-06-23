class person:
    conuntry ="India"
    def takebreath(self):
        print("gwalior")
class employees(person):
    company = "honda"
    def getsalary(self):
        print("salary 10000")
    def takebreath(self):
        super().takebreath()
        print("pninfosys")
class programmer(employees):
    #company = "fever"
    def getsalary(self):
        print(f"no salary to programmers")
    def takebreath(self):
        super().takebreath()
    def takebreath(self):
        super().takebreath()
        print("i am an programmer so i am luckly breathing++") 

p = programmer()
p.takebreath()
print(p.company)
