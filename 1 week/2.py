#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import random

while True:
    answer = random.randint(0,7)
    for i in range(3,0,-1):
        guess = input("请猜0~7的整数,你还有" + "\033[031m" + str(i) + "\033[0m" + "次机会哦！ ：")
        if str(guess).isdigit() and int(guess) <= 7 and int(guess) >= 0:
            if int(guess) == answer:
                print("\033[032mCongratulations! you win!\033[0m")
                break
            elif i == 1:
                print("\033[031mOops! you fail!\033[0m")
            else:
                print("You are wrong! Guess again!")
        else:
            print("请输入0~7之间的整数！！！")
            break