class employee:
    company ="google"
    def itm (self,a):
        print(f"hello,{self.company} itm gwalior{a}")
    @staticmethod # it is used when we want to use a method in a class but 
    #we dont want to use self or cls
    def rjit(a):
        print(a)
rohit = employee()
rohit.itm("delhi")
rohit.rjit("ram")        
