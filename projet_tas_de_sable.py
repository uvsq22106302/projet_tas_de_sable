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

H = 100
W = 100

def creation_random () :
    Config_random= [[], [], []]
    print(Config_random)
    for i in range (3):
        for j in range (3):
            Config_random[i] += [rd.randint(0, 6)]
    return(Config_random)

racine=tk.Tk()
canvas=tk.Canvas(racine, height=H, widht=W)