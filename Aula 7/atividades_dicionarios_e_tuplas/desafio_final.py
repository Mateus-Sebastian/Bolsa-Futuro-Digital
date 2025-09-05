alunos = {
    ('Bruno', 'Matemática'): (8.5, 9.0, 6.0),
    ('Bruno', 'C'): (7.5, 10.0, 3.0)
}

while True:
    achado = False
    opcao = input('Selecione uma opção: \n' \
    '1-Cadastrar um novo aluno com suas notas\n' \
    '2-Consultar todas as notas de um aluno\n' \
    '3-Consultar média geral do aluno em todas as disciplinas\n' \
    '4-Sair\n')

    if opcao == '1':
        nome = input('Nome do aluno: ')
        disciplina = input('Disciplina: ')
        notas = tuple(float(input(f'Nota {i}: ')) for i in range(1,4))
        alunos.update({(nome, disciplina): notas})
        print('Aluno cadastrado com sucesso!')
    elif opcao == '2':
        nome = input('Nome do aluno: ')
        for dados, notas in alunos.items():
            if dados[0] == nome:
                print(f'Notas da disciplina {dados[1]}: {notas[0]}, {notas[1]} e {notas[2]}')
                achado = True
        if not achado:
            print('Aluno não encontrado.')
    elif opcao == '3':
        nome = input('Nome do aluno: ')
        for dados, notas in alunos.items():
            if dados[0] == nome:
                media = sum(notas) / len(notas)
                print(f'Média geral do aluno {nome} em {dados[1]}: {media:.2f}')
                achado = True
        if not achado:
            print('Aluno não encontrado.')
    elif opcao == '4':
        print('Encerrando o programa.')
        break