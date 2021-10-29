###############################################################
maList = [int(input('Nombre 1:')), int(input('Nombre 2:'))]

somme, index = 0, 0

for n in maList:
    for i in range(1, n + 1):
        if not n % i: somme += i if not index else -i

    index += 1

print("Les nombres", maList[0], "et", maList[1], "sont amicaux" if not somme else "ne sont pas amicaux")
###############################################################

