#####################################################
# Groupe MI4
# Alexandre CHOLLET
# Adam HARBANE
# Bryan LE BLANC
# Kais CHEBOUB
# https://github.com/uvsq22106302/projet_tas_de_sable
#####################################################

import tkinter as tk

H = 500
W = 500

racine=tk.Tk()
canvas=tk.Canvas(racine, height=H, width=W, relief="ridge",borderwidth=3)
Bouton= tk.Button(racine, padx=20,font=("lines","10"),text="...",relief="ridge",borderwidth=3)

canvas.grid(column=1,row=0)
Bouton.grid(column=0,row=0,rowspan=1)

racine.mainloop()

