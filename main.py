import pygame as pg
from grille import Grille
from player import Player
from config import *
pg.init()

#   Preparation fenêtre du jeu
screen = pg.display.set_mode((LARGEUR, HAUTEUR))
pg.display.set_caption(TITRE)
icon = pg.image.load('assets/box.png')
pg.display.set_icon(icon)

# Gérer la musique du jeu (Pour plus tard)
# pg.mixer.music.load(r'sokoban-music.mp3')
# pg.mixer.music.play(-1)
# pg.mixer.music.set_volume(0.3)

#  Charger notre grille
grille = Grille('level/lv1')

# Charger position du joueur
player = Player(grille)

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
            pg.quit()
        if event.type == pg.KEYDOWN:
            player.move_player(event.key)

    grille.draw_map(screen)
    pg.display.flip()
