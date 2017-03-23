# coding: utf-8

from tkinter import *


#Classe de la VUE
class Vue():
     def __init__(self, parent, largeur, hauteur): #Parent = modele
        self.largeur = largeur
        self.hauteur = hauteur
        self.parent = parent
        self.root=Tk()
        
        #self.nouvelleTourArcher = False
        #self.nouvelleTourBombe = False
        #self.nouvelleTourCanon = False
        
        #initialisation des images 
        self.imgTourArcher = PhotoImage(file = "icones/tour_archer.png")
        self.imgTourBombe = PhotoImage(file = "icones/tour_bombe.png")
        self.imgTourCanon = PhotoImage(file = "icones/tour_canon.png")
        
        self.root.title("Mon premier Tkinter")
        
        self.cadreapp=Frame(self.root, bg="red", width=1000, height=1000)
                
        self.cadbtn=Frame(self.cadreapp, bg = "blue")
        self.cadScore=Frame(self.cadreapp, bg="green")
        self.cadUpdateTour=Frame(self.cadreapp, bg="yellow")
        
        
        labelAccessoires = Label(self.cadbtn, text = "--- OPTION ACCESSOIRES --- ")
        labelAccessoires.grid(row = 0, column = 0, columnspan=2, pady=10)
        #Bouton1 pour la tour archer
        btn1 = Button(self.cadbtn,image = self.imgTourArcher, height = 75, width = 75, command=self.parent.initialisationTourArcher)
        btn1.grid(row=1, column = 0, padx = 10, pady = 10)
        
        #Bouton2 pour la tour de bombe
        btn2 = Button(self.cadbtn,image =self.imgTourBombe, height = 75, width = 75, command=self.parent.initialisationTourBombe)
        btn2.grid(row=1, column = 1, padx = 10, pady = 10)
        
        #Bouton3 pour la tour de canon
        btn3 = Button(self.cadbtn,image = self.imgTourCanon, height = 75, width = 75, command=self.parent.initialisationTourCanon)
        btn3.grid(row=2, column = 0, padx = 10, pady = 10)
        
        #texte et textbox pour le nombre de creep
        label1 = Label(self.cadbtn, text = "Nombre de Creep : ")
        label1.grid(row = 3, column = 0, padx = 10, pady = 10)
        entry1 = Entry(self.cadbtn, width = 10)
        entry1.grid(row = 3, column = 1, padx = 10, pady = 10)
        
        #texte et textbox pour le nombre de vague
        label2 = Label(self.cadbtn, text = "Nombre de vagues : ")
        label2.grid(row = 4, column = 0, padx = 10, pady = 10)
        entry2 = Entry(self.cadbtn, width = 10)
        entry2.grid(row = 4, column = 1, padx = 10, pady = 10)
        
        #texte et textbox pour la vitesse des creeps
        label3 = Label(self.cadbtn, text = "Vitesse des creeps : ")
        label3.grid(row = 5, column = 0, padx = 10, pady = 10)
        entry3 = Entry(self.cadbtn, width = 10)
        entry3.grid(row = 5, column = 1, padx = 10, pady = 10)
        
         #texte et textbox pour le nombre de ressource disponible
        label4 = Label(self.cadbtn, text = "Nombre de Ressource : ")
        label4.grid(row = 6, column = 0, padx = 10, pady = 10)
        entry4 = Entry(self.cadbtn, width = 10)
        entry4.grid(row = 6, column = 1, padx = 10, pady = 10)
        
        #texte et textbox pour le nombre de ressource reçu lors d'un creeps décédé
        label5 = Label(self.cadbtn, text = "Ressource reçu des Creeps : ")
        label5.grid(row = 7, column = 0, padx = 10, pady = 10)
        entry5 = Entry(self.cadbtn, width = 10)
        entry5.grid(row = 7, column = 1, padx = 10, pady = 10)
        
        
        labelScoreJoueur = Label(self.cadScore, text = "--- SCORE DE LA PARTIE --- ")
        labelScoreJoueur.grid(row = 0, column = 0, columnspan=9, padx=10)
        #Texte pour les scores en bas de la fenêtre
        label6 = Label(self.cadScore, text = "Ressource : ")
        label6.grid(row=1, column = 0, padx = 20)
        
        #Texte pour les scores en bas de la fenêtre
        label7 = Label(self.cadScore, text = "Numéro de la vague : ")
        label7.grid(row=1, column = 1, padx = 20)
        
        #Texte pour les scores en bas de la fenêtre
        label8 = Label(self.cadScore, text = "Étoiles : ")
        label8.grid(row=1, column = 3, padx = 20)
        
        #ajout des étoiles
        etoileRempli = PhotoImage(file = "icones/etoile_rempli.png")
        label9 = Label(self.cadScore, bg = "green", image = etoileRempli)
        label9.grid(row = 1, column = 4, padx=2)
        label9.image = etoileRempli
        label10 = Label(self.cadScore, bg = "green", image = etoileRempli)
        label10.grid(row = 1, column = 5, padx=2)
        label10.image = etoileRempli
        label11 = Label(self.cadScore, bg = "green", image = etoileRempli)
        label11.grid(row =1, column = 6, padx=2)
        label11.image = etoileRempli
        label12 = Label(self.cadScore, bg = "green", image = etoileRempli)
        label12.grid(row = 1, column = 7, padx=2)
        label12.image = etoileRempli
        label13 = Label(self.cadScore, bg = "green", image = etoileRempli)
        label13.grid(row = 1, column = 8, padx=2)
        label13.image = etoileRempli
        
        #code pour la zone update de tour
        labelOptionTour = Label(self.cadUpdateTour, text = "--- OPTION TOUR --- ")
        labelOptionTour.grid(row = 0, column = 0, columnspan=3, pady=10)
        labelc= Label(self.cadUpdateTour, text = "Coût : ")
        labelc.grid(row = 1, column = 0, padx=10, pady=10)
        labelCout= Label(self.cadUpdateTour, text = " $$$$$ ")
        labelCout.grid(row = 1, column = 1, padx=10, pady=10)
        btnUpdate = Button(self.cadUpdateTour, text = "Amélioration")
        btnUpdate.grid(row = 1, column = 2, padx=10, pady=10)
        labeld= Label(self.cadUpdateTour, text = "Remb. : ")
        labeld.grid(row = 2, column = 0, padx=10, pady=10)
        labelCout= Label(self.cadUpdateTour, text = " $$$$$ ")
        labelCout.grid(row = 2, column = 1, padx=10, pady=10)
        btnDestruction = Button(self.cadUpdateTour, text = "Destruction")
        btnDestruction.grid(row = 2, column = 2, padx=10, pady=10)
        
        self.caddessin=Frame(self.cadreapp)
        self.canevas=Canvas(self.caddessin, width=self.largeur, height=self.hauteur, bg="white")
       
        #gerer le click dans la fenêtre
        
        self.canevas.bind("<Button-1>", self.gererClickGauche)
            
        
        #packer pour faire afficher dans le cadre ou dans le canvas
        #un layout manager par contenant
        self.cadreapp.pack()
        self.canevas.pack()    
        
        self.cadbtn.grid(row = 0, column = 1)
        self.cadScore.grid(row = 1, column = 0)
        self.cadUpdateTour.grid(row = 1, column = 1)
        self.caddessin.grid(row = 0, column = 0)
        
        
    
     def afficheModele(self, mod):    
        self.mod = mod
        #afficher les différentes tours
        #self.affichageTour()
         
     def gererClickGauche(self, evt):
         x= evt.x
         y=evt.y
         if self.parent.nouvelleTourBombe:
             self.parent.validationTourBombe(x,y)
         elif self.parent.nouvelleTourArcher:
             self.parent.validationTourArcher(x,y)
         elif self.parent.nouvelleTourCanon:
             self.parent.validationTourCanon(x, y)
         else:
             pass
     
     def affichageTourArcher(self, x, y):
         self.canevas.create_image(x, y, image = self.imgTourArcher, tags = ("TourArcher"))#ajouter tags   
        
class Joueur():
    def __init__(self, nom, score, ress, exp):
        self.nom = nom
        self.score = score
        self.ress = ress #ressources
        
    def setRessource(self, ressource):
        self.ress = ressource
        
# class Niveau():
#     def __init__(self, nbVagues, nbCreeps, ressourceMin, boss):
#         self.nbVagues = nbVagues
#         self.nbCreeps = nbCreeps
#         self.ressourceMin = ressourceMin
#         self.boss = boss
        
# class BossCreeps():
#     def __init__(self, hp, forceAtt, vitesse):
#         self.hp = hp
#         self.forceAtt = forceAtt
#         self.vitesse = vitesse
        
# class Creep():
#     def __init__(self, hp, forceAtt, vitesse, x, y):
#         self.hp = hp
#         self.forceAtt = forceAtt
#         self.vitesse = vitesse
#         self.x = x
#         self.y = y
        
#     def deplacement(self,x,y):
#         self.x = x
#         self.y = y

# #Classe du MODELE
# class Modele():
#     def __init__(self, largeur, hauteur):    
#         self.hauteur = hauteur
#         self.largeur = largeur
    
# #Classe du CONTROLEUR   
# class Controleur():
#     def __init__(self):
#         self.modele = Modele(800, 600)
#         self.vue = Vue(self,self.modele.largeur, self.modele.hauteur)
#         self.vue.afficheModele(self.modele)
    
#         self.vue.root.mainloop() 

# if __name__ == '__main__':
#     c = Controleur()