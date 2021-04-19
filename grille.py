import pygame as pg
from config import *


class Grille:
    def __init__(self, fichier):
        self.ref_img = {
            MUR: pg.image.load("assets/mur2.png"),
            CAISSE: pg.image.load("assets/caisse.png"),
            OBJECTIF: pg.image.load("assets/objectif.png"),
            CAISSE_OK: pg.image.load("assets/caisse_ok.png"),
            VIDE: pg.image.load("assets/vide.png"),
            PLAYER: pg.image.load('assets/player.png')
        }
        with open(fichier, 'r') as fich:
            self.lvtest = [[int(l) for l in line.strip().split(" ")] for line in fich]

        self.coord_objec = []
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                if self.lvtest[y][x] == OBJECTIF:
                    self.coord_objec.append((x, y))

    def draw_map(self, screen):
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                img = self.lvtest[y][x]
                screen.blit(self.ref_img[VIDE], (x * SIZE, y * SIZE))
                screen.blit(self.ref_img[img], (x * SIZE, y * SIZE))

    def get_player_position(self):
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                if self.lvtest[y][x] == PLAYER:
                    return (x*SIZE, y*SIZE)
