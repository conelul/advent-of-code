#!/usr/bin/env python3.10
from aocd import get_data, submit
from statistics import median

def main() -> None:
    INPUT = get_data(day=7, year=2021)
    positions = list(map(int, INPUT.split(",")))
    optimal_pos = int(median(positions))
    
    fuel_vals = [abs(pos - optimal_pos) for pos in positions]
    
    res = sum(fuel_vals)
    print(res)
    submit(res, day=7, year=2021)

if __name__ == '__main__':
    main()