import random

numero_secreto = random.randint(1, 10)
tentativas = 0

print("Tente adivinhar um número entre 1 e 10!")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("Maior")
    elif palpite > numero_secreto:
        print("Menor")
    else:
        print("Acertou!")
        print(f"Número de tentativas: {tentativas}")
        break
