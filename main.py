import random

password_digits = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("Write the length of your password: "))
password = ""

for i in range(password_length):
    password += random.choice(password_digits)

print(password)
