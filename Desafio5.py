numero = int(input("Digite um número inteiro: "))

if numero < 2:
    print(f"O número {numero} não é primo.")
else:
    divisor = 2
    eh_primo = True
    
    while divisor <= numero ** 0.5:
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1
        
    if eh_primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
