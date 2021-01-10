import sys

max_number = -sys.maxsize
comand = input()

while comand != "Stop":
    next_number = float(comand)
    if next_number >= max_number:
        max_number = next_number
    comand = input()

print(f"{max_number:.0f}")