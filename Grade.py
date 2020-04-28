
print("Welcome to the Grade System")

grades = []
grade = int(input(" Enter the Grade 1 "))
grades.append(grade)
grade = int(input(" Enter the Grade 2 "))
grades.append(grade)
grade = int(input(" Enter the Grade 3 "))
grades.append(grade)
grade = int(input(" Enter the Grade 4 "))
grades.append(grade)

grades.sort(reverse = True)
sd = len(grades)
print(sd)

rem = grades.pop()

print("The maximum grade " + str(grades[sd-2])+ " & The smallest one is " + str(grades[0]))

print(grades)
