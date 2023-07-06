import random

quick_picks = int(input("How many quick picks? "))

for quick_pick in range(quick_picks):
    numbers = [random.randint(1, 45) for n in range(6)]
    numbers.sort()
    print(" ".join(str(number) for number in numbers))
