#!/usr/bin/env python3.10
from loguru import logger
from aocd import get_data, submit

INPUT = list(map(int, get_data(day=1, year=2021).splitlines())) # Load data as a list of ints (from the initial big string)
logger.debug('Loaded the input data')

result = 0
# First value to compare against
compare_value = INPUT[0] + INPUT[1] + INPUT[2]

for i in range(1, len(INPUT) - 2): # For every group of three
    current_value = INPUT[i] + INPUT[i + 1] + INPUT[i + 2]
    
    if current_value > compare_value:
        result += 1
        
    compare_value = current_value

logger.success(f'Parsed input, result: {result}')
submit(result, part='b', day=1, year=2021)
