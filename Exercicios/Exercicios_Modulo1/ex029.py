v = int(input("Velocidade: "))
if v > 80:
    print("Você foi multado em R$ {},00 por excesso de velocidade!" .format((v-80)*7))