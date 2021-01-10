sum = 0
increase = input()

while increase != "NoMoreMoney":
    next_increase = float(increase)
    if next_increase < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {next_increase:.2f}")
    sum += next_increase
    increase = input()

print(f"Total: {sum:.2f}")

