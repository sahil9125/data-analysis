#
class papa:
    bike= "007"
    def showdetails(self):
        print("This s an employee")
class son(papa): #inheritats the attributes and method of papa class
    language = "python"
    #bike ="008"
    def getlanguage(self):
        print(f"the language is {self.language}")
        #def showdetails(self):
            #print("the is an programmer")

p = son()
print(p.bike)
p.showdetails()
p.getlanguage ()          
