import random

resposta=input("Deseja gerar uma senha? ").upper()
#Função de usar continuamente.


while resposta != "NAO":


    uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lowercase_letters = uppercase_letters.lower()
    digits_numbers = "0123456789"
    symbols = "!@()#"
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
        print("Senha gerada: " + password)
    resposta=input("Deseja gerar outra senha? ")
    if resposta=="nao":

        print("O programa foi fechado.")
        break


