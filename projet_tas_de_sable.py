#####################################################
# Groupe MI4
# Alexandre CHOLLET
# Adam HARBANE
# Bryan LE BLANC
# Kais CHEBOUB
# https://github.com/uvsq22106302/projet_tas_de_sable
#####################################################

import tkinter as tk
import random as rd

taille = 9

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def maj ():
    for i in range (taille):
        for j in range (taille):
                canvas.itemconfigure(L_obj[i][j], fill = get_color((config[i][j]) * (255 // 3), (config[i][j]) * (255 // 3), 255 - (config[i][j]) * (255 // 3)))

def config_coura ():
    global config
    global L_obj
    config = [[0] * taille for i in range(taille)]
    L_obj = [[] * taille for i in range(taille)]
    for i in range (taille) :
        for j in range (taille) :
            L_obj[i] += [canvas.create_rectangle((i * coeff, j * coeff), ((i+1) * coeff, (j+1) * coeff), fill = "white")]
    maj()

def config_alea ():
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

def iteration ():
    pass

racine = tk.Tk()
coeff = (min(racine.winfo_screenwidth(), racine.winfo_screenheight())/1.2) / taille
canvas = tk.Canvas(racine, height = taille * coeff, width = taille * coeff)
canvas.pack(side = "right")
bouton_coura = tk.Button(racine, text = "Configuration courante", command = config_coura)
bouton_coura.pack(side = "top", fill = "x")
bouton_aleat = tk.Button(racine, text = "Configuration aléatoire", command = config_alea)
bouton_aleat.pack(side = "top", fill = "x")
bouton_pile = tk.Button(racine, text = "Configuration Pile centrée", command = config_pile)
bouton_pile.pack(side = "top", fill ="x")
bouton_max = tk.Button(racine, text = "Configuration Max Stable", command = config_max)
bouton_max.pack(side = "top", fill = "x")
bouton_iden = tk.Button(racine, text = "Configuration Identity", command = config_iden)
bouton_iden.pack(side = "top", fill = "x")
bouton_iter = tk.Button(racine, text = "Lancer l'itération", command = iteration)
bouton_iter.pack(side = "bottom", fill = "x")
config_coura()
maj()

racine.mainloop()