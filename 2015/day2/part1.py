#!/usr/bin/env python3.10
from loguru import logger
from aocd import get_data, submit

INPUT = [list(map(int, box.split('x'))) for box in get_data(day=2, year=2015).splitlines()] # Get individual box dimensions and convert to ints
logger.debug("Loaded and formatted input data")

sqft_paper = 0
for box in INPUT:
    box.sort()
    sqft_paper += 2 * (box[0] * box[1]) + 2 * (box[1] * box[2]) + 2 * (box[0] * box[2]) # Add box surface area to total area of wrapping paper
    sqft_paper += box[0] * box[1] # Add the smallest side's area as the "extra" value
logger.debug("Parsed the input successfully")

submit(sqft_paper, day=2, year=2015)
logger.success(f"Submitted the result: {sqft_paper}")