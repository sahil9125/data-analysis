def game():
    return 1000
score = game()
with open(r"C:\Users\intel\OneDrive\Desktop\python pn\fileio\hiscore.txt",'r') as f:
    hiscore = int(f.read())
if hiscore<score:
    with open(r"C:\Users\intel\OneDrive\Desktop\python pn\fileio\hiscore.txt",'w') as f:
        f.write(str(score))