continuar = 'S'
while continuar.upper() == 'S':
    print("\nOperação - Adição!\n")
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    soma = num1 + num2
    
    num1_str = int(num1) if num1.is_integer() else num1
    num2_str = int(num2) if num2.is_integer() else num2
    soma_str = int(soma) if soma.is_integer() else soma
    
    print(f"\n{num1_str} + {num2_str} = {soma_str}\n")
    continuar = input("Deseja realizar mais uma soma? [S ou N]\nResposta: ")
