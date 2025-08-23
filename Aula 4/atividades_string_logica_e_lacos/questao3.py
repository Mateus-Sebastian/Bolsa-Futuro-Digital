frase = input("Digite uma frase: ").lower().split()
unicos = []
for i in frase:
    if i not in unicos:
        unicos.append(i)

for i in unicos:
    print(f"'{i}' se repete {frase.count(i)} vez(es)")