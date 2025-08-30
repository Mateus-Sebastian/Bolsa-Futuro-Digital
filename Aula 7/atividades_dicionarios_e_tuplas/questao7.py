notas = {
    ('Bruna', 'Inglês'): 8.5,
    ('Carlos', 'Matemática'): 9.0,
    ('Bruna', 'História'): 7.0
}

nome = input("Nome do aluno: ")
soma = 0
total = 0

if nome in [aluno[0] for aluno in notas.keys()]:
    for aluno, nota in notas.items():
        if aluno[0].lower() == nome.lower():
            print(f'Nota de {aluno[0]} em {aluno[1]}: {nota}')
            soma += nota
            total += 1
    print(f'Média geral de {nome}: {soma / total}')
else:
    print(f'Aluno {nome} não encontrado.')