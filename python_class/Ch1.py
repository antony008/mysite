# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
def grade():
    k = 0
    t = 0
    while k == 0:
        h = float(input('請輸入總分 => '))
        if h <= 0:
            print('別當我是笨蛋，給我重新輸入')
            t = t + 1
        if t == 5:
            print('你完蛋了!!!')
            print('留級!!!')
            os._exit()
        if h > 0:
            k = k + 1
    
    k = 0
    t = 0
    while k == 0:
        s = float(input('請輸入得分 => '))
        if s <= 0 or s >= h:
            print('別當我是笨蛋，給我重新輸入')
            t = t + 1
        if t == 5:
            print('你完蛋了!!!')
            print('留級!!!')
            os._exit()
        if s >= 0 and s <= h:
            k = k + 1          
    
    if s >= h * 0.6:
         print('恭喜，你及格了')
    else:
         print('留級!!!')
grade()         