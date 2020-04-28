import math
print("Welcome to Average App")

name = str(input("Enter the Student name: "))

no_grades = int(input("Num of grades u want to enter: "))

grades = []
for i in range(no_grades):
    grade = float(input("Enter  " +str(i+1) + "st grade "))
    grades.append(grade)
sd= sum(grades)/len(grades)

s=round(sd ,3)
print(grades)
                  
print("\n" + str(s))
