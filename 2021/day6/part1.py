#!/usr/bin/env python3.10
from aocd import get_data, submit

def main() -> None:
    INPUT = get_data(day=6, year=2021).split(",")
    fishies = list(map(int, INPUT))
    DAYS = 80
     
    for _ in range(DAYS):
        fishies = [(fish-1) for fish in fishies]
        [fishies.append(8) for fish in fishies if fish == -1]
        fishies = [fish if fish != -1 else 6 for fish in fishies]
             
    res = len(fishies)
    print(res)
    submit(res, day=6, year=2021)

if __name__ == '__main__':
    main()