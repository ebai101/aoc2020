#!/usr/bin/env python3
# this is just...not good

import re

class Passport:
    def __init__(self, entry):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None

        for i in entry:
            label = i[:3]
            value = i[4:]

            if label == 'byr':
                self.byr = int(value)
            elif label == 'iyr':
                self.iyr = int(value)
            elif label == 'eyr':
                self.eyr = int(value)
            elif label == 'hgt':
                self.hgt = value
            elif label == 'hcl':
                self.hcl = value
            elif label == 'ecl':
                self.ecl = value
            elif label == 'pid':
                self.pid = value

    def validate(self):
        try:
            # print('checking byr', self.byr)
            assert self.byr is not None
            assert self.byr >= 1920 and self.byr <= 2002

            # print('checking iyr', self.iyr)
            assert self.iyr is not None
            assert self.iyr >= 2010 and self.byr <= 2020

            # print('checking eyr', self.eyr)
            assert self.eyr is not None
            assert self.eyr >= 2020 and self.eyr <= 2030

            # print('checking hgt', self.hgt)
            assert self.hgt is not None
            if self.hgt[-2:] == 'cm':
                assert int(self.hgt[:-2]) >= 150 and int(self.hgt[:-2]) <= 193
            elif self.hgt[-2:] == 'in':
                assert int(self.hgt[:-2]) >= 59 and int(self.hgt[:-2]) <= 76
            else: raise AssertionError

            # print('checking hcl', self.hcl)
            assert self.hcl is not None
            assert len(re.findall(r'^#[0-9A-F]{6}$', self.hcl.upper())) > 0

            # print('checking ecl', self.ecl)
            assert self.ecl is not None
            assert self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

            # print('checking pid', self.pid)
            assert self.pid is not None
            assert self.pid.isdigit()
            assert len(self.pid) == 9

        except AssertionError as e:
            # print('invalid\n')
            return False
        else:
            print('byr: 1920', self.byr, '2002')
            print('iyr: 2010', self.iyr, '2020')
            print('eyr: 2020', self.eyr, '2030')
            if self.hgt[-2:] == 'cm':
                print('hgt: 150cm', self.hgt, '193cm')
            elif self.hgt[-2:] == 'in':
                print('hgt: 59in', self.hgt, '76in')
            print('hcl:', self.hcl)
            print('ecl:', self.ecl)
            print('pid:', self.pid, len(self.pid))
            print()
            return True

with open('input.txt', 'r') as f:
    count = 0
    data = []
    for i in f.read().split('\n\n'):
        data.append(i.replace('\n', ' ').strip().split())

    for entry in data:
        passport = Passport(entry)
        if passport.validate():
            count += 1

    print(count)
