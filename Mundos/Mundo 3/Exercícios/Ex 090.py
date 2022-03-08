dados = {}
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] < 7:
    print(f'Aluno: {dados["nome"]}, Média: {dados["media"]} Situação: REPROVADO')
else:
    print(f'Aluno: {dados["nome"]}, Média: {dados["media"]} Situação: APROVADO') 