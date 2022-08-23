km = float(input("Distância da viagem: "))
if km <= 200:
    print("Preço: {}".format(km*0.5))
else:
    print("Preço: {}" .format(km*0.45))