def ficha(nome = '', gols = ''):
  if nome == '':
    nome = '<desconhecido>'
  if gols == '':
    gols = 0  
  print(f'{nome} marcou {gols} gols!')
  print(f'PARABÉNS {nome}!!!')

ficha(str(input('Insira o nome do jogador: ')), (input('Insira quantos gols o jogador fez: ')))
