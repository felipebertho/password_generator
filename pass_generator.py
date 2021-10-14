import random

uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowercase_letters = uppercase_letters.lower()
digits_numbers = "0123456789"
symbols = "!@#$%¨&*()-+_"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits_numbers
if syms:
    all += symbols

length = 8
amount = 1

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)




