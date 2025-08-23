frase = input("Digite uma frase: ").replace(' ', '').lower()

if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")