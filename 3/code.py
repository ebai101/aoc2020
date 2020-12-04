#!/usr/bin/env python3

def traverse(over, down):
    idx = 0
    count = 0
    line_index = -1

    with open('input.txt', 'r') as f:
        for line in f:
            line_index += 1
            if line_index % down:
                continue
            if line[idx % 31] == '#':
                count += 1
            idx += over
    return count

print(traverse(1,1) * traverse(3,1) * traverse(5,1) * traverse(7,1) * traverse(1,2))
