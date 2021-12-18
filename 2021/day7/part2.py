#!/usr/bin/env python3.10
from aocd import get_data, submit

def main() -> None:
    INPUT = get_data(day=7, year=2021).split(",")
    positions = list(map(int, INPUT))

    fuel_vals = []
    for align_pos in range(max(positions)):
        fuel = 0
        for initial_pos in positions:
            fuel += sum(range(1, abs(initial_pos - align_pos) + 1))
        fuel_vals.append((align_pos, fuel))

    _, res = min(fuel_vals, key=lambda x: x[1])
    print(res)
    submit(res, part=2, day=7, year=2021)

if __name__ == "__main__":
    main()