lista_palavras = input("Digite as palavras separadas por espaço: ").split()
print()
a_palavras = []
palindromos = []
longas = []
comuns = []

def mostrar_palavras(palavras):
    for palavra in palavras:
        if palavra != palavras[-1] and palavra != palavras[-2]:
            print(palavra, end=', ')
        if palavra == palavras[-2]:
            print(palavra + ' e ', end='')
        if palavra == palavras[-1]:
            print(palavra + '.', end='')

for palavra in lista_palavras:
    print(palavra.capitalize())
    if palavra[0].lower() == 'a':
        print(' começa com a letra "a".')
        a_palavras.append(palavra)
    if palavra == palavra[::-1]:
        print(' é um palíndromo.')
        palindromos.append(palavra)
    if len(palavra) > 7:
        print('é uma palavra longa.')
        longas.append(palavra)
    else:
        print(' é uma palavra comum.')
        comuns.append(palavra)

print(f"\n{len(a_palavras)} palavra(s) que começam com 'a':", end=' ')
mostrar_palavras(a_palavras)
print(f"\n{len(palindromos)} palíndromo(s):", end=' ')
mostrar_palavras(palindromos)
print(f"\n{len(longas)} palavra(s) longa(s):", end=' ')
mostrar_palavras(longas)
print(f"\n{len(comuns)} palavra(s) comum(ns):", end=' ')
mostrar_palavras(comuns)