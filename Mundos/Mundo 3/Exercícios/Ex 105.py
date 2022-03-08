def notas():
  geral= dict()
  aluno = list()
  notaaluno = list()
  n = 0
  qnt = 0
  nome = ''
  soma = 0
  qnt_tot = 0
  maior_nota = 0
  menor_nota = 0 
  situacao = ''
  while True:
    nome = str(input('Nome do Aluno: ')).strip()
    aluno.append(nome)
    
    qnt = int(input(f'Deseja adicionar quantas notas para {nome}:'))
    qnt_tot += qnt
    for c in range(0,qnt):
      n = float(input(f'{c}º nota do aluno {nome}: '))
      soma += n
      notaaluno.append(n)
    aluno.append(notaaluno)    

    for k in notaaluno:
      if k >= maior_nota:
        maior_nota = k
      elif k < menor_nota:
        menor_nota = k  

    perg2 = str(input('Deseja saber a situação do aluno em questão? [S/N]')).upper().strip()[0]
    if perg2 == 'S':
      if soma/qnt_tot > 7:
        situacao = 'Boa!'
      elif soma/qnt_tot == 7:
        situacao = 'Recuperivis!'
      elif soma/qnt_tot < 7:
        situacao = 'Reprovado!'

    geral['Aluno'] = aluno
    geral['Maior nota'] = maior_nota
    geral['Menor nota'] = menor_nota
    geral['Média'] = soma/qnt_tot
    geral['Situação'] = situacao

    if perg2 == 'N':
       situacao = ''

    perg = str(input('Deseja continuar adicionando notas ? [S/N]')).upper().strip()[0]
    if perg == 'N':
      break
  

  return geral
resp = notas()
print(resp)


# [Turma [João [notaaluno]] [Aluno[notaaluno]] [Aluno[notaaluno]] [Aluno[notaaluno]] [Aluno[notaaluno]] [Aluno[notaaluno]] Turma]

