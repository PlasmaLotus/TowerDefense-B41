
from game import Game
from vue import Vue

#Classe du CONTROLEUR   
class Controleur():
    def __init__(self):
        self.modele = Game(800, 600)
        self.vue = Vue(self,self.modele.largeur, self.modele.hauteur)
        
        self.nouvelleTourArcher = False
        self.nouvelleTourBombe = False
        self.nouvelleTourCanon = False
        
        self.vue.afficheModele(self.modele)
    
        self.vue.root.mainloop() 
        
    def validationTourBombe(self,x,y):
         #faire verification endroit
         self.modele.ajoutTourBombe(x, y)
         self.vue.afficheModele(self.modele)
         
         self.vue.root.config(cursor="")
         
    def initialisationTourBombe(self):
         self.vue.root.config(cursor='hand2')
         self.vue.afficheModele(self.modele)
         self.nouvelleTourBombe = True
         
    def validationTourArcher(self,x,y):
         #faire verification endroit
         self.modele.ajoutTourArcher(x, y)
         self.vue.affichageTourArcher(x,y)
         #self.vue.afficheModele(self.modele)
         self.vue.root.config(cursor="")
         self.nouvelleTourArcher=False
         
    def initialisationTourArcher(self):
         self.vue.root.config(cursor='hand2')
         self.nouvelleTourArcher = True
    
    def validationTourCanon(self,x,y):
         #faire verification endroit
         self.modele.ajoutTourCanon(x, y)
         self.vue.root.config(cursor="")
         
    def initialisationTourCanon(self):
         self.vue.root.config(cursor='hand2')
         self.nouvelleTourCanon = True

if __name__ == '__main__':
    c = Controleur()