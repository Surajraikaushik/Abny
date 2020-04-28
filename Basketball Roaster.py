print(" Welcome to Favourite teaching ")

fav_teachers = []

name = str(input("Who is your first favorite teacher---").title())
fav_teachers.append(name)

name = str(input("Who is your second favorite teacher---").title())
fav_teachers.append(name)

name = str(input("Who is your third favorite teacher---").title())
fav_teachers.append(name)

name = str(input("Who is your fourth favorite teacher---").title())
fav_teachers.append(name)

print("Your favorite teachers ranked are :\n"+str(fav_teachers))

fav_teachers.sort()
print("Your favorite teachers alphabetically are: " + str(fav_teachers))

fav_teachers.sort(reverse = True)
print("Your favorite teachers in reverse alphabetical order are: " + str(fav_teachers))


