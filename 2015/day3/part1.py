#!/usr/bin/env python3.10
from loguru import logger
from aocd import get_data, submit

INPUT = get_data(day=3, year=2015)

santa_moves = [0, 0]
visited = [[0, 0]]

for i, direction in enumerate(INPUT):
    if i % 2 == 0:
    match direction:
        case '>':
            santa_moves[0] += 1
        case '<':
            santa_moves[0] -= 1
        case '^':
            santa_moves[1] += 1
        case 'v':
            santa_moves[1] -= 1

    if santa_moves not in visited:
        visited.append(santa_moves.copy())

res = len(visited)

logger.info(f"Result: {res}")
submit(res, day=3, year=2015)