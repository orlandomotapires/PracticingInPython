print('\033[1;39;40mVumbora meus minino')
nome = str(input('Insira o seu nome\n'))
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7;30m',
         'rosa' : '\033[35m'}

print('Olá! Muito prazer em te conhecer, {}{}{} !!!'. format(cores['rosa'], nome, cores['limpa']))