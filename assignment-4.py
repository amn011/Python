# Q1-print key word and get their meaning as their value using dictionary:

myDict={
"dabba": "box",
"kalam": "pen",
"kaam": "work",
"pankha": "fan" 

}
print("options are ", myDict.keys())
a= input("enter the hindi word to know english\n")
print("meaning of your hindi word is: ", myDict[a])



# Q2- enter 8 numbers and display all the unique numbers:

n1= int(input("enter number 1\n"))
n2= int(input("enter number 2\n"))
n3= int(input("enter number 3\n"))
n4= int(input("enter number 4\n"))
n5= int(input("enter number 5\n"))
n6= int(input("enter number 6\n"))
n7= int(input("enter number 7\n"))
n8= int(input("enter number 8\n"))

s={ n1, n2, n3, n4, n5, n6, n7, n7, n8 }
print("unique numbers are ", s)
