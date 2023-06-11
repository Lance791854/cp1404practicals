"""
CP1404/CP5632 - Practical
"""


def main():
    import random

    score = float(input("Enter score: "))
    random_result = calculate_result(random.randint(0, 100))
    user_result = calculate_result(score)
    print(random_result)
    print(user_result)


def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
