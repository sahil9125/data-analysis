class student:
    def __init__(self, name, marks, password):
        self.name = name
        self._marks = marks
        self.__password = password

    # public method    
    def display(self):
        print("name :" , self.name)
        print("marks"  , self._marks)

    #private method
    def __check_password(self):
       print("password :" , self.__password) 
    #public mehtod to access private method
    def login(self):
        self.__check_password()

class result(student):
    def grade(self):
        if self._marks >=90:
            print("grade : A")
        elif self._marks >=80:
            print("grade : B")
        elif self._marks >= 70:
            print("grade : C") 
        elif self._marks >= 60:
            print("grade : D") 
        else:
            print("grade : F")




a = result("shiv" , 67 , 4321)
a.display()
a.login()
a.grade()