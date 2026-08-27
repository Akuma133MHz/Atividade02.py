qtd = int(input("Quantos números deseja inserir? "))
contador = 0

soma = 0
maior = None
menor = None

while contador < qtd:
    num = float(input(f"Digite o {contador + 1}º número (entre 0 e 1000): "))
    
    while num < 0 or num > 1000:
        print("Valor inválido! Digite um número apenas entre 0 e 1000.")
        num = float(input(f"Digite novamente o {contador + 1}º número: "))
        
    soma += num
    
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num
        
    contador += 1

print(f"\nMenor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")
