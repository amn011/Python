myDICT= {
"name": "Aman",
"course": "B.Tech",
"marks": "[64, 74, 89]",
1:2
}

#dictionary methods:


print(myDICT.values())   #print the values from dictionary
print(myDICT.items())    #print the all items(key,value) from dictionary

updateDICT={
"name": "Kumar"
}

myDICT.update(updateDICT)  #update the dictionary
print(myDICT)

print(myDICT.get("name"))


