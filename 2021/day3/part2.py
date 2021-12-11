#!/usr/bin/env python3.10
from loguru import logger
from aocd import get_data, submit
from collections import Counter

INPUT = get_data(day=3, year=2021).splitlines()
logger.success('Loaded input list')

BINARY_LENGTH = len(INPUT[0]) # Determine how long the binary terms are

columns_count = [Counter() for _ in range(BINARY_LENGTH)]

for row in INPUT: # For every number
    for index, column in enumerate(row): # For every "column" (individual bit)
        columns_count[index][column] += 1
logger.success('Counted column frequencies')

oxygen_rating = INPUT
co2_rating = []
print(columns_count[index].most_common()[0][0])

for index1, row in enumerate(INPUT): # FOr every byte/number
    for index2, bit in enumerate(row): # FOr every bit in that number
        if bit != columns_count[index2].most_common()[0][0]: # If the first bit of the byte isn't the most common, remove it.
            oxygen_rating.pop(index1)
            co2_rating.append(row)

print(oxygen_rating)