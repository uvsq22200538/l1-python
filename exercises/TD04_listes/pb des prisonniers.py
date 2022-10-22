import random
nb_de_prisonniers = 100
nb_essai = 50

boites = [i for i in range(1, nb_de_prisonniers+1)]
random.shuffle(boites)
print(boites)

for i in range(1, nb_de_prisonniers+1):
    numero = i
    for o in range(nb_essai):
        if boites[i-1] == numero :
            print('Prisonnier', numero, 'trouve son numéro dans la boite', i, 'après', o+1, 'essais.')
            break
        else :
            i = boites[i-1]
    else :
        print('Prisonnier', numero, "n'a pas trouvé son numéro")
        break