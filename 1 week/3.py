#!/usr/bin/env python3


ls1 = [1,3,2,4,3,4,2,5,5,7]
ls2 = []

for i in ls1:
    if i not in ls2:
        ls2.append(i)

print(ls2)