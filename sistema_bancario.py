menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[c] Checar saldo
Selecione a opção: """
saldo = 1000
limite = 500
saques_realizados = 0
extrato = ''
while True:
    opcao = input(menu)
    if opcao=='d':
        deposito_solicitado = int(input('Informe o valor que deseja depositar: '))
        if deposito_solicitado<=0:
            print('Você não pode depositar esse valor.')
        else:
            print('Depósito realizado com sucesso!')
            saldo+=deposito_solicitado
            extrato+=f'Depósito de R${deposito_solicitado}\n'
    elif opcao=='s':
        if saques_realizados==3:
            print('Você atingiu o limite de saques disponíveis.')
            break
        saque_solicitado = int(input(f'Você possui R${saldo}. Informe o valor que deseja sacar: '))
        if saque_solicitado<=0 or saque_solicitado>500 or saque_solicitado>saldo:
            print('Você não pode sacar esse valor.')
        else:
            print('Saque realizado com sucesso!')
            saques_realizados+=1
            saldo-=saque_solicitado
            extrato+= f'Saque de R${saque_solicitado}\n'
    elif opcao=='e':
        if extrato=='':
            print('Você não tem nenhuma operação.')
        else:
            print(extrato)
    elif opcao=='q':
        print('Obrigado, volte sempre!')
        break
    elif opcao=='c':
        print(f'Seu saldo é R${saldo}')
    else:
        print('Opção invalida, selecione novamente a operação: ')