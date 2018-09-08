#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 输入 n, k
n, k = [int(i) for i in input().split()]

# 建立以 Person 对象为节点的循环链表
class Person:
    def __init__(self, id):
        self.id = id
        self.next = None
        
persons = Person(1)
firstp = persons
for i in range(2, n+1):
    persons.next = Person(i)
    persons = persons.next
    
persons.next = firstp

# 开始游戏
num = 1;
winner = firstp
pre = persons
while winner.next != winner:
    if num % k == 0 or str(num)[-1] == str(k):
        pre.next = winner.next
    else:
        pre = pre.next
    winner = winner.next
    num += 1
        
print(winner.id)