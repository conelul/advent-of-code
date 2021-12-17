#!/usr/bin/env python3.10
from loguru import logger
from aocd import get_data, submit

INPUT = [list(map(int, box.split('x'))) for box in get_data(day=2, year=2015).splitlines()] # Get individual box dimensions and convert to ints
logger.debug("Loaded the input data")

ribbon = 0
for box in INPUT:
    box.sort()
    ribbon += 2 * box[0] + 2 * box[1] # Add the smallest perimeter
    ribbon += box[0] * box[1] * box[2] # Add the volume
logger.debug("Successfully parsed the input")

logger.info(f"Result: {ribbon}")
submit(ribbon, day=2, year=2015)
logger.debug("Successfully submitted the result")
