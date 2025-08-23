curso = input("Digite o nome do curso: ")
sigla = []

for i in curso.split():
    if i not in ["a", "e", "de", "do", "da", "em", "o", "um", "uma", "para", "dos", "das", "na", "no"]:
        sigla.append(i[0].upper())

print(f"Bem vindo ao curso: {curso.capitalize()} - ({''.join(sigla)})")