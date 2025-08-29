pilha = []

def adicionar_a_pilha(item):
    pilha.append(item)
    print(f"'{item}' foi adicionado à pilha.")

def remover_da_pilha():
    if pilha:
        item = pilha.pop()
        print(f"'{item}' foi removido da pilha.")
    else:
        print("A pilha está vazia.")

def exibir_pilha():
    if pilha:
        print("Pilha atual:")
        for item in pilha:
            print(f" - {item}")
    else:
        print("A pilha está vazia.")

adicionar_a_pilha("item 1")
adicionar_a_pilha("item 2")
exibir_pilha()
remover_da_pilha()
exibir_pilha()