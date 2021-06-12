# to find result of a student if pass or fail:

m1=int(input("enter marks in physics  :"))
m2=int(input("enter marks in chemistry :"))
m3=int(input("enter marks in mathematics :"))
sum=(m1+m2+m3)/3
print("total marks obtained is :", sum)

if(sum>40):
    print("PASS")
elif(sum>33 and sum<40):
    print("PASS but not Eligible")
else:
    print("FAIL")        