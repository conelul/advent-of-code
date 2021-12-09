#!/usr/bin/env python3.10
from loguru import logger
from aocd import get_data, submit

INPUT = get_data(day=2, year=2021).splitlines()

depth = 0
horizontal = 0

for line in INPUT:
    direction, amount = line.split(' ')
    match direction:
        case 'forward':
            horizontal += int(amount)
        case 'up':
            depth -= int(amount)
        case 'down':
            depth += int(amount)

logger.success('Parsed the input')
logger.debug(f'Depth: {depth} - Horizontal Distance: {horizontal}')

result = depth * horizontal # Multiply because that's what the question asks for

submit(result, day=2, year=2021)
logger.success(f'Submitted the {result} as result')