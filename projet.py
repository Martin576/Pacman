print(42)

# labyrinthe stable 10x10
#étape 1 
def creerLabyrinthe10x10 (): 
  laby = [[]] * 11
  for i in range (0, 11):
    laby[i] = [0] * (11)
  laby[0][0] = [True, True]
  laby[0][10] = [True, False]
  for i in range (1, 10):
    laby[0][i] = [False, True]
  for j in range (1, 10):
    laby[j][0] = [True, False]
    laby[j][10] = [True, False]
    for k in range (1, 10):
      laby[j][k] = [False, False]
  laby[10][0] = [False, True]
  laby[10][10] = [False, False]
  for m in range (1, 10):
    laby[10][m] = [False,True]
  laby[0][2] = [True,True]
  laby[0][6] = [True,True]
  laby[1][2] = [False,True]
  laby[1][4] = [False,True]
  laby[1][5] = [True, False]
  laby[1][6] = [True, False]
  laby[1][7] = [False,True]
  laby[1][8] = [True, False]
  laby[1][9]= [True, True]
  laby[2][1]= [False, True]
  laby[2][2]= [True, False]
  laby[2][4]= [True, False]
  laby[2][5]= [True, False]
  laby[2][6]= [True, False]
  laby[2][7]= [True, True]
  laby[3][2]= [True, True]
  laby[3][3]= [True, True]
  laby[3][7]= [False, True]
  laby[3][8]= [True, False]
  laby[4][0]= [True, True]
  laby[4][3]= [True, False]
  laby[4][4]= [False, True]
  laby[4][5]= [True, True]
  laby[4][6]= [True, True]
  laby[4][7]= [False, True]
  laby[4][8]= [False, True]
  laby[5][2]=[True,False]
  laby[5][3]=[False,True]
  laby[5][4]=[True,False]
  laby[5][5]=[True,True]
  laby[5][6]=[True,False]
  laby[5][7]=[False,True]
  laby[5][8]=[False,True]
  laby[5][9]=[True,False]
  laby[6][1]=[True,True]
  laby[6][3]=[True,True]
  laby[6][8]=[True,False]
  laby[7][1]=[False,True]
  laby[7][2]=[True,False]
  laby[7][3]=[False,True]
  laby[7][5]=[True,True]
  laby[7][6]=[True,False]
  laby[7][8]=[False,True]
  laby[7][9]=[True,False]
  laby[8][1]=[True,False]
  laby[8][2]=[False,True]
  laby[8][3]=[True,True]
  laby[8][5]=[False,True]
  laby[8][6]=[True,False]
  laby[8][7]=[True,True]
  laby[9][0]=[True,True]
  laby[9][3]=[False,True]
  laby[9][4]=[False,True]
  laby[9][6]=[True,False]
  laby[9][9]=[False,True]
  return(laby)

def creerLabyrinthe6x6(): 
  laby = [[]] * (7)
  for i in range (0, 7):
    laby[i] = [0] * (7)
  laby[0][0] = [True, True]
  laby[0][6] = [True, False]
  for i in range (1, 6):
    laby[0][i] = [False, True]
  for j in range (1, 6):
    laby[j][0] = [True, False]
    laby[j][6] = [True, False]
    for k in range (1, 6):
      laby[j][k] = [False, False]
  laby[6][0] = [False, True]
  laby[6][6] = [False, False]
  for m in range (1, 6):
    laby[6][m] = [False,True]
  laby[0][1] = [True, True]
  laby[1][1] = [False, True]
  laby[1][2] = [False, True]
  laby[1][3] = [False, True]
  laby[1][4] = [True, False]
  laby[1][5] = [True, False]
  laby[2][1] = [False, True]
  laby[2][2] = [True, True]
  laby[2][5] = [False, True]
  laby[3][0] = [True, True]
  laby[3][1] = [True, False]
  laby[3][2] = [True, False]
  laby[3][3] = [False, True]
  laby[3][4] = [True, False]
  laby[3][5] = [False, True]
  laby[4][1] = [True, False]
  laby[4][2] = [False, True]
  laby[4][3] = [False, True]
  laby[4][5] = [True, False]
  laby[5][1] = [False, True]
  laby[5][3] = [False, True]
  laby[5][4] = [True, True]
  return(laby)

# Fonction : hauteurLabyrinthe
def hauteurLabyrinthe(laby): 
  h = len(laby) - 1
  return(h)

# Fonction : largeurLabyrinthe
def largeurLabyrinthe(laby): 
  l = len(laby[0]) - 1
  return(l)

def afficherUnMurAuDessus():
  return("+---")
def afficherPasDeMurAuDessus():
  return("+   ")
def afficherUnMurAGauche():
  return("|")
def afficherPasDeMurAGauche():
  return(" ")
def afficherContenuCase(iCase, jCase, iJoueur, jJoueur, tableauParallele, iFantome, jFantome, iFantome2, jFantome2, iFantome3, jFantome3):
  if (((iCase == iFantome) and (jCase == jFantome)) or ((iCase == iFantome2) and (jCase == jFantome2)) or ((iCase == iFantome3) and (jCase == jFantome3))):
    return(" F ")
  if ((iCase == iJoueur) and (jCase == jJoueur)):
    return(" O ")
  else:
    if (tableauParallele[iCase][jCase] == True):
      return("   ")
    else:
      return(" • ")
    

def afficherUneLigneDuHaut(t):
  l = len(t)
  u = [0] * (l + 1)
  for i in range (0, l):
    if (t[i][1] == True):
      u[i] = afficherUnMurAuDessus()
    else:
      u[i] = afficherPasDeMurAuDessus()
  for j in range (0, l):
    print(u[j], end="")
  print()

def afficherUneLigneMilieu(ligne, iLigne, iJoueur, jJoueur, tableauParallele, iFantome, jFantome, iFantome2, jFantome2, iFantome3, jFantome3):
  l = len(ligne)
  u = [0] * (l + 1)
  for j in range (0, l):
    if (ligne[j][0] == True):
      u[j] = afficherUnMurAGauche() + afficherContenuCase(iLigne, j, iJoueur, jJoueur, tableauParallele, iFantome, jFantome, iFantome2, jFantome2, iFantome3, jFantome3)
    else:
      u[j] = afficherPasDeMurAGauche() + afficherContenuCase(iLigne, j, iJoueur, jJoueur, tableauParallele, iFantome, jFantome, iFantome2, jFantome2, iFantome3, jFantome3)
  for k in range (0, l):
    print(u[k], end="")
  print()

def afficherLabyrinthe(laby, iJoueur, jJoueur, tableauParallele, iFantome, jFantome, iFantome2, jFantome2, iFantome3, jFantome3):
  h = hauteurLabyrinthe(laby) + 1
  for i in range(0, h):
    afficherUneLigneDuHaut(laby[i])
    afficherUneLigneMilieu(laby[i],i,iJoueur,jJoueur, tableauParallele, iFantome, jFantome, iFantome2, jFantome2, iFantome3, jFantome3)

#laby1 = creerLabyrinthe10x10()
#afficherLabyrinthe(laby1)
#laby2 = creerLabyrinthe6x6()
#afficherLabyrinthe(laby2)

def tableauParallele():
  laby = creerLabyrinthe10x10()
  l = len(laby[0]) 
  h = len(laby) 
  tableau = [[]] * h
  for i in range (h):
    tableau[i] = [False] * l
  for k in range (l):
    tableau[10][k] = True
  for k in range (h):
    tableau[k][10] = True

  return(tableau)

import random

class Partie:

  def __init__(self):
    self.labyrinthe = creerLabyrinthe10x10()
    self.positionDuJoueur = (0, 0)
    self.positionFantome = (9,9)
    self.positionFantome2 = (0,9)
    self.positionFantome3 = (9, 0)
    self.tableauParallele =  tableauParallele()
    self.compteur = -1

  def afficherPositionJoueur(self):
    print("Position du joueur :", self.positionDuJoueur)

  def deplacerJoueurVersLaDroite(self):
    (i, j) = self.positionDuJoueur
    if (self.peutSeDeplacerVersLaDroite(i, j)==True):
      self.positionDuJoueur = (i, j+1)
    else:
      print("Il y a un mur à droite....")

  def peutSeDeplacerVersLaDroite(self, iActuel, jActuel):
    return self.labyrinthe[iActuel][jActuel + 1][0] == False

  def deplacerJoueurVersLaGauche(self):
    (i, j) = self.positionDuJoueur
    if (self.peutSeDeplacerVersLaGauche(i, j)==True):
      self.positionDuJoueur = (i, j-1)
    else:
      print ("Mur à gauche...")

  def peutSeDeplacerVersLaGauche(self, iActuel, jActuel):
    return self.labyrinthe[iActuel][jActuel][0] == False

  def deplacerJoueurVersLeHaut(self):
    (i, j) = self.positionDuJoueur
    if (self.peutSeDeplacerVersLeHaut(i, j) == True):
      self.positionDuJoueur = (i-1, j)
    else:
      print("Il y a un mur en haut....")

  def peutSeDeplacerVersLeHaut(self, iActuel, jActuel):
    return self.labyrinthe[iActuel][jActuel][1] == False   
  
  def deplacerJoueurVersLeBas(self):
    (i, j) = self.positionDuJoueur
    if (self.peutSeDeplacerVersLeBas(i, j)==True):
      self.positionDuJoueur = (i+1, j)
    else:
      print ("Mur en Bas...")

  def peutSeDeplacerVersLeBas(self, iActuel, jActuel):
    x = self.labyrinthe[iActuel + 1][jActuel]
    if (self.labyrinthe[iActuel + 1][jActuel][1] == False):
      return(True)

  def mettreAJourTableauTest(self):
    (i, j) = self.positionDuJoueur
    if (self.tableauParallele[i][j] == True):
      self.tableauParallele[i][j] = True
    else :
      self.tableauParallele[i][j] = True
      self.compteur = self.compteur + 1
    return(self.tableauParallele)

  def afficher(self):
    # Ecrire une belle fonction qui utilise self.labyrinthe et self.positionDuJoueur
    (i, j) = self.positionDuJoueur
    (iFantome, jFantome) = self.positionFantome
    (iFantome2, jFantome2) = self.positionFantome2
    (iFantome3, jFantome3) = self.positionFantome3
    afficherLabyrinthe(self.labyrinthe, i, j, self.tableauParallele, iFantome, jFantome, iFantome2, jFantome2, iFantome3, jFantome3)

  def effectuerAction(self, partie, action):
    if (action == "haut"):
      partie.deplacerJoueurVersLeHaut()
    if (action == "bas"):
      partie.deplacerJoueurVersLeBas()
    if (action == "droite"):
      partie.deplacerJoueurVersLaDroite()
    if (action == "gauche"):
      partie.deplacerJoueurVersLaGauche()
    return(self.positionDuJoueur)

  def afficheLesCoordonneesDuJoueur(self):
    print(self.positionDuJoueur)

  def bougerAleatoirementUnFantome(self):
    (i, j) = self.positionFantome
    listeDesPositionsQueLeDePeutTirer = list()
    if (self.peutSeDeplacerVersLaDroite( i, j) == True):
      listeDesPositionsQueLeDePeutTirer.append(0)
    if (self.peutSeDeplacerVersLaGauche( i, j) == True):
      listeDesPositionsQueLeDePeutTirer.append(1)
    if (self.peutSeDeplacerVersLeHaut( i, j) == True):
      listeDesPositionsQueLeDePeutTirer.append(2)
    if (self.peutSeDeplacerVersLeBas( i, j) == True):
      listeDesPositionsQueLeDePeutTirer.append(3)
    longueur = len(listeDesPositionsQueLeDePeutTirer)
    x = random.randint(0,longueur-1)
    position = listeDesPositionsQueLeDePeutTirer.pop(x)
    if (position == 0):
      self.positionFantome = (i, j+1)
    if (position == 1):
      self.positionFantome = (i, j-1)
    if (position == 2):
      self.positionFantome = (i-1, j)
    if (position == 3):
      self.positionFantome = (i+1, j)
    return(self.positionFantome)
         
  def bougerAleatoirementUnFantome2(self):
    (i, j) = self.positionFantome2
    listeDesPositionsQueLeDePeutTirer = list()
    if (self.peutSeDeplacerVersLaDroite( i, j) == True): 
      listeDesPositionsQueLeDePeutTirer.append(0)
    if (self.peutSeDeplacerVersLaGauche( i, j) == True):
      listeDesPositionsQueLeDePeutTirer.append(1)
    if (self.peutSeDeplacerVersLeHaut( i, j) == True):
      listeDesPositionsQueLeDePeutTirer.append(2)
    if (self.peutSeDeplacerVersLeBas( i, j) == True):
      listeDesPositionsQueLeDePeutTirer.append(3)
    longueur = len(listeDesPositionsQueLeDePeutTirer)
    x = random.randint(0,longueur-1)
    position = listeDesPositionsQueLeDePeutTirer.pop(x)
    if (position == 0):
      self.positionFantome2 = (i, j+1)
    if (position == 1):
      self.positionFantome2 = (i, j-1)
    if (position == 2):
      self.positionFantome2 = (i-1, j)
    if (position == 3):
      self.positionFantome2 = (i+1, j)
    return(self.positionFantome2)
  
  def bougerAleatoirementUnFantome3(self):
    (i, j) = self.positionFantome3
    listeDesPositionsQueLeDePeutTirer = list()
    if (self.peutSeDeplacerVersLaDroite( i, j) == True):
      listeDesPositionsQueLeDePeutTirer.append(0)
    if (self.peutSeDeplacerVersLaGauche( i, j) == True):
      listeDesPositionsQueLeDePeutTirer.append(1)
    if (self.peutSeDeplacerVersLeHaut( i, j) == True):
      listeDesPositionsQueLeDePeutTirer.append(2)
    if (self.peutSeDeplacerVersLeBas( i, j) == True):
      listeDesPositionsQueLeDePeutTirer.append(3)
    longueur = len(listeDesPositionsQueLeDePeutTirer)
    x = random.randint(0,longueur-1)
    position = listeDesPositionsQueLeDePeutTirer.pop(x)
    if (position == 0):
      self.positionFantome3 = (i, j+1)
    if (position == 1):
      self.positionFantome3 = (i, j-1)
    if (position == 2):
      self.positionFantome3 = (i-1, j)
    if (position == 3):
      self.positionFantome3 = (i+1, j)
    return(self.positionFantome3)


def recupererProchainAction():
  action = input("Quelle est votre action ? (entre haut, bas, droite ou gauche)")
  return(action)  


partie = Partie()

partie.afficherPositionJoueur()

partie.afficher()
while(True):
  partie.mettreAJourTableauTest()
  partie.bougerAleatoirementUnFantome()
  partie.bougerAleatoirementUnFantome2()
  partie.bougerAleatoirementUnFantome3()
  #print (partie.mettreAJourTableauTest())
  partie.afficherPositionJoueur()
  print("Score : " ,partie.compteur)
  prochaineAction = recupererProchainAction() # Fonction basée sur input()
  partie.effectuerAction(partie, prochaineAction)
  partie.afficher()
  if (partie.compteur == 98):
    print("VOUS AVEZ GAGNE !!!!!!!!!!!!!!!!!!!!!!!!!!!")
    break
  if (partie.positionDuJoueur == partie.positionFantome):
    print("VOUS AVEZ PERDU !!!!!!!!!!!!!!!!!!!!!!!!!!!")
    break

 
