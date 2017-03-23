# -*- coding: utf-8 -*-
from tkinter import *
from helper import Helper as H
import random

        
class Coureur():
    def __init__(self,parent,x,y):
        self.parent=parent
        self.demitaillex=5
        self.demitailley=10
        self.couleur="blue"
        self.vitesse=3
        self.etendue=8
        self.angle=0
        self.cible=None
        self.x=x
        self.y=y
        
    def changercible(self,cible):
        self.cible=cible
        self.angle=H.calcAngle(self.x,self.y,self.cible[0],self.cible[1])
        
    def avancer(self):
        if self.cible:
            self.x,self.y=H.getAngledPoint(self.angle,self.vitesse,self.x,self.y)
            d=H.calcDistance(self.x,self.y,self.cible[0],self.cible[1])
            if self.vitesse > d:
                self.cible=None

class Modele():
    def __init__(self,parent,large,haut):
        self.parent=parent
        self.large=large
        self.haut=haut
        self.coureur=Coureur(self,large/2,haut/2)
        
    def changercible(self,x,y):
        self.coureur.changercible([x,y])
            
    def miseajour(self):
        self.coureur.avancer()
        
class Vue(object):
    def __init__(self,parent,modele):
        self.parent=parent
        self.modele=modele
        self.root=Tk()
        self.large=self.modele.large
        self.haut=self.modele.haut
        self.cadreprincipal=Frame(self.root,bg="yellow")
        self.canevas=Canvas(self.cadreprincipal,width=self.large,height=self.haut,bg="red")
        self.canevas.bind("<Button>",self.changercible)
        self.canevas.pack(side=LEFT,fill=BOTH)
        self.labmsg=Label(self.root,text="Cliquer sur la surface pour donner une cible au coureur")
        self.labmsg.pack()
        self.cadreprincipal.pack(expand=1,fill=BOTH)
    
    def changercible(self,evt):
        x=evt.x
        y=evt.y
        self.parent.changercible(x,y)
        
    def dessineJeu(self):
        self.canevas.delete("coureur")
        i=self.modele.coureur
        
        self.canevas.create_oval(i.x-i.etendue,i.y-i.etendue,
                                          i.x+i.etendue,i.y+i.etendue,fill=i.couleur,
                                          tags=("coureur",))
        
class Controleur(object):
    def __init__(self):
        self.modele=Modele(self,600,400)
        self.vue=Vue(self,self.modele)
        self.vue.dessineJeu()
        self.jouer()
        self.vue.root.mainloop()
        
    def jouer(self):
        self.modele.miseajour()
        self.vue.dessineJeu()
        self.vue.root.after(50,self.jouer)
        
    def changercible(self,x,y):
        self.modele.changercible(x,y)
        
if __name__ == '__main__':
    controleur=Controleur()