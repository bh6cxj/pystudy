#!/usr/bin/env python3

sum = 0
MyList = []
for i in range(1,50):
    MyList.append(i)

for j in MyList:
    if j <= 1:
        isPrime = False
    elif j == 2 or j == 3:
        isPrime = True
    else:
        for k in range(2,int(j/2)+1):
            if j%k == 0:
                isPrime = False
                break
        else:
            isPrime = True
    if isPrime == True:
        sum +=1

print("Prime number sum is %d" % sum)
