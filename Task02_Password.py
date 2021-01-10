username = input()
password = input()

next_password = input()

while next_password != password:
    next_password = input()

print(f"Welcome {username}!")
