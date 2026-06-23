day ="tuesday"
match(day):
  case"monday":
    print("it's Monday!")
  case"tuesday":
    print("it's Tuesday") 
  case"thursday":
    print("its's another day.")
  case"friday":
    print("It's Friday!")
  case"saturday":
    print("It's Saturday")
  case"sunday":
    print("it's Sunday!")
  case _:
    print("invalid")           