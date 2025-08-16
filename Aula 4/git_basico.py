
def adicionar(tarefa):
    tarefas.append(tarefa)
    
def remover(tarefa):
    tarefas.remove(tarefa)
    
# Sistema de tarefas - versão inicial
tarefas = ["Estudar", "Ler livro"]

adicionar("Fazer exercícios")

for tarefa in tarefas:
    if( tarefa == "Estudar"):
        remover(tarefa)

for tarefa in tarefas:
    print("-", tarefa)
