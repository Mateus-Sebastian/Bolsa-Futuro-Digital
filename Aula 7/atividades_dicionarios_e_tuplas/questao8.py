pontos_turisticos = {
    (-8.1584, -34.9224): 'Cristo Redentor',
    (-12.9714, -38.5014): 'Elevador Lacerda',
    (-7.2034, -39.3206): 'Açude Velho'
}

coordenadas = (input("Digite as coordenadas (latitude, longitude): ").split(','))

for i in range(len(coordenadas)):
    coordenadas[i] = float(coordenadas[i])
    
for i in pontos_turisticos.keys():
    if coordenadas == list(i):
        print(f'Ponto turístico: {pontos_turisticos[i]}')
        break
else:
    print('Coordenadas não encontradas.')