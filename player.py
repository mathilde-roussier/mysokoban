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
            self.check_libre_left(pos_grille)
            self.check_caisse_left(pos_grille)
        elif key == pg.K_RIGHT:
            pos_grille = self.grille.lvtest[self.y][self.x+1]
            self.check_libre_right(pos_grille)
            self.check_caisse_right(pos_grille)
        elif key == pg.K_UP:
            pos_grille = self.grille.lvtest[self.y-1][self.x]
            self.check_libre_up(pos_grille)
            self.check_caisse_up(pos_grille)
        elif key == pg.K_DOWN:
            pos_grille = self.grille.lvtest[self.y+1][self.x]
            self.check_libre_down(pos_grille)
            self.check_caisse_down(pos_grille)

    def check_libre_left(self, pos_grille):
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

    def check_caisse_left(self, pos_grille):
        if pos_grille in (CAISSE, CAISSE_OK):
            pos_grille_plus1 = self.grille.lvtest[self.y][self.x - 2]
            if pos_grille_plus1 in (VIDE, OBJECTIF):
                self.x -= 1
                self.grille.lvtest[self.y][self.x] = PLAYER
                pos_grille_plus1 = self.grille.lvtest[self.y][self.x-1]
                if pos_grille_plus1 == VIDE:
                    self.grille.lvtest[self.y][self.x-1] = CAISSE
                else:
                    self.grille.lvtest[self.y][self.x-1] = CAISSE_OK
                if self.objectif:
                    self.grille.lvtest[self.y][self.x + 1] = OBJECTIF
                    self.objectif = False
                else:
                    self.grille.lvtest[self.y][self.x + 1] = VIDE
                if (self.x, self.y) in self.grille.coord_objec:
                    self.objectif = True

    def check_libre_right(self, pos_grille):
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

    def check_caisse_right(self, pos_grille):
        if pos_grille in (CAISSE, CAISSE_OK):
            pos_grille_plus1 = self.grille.lvtest[self.y][self.x + 2]
            if pos_grille_plus1 in (VIDE, OBJECTIF):
                self.x += 1
                self.grille.lvtest[self.y][self.x] = PLAYER
                pos_grille_plus1 = self.grille.lvtest[self.y][self.x + 1]
                if pos_grille_plus1 == VIDE:
                    self.grille.lvtest[self.y][self.x+1] = CAISSE
                else:
                    self.grille.lvtest[self.y][self.x+1] = CAISSE_OK
                if self.objectif:
                    self.grille.lvtest[self.y][self.x-1] = OBJECTIF
                    self.objectif = False
                else:
                    self.grille.lvtest[self.y][self.x-1] = VIDE
                if (self.x, self.y) in self.grille.coord_objec:
                    self.objectif = True

    def check_libre_up(self, pos_grille):
        if pos_grille in (VIDE, OBJECTIF):
            self.y -= 1
            self.grille.lvtest[self.y][self.x] = PLAYER
            if self.objectif:
                self.grille.lvtest[self.y + 1][self.x] = OBJECTIF
                self.objectif = False
            else:
                self.grille.lvtest[self.y + 1][self.x] = VIDE
            if (self.x, self.y) in self.grille.coord_objec:
                self.objectif = True

    def check_caisse_up(self, pos_grille):
        if pos_grille in (CAISSE, CAISSE_OK):
            pos_grille_plus1 = self.grille.lvtest[self.y-2][self.x]
            if pos_grille_plus1 in (VIDE, OBJECTIF):
                self.y -= 1
                self.grille.lvtest[self.y][self.x] = PLAYER
                pos_grille_plus1 = self.grille.lvtest[self.y - 1][self.x]
                if pos_grille_plus1 == VIDE:
                    self.grille.lvtest[self.y-1][self.x] = CAISSE
                else:
                    self.grille.lvtest[self.y-1][self.x] = CAISSE_OK
                if self.objectif:
                    self.grille.lvtest[self.y+1][self.x] = OBJECTIF
                    self.objectif = False
                else:
                    self.grille.lvtest[self.y+1][self.x] = VIDE
                if (self.x, self.y) in self.grille.coord_objec:
                    self.objectif = True

    def check_libre_down(self, pos_grille):
        if pos_grille in (VIDE, OBJECTIF):
            self.y += 1
            self.grille.lvtest[self.y][self.x] = PLAYER
            if self.objectif:
                self.grille.lvtest[self.y - 1][self.x] = OBJECTIF
                self.objectif = False
            else:
                self.grille.lvtest[self.y - 1][self.x] = VIDE
            if (self.x, self.y) in self.grille.coord_objec:
                self.objectif = True

    def check_caisse_down(self, pos_grille):
        if pos_grille in (CAISSE, CAISSE_OK):
            pos_grille_plus1 = self.grille.lvtest[self.y+2][self.x]
            if pos_grille_plus1 in (VIDE, OBJECTIF):
                self.y += 1
                self.grille.lvtest[self.y][self.x] = PLAYER
                pos_grille_plus1 = self.grille.lvtest[self.y+1][self.x]
                if pos_grille_plus1 == VIDE:
                    self.grille.lvtest[self.y+1][self.x] = CAISSE
                else:
                    self.grille.lvtest[self.y+1][self.x] = CAISSE_OK
                if self.objectif:
                    self.grille.lvtest[self.y-1][self.x] = OBJECTIF
                    self.objectif = False
                else:
                    self.grille.lvtest[self.y-1][self.x] = VIDE
                if (self.x, self.y) in self.grille.coord_objec:
                    self.objectif = True
