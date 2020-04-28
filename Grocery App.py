import  datetime

print("Welcome to the Grocery List App.")

now = datetime.datetime.now()
print("Current Date and Time " + str(now))

groceries = []

grocery = str(input("Enter the grocery  item__ "))
groceries.append(grocery)

grocery = str(input("Enter the grocery  item__ "))
groceries.append(grocery)

grocery = str(input("Enter the grocery  item__ "))
groceries.append(grocery)

grocery = str(input("Enter the grocery  item__ "))
groceries.append(grocery)

print("Here your grocery list:\n" + str(groceries))

groceries.sort()
print("Here your sorted grocery list:\n" +str(groceries) +"\n")

b = len(groceries)

print("No of items in your list....." + str(b))

purchase = str(input("Enter the item u purchased :\n"))
groceries.remove(purchase)

a = len(groceries)

print("No of items in your list....." + str(a))
print("Here your grocery list to yet purchase:\n" +str(groceries))               
