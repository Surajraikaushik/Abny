
#vvvv imp que

max_no = int(input("Enter the Maximum range-----"))

lst_rng = list(range(1,max_no+1))

binary =[]
hexadecimal=[]

for num in lst_rng:
    binary.append(bin(num))
    hexadecimal.append(hex(num))


lower_range = int(input(" Enter the Lower range-----"))
upper_range = int(input(" Enter the higher range----"))
                  

for  num in binary[lower_range-1 : upper_range]:
    print(num)

for no in hexadecimal[lower_range-1 : upper_range]:
    print(no)

for d, b, h in zip(lst_rng, binary, hexadecimal):
     print(str(d) + "----" + str(b) + "----" + str(h))
