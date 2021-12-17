#!/usr/bin/env python3.10
from loguru import logger
from aocd import get_data, submit

INPUT = get_data(day=1, year=2015)
logger.debug("Loaded input data")

floor = 0
for char in INPUT:
    if char == '(': floor += 1
    else: floor -= 1
logger.debug("Parsed the input successfully")

submit(floor, day=1, year=2015)
logger.success(f"Submitted result: {floor}")