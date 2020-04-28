import math
print("Welcome to factorial App")

num = int(input("Enter the number for factorial"))
x=1
for i in range(1, num+1):
    x=x*i
    
print(x)

y = math.factorial(num)

print(y)
