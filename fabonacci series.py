

num = int(input("Enter the number for fabonacci series---"))
fb = [1,1]
for i in range(num-1):
    sd = fb[i]+fb[i+1]
    fb.append(sd)
    
    
print(fb)
