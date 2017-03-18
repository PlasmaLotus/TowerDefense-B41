
from game import Game
from vue import Vue


class Controleur():
    '''le controleur'''
    def __init__(self):
        self.modele = Game()
        self.vue = Vue(self, 800, 600)
        self.vue.afficheModele(self.modele)

        self.vue.root.mainloop()

if __name__ == '__main__':
    Controleur()
