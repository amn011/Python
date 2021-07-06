#this program will access a file fron your directory and you manipulate them:

f=open('sample.txt', 'r')      #----> opens file named sample.txt
data=f.read()                  #----> will read the file
print(data)                    #----> print the text from file on screen
f.close()                      #----> closes the file(always remember to close the opened file)