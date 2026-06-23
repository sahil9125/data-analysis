def is_prime(num):
    if num <=1:
        return "not prime"
    for i in range (2,num):
        if num%i == 0:
          return "not prime"
    return "prime"
n = int(input("enter a number:"))  
print (is_prime(n))          