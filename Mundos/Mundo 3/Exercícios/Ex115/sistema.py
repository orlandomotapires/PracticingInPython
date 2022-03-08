from Ex115.lib.interface import *
from Ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
   criarArquivo(arq)  

while True:
  resposta = menu(['Ver pessoas cadastradas', 'Cadastrat nova pessoa', 'Sair do sistema'])
  if resposta == 1:
    #Opção de listar o conteúdo de um arquivo
    lerArquivo(arq)
  
  if resposta == 2:
    #Opção cadastrar uma nova pessoa
    cabeçalho('NOVO CADASTRO')
    nome = str(input('Nome: '))
    idade = leiaint('Idade: ')
    cadastrar(arq, nome, idade)
  if resposta == 3:
    cabeçalho('Saindo do sistema... até logo!')   
    break
  else:
    print('ERRO! Digite uma opção válida!') 
  sleep(2)  