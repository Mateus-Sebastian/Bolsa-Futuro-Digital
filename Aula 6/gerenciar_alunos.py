fila_de_alunos = [
    {
        "nome": "Ana",
        "nota": 5.2,
    },
    {
        "nome": "Bruno",
        "nota": 8.5,
    },
    {
        "nome": "Carlos",
        "nota": 6.7,
    },
    {
        "nome": "Diana",
        "nota": 7.5,
    }
]
c = 1
for aluno in fila_de_alunos[:]:
    atual = fila_de_alunos.pop(0)
    print(f"{c}) Nome: {atual['nome']} | Nota: {atual['nota']} | {'Aprovado' if atual['nota'] >= 7 else 'Reprovado'}")
    c += 1

print(fila_de_alunos)