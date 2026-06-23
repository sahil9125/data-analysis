# f = open(r"C:\Users\intel\OneDrive\Desktop\python pn\fileio\student.txt",'r')
# data = f.read()
# print(data)
# f.close()
#----------orr 
with open(r"C:\Users\intel\OneDrive\Desktop\python pn\fileio\student.txt",'r') as f:
    print(f.read())
