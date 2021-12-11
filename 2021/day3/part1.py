#!/usr/bin/env python3.10
from loguru import logger
from aocd import get_data, submit
from collections import Counter

INPUT = get_data(day=3, year=2021).splitlines()
logger.success('Loaded input list')

BINARY_LENGTH = len(INPUT[0]) # Determine how long the binary terms are

gamma = ""
epsilon = ""
columns_count = [Counter() for _ in range(BINARY_LENGTH)]

for row in INPUT: # For every number
    for index, column in enumerate(row): # For every "column" (individual bit)
        columns_count[index][column] += 1
logger.success('Counted column frequencies')

for count in columns_count:
    gamma += count.most_common()[0][0]
    epsilon += count.most_common()[1][0]
logger.success(f'Determined Gamma and Epsilon numbers: {gamma} and {epsilon}')

result = int(gamma, base=2) * int(epsilon, base=2)

submit(result, day=3, year=2021)
logger.success(f'Submitted {result} as the result')