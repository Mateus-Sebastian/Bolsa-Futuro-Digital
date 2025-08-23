frase = 'Mateus Sebastian de Albuquerque Rocha'
f = 0
c = 0
for i in frase:
    if i.isalpha() and i.lower() in 'aeiouáéíóúâêîôûãõ':
        f += 1
    elif i.isalpha():
        c += 1
print(f"Vogais: {f} | Consoantes: {c}")