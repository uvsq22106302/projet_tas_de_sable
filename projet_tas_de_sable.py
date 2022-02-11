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

H = 500
W = 500

def config_courante (p, q):
    global config
    config = [[0] * p for i in range(q)]

def maj ():
    global config
    for i in range (len(config) - 1):
        for j in range (len(config[0]) - 1):
            if config[i][j] == 0 :
                color = "purple"
            if config[i][j] == 1 :
                color = "blue"
            if config[i][j] == 2 :
                color = "green"
            if config[i][j] == 3 :
                color = "yellow"
            
racine=tk.Tk()
canvas=tk.Canvas(racine, height = H, width = W, relief="ridge",borderwidth = 3)
Bouton= tk.Button(racine, padx = 20, font = ("lines", "10"), text = "...", relief = "ridge", borderwidth = 3)

canvas.grid(column = 1, row = 0)
Bouton.grid(column = 0, row = 0, rowspan = 1)

racine.mainloop()