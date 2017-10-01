import random
import os
import sys


random_num = random.randrange(0,100)

while(random_num !=15):
    print(random_num)
    random_num = random.randrange(0,100)

i=0
while(i<=20):
    if(i%2==0):
        print(i)
    elif(i==9):
        print(i)
        break;
    else:
        i+=1
        continue
