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

