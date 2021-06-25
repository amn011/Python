#1st problem:

 name= input("enter your name")
 print("Good Afternoon, "+name)

#2nd problem:

letter=''' Good morning <name>, you
got selecteD for the role of SDE in our 
company. hope you join us as soon as
possible, plz reply back to us before <date> .
thanks.'''

name= input("enter the name")
date= input("enter the date")
letter= letter.replace("<name>", name)
letter= letter.replace("<date>", date)

print(letter)
