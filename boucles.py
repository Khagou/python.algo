# semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
# i=0

# while i < 7:
#     print(semaine[i])
#     i= i+1

# tab = [10, 14, 2, 6, 9, 23, 21, 49, 90, 239, 21]
# i=0
# x=0

# while i < 11:
#     x = x+tab[i]
#     i= i+1

# print(x)

# liste_total=[12,24,32,41,5,96,72,82,90]

# for i in liste_total:
#     if i%2 == 0:
#         print( i, "est paire")
#     else:
#         print(i, "est impaire")

# tabl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i=0

# while i < 5:
#     print(tabl[i])
#     i= i+1

# for i in tabl:
#     if i <= 5:
#         print(i)
#     else:
#         break

# import random

# rnd = random.randint(0, 10)
# nb = int(input("choissisez un chiffre entre 0 et 10 :"))

# while nb != rnd:
#     nb = int(input("Dommage, choissisez un nouveau chiffre entre 0 et 10 :"))
# print("bravo vous avez trouvez le chiffre qui est le chiffre", nb)

# table = 0

# while table <= 20:
#     if (table % 3) == 0:
#         print (table * 7, "*")
#     else:
#         print (table * 7)

#     table += 1

# paper = 0.1
# i = 0

# while paper <= 324000:
#     paper = paper * 2
#     i = i+1
# print(i)

# import random

# x = 0
# y = 0
# i = 0
# p = 0

# while i <= 10:
#     x = random.randint(0, 10)
#     y = random.randint(0, 10)
#     a = x * y
#     r = int(input("Entrez le resultat de " + str(x) + "x" + str(y) + ":"))
#     i = i+1
#     if r == a:
#         print("bonne reponse")
#         p = p + 1
#     else:
#         print("Dommage la reponse etait", a)
# if p >= 5:
#     print("Bien joue votre score est de", str(p)+"/10")
# else:
#     print("Votre score est de", str(p)+"/10 vous ferez mieux la prochaine fois")
