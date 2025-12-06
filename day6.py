from functools import reduce
from typing import List, Tuple
from helper import read_input


sample = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

input = read_input("day6_input.txt")


def get_nums_and_ops(input: str) -> Tuple[List[List[str]], List[str]]:
    rows = input.strip().split("\n")

    nums = []
    ops = []

    for ri, row in enumerate(rows):
        cols = row.strip().split()
        if ri == 0:
            nums = [[] for _ in range(len(cols))]

        for ci, col in enumerate(cols):
            if ri != len(rows) - 1:
                nums[ci].append(col)
            else:
                ops.append(col)

    return nums, ops


def question_1(input: str) -> int:
    nums, ops = get_nums_and_ops(input)

    res = 0
    for i, op in enumerate(ops):
        if op == "+":
            res += reduce(lambda s, n: s + int(n), nums[i], 0)
        elif op == "*":
            res += reduce(lambda s, n: s * int(n), nums[i], 1)
        else:
            raise ValueError(f"Unknown operator: {op}")
    return res


def get_nums_and_ops_2(input: str) -> Tuple[List[List[str]], List[str]]:
    rows = input.split("\n")
    try:
        rows.remove("")  # Remove empty lines
    except ValueError:
        pass

    c_len = max(map(len, rows))

    nums = []
    ops = []
    num_list = []
    for ci in range(c_len):
        num = ""
        for ri in range(len(rows)):
            if ri < len(rows) - 1:
                num += rows[ri][ci]
            elif rows[ri][ci] == "+" or rows[ri][ci] == "*":
                ops.append(rows[ri][ci])

        num = num.strip()
        if num:
            num_list.append(num)
        else:
            nums.append(num_list)
            num_list = []
    nums.append(num_list)

    return nums, ops


def question_2(input: str) -> int:
    nums, ops = get_nums_and_ops_2(input)

    res = 0
    for i, op in enumerate(ops):
        if op == "+":
            res += reduce(lambda s, n: s + int(n), nums[i], 0)
        elif op == "*":
            res += reduce(lambda s, n: s * int(n), nums[i], 1)
        else:
            raise ValueError(f"Unknown operator: {op}")
    return res


print("Sample Question 1:", question_1(sample))  # 4277556
print("Question 1:", question_1(input))  # 5877594983578

print("Sample Question 2:", question_2(sample))  # 3263827
print("Question 2:", question_2(input))  # 11159825706149
