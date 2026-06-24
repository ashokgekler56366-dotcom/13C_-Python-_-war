#!/usr/bin/env python3
import os

BLACK = "\033[40m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

os.system('clear')
print(BLACK + CYAN + "=== 13C War Chest ===" + RESET)

# STR: Text with quotes - used for names, labels
name = "Commander"  # str applied: user name is text
phone = "Redmi 13C"  # str applied: model name
goal = "Poco X6 Pro"  # str applied: target text

# INT: Numbers no quotes - used for math
salary = 10000  # int applied: salary for calculation
save = 3000  # int applied: monthly saving
price = 19000  # int applied: phone price

# INT MATH: int // int = int
months = price // save  # int applied: 19000 // 3000 = 6 months

print(BLACK + GREEN + f"Name: {name}" + RESET)  # str used
print(BLACK + GREEN + f"Phone: {phone}" + RESET)  # str used
print(BLACK + YELLOW + f"Salary: {salary}" + RESET)  # int used
print(BLACK + YELLOW + f"Months to {goal}: {months}" + RESET)  # int + str used
print(BLACK + RESET)

