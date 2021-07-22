# -*- coding: utf-8 -*-
#Day 3 (30 days of coding challenge)
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

i=N
if i%2!=0:
    print('Weird')
elif i>2 and i<5:
    print('Not Weird')
elif i>6 and i<=20:
    print('Weird')
elif i>20 and i<101:
    print('Not Weird')


