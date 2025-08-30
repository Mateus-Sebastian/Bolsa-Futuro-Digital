agenda = {
    'Maria': ('(83) 98375-0056', 'maria@gmail.com'),
    'João': ('(85) 98765-4321', 'joao@gmail.com'),
    'Ana': ('(11) 91234-5678', 'ana@gmail.com')
}

for nome, contato in agenda.items():
    print(f"{nome} → Telefone: {contato[0]} | Email: {contato[1]}")