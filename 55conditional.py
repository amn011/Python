# get message as input and check if it is a spam or not:


text= input("enter the message : ")
if("a lot of money" in text):
    print("spam detected")
elif("buy now" in text):
    print("spam detected")
elif("subscribe now" in text):
    print("spam detected")
else:
    print("not a spam")