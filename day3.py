from helper import read_input


sample = "987654321111111\n811111111111119\n234234234234278\n818181911112111"

input = read_input("day3_input.txt")


def find_max_jolts(
    bank: str, num_digits: int, start_digits: str = "", end_digits: str = ""
):
    max_digit = max(bank)
    if num_digits == 1:
        res = f"{start_digits}{max_digit}{end_digits}"
        return res
    if bank.count(max_digit) >= num_digits:
        return f"{start_digits}{max_digit * num_digits}{end_digits}"
    else:
        pos = bank.index(max_digit)
        if pos == len(bank) - num_digits:
            return f"{start_digits}{bank[pos : pos + num_digits]}{end_digits}"
        elif pos < len(bank) - num_digits:
            start_digits += max_digit
            return find_max_jolts(
                bank[pos + 1 :], num_digits - 1, start_digits, end_digits
            )
        else:
            end_digits = bank[pos:] + end_digits
            return find_max_jolts(
                bank[:pos], num_digits - len(bank[pos:]), start_digits, end_digits
            )


def question_1(input):
    banks = input.strip().split("\n")
    total_jolts = 0
    for b in banks:
        max_jolts = find_max_jolts(b, 2)
        total_jolts += int(max_jolts)
    return total_jolts


def question_2(input):
    banks = input.strip().split("\n")
    total_jolts = 0
    for b in banks:
        max_jolts = find_max_jolts(b, 12)
        total_jolts += int(max_jolts)
    return total_jolts


print("Sample Question 1:", question_1(sample))  # 357
print("Question 1:", question_1(input))  # 17493

print("Sample Question 2:", question_2(sample))  # 3121910778619
print("Question 2:", question_2(input))  # 173685428989126
