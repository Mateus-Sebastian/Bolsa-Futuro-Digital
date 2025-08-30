tabuleiro = {
    (0, 0): '-', (0, 1): '-', (0, 2): '-',
    (1, 0): '-', (1, 1): '-', (1, 2): '-',
    (2, 0): '-', (2, 1): '-', (2, 2): '-'
}

(x,y) = input('Digite a posição que deseja jogar X (linha,coluna): ').split(',')
tabuleiro[(int(x), int(y))] = 'X'

(x,y) = input('Digite a posição que deseja jogar O (linha,coluna): ').split(',')
tabuleiro[(int(x), int(y))] = 'O'

print(f"{tabuleiro[(0, 0)]} | {tabuleiro[(0, 1)]} | {tabuleiro[(0, 2)]}")
print(f"{tabuleiro[(1, 0)]} | {tabuleiro[(1, 1)]} | {tabuleiro[(1, 2)]}")
print(f"{tabuleiro[(2, 0)]} | {tabuleiro[(2, 1)]} | {tabuleiro[(2, 2)]}")