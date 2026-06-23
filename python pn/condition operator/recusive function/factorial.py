def fact (n):
    if n == 0 :
      return 1
    else:
     return n*fact(n-1)
print(fact (5))   

#fact(0)= 1 yaha se calculation start hoti hai
#fact(1)= 1 x 1 = 1
#fact(2)= 2 x 1 = 2
#fact(3)= 3 x 2= 6
#fact(4)= 4 x 6= 24
#fact(5)= 5 x 24 = 120