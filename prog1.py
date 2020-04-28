"""
# Letter count

fd = 'RAIAbhinay'
sj = fd.lower()
s = input('letter')
ad=s.lower()
print(ad)
d=sj.count(ad)
print(d)
# Right angle triangle
"""
import math

#de= float(input(" Enter default value"))
#wd = def1
le = float(input("Please enter the Lenght :  "))
bt = float(input("Please enter the width  :  " ))
hypt  = int(input("Enter hypt "))
if hypt > 0:
    print("Hypotenuse of the right triangel by default " + str(hypt)
          +" please don't enter value " )
else:
    hyp = math.sqrt(le**2 + bt**2)
    sd = round(hyp,3)
    print("Hypotenuse of the right triangel " + str(sd))
    
if le == 0:
    le =math.sqrt(hypt**2 - bt**2)

if bt == 0 :
    bt =math.sqrt(hypt**2 - le**2)
    

area = 0.5*le*bt
ara = round(area , 2)
print("Area of the right angle traiangle " + str(ara))


