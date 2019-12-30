# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:08:00 2019

@author: DEVANSH JAIN
"""

print("Game to guess")
print("The word - capital of a country with length-10")
word="WASHINGTON"
word=list(word)
gword="_"*len(word)
gword=list(gword)
count=0
ip=input("enter a guess letter")
while True:
    if ip.upper() in word:
        index=word.index(ip.upper())
        gword[index]=ip.upper()
        print(''.join(gword))
        word[index]="_"
    if '_' not in gword:
        print("You won the match")
        break
    else:
       ip=input("enter a guess letter")
    count=count+1
    print(str(25-count)+ " Attempts left")
    if count>25:
        print("The number of available attempts finished")
        print("You could not win you can try again")


print("The age of %s is %d"%('John',32))

x=['ram','shyam','chin','john','shawn']
age=[32,34,45,54,22]

for i in range(len(x)):
    print("The age of %s is %d"%(x[i],age[i]))










