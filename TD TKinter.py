import sys
import random


# Import du module tkinter
import tkinter

# Creation d'une classe qui herite de la classe tkinter.Tk
class MaFenetreGraphique(tkinter.Tk):
 def __init__(self,largeur=400,hauteur=400, parent = None):
    tkinter.Tk.__init__(self, parent)
    #texte label
    self.monLabel = tkinter.Label(self, text="pacman")
    self.monLabel.pack()
    # Declaration du contenu de la fenetre
    self.monCanvas = tkinter.Canvas(self, width = largeur, height = hauteur, background = "red")
    self.monCanvas.pack()
    #label
    self.monLabel = tkinter.Label(self, text="Texte du label")
    self.monLabel.pack()

    #bouton
    self.monBouton = tkinter.Button(self, text="Gagnez des millions")
    self.monBouton.pack()
    #champ de saisie (ceci peut être assimilé à un compteur de score)
    x=1
    self.maVariableTexte = tkinter.StringVar()
    self.maVariableTexte.set(x)
    self.monChampDeSaisie = tkinter.Entry(self, textvariable=self.maVariableTexte)
    self.monChampDeSaisie.pack()

    # Tracer une ligne du point (50, 100) au point (150, 25), de couleur rouge et d'epaisseur 4
    self.monCanvas.create_line(0, 0, 400, 400, fill="yellow", width=4)
    # Tracer un rectangle compris entre les points (150, 50) et (275, 100), avec un fond bleu clair et sans bordure
    self.monCanvas.create_rectangle(150, 70, 105, 100, fill="lightblue", outline="blue", width=0)
    # Tracer une ellipse comprise entre les points (25, 125) et (100, 175), avec un fond blanc et une bordure orange d'epaisseur 5
    self.monCanvas.create_oval(10, 125, 100, 50, fill="white", outline="orange", width="5")
    # Tracer une triangle défini par les points (125, 175), (175, 125) et (225, 150), avec un fond noir et avec une bordure bleue d'epaisseur 15
    self.monCanvas.create_polygon(125, 175, 175, 125, 225, 150, fill="black", outline="blue",width="15")
    #Editer ou supprimer un élément dans un Canvas 
    self.identifiantOval = self.monCanvas.create_oval(10, 125, 100, 50, fill="white", outline="orange", width="5")
    #supprimer un élement du Canvas
    self.monCanvas.delete(self.identifiantOval)
    # Deplace l'ellipse identifiee par self.identifiantEllipse de 50 pixels vers la droite, et de25 pixels vers le bas
    self.identifiantPolygon = self.monCanvas.create_polygon(125, 175, 175, 125, 225, 150, fill="black", outline="blue",width="15")
    self.monCanvas.move(self.identifiantPolygon, 50, 25)
    #Deforme le rectangle identifie par self.identifiantRectangle pour qu'il soit compris entreles points (100, 150) (150, 50)
    self.identifiantRectangle = self.monCanvas.create_rectangle(150, 70, 105, 100, fill="lightblue", outline="blue", width=0)
    self.monCanvas.coords(self.identifiantRectangle, 185, 12, 105, 100)
    #commandes (ne fonctionne pas encore)
    self.monBouton1 = tkinter.Button(self, text="Texte du bouton 1", command = self.monCanvas.create_rectangle(10,20, 120, 200, fill="blue"))
    self.monBouton1.pack()
    self.monBouton2 = tkinter.Button(self, text="Texte du bouton 2", command = self.monCanvas.move(self.identifiantPolygon, 50, 25))
    self.monBouton2.pack()
    self.mainloop()
    
    
    
   # Methodes propres a la fenetre
 # ...
# Creation d'un objet de type MaFenetreGraphique
MaFenetreGraphique()