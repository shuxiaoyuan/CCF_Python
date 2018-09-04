#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
nums = [int(n) for n in input().split()]
nums.sort()
min = 10000
for i in range(len(nums) - 1):
    res = nums[i+1] - nums[i]
    if res < min:
        min = res
print(min)