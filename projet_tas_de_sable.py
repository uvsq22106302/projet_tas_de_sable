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

def creation_random () :
    Config_random= [[], [], []]
    print(Config_random)
    for i in range (3):
        for j in range (3):
            Config_random[i] += [rd.randint(0, 6)]
    return(Config_random)

racine=tk.Tk()
canvas=tk.Canvas(racine, height=H, width=W, relief="ridge",borderwidth=3)
Bouton= tk.Button(racine, padx=20,font=("lines","10"),text="...",relief="ridge",borderwidth=3)

canvas.grid(column=1,row=0)
Bouton.grid(column=0,row=0,rowspan=1)

racine.mainloop()

