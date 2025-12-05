# aoc_template.py

import pathlib
import sys
import copy
import grid_helper

def parse(puzzle_input):
    lines = puzzle_input.splitlines()
    print("\n--- Parsed Lines ---")
    for i, line in enumerate(lines):
        print(f"Line {i + 1}: '{line}'")
    return lines

def part1(data):
    """Solve part 1."""
    # Load grid
    grid = grid_helper.load_grid(data)
    grid_helper.print_grid(grid)

    # Get paper that can be removed
    result = remove_paper(grid)
    return result[1]

def remove_paper(grid):
    result_grid = copy.deepcopy(grid)
    result = 0
    for r_idx, row in enumerate(grid):
        for c_idx, char in enumerate(row):
            if char == '@':
                direct_neighbors = grid_helper.get_neighbors(grid, r_idx, c_idx, True)
                total = 0
                for neighbor in direct_neighbors:
                    if neighbor[2] == '@':
                        total += 1
                #print(f"Coordinate: ({r_idx}, {c_idx}), Value: {char}, total {total}")
                if total < 4:
                    result += 1
                    result_grid[r_idx][c_idx] = '.'
    return (result_grid, result)

def part2(data):
    """Solve part 2."""
    # Load grid
    grid = [list(line) for line in data]
    grid_helper.print_grid(grid)

    # Get paper that can be removed
    final_result = 0
    result = remove_paper(grid)
    final_result += result[1]
    while result[1] > 0:
        result = remove_paper(result[0])
        final_result += result[1]
    grid_helper.print_grid(result[0])
    return final_result

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