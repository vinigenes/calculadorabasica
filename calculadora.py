def escolher_numeros(): 
     num_escolhido = float(input('\nDigite o primeiro número escolhido: '))
     num_escolhido2 = float(input('Digite o segundo número escolhido: '))
     print(f'Seus números são {num_escolhido} e {num_escolhido2}\n')
     return num_escolhido, num_escolhido2
 
 while True:
         print('Escolha uma das opções abaixo: Exemplo: "a"')
         print('a) soma')
         print('b) subtração') 
         print('c) divisão')
         print('d) multiplicação')
         print('e) Sair \n')
         opcao_escolhida = str(input('Digite: ')).lower()
 
         if opcao_escolhida == 'e':
             print('Programa finalizado.\n')
             break
         
         if opcao_escolhida in ['a', 'b', 'c', 'd']:
             num_escolhido, num_escolhido2 = escolher_numeros()
         
         if opcao_escolhida == 'a':
             print('Você escolheu soma:')
             soma = num_escolhido + num_escolhido2
             print(f'Resultado: {soma}\n')            
 
         elif opcao_escolhida == 'b':
             print('Você escolheu subtração:')
             sub = num_escolhido - num_escolhido2
             print(f'Resultado: {sub}\n')
 
         elif opcao_escolhida == 'c':
             print('Você escolheu divisão:')
             if num_escolhido2 != 0:
                 div = num_escolhido / num_escolhido2
                 print(f'Resultado: {div}\n')
             else:
                 print("Erro: Divisão por zero não é permitida.\n")
 
         elif opcao_escolhida == 'd':
             print('Você escolheu multiplicação:')
             mult = num_escolhido * num_escolhido2
             print(f'Resultado: {mult}\n')
 
         else:
             print('Opção inválida.\n')
