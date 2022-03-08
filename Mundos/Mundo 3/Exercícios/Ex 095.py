jogador = dict()
partida = list()
time = list()
totgols = busca = 0
while True:
    jogador.clear()
    partida.clear()
    totgols = 0
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))  
    for c in range(0,jogador['partidas']):
        gol = int(input(f'Quantidade de gols na partida {c+1}: '))
        totgols += gol
        partida.append(gol)
    jogador['gols'] = partida[:]  
    jogador['totgols'] = totgols  
    perg = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while perg not in 'SN':
        print('Resposta inválida, tende novamente!')
        perg = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    time.append(jogador.copy())   
    if perg in 'N':
        break    
print('-=' * 30)
print('cod', end = '')
for i in jogador.keys():
    print(f'{i:<15} ', end = '')
print('-'*30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()    
while busca != 999:
    busca = int(input('Buscar dados de qual jogador ? (999 para parar) '))
    if busca >= len(time):
        print(f'Número de jogador {busca} inválido!!!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')   
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i + 1} fez {g} gols')
