valor = float(input("Valor da casa "))
salario = float(input("Salário do comprador "))
anos = int(input("Em quantos anos vai pagar: "))

prestacao = valor/(12*5)

if prestacao <= (salario*0.3):
    print("Valor da prestação é de R$ {:.2f}, empréstimo aprovado!" .format(prestacao))
else:
    print("Empéstimo negado!")