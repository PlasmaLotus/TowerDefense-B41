from game import Game
from vue import Vue

#Classe du CONTROLEUR   
class Controleur():
    def __init__(self):
        self.modele = Game(800, 600)
        self.vue = Vue(self,self.modele.largeur, self.modele.hauteur)
        self.vue.afficheModele(self.modele)
    
        self.vue.root.mainloop() 

if __name__ == '__main__':
    c = Controleur()