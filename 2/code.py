#!/usr/bin/env python3
import re

class Entry:
    def __init__(self, line):
        res = re.findall(r'(\d+)-(\d+) (.): (.*)', line)[0]
        self.req_char_min = res[0]
        self.req_char_max = res[1]
        self.req_char = res[2]
        self.password = res[3]

    def validate(self):
        char_count = 0
        for c in self.password:
            if c == self.req_char:
                char_count += 1
        valid = char_count >= int(self.req_char_min) and char_count <= int(self.req_char_max)
        print(char_count, 'found,', self.req_char_min + '-' + self.req_char_max, 'range', valid)
        return valid

    def validate_position(self):
        valid = (self.password[int(self.req_char_min) - 1] == self.req_char) ^ (self.password[int(self.req_char_max) - 1] == self.req_char)
        print(self.req_char_min, self.req_char_max, self.req_char, self.password, '-', valid)
        return valid

with open('input.txt', 'r') as f:
    count = 0
    for line in f:
        e = Entry(line)
        if e.validate_position():
            count += 1

    print(count, 'valid passwords')
