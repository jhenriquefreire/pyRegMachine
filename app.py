
def cashier(prod):
    total = 0
    while prod != 0:
        total += prod
        prod = int(input('Insira o código do produto: '))
    #payMenu(int(input("Escolha a opção de pagamento: ")))
    return total

def payMenu(opt):
    while True:
        match(opt):
            case 1:
                pay = int(input("Coloque o valor pago: "))#int provisório, mudar p/ Float
                cash(pay)
                break
            case 2:
                card()
                break
            case 3:
                pay = int(input("Coloque o valor pago: "))#int provisório, mudar p/ Float
                part = int(input("Insira o número de parcelas: "))
                credit(pay, part)
                break
            case _:
                print('Opção inválida. Tente novamente')
                payMenu(int(input("Escolha a opção de pagamento: ")))


def cash (pay):
    global prod
    if pay > prod:
        total = pay-prod
        print(f"O troco será de {total}")
    elif pay < prod:
        total = prod - pay
        print(f"Ainda falta {total} para o pagamento")
    else:
        print(f"Não precisará de troco")

def card ():
    while True:
        try:
            pw = int(input("Digite sua senha: "))
        except ValueError:
            print('Erro! Insira uma senha válida (apenas números):')
        else:
            print("Senha correta")
            break

def credit (pay, part):
    card()
    parc = pay/part
    print(f"O pagamento de {pay} será feito em {part} vezes de {parc:.2f}")


prod = cashier(int(input('Insira o código do produto: ')))#Prod provisório, vai ler DB
print(prod)
