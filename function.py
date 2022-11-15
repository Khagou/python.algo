def bonjour(prenom):
    phrase = "bonjour " + prenom
    return phrase


prenom = "caroline"
print(bonjour(prenom))


##################################################################


def hypothenuse(l1, l2):
    resultat = (l1**2+l2**2)**0.5
    return resultat


l1 = int(input("Entrez une valeur"))
l2 = int(input("entrez votre 2eme valeur"))

print("l'hypothenuse mesure", hypothenuse(l1, l2))


#####################################################################


cl = ["Monsieur ", "Madame "]
dp = [" 59", " 62"]
nt = [" francaise", " belge"]
jb = [" developpeur", " admin sys"]


def courrier(client, nom, dep, job, nat):

    if client == 1:
        client = cl[0]
    elif client == 2:
        client = cl[1]
    else:
        client = input("entrez la valeur correspondante")

    if dep == 1:
        dep = dp[0]
    elif dep == 2:
        dep = dp[1]
    else:
        dep = input("entrez la valeur correspondante")

    if nat == 1:
        nat = nt[0]
    elif nat == 2:
        nat = nt[1]
    else:
        nat = input("entrez la valeur correspondante")

    if job == 1:
        job = jb[0]
    elif job == 2:
        job = jb[1]
    else:
        job = input("entrez la valeur correspondante")

    email = client + nom + "\n \n Merci de contrôler l’exactitude de ces informations :\n - Vous vivez dans le département" + \
        dep + ".\n - Votre nationalité est"+nat + \
        "\n - Vous êtes"+job+"\n\n Cordialement"

    return email


print(cl)
client = int(input("entrez la valeur correspondante"))
print(dp)
dep = int(input("entrez la valeur correspondante"))
print(nt)
nat = int(input("entrez la valeur correspondante"))
print(jb)
job = int(input("entrez la valeur correspondante"))
nom = input("Entrez le nom du client")

print(courrier(client, nom, dep, job, nat))


####################################################################


def pair(nbr):
    x = 0

    for i in range(0, nbr):
        if i % 2 == 0:
            x = x+i
    return x+nbr


def impair(nbr):
    x = 0

    for i in range(0, nbr):
        if i % 2 == 1:
            x = x+i
    return x+nbr


nbr = int(input("saisir un nombre"))

if nbr % 2 == 0:
    print(pair(nbr))
else:
    print(impair(nbr))


for i in range(0, 10):
    x = 0
    x = x + i

print(x)
