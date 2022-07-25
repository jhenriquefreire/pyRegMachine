dayIncome = 0
numVendas = 0

while True:
    print('''
    Escolha entre as opções:
    1 - Iniciar nova compra
    2 - Mostrar ganhos do dia
    0 - Encerrar caixa''')
    mainMenu = int(input("Insira uma opção: "))
    match (mainMenu):
        case 0:
            print(f"O rendimento bruto do dia foi de R${dayIncome}. Parabéns.")
            break
        case 1:
            prodCode = int(input("Insira o código do produto (digite 0 para sair): ")) #momentaneamente é o preço, fazer update.
            shopTotal = 0
            while prodCode != 0:
                shopTotal += prodCode
                prodCode = int(input("Insira o código do produto (digite 0 para sair): "))
            dayIncome += shopTotal
            numVendas += 1
            print(f"O valor total é de {shopTotal}, escolha uma forma de pagamento:")
            print('''
            1 - Dinheiro
            2 - Débito
            3 - Crédito
            4 - Pix''')
            while True:
                payWay = int(input("Insira aqui a forma de pagamento: "))
                if payWay == 1:
                    payCash = int(input("Coloque o valor entregue: "))
                    if payCash > shopTotal:
                        change = payCash - shopTotal
                        print(f"É preciso dar {change} de troco")
                    elif payCash < shopTotal:
                        missing = shopTotal - payCash
                        print(f"Ainda faltam {missing} para completar o total da compra")
                    else:
                        print(f"Obrigado e volte sempre!")
                    break
                elif payWay == 2:
                    print("Insira seu cartão:")
                    print("Obrigado e volte sempre!")
                    break
                elif payWay == 3:
                    numParc = int(input("Parcelar a compra em quantas vezes?"))
                    print(f"A compra será paga em {numParc} vezes de {shopTotal / numParc}.")
                    while True:
                        creditCc = int(input("Digite 1 para corrigir as informações ou qualquer tecla para continuar: "))
                        if creditCc == 1:
                            numParc = int(input("Parcelar a compra em quantas vezes?"))
                            print(f"A compra será paga em {numParc} vezes de {shopTotal / numParc}.")
                        else:
                            break
                    break
                else:
                    print("Opção inválida, tente novamente")
        case 2:
            print(f"O resultado momentâneo é de: R${dayIncome} em {numVendas} compras feitas.")
        case _:
            print("Opção inválida, tente novamente")