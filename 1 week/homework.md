1.range函数中，当start比stop小的时候会发生什么情况？
  range函数中，当step为负数时，会产生什么情况？

    1. range(m,n)
        M > N, 返回空。
        M < N, 返回[M,N),step = 1，升序列表
        3.X中range()函数直接执行范围本身
        >>>range(0,10)
        range(0,10)
    2.range(m,n,s)
        M > N 且 s < 0, 返回[M,N)，step = |s| 的降序列表。

2. 在程序中给定一个int常量，你有三次机会猜数字的大小，如果猜中，输出congratulations! you win!，如果机会用完，还未猜中，输出Oops! you fail!
    可以使用input函数获取输入
    可以使用int函数把输入转化为整型

    #!/usr/bin/env python3
    # -*- coding:utf-8 -*-

    import random

    while True:
        for i in range(3,0,-1):
            guest = input("请猜0~7的整数,你还有" + str(i) + "次机会哦！ ：")
            if str(guest).isdigit() and int(guest) <= 7 and int(guest) >= 0:
                answer = random.randint(0,7)
                if int(guest) == answer:
                    print("Congratulations! you win!")
                    break
                elif i == 1:
                    print("Oops! you fail!")
            else:
                print("请输入0~7之间的整数！！！")
                break

3.给定一个列表，其中一些元素是重复的，请移除重复的元素，只保留第一个，并且保持序列原来的次序。
例如：[1,3,2,4,3,4,2,5,5,7]
输出：[1, 3, 2, 4, 5, 7]

    #!/usr/bin/env python3

    ls1 = [1,3,2,4,3,4,2,5,5,7]
    ls2 = []

    for i in ls1:
        if i not in ls2:
            ls2.append(i)

    print(ls2)

4.给定一个列表，其中元素为正整数，计算其中素数个数？
例如：[2,3,4,5,6,7] 输出 4

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