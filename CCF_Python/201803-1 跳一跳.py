#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sum, t = 0, 0
for n in input().split():
    n = int(n)
    if n == 0:
        print(sum)
    elif n == 1:
        t = 0
        sum += 1
    elif n == 2:
        t += 1
        sum += t * 2