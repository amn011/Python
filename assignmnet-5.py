m1= float(input("enter makrs in subj-1: "))
m2= float(input("enter makrs in subj-2: "))
m3= float(input("enter makrs in subj-3: "))
m4= float(input("enter makrs in subj-4: "))
m5= float(input("enter makrs in subj-5: "))

m6= (m1+m2+m3+m4+m5/5)
if(m6<50):
    print("F")
elif(m6>50 and m6<60):
    print("D")
elif(m6>60 and m6<70):
    print("C")
elif(m6>70 and m6<80):
    print("B")
elif(m6>80 and m6<90):
    print("A")
else:
    print("A+")



