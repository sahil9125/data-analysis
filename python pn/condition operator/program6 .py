units = int (input("enter the number of unit consumed:"))
if units <= 100:
    bill = units *5
elif units <= 200:
    bill = (100*5)+((units - 100)*7)
else:
    bill = (100*5)+(100*7)+((units -200)*10)
print("the electricity bill is:", bill)       