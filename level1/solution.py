#!/usr/bin/env python
import sys

input_lines = sys.stdin.read().strip().split()

paths = input_lines[1:]

for path in paths:
    north = path.count('W')
    east = path.count('D')
    south = path.count('S')
    west = path.count('A')

    print(north, east, south, west)
