# Question 1
OUTPUT_FILE = "name.txt"

name = input("What is your name:")
out_file = open(OUTPUT_FILE, 'w')
print(name, file=out_file)
out_file.close()


OPEN_FILE = open(OUTPUT_FILE, 'r')
names_from_file = OPEN_FILE.read()
print(f"Your name is {names_from_file}")
OPEN_FILE.close()


NUMBERS_FILE = "numbers.txt"
OPEN_FILE = open(NUMBERS_FILE, 'r')
numbers = OPEN_FILE.readlines()
new_number = int(numbers[0]) + int(numbers[1])
print(new_number)
OPEN_FILE.close()


total_sum = 0
OPEN_FILE = open(NUMBERS_FILE, 'r')
numbers = OPEN_FILE.readlines()
for lines in numbers:
    total_sum += int(lines)
print(total_sum)