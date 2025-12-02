#Captain Cook Robot bartender
#WelcomeCustomer
print("Goodday and welcome to captain cook")
name=input("We would like to know your name \n")
menu="Meatpie, Friedrice, Jollofrice, Chicken"
print(f"Hi there {name} good to have you")
print(f"Here's whats available today {menu}")
order=input("what would like today? /n")
if order == "Meatpie" :
    price=6
elif order == "Chicken":
    price =4
elif order == "Friedrice"   :
    price =8
elif order == "Jollofrice" :
    price= 7
else:print("That is not available today") or exit()
quantity=int(input("How many of that would you like? \n"))
bill= price * quantity
print (f"Okay {name} that would be {bill} dollars")
    
