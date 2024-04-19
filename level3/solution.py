#!/usr/bin/env python
import sys

def find_start_positions(lawn, height, width):
    border_positions = []

    border_positions.extend((x, 0) for x in range(width) if lawn[0][x] == '.')
    border_positions.extend((x, height-1) for x in range(width) if lawn[height-1][x] == '.')

    border_positions.extend((0, y) for y in range(1, height-1) if lawn[y][0] == '.')
    border_positions.extend((width-1, y) for y in range(1, height-1) if lawn[y][width-1] == '.')

    return border_positions

def is_valid_path(width, height, lawn, path, start_x, start_y):
    x, y = start_x, start_y
    visited = set([(x, y)])

    print(f"Starting in: x={start_x}, y={start_y}", file=sys.stderr)

    moves = {
        'W': (0, -1),
        'D': (1, 0),
        'S': (0, 1),
        'A': (-1, 0)
    }

    for move in path:
        dx, dy = moves[move]
        x += dx
        y += dy

        print(f"Moving to x={x}, y={y} after movement {move}", file=sys.stderr)

        if not (0 <= x < width and 0 <= y < height) or lawn[y][x] == 'X' or (x, y) in visited:
            return False

        visited.add((x, y))

    all_free_cells = {(ix, iy) for iy in range(height) for ix in range(width) if lawn[iy][ix] == '.'}

    if visited == all_free_cells:
        print("All free cells was visited only one time.\n", file=sys.stderr)
        return True

    print("Some free cells wasn't visited.\n", file=sys.stderr)
    return False

input_data = sys.stdin.read().strip().split('\n')
n = int(input_data[0])
index = 1

for i in range(n):
    print(f"\nProcessing {i}", file=sys.stderr)
    width, height = map(int, input_data[index].split())
    index += 1
    lawn = [input_data[index + i].strip() for i in range(height)]
    index += height
    path = input_data[index].strip()
    index += 1

    start_positions = find_start_positions(lawn, height, width)
    valid_path_found = False
    for start_x, start_y in start_positions:
        if is_valid_path(width, height, lawn, path, start_x, start_y):
            print("VALID")
            valid_path_found = True
            break

    if not valid_path_found:
        print("INVALID")
