frase = input("Digite uma frase: ")
v = 0
c = 0

for i in frase:
    if i.isalpha() and i.lower() in 'aeiouáéíóúâêîôûãõ':
        v += 1
    elif i.isalpha():
        c += 1

print(f"Vogais: {v} | Consoantes: {c}")