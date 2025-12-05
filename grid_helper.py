# grid_helper.py

def load_grid(data):
    # Load grid
    grid = [list(line) for line in data]
    return grid

def print_grid(grid):
    for row in grid:
        # Join the elements of the current row with a space and print
        print("".join(str(item) for item in row))

def get_grid_dimensions(grid):
    """
    Returns the dimensions (rows, columns) of a 2D grid.
    """
    rows = len(grid)
    if rows == 0:
        return 0, 0
    cols = len(grid[0])
    return rows, cols

def get_neighbors(grid, row, col, include_diagonals=False):
    """
    Returns a list of (neighbor_row, neighbor_col, neighbor_char) tuples
    for a given point (row, col) in the grid.
    Optionally includes diagonal neighbors.
    """
    rows, cols = get_grid_dimensions(grid)
    neighbors = []

    # Define relative coordinates for neighbors (up, down, left, right)
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    if include_diagonals:
        # Add diagonal directions
        directions.extend([
            (-1, -1), # Up-Left
            (-1, 1),  # Up-Right
            (1, -1),  # Down-Left
            (1, 1)    # Down-Right
        ])

    for dr, dc in directions:
        n_row, n_col = row + dr, col + dc

        # Check if neighbor is within grid bounds
        if 0 <= n_row < rows and 0 <= n_col < cols:
            neighbors.append((n_row, n_col, grid[n_row][n_col]))

    return neighbors