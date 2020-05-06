import tkinter
import sys
import random

class MaFenetreGraphique(tkinter.Tk):

    def __init__(self, largeur = 200, hauteur = 200, parent = None):
        tkinter.Tk.__init__(self, parent)

        self.monCanvas = tkinter.Canvas(self, width = largeur, height = hauteur, background = "skyblue")
        self.monCanvas.pack()

        self.monLabel = tkinter.Label(self, text = "Bonjour !")
        self.monLabel.pack()
        
        a = random.randint(10, 20)
        b = random.randint(10, 20)
        c = random.randint(180, 190)
        d = random.randint(180, 190)

        def MaFonction1():
            self.monCanvas.create_oval(a, b, c, d, fill = "red")
          
        self.monBouton1 = tkinter.Button(self, text = "Trace un disque", command = MaFonction1)
        self.monBouton1.pack()

        def MaFonction2():
            self.quit()

        self.monBouton2 = tkinter.Button(self, text = "Quitter", command = MaFonction2)
        self.monBouton2.pack()

        def MaFonction3():
            self.monLabel["text"] = "Rebonjour !"

        self.monBouton3 = tkinter.Button(self, text = "Changement de texte...", command = MaFonction3)
        self.monBouton3.pack()

        def Mafonction4():
            self.monLabelFonction4 = tkinter.Label(self, text = "nombre de clics")
            self.monLabelFonction4.pack()

        self.monBouton4 = tkinter.Button(self, text = "Affiche le nombre de clics sur ce bouton", command = Mafonction4)
        self.monBouton4.pack()

        self.maVariableTexte = tkinter.StringVar()
        self.maVariableTexte.set("valeur de défaut")
        self.monChampDeSaisie = tkinter.Entry(self, textvariable = self.maVariableTexte)
        self.monChampDeSaisie.pack()


        self.mainloop()
    


MaFenetreGraphique()


# tracer une ligne : self.identifiantLine = self.monCanvas.create_line(0, 10, 300, 10, fill = "blue", width = 2)
# effacer cette ligne : self.monCanvas.delete(self.identifiantLine)
# 
# tracer une ellipse : self.identifiantOval = self.monCanvas.create_oval(25, 80, 275, 130, fill = "green", outline = "orange", width = 2)
# bouger cette ellipse : self.monCanvas.coords(self.identifiantOval, 0, 100, 300, 110)
# 
# tracer un triangle : self.identifiantTriangle = self.monCanvas.create_polygon(100, 190, 150, 140, 200, 190, fill = "black", outline = "blue", width = 8)
# bouger ce triangle : self.monCanvas.move(self.identifiantTriangle, 75, 0)     

class MaFenetreGraphique2(tkinter.Tk):

    def __init__(self, parent = None):
        tkinter.Tk.__init__(self, parent)

        self.maVariable1 = tkinter.IntVar()
        self.monChampDeSaisie1 = tkinter.Entry(self, textvariable = self.maVariable1)
        self.monChampDeSaisie1.grid(row = 1, column = 2)

        self.monLabel1 = tkinter.Label(self, text = "+")
        self.monLabel1.grid(row = 2, column = 1)

        self.maVariable2 = tkinter.IntVar()
        self.monChampDeSaisie2 = tkinter.Entry(self, textvariable = self.maVariable2)
        self.monChampDeSaisie2.grid(row = 2, column = 2)       

        self.monLabel2 = tkinter.Label(self, text = "=")
        self.monLabel2.grid(row = 3, column = 1) 
    
        def FonctionCalculer():
            x = self.maVariable1
            y = self.maVariable2
            self.maVariable3 = x + y
            self.monLabel3 = tkinter.Label(self, text = self.maVariable3)
            self.monLabel3.grid(row = 3, column = 2)

        self.monBouton = tkinter.Button(self, text = "Calculer !", command = FonctionCalculer)
        self.monBouton.grid(row = 4, column = 2)



        self.mainloop()

MaFenetreGraphique2()

# self.monBouton.grid(row = 2, column = 3)
# self.monChampDeSaisie1 = tkinter.Entry(self)
# self.monChampDeSaisie1.grid(row = 0, column = 1)
