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
#delai d'affichage entre chaque changement de couleur des cases pendant l'iteration
delai = 100

###############################################################################################################################################
#Variables globales
L_coul = ["black", "yellow", "green", "blue", "white", "red", "magenta", "cyan"]
stop = 0
i0 = 0
j0 = 0

###############################################################################################################################################
#Fonctions
def maj ():
    """
    Met à jour les couleurs des carrés et réactive le bouton de lancement de l'itération
    """
    bouton_iter.config(state = tk.NORMAL)
    for i in range (taille):
        for j in range (taille):
                canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]])
    racine.after(delai,racine.update())

def config_alea ():
    """
    Créé une configuration aléatoire de taille (taille x taille) puis l'affiche grâce à la fonction maj
    """
    for i in range (taille):
        for j in range (taille):
            config[i][j] = rd.randint(0, 4)
    maj()

def config_pile ():
    pass

def config_max ():
    pass

def config_iden ():
    pass

def config_save ():
    pass

def iteration ():
    """
    - Si c'est la première fois que le bouton bouton_iter est cliqué :
      Lance l'itération et modifie le texte du bouton en "Mettre en pause l'itération".
    - Si c'est la deuxième fois que le bouton est cliqué :
      Stoppe l'itération et modifie le texte du bouton en "Reprendre l'itération".
    - Si c'est la troisième fois que le bouton est cliqué :
      Relance l'itération et modifie le texte du bouton en "Mettre en pause l'itération"
    - Si l'itération est finie :
      Stoppe l'iteration, modifie le texte du bouton en "Lancer l'itération" et désactive le bouton
    """
    global stop, i0, j0, compteur
    bouton_iter.config(text = "Mettre en pause l'itération")
    if stop == 0 :
        stop = 1
        compteur = 1
        while compteur != 0:
            compteur = 0
            for i in range (i0, taille):
                i0 = 0
                for j in range (j0, taille):
                    j0 = 0
                    if config[i][j] > 3 :
                        compteur += 1
                        config[i][j] -= 4
                        if i-1 > -1 :
                            config[i-1][j] += 1
                        if j+1 < taille :
                            config[i][j+1] += 1
                        if i+1 < taille :
                            config[i+1][j] += 1
                        if j-1 > -1 :
                            config[i][j-1] += 1
                        maj()
                    if stop == 2:
                        j0 = j
                        break
                if stop == 2:
                    i0 = i
                    break
            if stop == 2:
                break
    elif stop == 1 :
        bouton_iter.config(text = "Reprendre l'iteration")
        stop = 2
    elif stop == 2:
        stop = 0
        iteration()
    if stop == 1 and compteur == 0:
        bouton_iter.config(text = "Lancer l'iteration", state = tk.DISABLED)
        stop = 0

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
        L_obj[i] += [canvas.create_rectangle((i * coeff, j * coeff), ((i+1) * coeff, (j+1) * coeff), fill = "white")]
maj()

#Boucle principale
racine.mainloop()