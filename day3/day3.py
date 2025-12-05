# aoc_template.py

import pathlib
import sys
import array

def parse(puzzle_input):
    lines = puzzle_input.splitlines()
    print("\n--- Parsed Lines ---")
    for i, line in enumerate(lines):
        print(f"Line {i + 1}: '{line}'")
    return lines

def part1(data):
    """Solve part 1."""
    total = 0
    for bank in data:
        batteries = [int(char) for char in bank]
        """Find highest battery on left_pos side"""
        left_pos = 0
        right_pos = len(batteries) - 1
        highest_left_pos = findHighest(batteries, left_pos, right_pos - 1)
        highest_right_pos = findHighest(batteries, highest_left_pos + 1, right_pos)
        print(f"{batteries[highest_left_pos]}{batteries[highest_right_pos]}")
        total += (batteries[highest_left_pos] * 10) +  batteries[highest_right_pos]
    return total

def part2(data):
    """Solve part 2."""
    total = 0
    for bank in data:
        batteries = [int(char) for char in bank]
        """Find highest battery on left_pos side"""
        left_pos = 0
        right_pos = len(batteries) - 11
        pos1 = findHighest(batteries, left_pos, len(batteries) - 12)
        pos2 = findHighest(batteries, pos1 + 1, len(batteries) - 11)
        pos3 = findHighest(batteries, pos2 + 1, len(batteries) - 10)
        pos4 = findHighest(batteries, pos3 + 1, len(batteries) - 9)
        pos5 = findHighest(batteries, pos4 + 1, len(batteries) - 8)
        pos6 = findHighest(batteries, pos5 + 1, len(batteries) - 7)
        pos7 = findHighest(batteries, pos6 + 1, len(batteries) - 6)
        pos8 = findHighest(batteries, pos7 + 1, len(batteries) - 5)
        pos9 = findHighest(batteries, pos8 + 1, len(batteries) - 4)
        pos10 = findHighest(batteries, pos9 + 1, len(batteries) - 3)
        pos11 = findHighest(batteries, pos10 + 1, len(batteries) - 2)
        pos12 = findHighest(batteries, pos11 + 1, len(batteries) - 1)

        result = str(batteries[pos1]) + str(batteries[pos2]) + str(batteries[pos3]) + str(batteries[pos4]) + str(batteries[pos5]) + str(batteries[pos6]) + str(batteries[pos7]) +str(batteries[pos8]) + str(batteries[pos9]) + str(batteries[pos10]) + str(batteries[pos11]) + str(batteries[pos12])
        print(f"{result}")
        total += int(result)
    return total

def findHighest(batteries, starting_pos, end_pos):
    pos = starting_pos
    highest_pos = starting_pos
    while pos <= end_pos:
        if batteries[pos] > batteries[highest_pos]:
            highest_pos = pos
        pos += 1
    return highest_pos

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