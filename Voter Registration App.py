print("Welcome to Voter Registraion App .")

party_lst =["Hindu yuwa wahini","BJP","Congress" ,"Samajwadi Party " ,"BSP"]

name = str(input("Please enter the voter name " ))
age = int(input("Please enter the voter age " ))

if age > 18:
    print("Congratulations "+ name +" ! You are old enough to register to vote. ")
    print("Here list of the Political Parties :")
    for i in party_lst:
        print('-' + i)
        
    choice = str(input("What party would you like to join :"))
    if choice in party_lst:
        print("Congratulations " +name +" !"+"You have joined the " + str(choice) + " Party !")
        if choice == "BJP" or "Congress":
            print("That is a major party!" )
        else :
            print("You are an independent person! ")
        
    else:
        print("Hey your party not register for this Election")
              
        
else:
    print("You are not old enough to register to vote. ")

