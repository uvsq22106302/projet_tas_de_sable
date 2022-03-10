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
import copy as cp

###############################################################################################################################################
#Constantes
#taille de base de la grille
taille = 9

#delai d'affichage entre chaque changement de couleur de chaque case pendant l'iteration
delai = 100

#liste des couleurs des carrés, si il y a i grains de sable dans une case alors la couleur sera L_coul[i]
L_coul = ["black", "red", "green", "blue", "white", "yellow", "cyan", "magenta"]

#Nombre de grains de sable ajoutés par clic
nbr = 1

###############################################################################################################################################
#Variables globales
stop = 0
etape = 0
affiche = 1

###############################################################################################################################################
#Fonctions
def ajout_coul (i, j):
    """
    Si la case (i,j) a plus de grains de sable que de couleurs dans la liste L_coul : ajoute la couleur orange autant de fois que nécessaire
    """
    for n in range (config[i][j] - (len(L_coul) - 1)):
        L_coul.append("orange")

def init ():
    """
    Recalcule le coeff
    Initialise la grille à 0 grains de sable dans toutes les cases et créé les carrés
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
    Met entre 0 et 3 grains de sable à toutes les cases et met à jour la couleur des cases
    """
    global config, L_obj
    for i in range (taille):
        for j in range (taille):
            config[i][j] = rd.randint(0, 3)
            if affiche == 1:
                canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])

def fen_config_pile ():
    """
    Créé une sous-fenêtre "fen_pc" qui permet d'entrer le nombre de grains de sable voulus dans la case du milieu
    Quand la touche "Entrée" est appuyée : execute la fonction config_pile
    """
    global fen_pc, entree_pc
    fen_pc = tk.Toplevel()
    fen_pc.title("Fenêtre de selection de taille pour configuration pile centrée")
    entree_pc = tk.Entry(fen_pc)
    label_pc = tk.Label(fen_pc, text = "Veuillez saisir le nombre de grains de sable que vous voullez au milieu (attention, seuls les entiers sont accéptés).")
    entree_pc.pack(side = "bottom", fill ="x")
    label_pc.pack(side = "top", fill = "x")
    fen_pc.bind("<Return>", config_pile)

def config_pile (event):
    """
    Met 0 grains de sable à toutes les cases
    Puis met N (nombre choisi dans la sous-fenêtre "fen_pc") grains de sable à la case du milieu
    Met à jour la couleur des cases
    Ferme la sous-fenêtre "fen_pc"
    """
    global config, L_obj
    for i in range (taille):
        for j in range (taille):
            config[i][j] = 0
            if affiche == 1:
                canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])
    N = int(entree_pc.get())
    milieu = int(taille/2)
    config[milieu][milieu] = N
    ajout_coul(milieu, milieu)
    if affiche == 1:
        canvas.itemconfigure(L_obj[milieu][milieu], fill = L_coul[config[milieu][milieu]], outline = L_coul[config[milieu][milieu]])
    fen_pc.destroy()

def config_max ():
    """
    Mat 3 grains de sable à toute les cases et met à jour les couleurs des cases
    """
    global config, L_obj
    for i in range (taille):
        for j in range (taille):
            config[i][j] = 3
            if affiche == 1:
                canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])

def config_iden ():
    """
    Aditionne la configuration max stable à elle-même : on obtient double max stable
    Stabilise la configuration double max stable
    Soustrait double max stable stabilisée à double max stable
    Stabilise cette configuration
    Toutes ces actions sont faites sans changer les carrés, les carrés sont modifiés à la fin de la fonction
    """
    global affiche, operationv
    affiche = 0
    operationv = "additionner"
    config_max()
    config1 = cp.deepcopy(config)
    config2 = cp.deepcopy(config)
    operat(config1, config2)
    config1 = cp.deepcopy(config)
    iteration()
    config2 = cp.deepcopy(config)
    operationv = "soustraire"
    operat(config1,config2)
    iteration()
    affiche = 1
    for i in range (taille):
        for j in range (taille):
            canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])

def config_clic(event):
    """
    Ajoute ou enlève nbr grains de sable à la case qui a été cliquée
    """
    global config, L_obj
    i = int(event.x/coeff)
    j = int(event.y/coeff)
    if config[i][j] + nbr < 0 and nbr < 0:
        config[i][j] = 0
    else:
        config[i][j] += nbr
    ajout_coul(i, j)
    if affiche == 1:
        canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])

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

def config_save ():
    """
    Récupère la taille dans le fichier Sauvegarde.txt puis réinitialise la grille puis récupère la configuration dans Sauvegarde.txt et l'affiche sur la grille
    """
    global taille, config, L_obj
    file = open("sauvegarde.txt", "r")
    taille = int(file.readline())
    init()
    i = j = 0
    for ligne in file:
        config[i][j] = int(ligne)
        ajout_coul(i, j)
        if affiche == 1:
            canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])
        j += 1
        if j == taille:
            j = 0
            i += 1

def iteration():
    """
    Lance le processus de stabilisation en modifiant le bouton bouton_iter pour pouvoir stopper le processus
    Si rien n'a été modifié pendant la dernière fois que la grille à été parcourue : arrêt de l'itération et modification du bouton bouton_iter à son état d'origine
    Si la fonction etape est executée : parcoure une seule fois la grille
    Si la fonction arret est executée : arrêt du processus et modification du bouton bouton_iter à son état d'origine
    Actualise la couleurs des cases à chaque fois que la grille à étée parcourue une fois en atendant delai ms
    """
    global stop, config, L_obj, etape, compteur
    compteur = 1
    while compteur != 0:
        if etape == 0 and affiche == 1:
            bouton_iter.config(text = "Stopper l'itération", command = arret)
        compteur = 0
        for i in range (taille):
            for j in range (taille):
                if config[i][j] > 3 :
                    compteur += 1
                    config[i][j] -= 4
                    ajout_coul(i, j)
                    if affiche == 1:
                        canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])
                    if i-1 > -1 :
                        config[i-1][j] += 1
                        ajout_coul(i-1, j)
                        if affiche == 1:
                            canvas.itemconfigure(L_obj[i-1][j], fill = L_coul[config[i-1][j]], outline = L_coul[config[i-1][j]])
                    if j+1 < taille :
                        config[i][j+1] += 1
                        ajout_coul(i, j+1)
                        if affiche == 1:
                            canvas.itemconfigure(L_obj[i][j+1], fill = L_coul[config[i][j+1]], outline = L_coul[config[i][j+1]])
                    if i+1 < taille :
                        config[i+1][j] += 1
                        ajout_coul(i+1, j)
                        if affiche == 1 :
                            canvas.itemconfigure(L_obj[i+1][j], fill = L_coul[config[i+1][j]], outline = L_coul[config[i+1][j]])
                    if j-1 > -1 :
                        config[i][j-1] += 1
                        ajout_coul(i, j-1)
                        if affiche == 1 :
                            canvas.itemconfigure(L_obj[i][j-1], fill = L_coul[config[i][j-1]], outline = L_coul[config[i][j-1]])
                if stop == 1:
                        break
            if stop == 1:
                break
        if affiche == 1:
            racine.after(delai, racine.update())
        if compteur == 0:
            bouton_iter.config(text = "Lancer l'itération", command = iteration)
        if etape == 1:
            etape = 0
            break
        if stop == 1:
            stop = 0
            bouton_iter.config(text = "Lancer l'itération", command = iteration)
            break

def arret ():
    """
    Change la variable stop en 1
    """
    global stop
    stop = 1

def iteration_unique():
    """
    Change la variable etape en 1 et execute iteration
    """
    global etape
    etape = 1
    iteration()

def fen_change_taille():
    """
    Créé une sous-fenêtre "fen-t" qui permet d'entrer la nouvelle taille voulue
    Quand la touche "Entrée" est appuyée : execute la fonction change_taille
    """
    global taille, fen_t, entree_t
    fen_t = tk.Toplevel()
    fen_t.title("Fenêtre de changement de taille")
    entree_t = tk.Entry(fen_t)
    label_t = tk.Label(fen_t, text = "Veuillez saisir la nouvelle taille (attention, seuls les entiers sont accéptés).")
    entree_t.pack(side = "bottom", fill ="x")
    label_t.pack(side = "top", fill = "x")
    fen_t.bind("<Return>", change_taille)

def change_taille (event):
    """
    Réinitialise la grille avec la nouvelle taille choisie dans la sous-fenêtre "fen_t" et ferme cette sous-fenêtre
    """
    global taille
    taille = int(entree_t.get())
    fen_t.destroy()
    init()

def addi ():
    """
    Modifie les variables operation et operationv et execute la focntion fen_oper
    """
    global operation, operationv
    operation = "d'addition"
    operationv = "additionner"
    fen_operat()

def soustr ():
    """
    Modifie les variables operation et operationv et execute la focntion fen_oper
    """
    global operation, operationv
    operation = "de soustraction"
    operationv = "soustraire"
    fen_operat()

def fen_operat ():
    """
    Créé une sous fenêtre "fen_o" pour choisir avec quelle configuration il faut aditionner ou soustraire la configuration actuelle
    Quand la touche "Entrée" est appuyée : execute la fonction mem_config
    """
    global fen_o, var_o, L_o, affiche
    affiche = 0
    L_o = ["Configuration aléatoire", "Configuration Pile centrée", "Configuration Max Stable", "Configuration Identity", "Configuration sauvegardée"]
    fen_o = tk.Toplevel()
    fen_o.title("Fenêtre de choix " + operation)
    var_o = tk.StringVar(fen_o)
    var_o.set(L_o[0])
    menu_o = tk.OptionMenu(fen_o, var_o, *L_o)
    label_o = tk.Label(fen_o, text = "Veuillez choisir avec quelle configuration vous shouaitez " + operationv + " la configuration actuelle.")
    label_o.pack(side = "top", fill = "x")
    menu_o.pack(side = "bottom", fill = "x")
    fen_o.bind("<Return>", mem_config)

def mem_config (event):
    """
    Met la configuration actuelle et la configuration choisie dans la sous-fenêtre "fen_o" dans 2 variables différentes (config1 et config2)
    Ferme la sous-fenêtre "fen_o"
    Execute la fonction operat avec les deux configuration (config1 et config2)
    """
    global affiche, config, L_obj
    config1 = cp.deepcopy(config)
    configu = var_o.get()
    exist_fen_o = 1
    if configu == L_o[0]:
        config_alea()
        config2 = cp.deepcopy(config)
    if configu == L_o[1]:
        fen_config_pile()
        fen_o.destroy()
        racine.wait_window(fen_pc)
        exist_fen_o = 0
        config2 = cp.deepcopy(config)
    if configu == L_o[2]:
        config_max()
        config2 = cp.deepcopy(config)
    if configu == L_o[3]:
        config_iden()
        config2 = cp.deepcopy(config)
    if configu == L_o[4]:
        config_save()
        config2 = cp.deepcopy(config)
    affiche = 1
    if exist_fen_o == 1:
        fen_o.destroy()
    operat(config1, config2)

def operat (config1, config2):
    """
    Additionne ou soustrait (en fonction de la variable operationv) les configuration config1 et config2 (la soustrtaction étant config1 - config2)
    Met à jour les couleurs des cases
    """
    for i in range (taille):
        for j in range(taille):
            if operationv == "additionner":
                config[i][j] = config1[i][j] + config2[i][j]
                ajout_coul(i, j)
                if affiche == 1:
                    canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])
            elif operationv == "soustraire":
                if config1[i][j] - config2[i][j] < 0:
                    config[i][j] = 0
                else :
                    config[i][j] = config1[i][j] - config2[i][j]
                    ajout_coul(i, j)
                if affiche == 1:
                    canvas.itemconfigure(L_obj[i][j], fill = L_coul[config[i][j]], outline = L_coul[config[i][j]])

def fen_xclic ():
    """
    Créé une sous-fenêtre "fen-c" qui permet d'entrer le nouveau nombre de grains de sable à ajouter/supprimer pour un clic
    """
    global fen_c, entree_c
    fen_c = tk.Toplevel()
    fen_c.title("Fenêtre de choix de nombre de grains de sable ajoutés/supprimés par clic")
    label_c = tk.Label(fen_c, text = "Veuillez choisir le nombre de grains de sable que vous voullez ajouter/supprimer par clic (attention, seuls les entiers sont accéptés).")
    entree_c = tk.Entry(fen_c)
    label_c.pack(side = "top", fill = "x")
    entree_c.pack(side = "bottom", fill ="x")
    fen_c.bind("<Return>", xclic)

def xclic (event):
    """
    Met le nouveau nombre de grains de sable à ajouter/supprimer pour un clic dans la variable nbr et ferme la sous-fenêtre "fen_c"
    """
    global nbr
    nbr = int(entree_c.get())
    fen_c.destroy()
    
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
bouton_taille = tk.Button(racine, text = 'Changer la taille', command = fen_change_taille)
bouton_addi = tk.Button(racine, text = "Additionner une configuration", command = addi)
bouton_soustr = tk.Button(racine, text = "Soustraire une configuration", command = soustr)
bouton_xclic = tk.Button(racine, text = "Changer le nombre de grains de sable ajoutés/supprimés par clic", command = fen_xclic)
bouton_aleat = tk.Button(racine, text = "Configuration aléatoire", command = config_alea)
bouton_pile = tk.Button(racine, text = "Configuration Pile centrée", command = fen_config_pile)
bouton_max = tk.Button(racine, text = "Configuration Max Stable", command = config_max)
bouton_iden = tk.Button(racine, text = "Configuration Identity", command = config_iden)
bouton_save = tk.Button(racine, text = "Configuration sauvegardée", command = config_save)

#Placement des widgets
canvas.pack(side = "right")
bouton_iter.pack(side = "top", fill = "x")
bouton_etape.pack(side = "top", fill = "x")
bouton_sauv.pack(side = "top", fill = "x")
bouton_taille.pack(side = "top", fill = "x")
bouton_addi.pack(side = "top", fill = "x")
bouton_soustr.pack(side = "top", fill = "x")
bouton_xclic.pack(side = "top", fill = "x")
bouton_save.pack(side = "bottom", fill = "x")
bouton_iden.pack(side = "bottom", fill = "x")
bouton_max.pack(side = "bottom", fill = "x")
bouton_pile.pack(side = "bottom", fill ="x")
bouton_aleat.pack(side = "bottom", fill = "x")

#Liens
canvas.bind("<Button-1>", config_clic)

#Initialisation
init()

#Boucle principale
racine.mainloop()