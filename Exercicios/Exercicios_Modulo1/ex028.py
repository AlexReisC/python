from random import randint
n = randint(0, 5)
chute = int(input("Chute um número: "))

if chute == n:
    print("Você acertou!")
else:
    print("Você errou! O computador pensou no {}." .format(n))