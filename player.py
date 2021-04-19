import pygame as pg
from grille import Grille
from config import *


#  Creer une premiere classe qui va représenter notre joueur
class Player(pg.sprite.Sprite):

    def __init__(self, grille):
        super().__init__()
        self.grille = grille
        self.pos = self.grille.get_player_position()
        self.x = int(self.pos[0]/SIZE)
        self.y = int(self.pos[1]/SIZE)
        self.objectif = False

    def move_player(self, key):
        if key == pg.K_LEFT:
            pos_grille = self.grille.lvtest[self.y][self.x-1]
            if pos_grille in (VIDE, OBJECTIF):
                self.x -= 1
                self.grille.lvtest[self.y][self.x] = PLAYER
                if self.objectif:
                    self.grille.lvtest[self.y][self.x + 1] = OBJECTIF
                    self.objectif = False
                else:
                    self.grille.lvtest[self.y][self.x + 1] = VIDE
                if (self.x, self.y) in self.grille.coord_objec:
                    self.objectif = True
        elif key == pg.K_RIGHT:
            pos_grille = self.grille.lvtest[self.y][self.x+1]
            if pos_grille in (VIDE, OBJECTIF):
                self.x += 1
                self.grille.lvtest[self.y][self.x] = PLAYER
                if self.objectif:
                    self.grille.lvtest[self.y][self.x - 1] = OBJECTIF
                    self.objectif = False
                else:
                    self.grille.lvtest[self.y][self.x - 1] = VIDE
                if (self.x, self.y) in self.grille.coord_objec:
                    self.objectif = True
        elif key == pg.K_UP:
            pos_grille = self.grille.lvtest[self.y-1][self.x]
            if pos_grille in (VIDE, OBJECTIF):
                self.y -= 1
                self.grille.lvtest[self.y][self.x] = PLAYER
                if self.objectif:
                    self.grille.lvtest[self.y+1][self.x] = OBJECTIF
                    self.objectif = False
                else:
                    self.grille.lvtest[self.y+1][self.x] = VIDE
                if (self.x, self.y) in self.grille.coord_objec:
                    self.objectif = True
        elif key == pg.K_DOWN:
            pos_grille = self.grille.lvtest[self.y+1][self.x]
            if pos_grille in (VIDE, OBJECTIF):
                self.y += 1
                self.grille.lvtest[self.y][self.x] = PLAYER
                if self.objectif:
                    self.grille.lvtest[self.y-1][self.x] = OBJECTIF
                    self.objectif = False
                else:
                    self.grille.lvtest[self.y-1][self.x] = VIDE
                if (self.x, self.y) in self.grille.coord_objec:
                    self.objectif = True
