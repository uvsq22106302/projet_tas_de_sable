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

#taille de base de la grille
taille = 9

#delai d'affichage entre chaque changement de couleur de chaque case pendant l'iteration
delai = 100

#liste des couleurs des carrés, si il y a i grains de sable dans une case alors la couleur sera L_coul[i]
L_coul = ["black", "red", "green", "blue", "white", "yellow", "cyan", "magenta"]

###############################################################################################################################################
#Variables globales

stop = 0
etape = 0

###############################################################################################################################################
#Fonctions

def init ():
    """
    Initialise la grille
    """
    global config, L_obj, coeff
    coeff = (min(racine.winfo_screenwidth(), racine.winfo_screenheight())/1.2) / taille
    config = [[0] * taille for i in range(taille)]
    L_obj = [[] * taille for i in range(taille)]
    for i in range (taille) :
        for j in range (taille) :
            L_obj[i] += [canvas.create_rectangle((i * coeff, j * coeff), ((i+1) * coeff, (j+1) * coeff), fill = L_coul[0], outline = L_coul[0])]

def config_alea ():
    """
    Créé une configuration aléatoire de taille (taille x taille) puis l'affiche grâce à la fonction maj
    """
    for i in range (taille):
        for j in range (taille):
            config[i][j] = rd.randint(0, 3)
            canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])

def config_pile ():
    config[taille//2][taille//2]= 6
    for i in range (taille):
        for j in range (taille):
            if config[i][j] != config[taille//2][taille//2]:
                config[i][j] = 0
            else:
                continue
    init()

def config_max ():          ##### configuration Max_stable qui injecte 3 grains de sable à chaque case
    for i in range(taille):     ##### i parcourt les cases
        for j in range(taille): #### j parcourt également les cases
            config_max[i][j]=3   #### Chaque case d'index i et j, attribué la valeur 3.
    init()

def config_iden(row,col):     ### Configuration Identity
    double_max=config_max[i][j]*2  ### double max est l'addition de Max_stable ave lui meme
    config_iden[row][col] = double_max  ### On attribue la valeur 6 à config_iden
    quotient = divmod(config_iden[row][col],4)     ### divmod est une fonction permettant d'afficher le quotient et le reste d'une division
    for row in range(taille):     ### row parcourt les cases
        for col in range(taille): ### col parcourt les cases
            if config_iden[row][col] > 3 :                                   ### si la config n'est pas stable donc >3 alors :
                for i,j in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:  ### i,j parcourt les cases voisines (celle d'au dessus, en dessous,de gauche et de droite)
                    config_iden[i][j] += quotient[0]                        #### On affecte a config_iden la valeur du quotient de divmod.
            else:
                return 
    init()

def config_clic(event):

    pass
    

def config_save ():
    """
    Récupère la taille dans le fichier Sauvegarde.txt puis réinitialise la grille puis récupère la configuration dans Sauvegarde.txt et l'affiche sur la grille
    """
    global taille
    file = open("sauvegarde.txt", "r")
    taille = int(file.readline())
    init()
    i = j = 0
    for ligne in file:
        config[i][j] = int(ligne)
        canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])
        j += 1
        if j == taille:
            j = 0
            i += 1

def iteration():
    """
    Lance l'iteration en modifiant le bouton bouton_iter
    Si la fonction arret est executée : arrêt de l'itération et modification du bouton bouton_iter
    Si rien n'a été modifié pendant la dernière itération : arrêt de l'itération et modification du bouton bouton_iter
    """
    global stop
    if etape == 0 :
        bouton_iter.config(text = "Stopper l'itération", command = arret)
    compteur = 0
    for i in range (taille):
        for j in range (taille):
            if stop == 1:
                bouton_iter.config(text = "Lancer l'itération", command = iteration)
                stop = 0
                return
            if config[i][j] > 3 :
                compteur += 1
                config[i][j] -= 4
                canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])
                if i-1 > -1 :
                    config[i-1][j] += 1
                    canvas.itemconfigure(L_obj[i-1][j], fill = L_coul[config[i-1][j]], outline = L_coul[config[i-1][j]])
                if j+1 < taille :
                    config[i][j+1] += 1
                    canvas.itemconfigure(L_obj[i][j+1], fill = L_coul[config[i][j+1]], outline = L_coul[config[i][j+1]])
                if i+1 < taille :
                    config[i+1][j] += 1
                    canvas.itemconfigure(L_obj[i+1][j], fill = L_coul[config[i+1][j]], outline = L_coul[config[i+1][j]])
                if j-1 > -1 :
                    config[i][j-1] += 1
                    canvas.itemconfigure(L_obj[i][j-1], fill = L_coul[config[i][j-1]], outline = L_coul[config[i][j-1]])
    racine.after(delai, racine.update())
    if compteur != 0 and stop == 0 and etape == 0:
        racine.after(0, iteration)
    if compteur == 0:
        bouton_iter.config(text = "Lancer l'itération", command = iteration)

def arret ():
    """
    Change la variable stop en 1
    """
    global stop
    stop = 1

def iteration_unique():
    """
    Change la variable etape en 1
    """
    global etape
    etape = 1
    iteration()

def sauvegarde ():
    """
    Supprime tout ce qu'il y a dans le fichier Sauvegarde.txt et sauvegarde la configuration (liste config) et la taille dans ce fichier
    """
    file = open("sauvegarde.txt", "w")
    file.write(str(taille) + "\n")
    for i in range (taille):
        for j in range (taille):
            file.write(str(config[i][j]) + "\n")
    file.close()

def change_taille():
    """
    Créé une autre petite fenêtre avec une entrée et un label pour permetttre de saisir un entier (taille) et un lien entre la touche "Entrée" et la fonction appui
    """
    global taille, fen, entree_taille

    fen = tk.Tk()
    fen.title("Fenêtre de changement de taille")
    entree_taille = tk.Entry(fen)
    label = tk.Label(fen, text = "Veuillez saisir la nouvelle taille (attention, seuls les entiers sont accéptés).")
    entree_taille.pack(side = "bottom", fill ="x")
    label.pack(side = "top", fill = "x")
    fen.bind("<Return>", appui)

def appui (event):
    """
    Réinitialise la grille avec la nouvelle taille et ferme la fenetre fen
    """
    global taille
    taille = int(entree_taille.get())
    fen.destroy()
    init()


def addition ():
    pass

def soustraction ():
    pass

###############################################################################################################################################
#Partie principale

#Création de la fenêtre
racine = tk.Tk()
racine.title("Simulation de l'écoulement du sable")

#Calcul du coefficient en fonction de la taille de l'écran actuel
coeff = (min(racine.winfo_screenwidth(), racine.winfo_screenheight())/1.2) / taille

#Creation des widgets
canvas = tk.Canvas(racine, height = taille * coeff, width = taille * coeff)
bouton_iter = tk.Button(racine, text = "Lancer l'itération", command = iteration)
bouton_etape = tk.Button(racine, text = "Faire une étape de l'itération", command = iteration_unique)
bouton_sauv = tk.Button(racine, text = 'Sauvegarder la configuration actuelle', command = sauvegarde)
bouton_taille = tk.Button(racine, text = 'Changer la taille', command = change_taille)
bouton_aleat = tk.Button(racine, text = "Configuration aléatoire", command = config_alea)
bouton_pile = tk.Button(racine, text = "Configuration Pile centrée", command = config_pile)
bouton_max = tk.Button(racine, text = "Configuration Max Stable", command = config_max)
bouton_iden = tk.Button(racine, text = "Configuration Identity", command = config_iden)
bouton_save = tk.Button(racine, text = "Configuration sauvegardée", command = config_save)

#Placement des widgets
canvas.pack(side = "right")
bouton_iter.pack(side = "top", fill = "x")
bouton_etape.pack(side = "top", fill = "x")
bouton_sauv.pack(side = "top", fill = "x")
bouton_taille.pack(side = "top", fill = "x")
bouton_save.pack(side = "bottom", fill = "x")
bouton_iden.pack(side = "bottom", fill = "x")
bouton_max.pack(side = "bottom", fill = "x")
bouton_pile.pack(side = "bottom", fill ="x")
bouton_aleat.pack(side = "bottom", fill = "x")

#Initialisation
init()

#Boucle principale
racine.mainloop()