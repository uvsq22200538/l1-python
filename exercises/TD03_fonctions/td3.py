def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    seconde = temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]
    return seconde


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours = seconde//86400
    heures = (seconde-86400*jours)//3600
    minutes = (seconde-86400*jours-3600*heures)//60
    secondes = (seconde-86400*jours-3600*heures-60*minutes)
    temps = (jours, heures, minutes, secondes)
    return temps


def sommeTemps(temps1,temps2):
    """Permet d'additionner 2 temps"""
    return secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))


def demandeTemps():
    """Permet de demander le temps à l'utilisateur"""
    temps, format = [], ("jour(s) : ", "heure(s) : ", "minute(s) : ", "seconde(s) : ", 999, 23, 59, 59)
    for i in range(4) :
        while True :
            try : 
                ans = int(input(format[i]))
                if 0 > ans or ans > format[i+4] : raise ValueError
                temps.append(ans)
                break

            except ValueError : 
                print("Entrée non valide")
                continue
    return temps


def afficheTemps(temps):
    "Permet de convertir le temps en phrase"
    if temps[0] > 1 : print(temps[0], "jours", end = " ")
    elif temps[0] == 1 : print("1 jour", end = " ")

    if temps[1] > 1 : print(temps[1], "heures", end = " ")
    elif temps[1] == 1 : print("1 heure", end = " ")

    if temps[2] > 1 : print(temps[2], "minutes", end = " ")
    elif temps[2] == 1 : print("1 minute", end = " ")

    if temps[3] > 1 : print(temps[3], "secondes", end = " ")
    elif temps[3] == 1 : print("1 seconde", end = " ")




"""
def tempsEnDate(temps):
    return (temps[0]//365, temps[0]%365, temps[1], temps[2], temps[3])

def afficheDate(date):
    jour_mois = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365)
    nom_mois = (' ', 'janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre')
    jour = 1
    for i in range(1,13) :
        if date[1] < jour_mois[i] :
            jour += date[1] - jour_mois[i-1]
            break
    

    print(str(jour) + ' ' + nom_mois[i] + ' ' + str(date[0]+1970) + ' à ' + str(date[2]) + ':' + str(date[3]) + ':' + str(date[4]))
    
temps = secondeEnTemps(1000000000)
#temps = secondeEnTemps(360000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
"""

"""
def bisextile(jour):
    date = 1970
    bis_count = 0
    while jour > 0 :
        if date % 4 == 0 and (date % 100 != 0 or date % 400 == 0) :
            bis_count += 1
            date += 1
            jour -= 366
        else :
            date += 1
            jour -= 365
    return bis_count
    
bisextile(20000)
"""

"""
def nombreBisextile(jour):
    date = 1970
    bis_count = 0
    while jour > 0 :
        if date % 4 == 0 and (date % 100 != 0 or date % 400 == 0) :
            bis_count += 1
            date += 1
            jour -= 366
        else :
            date += 1
            jour -= 365
    return bis_count

def tempsEnDateBisextile(date):
    
    return (temps[0]//365, temps[0]%365, temps[1], temps[2], temps[3])
   
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))
"""
l = [[0,'#FF0000aaaa'], [4], [1,'#FFzefjezjzefjnzef00FF']]
l.sort()
print(l)