fila = []

def adicionar_a_fila(item):
    fila.append(item)
    print(f"'{item}' foi adicionado à fila.")

def remover_da_fila():
    if fila:
        item = fila.pop(0)
        print(f"'{item}' foi removido da fila.")
    else:
        print("A fila está vazia.")

def exibir_fila():
    if fila:
        print("Fila atual:")
        for item in fila:
            print(f" - {item}")
    else:
        print("A fila está vazia.")

adicionar_a_fila("item 1")
adicionar_a_fila("item 2")
exibir_fila()
remover_da_fila()
exibir_fila()