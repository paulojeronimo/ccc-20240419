#!/usr/bin/env python
import sys

input_lines = sys.stdin.read().strip().split()
paths = input_lines[1:]

for path in paths:
    x, y = 0, 0
    min_x, max_x = 0, 0
    min_y, max_y = 0, 0

    for direction in path:
        if direction == 'W':
            y += 1
        elif direction == 'D':
            x += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'A':
            x -= 1
        
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    print(width, height)
