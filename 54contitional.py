# get 4 numbers as input and print greatest number:
n1= float(input("enter 1st number: "))
n2= float(input("enter 2nd number: "))
n3= float(input("enter 3rd number: "))
n4= float(input("enter 4th number: "))

if(n1>n2 and n1>n3 and n1>n4):
    print(n1)
elif (n2>n1 and n2>n3 and n2>n4):
    print(n2)
elif(n3>n1 and n3>n2 and n3>n4):
    print(n3)
elif(n4>n1 and n4>n2 and n4>n3):
    print(n4)
else:
    print("something wrong")