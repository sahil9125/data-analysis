letter = '''Dear <|NAME|>,
You are selected!
Have a great day ahead!
Thanks and regards,
pninfosys   <|NAME|>

DATE: <|date|>
'''
name=input("Enter Your Name:\n")
date= input("Enter Date:")

letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|date|>",date)

print(letter)