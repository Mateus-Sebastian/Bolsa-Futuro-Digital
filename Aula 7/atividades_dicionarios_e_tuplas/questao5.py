precos = {
    ('Casaco', 'G'): 50,
    ('Camisa', 'M'): 37.5,
    ('Casaco', 'P'): 40
}

(item, tamanho) = input("Digite o item e o tamanho: ").split(' ')

preco = precos.get((item, tamanho), "Item não encontrado")

print(f'{preco} reais' if isinstance(preco, (int, float)) else preco)