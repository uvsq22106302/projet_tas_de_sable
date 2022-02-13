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

taille = 3
H = taille * 100
W = taille * 100

def config_courante (taille):
    global config
    global L_obj
    config = [[0] * taille for i in range(taille)]
    L_obj = [[] * taille for i in range(taille)]

def maj ():
    global config
    global L_obj
    for i in range (taille):
        for j in range (taille):
                canvas.itemconfigure(L_obj[i][j], fill = get_color(255, (config[i][j]) * (255 // ((taille + 1) * 2)), 0))

def get_color(r=0, g=0, b=0):
    """ Retourne une couleur à partir de ses composantes r, g, b"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
            
config_courante(taille)
racine = tk.Tk()
canvas = tk.Canvas(racine, height = H, width = W)
canvas.grid(column = 1, row = 0)
bouton = tk.Button(racine, padx = 20, font = ("lines", "10"), text = "...", relief = "ridge", borderwidth = 3)
bouton.grid(column = 0, row = 0, rowspan = 1)
for i in range (taille) :
    for j in range (taille) :
        L_obj[i] += [canvas.create_rectangle((i * 100, j * 100), ((i+1) * 100, (j+1) * 100), fill = "white")]
maj()

racine.mainloop()