f= open(r"C:\Users\intel\OneDrive\Desktop\python pn\fileio\student.txt",'r')
t = f.read()
if 'hello' in t:
    print("present")
else:
    print("not present")
f.close()        