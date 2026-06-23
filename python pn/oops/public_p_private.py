class employee:
    public = 8
    _protec= 100
    __private = "vikas"
    def display(self):
      print(self.__private)
    #access modified 
a= employee()
print(a.public)
print(a._protec)
a.display()
#print(a.__private)