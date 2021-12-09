#!/usr/bin/env python3.10
from loguru import logger
from aocd import get_data, submit

INPUT = list(map(int, get_data(day=1, year=2021).splitlines())) # Load data as a list of ints (from the initial big string)
logger.debug('Loaded input data')

result = 0
for i, depth in enumerate(INPUT):
    if i == 0:
        logger.trace('First depth, skipping...')
        continue
    elif INPUT[i - 1] < depth:
        result += 1
logger.success(f'Parsed input, result: {result}')

submit(result, day=1, year=2021)
logger.success('Uploaded result')