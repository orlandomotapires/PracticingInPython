from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['carteira'] = int(input('Carteira de trabalho (0 Não tem): '))
if dados['carteira'] != 0:
    dados['contrat'] = int(input('Ano de contratação: '))
    anocontrat = dados['contrat'] - nasc
    dados['sal'] = float(input('Salário: '))
    dados['anoapos'] = 35 + anocontrat
    print(f"""
    Nome: {dados["nome"]}
    Idade: {dados["idade"]}
    CTPS: {dados["carteira"]}
    Contratado no ano de: { dados["contrat"]}
    Salário: {dados["sal"]}
    Aposentadoria com: {dados["anoapos"]} anos
    """)
else:
    print(f""" 
    Nome: {dados["nome"]}
    Idade: {dados["idade"]}
    CTPS: {dados["carteira"]}
    """)    