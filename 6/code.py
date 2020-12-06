#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    groups = f.read().split('\n\n')
    any_sum = 0
    every_sum = 0

    for g in groups:
        any_sum += len(''.join(set(g.replace('\n', ''))))
        charset = 'abcdefghijklmnopqrstuvwxyz'
        for p in g.split('\n'):
            if len(p) < 1: continue
            for c in charset:
                if c not in p:
                    charset = charset.replace(c, '')
        every_sum += len(charset)

    print('part1:', any_sum)
    print('part2:', every_sum)
