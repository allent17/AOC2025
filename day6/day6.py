# aoc_template.py
import math
import sys
import pathlib
import numpy as np
from io import StringIO

def load_data_split_last(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        data_lines = lines[:-1]
        last_line = lines[-1].strip() # Use strip() to remove newline characters

    if data_lines: # Check if there are lines to load
        # Use StringIO to treat the list of lines as a single file-like object for numpy
        data_array = np.loadtxt(StringIO("".join(data_lines)))
    else:
        data_array = np.array([]) # Return an empty array if no data lines exist

    return data_array, last_line.split()

def perform_math(operation, numbers):
    if operation == "+":
        return sum(numbers)
    if operation == "*":
        return math.prod(numbers)
    return 0

def part1(filename):
    """Solve part 1."""
    total = 0
    (numbers, operations) = load_data_split_last(filename)
    for col_idx, column in enumerate(numbers.T):
        result = perform_math(operations[col_idx], column)
        print(f"{numbers[:, col_idx]} {operations[col_idx]} = {result}")
        total += result
    return total

def parse(puzzle_input):
    lines = puzzle_input.splitlines()
    print("\n--- Parsed Lines ---")
    for i, line in enumerate(lines):
        print(f"Line {i + 1}: '{line}'")
    return lines

def part2(filename):
    """Solve part 2."""
    puzzle_input = pathlib.Path(filename).read_text().strip()
    lines = parse(puzzle_input)
    index = 0
    last_line = lines[len(lines) - 1]
    print(last_line)
    total = 0
    result = 0
    numbers = []
    operation = ""
    longest = len(max(lines, key=len))
    while index < longest:
        digits = []
        for line in lines:
            if line != last_line and index < len(line):
                digits.append(line[index])
        num_str = "".join(digits)
        if num_str.isspace():
            # reset numbers
            result = perform_math(operation, numbers)
            total += result
            print(f"{numbers} {operation} = {result}")
            numbers = []
        else:
            if len(num_str) > 0:
                numbers.append(int(num_str))
        if index < len(last_line):
            if (last_line[index] == "+" or last_line[index] == "*"):
                operation = last_line[index]
        index += 1
    result = perform_math(operation, numbers)
    total += result
    print(f"{numbers} {operation} = {result}")
    return total

def solve(filename):
    """Solve the puzzle for the given input."""
    solution1 = part1(filename)
    solution2 = part2(filename)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        solutions = solve("data.txt")
        print("\n".join(str(solution) for solution in solutions))