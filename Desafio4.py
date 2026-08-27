nome = input("Digite o nome (mais de 3 caracteres): ")
while len(nome) <= 3:
    nome = input("Nome inválido. Digite novamente: ")

idade = int(input("Digite a idade (entre 0 e 150): "))
while idade < 0 or idade > 150:
    idade = int(input("Idade inválida. Digite novamente: "))

salario = float(input("Digite o salário (maior que 0): "))
while salario <= 0:
    salario = float(input("Salário inválido. Digite novamente: "))

sexo = input("Digite o sexo ('f' ou 'm'): ").lower()
while sexo not in ['f', 'm']:
    sexo = input("Sexo inválido. Digite 'f' ou 'm': ").lower()

estado_civil = input("Digite o estado civil ('s', 'c', 'v', 'd'): ").lower()
while estado_civil not in ['s', 'c', 'v', 'd']:
    estado_civil = input("Estado civil inválido. Digite 's', 'c', 'v' ou 'd': ").lower()

print("\nTodos os dados foram validados e cadastrados com sucesso!")
