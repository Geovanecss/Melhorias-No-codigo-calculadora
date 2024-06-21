def soma(n1,n2):
    return n1+n2

def subtrair(n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1*n2

def dividir(n1,n2):
    return n1/n2

while True:
    print("+===================+")
    print("| MENU DE OPERAÇÕES |")
    print("|  1 - Somar        |")
    print("|  2 - Subtrair     |")
    print("|  3 - Multiplicar  |")
    print("|  4 - Dividir      |")
    print("|  0 - Sair         |")
    print("+===================+")
    
    op = int(input("Qual operação você deseja? "))
    if op >= 5:
        print("Operação inválida!")
        break
    
    if op==0:
        print("Programa encerrado!")
        break
    
    n1 = int(input("Primeiro número: "))
    n2 = int(input("Segundo número: "))

    if op==1:
        print("O resultado da soma é:", soma(n1,n2))
        break
    
    elif op==2:
        print("O resultado da subtração é:",subtrair(n1,n2))
        break
    elif op==3:
        print("O resultado da multiplicação é:",multiplicar(n1,n2))
        break
    elif op==4:
        print("O resultado da divisão é:",dividir(n1,n2))
        break
    else:
        print("Digite um número válido")
