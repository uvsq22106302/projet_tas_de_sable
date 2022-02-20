#####################################################
# Groupe MI4
# Alexandre CHOLLET
# Adam HARBANE
# Bryan LE BLANC
# Kais CHEBOUB
# https://github.com/uvsq22106302/projet_tas_de_sable
#####################################################

###############################################################################################################################################
#Importation des modules
import tkinter as tk
import random as rd

###############################################################################################################################################
#Constantes
#taille de la grille
taille = 9
#delai d'affichage entre chaque changement de couleur de chaque case pendant l'iteration
delai = 50

###############################################################################################################################################
#Variables globales
L_coul = ["black", "yellow", "green", "blue", "white", "red", "magenta", "cyan"]
stop = 0

###############################################################################################################################################
#Fonctions
def maj ():
    """
    Met à jour la couleur de tous les carrés
    """
    for i in range (taille):
        for j in range (taille):
                canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])

def maj_unique(i,j):
    """
    Mat à jour la couleur du carré en position (i, j) en actualisant l'affichage juste après
    """
    canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])
    racine.after(delai, racine.update())

def config_alea ():
    """
    Créé une configuration aléatoire de taille (taille x taille) puis l'affiche grâce à la fonction maj
    """
    for i in range (taille):
        for j in range (taille):
            config[i][j] = rd.randint(0, 3)
    maj()

def config_pile ():
    pass

def config_max ():
    pass

def config_iden ():
    pass

def config_save ():
    pass

def iteration():
    """
    Lance l'iteration en modifiant le bouton bouton_iter
    Si la fonction arret est executée : arrêt de l'itération et modification du bouton bouton_iter
    Si rien n'a été modifié pendant la dernière itération : arrêt de l'itération et modification du bouton bouton_iter
    """
    global stop
    bouton_iter.config(text = "Stopper l'itération", command = arret)
    compteur = 0
    for i in range (taille):
        for j in range (taille):
            if stop == 1:
                bouton_iter.config(text = "Lancer l'itération", command = iteration)
                stop = 0
                return()
            if config[i][j] > 3 :
                compteur += 1
                config[i][j] -= 4
                maj_unique(i,j)
                if i-1 > -1 :
                    config[i-1][j] += 1
                    maj_unique(i-1,j)
                if j+1 < taille :
                    config[i][j+1] += 1
                    maj_unique(i,j+1)
                if i+1 < taille :
                    config[i+1][j] += 1
                    maj_unique(i+1,j)
                if j-1 > -1 :
                    config[i][j-1] += 1
                    maj_unique(i,j-1)
    if compteur != 0 and stop == 0:
        racine.after(0, iteration)
    if compteur == 0:
        bouton_iter.config(text = "Lancer l'itération", command = iteration)

def arret ():
    """
    Fonction qui change la variable stop en 1
    """
    global stop
    stop = 1

###############################################################################################################################################
#Partie principale

#Création de la fenêtre
racine = tk.Tk()

#Calcul du coefficient en fonction de la taille de l'écran actuel
coeff = (min(racine.winfo_screenwidth(), racine.winfo_screenheight())/1.2) / taille

#Creation des widgets
canvas = tk.Canvas(racine, height = taille * coeff, width = taille * coeff)
bouton_aleat = tk.Button(racine, text = "Configuration aléatoire", command = config_alea)
bouton_pile = tk.Button(racine, text = "Configuration Pile centrée", command = config_pile)
bouton_max = tk.Button(racine, text = "Configuration Max Stable", command = config_max)
bouton_iden = tk.Button(racine, text = "Configuration Identity", command = config_iden)
bouton_save = tk.Button(racine, text = "Configuration sauvegardée", command = config_save)
bouton_iter = tk.Button(racine, text = "Lancer l'itération", command = iteration, state = tk.NORMAL)

#Placement des widgets
canvas.pack(side = "right")
bouton_aleat.pack(side = "top", fill = "x")
bouton_pile.pack(side = "top", fill ="x")
bouton_max.pack(side = "top", fill = "x")
bouton_iden.pack(side = "top", fill = "x")
bouton_save.pack(side = "top", fill = "x")
bouton_iter.pack(side = "bottom", fill = "x")

#Initialisation
config = [[0] * taille for i in range(taille)]
L_obj = [[] * taille for i in range(taille)]
for i in range (taille) :
    for j in range (taille) :
        L_obj[i] += [canvas.create_rectangle((i * coeff, j * coeff), ((i+1) * coeff, (j+1) * coeff), fill = "black", outline = "black")]
maj()

#Boucle principale
racine.mainloop()