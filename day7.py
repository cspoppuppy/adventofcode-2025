from typing import Tuple
from helper import read_input


sample = read_input("day7_sample.txt")
input = read_input("day7_input.txt")


def tachyon_split(input: str) -> Tuple[int, int]:
    rows = input.strip().split("\n")
    grid = [list(row) for row in rows]

    split_cnt = 0
    grid_timelines = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for ri, row in enumerate(grid):
        # Skip first row
        if ri == 0:
            continue
        for ci in range(len(row)):
            if grid[ri - 1][ci] == "S":
                row[ci] = "|"
                grid_timelines[ri][ci] = 1
                break
            # Found "^" with "|" below it
            elif grid[ri][ci] == "^" and grid[ri - 1][ci] == "|":
                if ci - 1 >= 0:
                    row[ci - 1] = "|"
                    grid_timelines[ri][ci - 1] += grid_timelines[ri - 1][ci]
                if ci + 1 < len(row):
                    row[ci + 1] = "|"
                    grid_timelines[ri][ci + 1] += grid_timelines[ri - 1][ci]
                split_cnt += 1
            # Carry the "|" down
            elif grid[ri - 1][ci] == "|":
                row[ci] = "|"
                grid_timelines[ri][ci] += grid_timelines[ri - 1][ci]

    timeline_sum = sum(grid_timelines[-1])

    return split_cnt, timeline_sum


sample_split_cnt, sample_timelines_sum = tachyon_split(sample)
input_split_cnt, input_timelines_sum = tachyon_split(input)


print("Sample Question 1:", sample_split_cnt)  # 21
print("Question 1:", input_split_cnt)  # 1546

print("Sample Question 2:", sample_timelines_sum)  # 40
print("Question 2:", input_timelines_sum)  # 13883459503480
