#!/usr/bin/env python3.10
from loguru import logger
from aocd import get_data, submit

INPUT = get_data(day=1, year=2015)
logger.debug("Loaded input data")

floor = 0
for index, char in enumerate(INPUT):
    logger.info(f"Index: {index}")
    if floor == -1:
        position = index
        break # Break so you don't reassign
    if char == '(': floor += 1
    elif char == ')': floor -= 1

logger.debug("Parsed input data successfully")

submit(position, day=1, year=2015)
logger.success(f"Submitted result: {position}")