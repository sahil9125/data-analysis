class employee:
    car ="pninfosys"
    ecode = 120
class freelancer:
    car = "google" 
    level =0
    def upgradelevel(self):
       self.level = self.level + 1
class programmer(employee,freelancer):
    #car="abcd"
    name="vikas"
p= programmer()
print(p.car)
p.upgradelevel()
print(p.level)    

