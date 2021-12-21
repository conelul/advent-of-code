#!/usr/bin/env python3.10
from aocd import get_data, submit
from functools import reduce

def main() -> None:
    # ( ͡° ͜ʖ ͡°) Teehee fancy one liner go brrrrrrrr
    submit(len([char for char in reduce(lambda x,y: x+y, [line.split('| ')[1].split() for line in get_data(day=8, year=2021).splitlines() ]) if len(char) in (2, 3, 4, 7)]), part=1, day=8, year=2021)
    
if __name__ == '__main__':
    main()