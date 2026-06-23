#email = "admin@gmail.com"
#password = "admin@123"
email= input("emter your email:")
password =input("enter you password:")
if email=="admin@gamil.com" and password =="admin123":
    print("login successful")
elif email =="student@gmail.com" and password == "student123":
    print ("student login")
elif email =="hr@gmail.com" and password == "hr123":
    print ("hr login") 
else:
    print("invalid")       