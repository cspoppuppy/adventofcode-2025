import re
from helper import read_input


sample = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

input = read_input("day2_input.txt")


def is_num_repeated(num_str: str, repeat_len: int) -> bool:
    if repeat_len <= 0:
        return False
    if len(num_str) % repeat_len != 0 or len(num_str) < repeat_len * 2:
        return False
    for i in range(1, len(num_str) // repeat_len):
        if num_str[i * repeat_len : (i + 1) * repeat_len] != num_str[0:repeat_len]:
            return False
    return True


def is_num_repeated_recursive(num_str: str, initial_repeat_len: int) -> bool:
    if initial_repeat_len <= 0:
        return False
    if is_num_repeated(num_str, initial_repeat_len):
        return True
    else:
        return is_num_repeated_recursive(num_str, initial_repeat_len - 1)


def question_1(input):
    input_split = input.split(",")
    sum_invalid = 0
    for i in input_split:
        a, b = map(int, i.split("-"))
        for num in range(a, b + 1):
            s = str(num)
            if len(s) % 2 == 0:
                sum_invalid += num if is_num_repeated(s, len(s) // 2) else 0
    return sum_invalid


def question_2_lazy(input):
    input_split = input.split(",")

    sum_invalid = 0

    for i in input_split:
        a, b = map(int, i.split("-"))
        for num in range(a, b + 1):
            s = str(num)
            if re.fullmatch(r"(\d+)\1+", s):
                sum_invalid += num
    return sum_invalid


def question_2(input):
    input_split = input.split(",")
    sum_invalid = 0
    for i in input_split:
        a, b = map(int, i.split("-"))
        for num in range(a, b + 1):
            s = str(num)
            sum_invalid += num if is_num_repeated_recursive(s, len(s) // 2) else 0
    return sum_invalid


print("Sample Question 1:", question_1(sample))  # 1227775554
print("Question 1:", question_1(input))  # 44854383294

print("Sample Question 2:", question_2(sample))  # 4174379265
print("Question 2:", question_2(input))  # 55647141923
