import sys

min_number = sys.maxsize
comand = input()

while comand != "Stop":
    next_number = float(comand)
    if next_number <= min_number:
        min_number = next_number
    comand = input()

print(f"{min_number:.0f}")