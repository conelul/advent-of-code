#!/usr/bin/env python3.10
from loguru import logger
from aocd import get_data, submit

INPUT = get_data(day=2, year=2021).splitlines()
logger.success('Loaded data')

aim = 0
depth = 0
horizontal = 0

for line in INPUT:
    direction, amount = line.split(' ')
    match direction:
        case 'down':
            aim += int(amount)
        case 'up':
            aim -= int(amount)
        case 'forward':
            horizontal += int(amount)
            depth += aim * int(amount)
logger.success('Parsed the input data')
logger.debug(f'Aim: {aim} - Depth: {depth} - Horizontal: {horizontal}')

result = depth * horizontal
logger.debug(f'Result: {result}')

submit(result, day=2, year=2021)
logger.success('Submitted the result')