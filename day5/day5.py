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

def parse_database(data):
    range_mode = True
    ranges = []
    ingredient_ids = []

    for line in data:
        if line == "":
            range_mode = False
        else:
            if range_mode:
                range_str = line.split('-')
                ranges.append((int(range_str[0]), int(range_str[1])))
            else:
                ingredient_id = int(line)
                ingredient_ids.append(ingredient_id)
    return ranges, ingredient_ids

def part1(data):
    """Solve part 1."""
    (ranges, ingredient_ids) = parse_database(data)
    print(ranges)
    print(ingredient_ids)
    total_valid = 0
    for ingredient_id in ingredient_ids:
        valid = False
        for cur_range in ranges:
            if ingredient_id >= cur_range[0] and ingredient_id <= cur_range[1]:
                valid = True
        if valid:
            total_valid += 1
    return total_valid


def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by their start points
    intervals.sort(key=lambda x: x[0])

    merged = []
    for current_start, current_end in intervals:
        if not merged or current_start > merged[-1][1]:
            # No overlap, or merged list is empty, add the current interval
            merged.append([current_start, current_end])
        else:
            # Overlap exists, merge with the last interval in 'merged'
            merged[-1][1] = max(merged[-1][1], current_end)

    return [tuple(r) for r in merged]  # Convert back to tuples for consistency

def part2(data):
    """Solve part 2."""
    (ranges, ingredient_ids) = parse_database(data)
    print(ranges)
    merged = merge_intervals(ranges)
    print(merged)
    total = 0
    for cur_range in merged:
        total += cur_range[1] - cur_range[0] + 1
    return total

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