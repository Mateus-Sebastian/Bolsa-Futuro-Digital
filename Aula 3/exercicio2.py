def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    return numero1 / numero2

print("Calculadora básica")
print("Qual operação deseja realizar?")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

opcao = input("Digite o número da operação desejada: ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if opcao == "1":
    print("O resultado é:", somar(numero1, numero2))
elif opcao == "2":
    print("O resultado é:", subtrair(numero1, numero2))
elif opcao == "3":
    print("O resultado é:", multiplicar(numero1, numero2))
elif opcao == "4":
    print("O resultado é:", dividir(numero1, numero2))