n = int(input("Digite quantos elementos da sequência deseja mostrar: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()
