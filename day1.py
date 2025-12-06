from helper import read_input


sample = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

raw_input = read_input("day1_input.txt")
input = raw_input.strip().split("\n")


def question_1(input):
    pos = 50
    count_0 = 0

    for r in input:
        direction = r[0]
        steps = int(r[1:])
        steps = steps * (-1 if direction == "L" else 1)
        pos = (pos + steps) % 100
        count_0 += 1 if pos == 0 else 0

    return count_0


def question_2(input):
    pos = 50
    pass_0 = 0

    for r in input:
        direction = r[0]
        steps = int(r[1:])

        rounds = steps // 100  # Full rounds
        reminder = steps % 100

        if direction == "L":
            steps = -steps
            # Extra if reminder >= pos for left
            if pos > 0 and reminder >= pos:
                rounds += 1
        else:
            # Extra if reminder + pos >= 100 for right
            if pos > 0 and reminder + pos >= 100:
                rounds += 1

        pass_0 += rounds
        pos = (pos + steps) % 100

    return pass_0


print("Sample Question 1:", question_1(sample))  # 3
print("Question 1:", question_1(input))  # 1139

print("Sample Question 2:", question_2(sample))  # 6
print("Question 2:", question_2(input))  # 6684
