#print the multiplication table of any number using for loop:

a=int(input("enter number :"))
for i in range(1,11):
    print(str(a)+ str("x")+ str(i)+ str("=") +str(a*i))