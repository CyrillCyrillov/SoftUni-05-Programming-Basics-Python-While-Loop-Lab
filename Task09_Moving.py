import math

width = int(input())
length = int(input())
height = int(input())
free_volume = width * length * height

#next_boxes = input()

while free_volume >= 0:
    next_boxes = input()
    if next_boxes == "Done":
        break
    free_volume -= int(next_boxes)

if next_boxes == "Done":
    print(f"{free_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_volume)} Cubic meters more.")