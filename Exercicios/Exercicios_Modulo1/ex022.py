nome = str(input("Digite seu nome completo "))

print(nome.upper()) 
print(nome.lower()) 
nome2 = nome.split()
print(len("".join(nome2))) #n° letras sem espaços
print(len(nome2[0])) #n° letras do primeiro nome