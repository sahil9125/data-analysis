# f =open(r"C:\Users\intel\OneDrive\Desktop\python pn\fileio\student.txt",'r')
# print(f.readline())    # first element print krta hai
# print(f.readline())   # jitni bar readline use karege utni baar hi one line ko print karega
# print(f.readlines())  #list kai ander print karta hai

# with open(r"C:\Users\intel\OneDrive\Desktop\python pn\fileio\student.txt",'r') as f:
#     lines = f.readlines()
#     print(lines[0])  #ram

with open (r"C:\Users\intel\OneDrive\Desktop\python pn\fileio\student.txt",'r')as f:
    for line in f:
        print(line.strip())  # .strip()  remove extra space