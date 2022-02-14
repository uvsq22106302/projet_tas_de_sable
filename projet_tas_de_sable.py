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

taille = 100

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def maj ():
    global config
    global L_obj
    for i in range (taille):
        for j in range (taille):
                canvas.itemconfigure(L_obj[i][j], fill = get_color(255, (config[i][j]) * (255 // 3), 0))

def config_courante (taille):
    global config
    global L_obj
    config = [[0] * taille for i in range(taille)]
    L_obj = [[] * taille for i in range(taille)]

def aleatoire ():
    for i in range (taille):
        for j in range (taille):
            config[i][j] = rd.randint(0, 3)
    maj()

config_courante(taille)
racine = tk.Tk()
coeff = (min(racine.winfo_screenwidth(), racine.winfo_screenheight()) - 100) / taille
canvas = tk.Canvas(racine, height = taille * coeff, width = taille * coeff)
canvas.grid(column = 1, row = 0)
bouton = tk.Button(racine, text = "Configuration aléatoire", command = aleatoire)
bouton.grid(column = 0, row = 0)
for i in range (taille) :
    for j in range (taille) :
        L_obj[i] += [canvas.create_rectangle((i * coeff, j * coeff), ((i+1) * coeff, (j+1) * coeff), fill = "white")]
maj()

racine.mainloop()