name = input()
bad_grades = 0
sum = 0
year = 0

while year < 12 and bad_grades < 2:
    next_grade = float(input())
    year += 1
    sum += next_grade
    if next_grade < 4:
        bad_grades += 1

if bad_grades == 2:
    print(f"{name} has been excluded at {year - 1} grade")
else:
    print(f"{name} graduated. Average grade: {sum / 12:.2f}")
