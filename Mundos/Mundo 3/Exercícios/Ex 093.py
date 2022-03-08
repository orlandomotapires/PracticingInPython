dados = dict()
gols = list()
totgols = 0
dados['nome'] = str(input('Nome do jogador: '))
dados['partidas'] = int(input('Quantiade de partidas jogadas: '))
for c in range(0,dados['partidas']):
    gol = int(input(f'Quantidade de gols na partida {c+1}: '))
    totgols += gol
    gols.append(gol)
dados['gols'] = gols    
dados['totgols'] = totgols
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas e fez {dados["totgols"]} gols em toda sua carreira!!!')
for k, v in enumerate(dados['gols']):
    print(f'Na partida {k}, fez {v} gols')
print('-='*30,f'PARABÉNS {dados["nome"]}!!!', '-='*30)   