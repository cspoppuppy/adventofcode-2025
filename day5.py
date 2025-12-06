from helper import read_input


sample = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

sample2 = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

input = read_input("day5_input.txt")


def question_1(input):
    fresh_range, ingredients = input.strip().split("\n\n")
    fresh_range_list = fresh_range.split("\n")
    ingredient_list = list(map(int, ingredients.strip().split("\n")))

    fresh_invervals = [fr.split("-") for fr in fresh_range_list]
    fresh_intervals_int = [(int(a), int(b)) for a, b in fresh_invervals]

    fresh_count = 0
    for i in ingredient_list:
        for a, b in fresh_intervals_int:
            if a <= i <= b:
                fresh_count += 1
                break

    return fresh_count


def question_2(input):
    fresh_range, _ = input.strip().split("\n\n")
    fresh_range_list = fresh_range.split("\n")
    fresh_invervals = [fr.split("-") for fr in fresh_range_list]
    fresh_intervals_int = sorted(
        [[int(a), int(b)] for a, b in fresh_invervals], key=lambda x: (x[0], x[1])
    )

    cleaned_intervals = []
    fresh_cnt = 0

    for f in fresh_intervals_int:
        processed = False
        if cleaned_intervals:
            for c in cleaned_intervals:
                # Check overlap
                if f[0] <= c[1] and f[1] <= c[1]:
                    processed = True
                    break
                elif f[0] <= c[1] and f[1] > c[1]:
                    fresh_cnt += f[1] - c[1]
                    c[1] = f[1]
                    processed = True
                    break
                elif processed and f[1] >= c[1]:
                    fresh_cnt -= c[1] - c[0] + 1
                    cleaned_intervals.remove(c)
                elif processed and f[1] > c[0]:
                    fresh_cnt -= f[1] - c[0] + 1
                    c[0] = f[1] + 1

            if not processed:
                fresh_cnt += f[1] - f[0] + 1
                cleaned_intervals.append(f)
        else:
            fresh_cnt += f[1] - f[0] + 1
            cleaned_intervals.append(f)

    return fresh_cnt


print("Sample Question 1:", question_1(sample))  # 3
print("Question 1:", question_1(input))  # 558

print("Sample Question 2:", question_2(sample2))  # 14
print("Question 2:", question_2(input))  # 344813017450467
