lista_palavras = input("Digite as palavras separadas por espaço: ").split()
print()
a_palavras = []
palindromos = []
longas = []
comuns = []
mensagem = []

def mostrar_palavras(palavras):
    for palavra in palavras:
        if len(palavras) > 2 and palavra != palavras[-1] and palavra != palavras[-2]:
            print(palavra, end=', ')
        if len(palavras) > 1 and palavra == palavras[-2]:
            print(palavra + ' e ', end='')
        if palavra == palavras[-1]:
            print(palavra + '.')

for palavra in lista_palavras:
    print(palavra.capitalize(), end=' ')
    comum = True
    if palavra[0].lower() == 'a':
        mensagem.append('começa com a letra "a"')
        a_palavras.append(palavra)
        comum = False
    if len(palavra) > 7:
        mensagem.append('é uma palavra longa')
        longas.append(palavra)
        comum = False
    if palavra == palavra[::-1]:
        mensagem.append('é um palíndromo')
        palindromos.append(palavra)
        comum = False
    if comum:
        mensagem.append('é uma palavra comum')
        comuns.append(palavra)
    mostrar_palavras(mensagem)
    mensagem.clear()

print(f"\nResumo:\n{len(a_palavras)} palavra(s) que começam com 'a':", end=' ')
mostrar_palavras(a_palavras)
print(f"{len(palindromos)} palíndromo(s):", end=' ')
mostrar_palavras(palindromos)
print(f"{len(longas)} palavra(s) longa(s):", end=' ')
mostrar_palavras(longas)
print(f"{len(comuns)} palavra(s) comum(ns):", end=' ')
mostrar_palavras(comuns)