# f = open(r"C:\Users\intel\OneDrive\Desktop\python pn\fileio\student.txt",'a')
# f.write("\nhello pninfosys")   # isse new data add hota bina old data ko remove kiye 
# f.close()



with open(r"C:\Users\intel\OneDrive\Desktop\python pn\fileio\student.txt",'r') as f:
     print(f.read())
with open(r"C:\Users\intel\OneDrive\Desktop\python pn\fileio\student.txt",'w') as f:
    f.write("hello123")
with open(r"C:\Users\intel\OneDrive\Desktop\python pn\fileio\student.txt",'a') as f:
    f.write("\nhello pninfosys again")
        
        
