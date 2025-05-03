menu = '''

SELECIONE A OPCAO DESEJADA:

******MENU*****
[S] SACAR
[D] DEPOSITAR
[E] EXTRATO
[Q] SAIR
===============

'''

limete_de_sacar = float(500)
saldo=float(0)
numero_de_saque=int(1)
LIMITE_SAQUES=3
limite_maximo_diario = float(0)
lista_saque=[]
lista_deposito=[]


while True:

    opcao = input(menu).upper()

    if opcao == 'S':        
        if saldo == 0:
            print(f'Você não tem saldo o suficinte para sacar, seu saldo e: R$ {saldo}')
        
               

        else:
            saque=float(input("quanto deseja sacar, limite maximo de R$ 500 por saque e R$ 1500 diario: R$ "))
            if saque <= limete_de_sacar and numero_de_saque <= 3 and saque < saldo:            
                saldo = saldo - saque
                print(f"Saque realizado com sucesso, seu novo saldo é:R$ {saldo}")
                numero_de_saque+=1
                limite_maximo_diario +=saque
                lista_saque.append(saque)

            if saque > saldo:
                print(f'Você não tem saldo o suficinte para sacar seu saldo e R$ {saldo}')
            if saque > 500:
                print("Acima do limete de saque, tente novamente")
                          
            if numero_de_saque > 3:
                print("Excedeu o numero diario de saques, entre em contato com o seu Banco")
                 
          
                   
       
    elif opcao == "E":
        print(f"Seu saldo é: R$ {saldo}")
        print("Seus deposito:")
        for d in lista_deposito: print(f" R$ {d}")
        print("Seus saques:")
        for s in lista_saque:print(f"R$ {s}")

    elif opcao == "D":
        deposito=float(input("Qual o valor que você deseja depositar? R$"))
        saldo += deposito
        lista_deposito.append(deposito)
       
        print(f"Seu novo saldo e R$ {saldo}")

    
    elif opcao == 'Q':
        print("Obrigado por fazer parte do grupo, volte sempre")
        break
  
    else: 
        print("Operação invalida tenta novamente...")
        