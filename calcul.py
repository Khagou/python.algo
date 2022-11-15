# a = input("entrez le 1er chiffre")
# b = input("entrez le 2eme chiffre")
# c = input("entrez le 3eme chiffre")

# calcul = (int(a) + int(b)) * int(c)
# print(calcul)

# a = input("entrez le 1er chiffre ")
# b = input("entrez le 2eme chiffre ")
# c = input("entrez le 3eme chiffre ")
# d = input("entrez le 4eme chiffre ")
# e = input("entrez le 5eme chiffre ")

# moyenne = (int(a) + int(b) + int(c) + int(d) + int(e))/5
# print ("La moyenne est de " + str(moyenne))

# x = input("entrez la 1ere longueur ")
# y = input("entrez la 2eme longueur ")

# hypothenuse = str((int(x)**2 + int(y)**2)**0.5)
# print("La longueur de l'hypothenuse est de " + hypothenuseCarre)


time = int(input("entrez une duree en secondes : "))

heures=divmod(time, 3600)
minutes=divmod(heures[1], 60)
secondes=minutes[1]

print (time, "s =", heures[0], "heure(s)", minutes[0], "minutes", secondes, "secondes")
