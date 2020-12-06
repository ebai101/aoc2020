#!/usr/bin/env python3

def calc_seat_id(entry):
    row = 0
    col = 0
    for direction in entry[0:7]:
        row = row << 1
        if direction == 'B':
            row = row ^ 1
    for direction in entry[7:10]:
        col = col << 1
        if direction == 'R':
            col = col ^ 1
    return int(row) * 8 + int(col)

with open('input.txt', 'r') as f:
    max_id = 0
    id_list = []

    for line in f:
        cur_id = calc_seat_id(line)
        id_list.append(cur_id)

        if cur_id > max_id:
            max_id = cur_id
    print('part1:', max_id)

    id_list.sort()
    for i in range(len(id_list)):
        if i > 0:
            if id_list[i] - id_list[i-1] > 1:
                print('part2:', id_list[i] - 1)

