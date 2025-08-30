notas = {
    'Ana': (9.5, 8.0, 7.0),
    'Mario': (6.5, 6.0, 6.0),
    'Luíza': (8.0, 10, 7.5)
}

print(f'Notas de Ana: {notas["Ana"]}\n')

for aluno, notas in notas.items():
    media = sum(notas) / len(notas)
    print(f"Média das notas de {aluno}: {media:.1f}")