print("Welcome to the Shipping Accounts Program.")

users = []

no_of_user = int(input("Enter the no of user ") )

for i in range(1, no_of_user+1):
    user = str(input("Please Enter the name ")).lower().strip()
    users.append(user)
name = input("Hello, what is your username:").lower().strip()
        

if name in users:
    print("Hello" + str(name)+"."+  "Welcome back to your account. ")
    print("Current shipping prices are as follows:")
    print("\nShipping orders 0 to 100: \t\t$5.10 each")
    print("Shipping orders 100 to 500: \t\t$5.00 each")
    print("Shipping orders 500 to 1000: \t\t$4.95 each")
    print("Shipping orders over 1000: \t\t$4.80 each")

    quantity = int(input("\nHow many items would you like to ship: "))
    if quantity < 100:
          cost = 5.10
    elif quantity < 500:
          cost = 5.00
    elif quantity < 1000:
          cost = 4.95
    else:
          cost = 4.80

    bill = quantity*cost
    bill = round(bill , 2)
    print("To ship " + str(quantity) + " items it will cost you $" + str(bill) + " at $" + str(cost) + " per item.")
    choice = input("\nWould you like to place this order (y/n): ").lower()
    if choice.startswith('y'):
         print("Okay.  Shipping your " + str(quantity) + " items.")
    else:
         print("Okay, no order is being placed at this time.")
         #Our user is not in the list 44 else: 45    
else :
   print("Sorry, you do not have an account with us.  Goodbye.")




 
