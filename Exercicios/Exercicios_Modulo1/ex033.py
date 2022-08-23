n1 = int(input("Primeiro número: "))
n2 = int(input("Segunda número: "))
n3 = int(input("Terceiro número: "))

if n1 > n2 and n1 > n3:
    print("{} é o maior" .format(n1))
elif n2 > n1 and n2 > n3:
    print("{} é  o maior" .format(n2))
else:
    print("{} é o maior" .format(n3))