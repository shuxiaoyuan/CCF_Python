#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 输入
line_one = input()
line_two = input()

# 对输入进行处理
n, L, t = [int(n) for n in line_one.split()]
balls_pos = [int(n) for n in line_two.split()]

# 球类
class Ball:
    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction
        
# 创建球的数组
balls = [Ball(pos, -1 if pos == L else 1) for pos in balls_pos]

# 记录每个位置上球的数量
ball_nums = [1 if pos in balls_pos else 0 for pos in range(L + 1)]
        
# 经过 t s 的运动
for i in range(t):
    # 运动只改变位置
    for ball in balls:
        ball_nums[ball.pos] -= 1    # 当前位置球的数量减一
        ball.pos += ball.direction  # 球运动
        ball_nums[ball.pos] += 1    # 球运动后所在位置的球的数量加一
    # 检查只改变方向
    for ball in balls:
        if ball.pos == L and ball.direction == 1:       # 位置到右端且方向向右
            ball.direction = -1
        elif ball.pos == 0 and ball.direction == -1:    # 位置到左端且方向向左
            ball.direction = 1
        elif ball_nums[ball.pos] == 2:                  # 位置不在两端，但当前位置有两个球
            ball.direction *= -1
            
# 打印结果
for ball in balls:
    if ball == balls[-1]:
        print(ball.pos, end='')
    else:
        print(ball.pos, end=' ')
print()
    
        
            
            
            