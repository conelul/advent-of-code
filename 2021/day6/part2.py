#!/usr/bin/env python3.10
from aocd import get_data, submit

def inital_freq(li: list[int]) -> dict:
    freqs = {}
    for i in range(9):
        freqs[i] = li.count(i)
    return freqs

def main() -> None:
    INPUT = get_data(day=6, year=2021).split(",")
    fishies = list(map(int, INPUT))
    DAYS = 256
    
    freqs = inital_freq(fishies)    
    for _ in range(DAYS):
        prev_freqs = freqs.copy()
        for i in range(0, len(freqs)):
            freqs[i] = prev_freqs[(i+1)%9]
        freqs[6] += prev_freqs[0]

    res = sum(freqs[key] for key in freqs)
    print(res)
    submit(res, day=6, year=2021)

if __name__ == '__main__':
    main()