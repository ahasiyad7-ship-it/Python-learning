name = input("Enter customer name:")
amount = int(input("Enter purchase amount:"))
is_member = input("Are you a member?(Yes/No)")

if(amount>=1000 and is_member == "Yes"):
    print("You got 20% discount")
elif(amount>=1000 or is_member == "No"):
    print("You got 10% discount")
else:
    print("No discount available")

print("Thankyou for shopping,",name)
