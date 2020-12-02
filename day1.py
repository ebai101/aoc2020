#!/usr/bin/env python3

numbers = []

with open('day1.txt', 'r') as f:
    for i in f:
        numbers.append(int(i))

for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == 2020:
                print(i, j, k, i * j * k)
