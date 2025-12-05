# aoc_template.py

import pathlib
import sys
import re

def check_invalid(ranges):
    result = 0
    for i in range(int(ranges[0]),int(ranges[1])):
        if has_same_halves(i):
            result += i
    return result

def has_same_halves(number):
    num_str = str(number)
    length = len(num_str)
    if length % 2 != 0:  # Check for odd length
        return False
    midpoint = length // 2
    first_half = num_str[:midpoint]
    second_half = num_str[midpoint:]
    return first_half == second_half

def check_invalid2(ranges):
    result = 0
    for i in range(int(ranges[0]),int(ranges[1])):
        pattern = has_repeated_sets(str(i))
        if pattern != None:
            result += i
    return result

def has_repeated_sets(s):
    pattern = r"(.+?)\1+"
    match = re.fullmatch(pattern, s)
    if match:
        #print(f"{match.group(1)} in {s}")
        return match.group(1) # Returns the captured repeating set
    return None

def parse(puzzle_input):
    return puzzle_input.split(',')

def part1(data):
    """Solve part 1."""
    result = 0
    for product_id in data:
        range = product_id.split('-')
        result += check_invalid(range)
        #print(f"{range[0]} - {range[1]} : {result}")
    return result

def part2(data):
    """Solve part 2."""
    result = 0
    for product_id in data:
        range = product_id.split('-')
        result += check_invalid2(range)
        #print(f"{range[0]} - {range[1]} : {result}")
    return result

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))