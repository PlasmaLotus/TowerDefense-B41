# coding: utf-8

from tkinter import *


#Classe de la VUE
class Vue():
     def __init__(self, parent, largeur, hauteur): #Parent = modele
        self.largeur = largeur
        self.hauteur = hauteur
        self.parent = parent
        self.root=Tk()
        
        self.root.title("Mon premier Tkinter")
        
        self.cadreapp=Frame(self.root, bg="red", width=1000, height=1000)
                
        self.cadbtn=Frame(self.cadreapp, bg = "blue", padx = 10)
        self.cadScore=Frame(self.cadreapp, bg="green", padx = 10, pady = 10)
        
        #Bouton1 pour la tour archer
        imgTourArcher = PhotoImage(file = "./icones/tour_archer.png")
        btn1 = Button(self.cadbtn,image = imgTourArcher, height = 75, width = 75, command=self.validationTourArcher())
        btn1.grid(row=0, column = 0, padx = 10, pady = 10)
        btn1.image = imgTourArcher
        
        #Bouton2 pour la tour de bombe
        imgTourBombe = PhotoImage(file = "./icones/tour_bombe.png")
        btn2 = Button(self.cadbtn,image =imgTourBombe, height = 75, width = 75, command=self.validationTourBombe())
        btn2.grid(row=0, column = 1, padx = 10, pady = 10)
        btn2.image = imgTourBombe
        
        #Bouton3 pour la tour de canon
        imgTourCanon = PhotoImage(file = "./icones/tour_canon.png")
        btn3 = Button(self.cadbtn,image =imgTourCanon, height = 75, width = 75, command=self.validationTourBombe())
        btn3.grid(row=1, column = 0, padx = 10, pady = 10)
        btn3.image = imgTourCanon
        
        #texte et textbox pour le nombre de creep
        label1 = Label(self.cadbtn, text = "Nombre de Creep : ")
        label1.grid(row = 2, column = 0, padx = 10, pady = 10)
        entry1 = Entry(self.cadbtn, width = 10)
        entry1.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        #texte et textbox pour le nombre de vague
        label2 = Label(self.cadbtn, text = "Nombre de vagues : ")
        label2.grid(row = 3, column = 0, padx = 10, pady = 10)
        entry2 = Entry(self.cadbtn, width = 10)
        entry2.grid(row = 3, column = 1, padx = 10, pady = 10)
        
        #texte et textbox pour la vitesse des creeps
        label3 = Label(self.cadbtn, text = "Vitesse des creeps : ")
        label3.grid(row = 4, column = 0, padx = 10, pady = 10)
        entry3 = Entry(self.cadbtn, width = 10)
        entry3.grid(row = 4, column = 1, padx = 10, pady = 10)
        
         #texte et textbox pour le nombre de ressource disponible
        label4 = Label(self.cadbtn, text = "Nombre de Ressource : ")
        label4.grid(row = 5, column = 0, padx = 10, pady = 10)
        entry4 = Entry(self.cadbtn, width = 10)
        entry4.grid(row = 5, column = 1, padx = 10, pady = 10)
        
        #texte et textbox pour le nombre de ressource reçu lors d'un creeps décédé
        label5 = Label(self.cadbtn, text = "Ressource reçu des Creeps : ")
        label5.grid(row = 6, column = 0, padx = 10, pady = 10)
        entry5 = Entry(self.cadbtn, width = 10)
        entry5.grid(row = 6, column = 1, padx = 10, pady = 10)
        
        #Texte pour les scores en bas de la fenêtre
        label6 = Label(self.cadScore, text = "Ressource : ")
        label6.grid(row=0, column = 0, padx = 20)
        
        #Texte pour les scores en bas de la fenêtre
        label7 = Label(self.cadScore, text = "Numéro de la vague : ")
        label7.grid(row=0, column = 1, padx = 20)
        
        #Texte pour les scores en bas de la fenêtre
        label8 = Label(self.cadScore, text = "Étoiles : ")
        label8.grid(row=0, column = 3, padx = 20)
        
        #ajout des étoiles
        etoileRempli = PhotoImage(file = "./icones/etoile_rempli.png")
        label9 = Label(self.cadScore, bg = "green", image = etoileRempli)
        label9.grid(row = 0, column = 4, padx=2)
        label9.image = etoileRempli
        label10 = Label(self.cadScore, bg = "green", image = etoileRempli)
        label10.grid(row = 0, column = 5, padx=2)
        label10.image = etoileRempli
        label11 = Label(self.cadScore, bg = "green", image = etoileRempli)
        label11.grid(row = 0, column = 6, padx=2)
        label11.image = etoileRempli
        label12 = Label(self.cadScore, bg = "green", image = etoileRempli)
        label12.grid(row = 0, column = 7, padx=2)
        label12.image = etoileRempli
        label13 = Label(self.cadScore, bg = "green", image = etoileRempli)
        label13.grid(row = 0, column = 8, padx=2)
        label13.image = etoileRempli
        
        self.caddessin=Frame(self.cadreapp)
        self.canevas=Canvas(self.caddessin, width=self.largeur, height=self.hauteur, bg="white")
       
        
        #packer pour faire afficher dans le cadre ou dans le canvas
        #un layout manager par contenant
        self.cadreapp.pack()
        self.canevas.pack()    
        
        self.cadbtn.pack(side = RIGHT)
        self.cadScore.pack(side = BOTTOM)
        self.caddessin.pack()
    
     def afficheModele(self, mod):    
        self.mod = mod
        
     def validationTourArcher(self):
         pass
      
     def validationTourBombe(self):
         pass
     
     def validationTourCanon(self):
         pass  
        
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