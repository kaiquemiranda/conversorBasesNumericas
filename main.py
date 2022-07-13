num = int(input('digite um numero inteiro: '))
print('Escolha uma das bases para converter: ')
print('[1] BINARIO \n[2] OCTAL \n[3] HEXADECIMAL')
opcao = int(input('sua opção: '))

if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('opção invalida')

