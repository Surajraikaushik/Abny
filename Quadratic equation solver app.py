#ax^2 +bx+c =0

import cmath
x = round(2.023, 1)

print(x)
print("Welcome to the Quadratic Equation Solver App. ")
print("A complex number has two parts:  a + bj where b is imaginery part ")

no_of_enq = int(input("No of equation solve---"))

for i in range(no_of_enq):
     print("Equation solve for" +str(i+1))
     a = float(input("Enter the x**2 cofficient ----"))
     b = float(input("Enter the x cofficient ----"))
     c = float(input("Enter the c value ----"))

     x1 = (-b+cmath.sqrt(b**2 -4*a*c))/(2*a)
     x2 = (-b-cmath.sqrt(b**2 -4*a*c))/(2*a)
     

     print("Value of x1" +str(x1))
     print("Value of x2" +str(x2))
    
                   
