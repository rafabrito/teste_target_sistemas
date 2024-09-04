import os

# Função para o calculo da sequência de Fibonacci
def fibb(num):
    seq = []
    
    seq.append(0) # adição do valor 0 na sequencia
    seq.append(1) # adição do valor 1 na sequencia
    
    temp = 0
    j = 1
    k = 0
    for _ in range(1, num + 1):
        temp =  k + j # calcula os termos através da soma dos dois valores anteriores da sequência
        k = j
        j = temp
        seq.append(j)
    return seq


while True:
    print('\n######### MENU #########')
    print('1 - Calcular Fibonacci')
    print('0 - Sair')
    op = int(input('Opção: '))
    
    os.system('cls' if os.name == 'nt' else 'clear') # limpa o terminal

    if op == 1:
        num = int(input('Informe um número para calcular a sequência de Fibonacci: '))
        seq_fibb = fibb(num) # sequência de fibonacci
        
        # verifica se o número digitado pertence a sequência de Fibonacci
        if num in seq_fibb:
            print('\nO número {} pertence a sequência de Fibonacci!'.format(num))
        else:
            print('\nO número {} não pertence a sequência de Fibonacci!'.format(num))
    elif op == 0:
        break

    


