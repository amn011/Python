num=int(input("enter the number :"))
prime=True
for i in range(2, num):
    if(num%2==0):
        prime=False
        break
if prime:
    print("it is a prime number")
else:
    print("it is not a prime number")    