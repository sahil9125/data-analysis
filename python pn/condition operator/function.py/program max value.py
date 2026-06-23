# def find_max (a,b,c):
#     return max(a,b,c)
# print("max:", find_max(10,30,29))    

# or
def find_max(a,b,c):
    if a>=b and a>=c:
        return a
    else:
        return c
print("max:",find_max(10,30,29))            