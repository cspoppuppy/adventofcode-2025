from typing import Tuple, List
from helper import read_input


sample = "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@."

input = read_input("day4_input.txt")


def remove_rolls(grid: List[str]) -> Tuple[int, List[str]]:
    rows = len(grid)
    cols = len(grid[0])
    removed_rolls = 0
    new_grid = grid.copy()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            adjacent_rolls = 0
            # Check top
            if r > 0:
                if grid[r - 1][c] == "@":
                    adjacent_rolls += 1
                if c > 0 and grid[r - 1][c - 1] == "@":
                    adjacent_rolls += 1
                if c < cols - 1 and grid[r - 1][c + 1] == "@":
                    adjacent_rolls += 1

            # Check left & right
            if c > 0 and grid[r][c - 1] == "@":
                adjacent_rolls += 1
            if c < cols - 1 and grid[r][c + 1] == "@":
                adjacent_rolls += 1

            # Check bottom
            if r < rows - 1:
                if grid[r + 1][c] == "@":
                    adjacent_rolls += 1
                if c > 0 and grid[r + 1][c - 1] == "@":
                    adjacent_rolls += 1
                if c < cols - 1 and grid[r + 1][c + 1] == "@":
                    adjacent_rolls += 1

            # Count remove roll if adjacent rolls less than 4
            if adjacent_rolls < 4:
                removed_rolls += 1
                new_grid[r] = new_grid[r][:c] + "x" + new_grid[r][c + 1 :]

    return removed_rolls, new_grid


def question_1(input):
    grid = input.strip().split("\n")
    removed_rolls, _ = remove_rolls(grid)
    return removed_rolls


def question_2(input):
    grid = input.strip().split("\n")
    total_removed = 0

    while True:
        removed_rolls, grid = remove_rolls(grid)
        if removed_rolls == 0:
            break
        total_removed += removed_rolls

    return total_removed


print("Sample Question 1:", question_1(sample))  # 13
print("Question 1:", question_1(input))  # 1409

print("Sample Question 2:", question_2(sample))  # 43
print("Question 2:", question_2(input))  # 8366
