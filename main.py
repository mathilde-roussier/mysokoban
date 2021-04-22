import pygame as pg
from game import Game
from grille import Grille
from player import Player
from config import *
pg.init()

#   Preparation fenêtre du jeu
screen = pg.display.set_mode((LARGEUR, HAUTEUR))
pg.display.set_caption(TITRE)
icon = pg.image.load('assets/box.png')
pg.display.set_icon(icon)

myfont = pg.font.Font('assets/fonts/blox2.ttf', 100)
name_game = myfont.render('My Sokoban', False, (255, 153, 51))
name_game_rect = name_game.get_rect()
name_game_rect.x = LARGEUR / 12
name_game_rect.y = HAUTEUR / 6

myfont_play = pg.font.Font('assets/fonts/blox2.ttf', 60)
play_button = myfont_play.render('Jouer', False, (255, 120, 51))
play_button_rect = play_button.get_rect()
play_button_rect.x = LARGEUR / 2.75
play_button_rect.y = HAUTEUR / 1.75

# Gérer la musique du jeu (Pour plus tard)
# pg.mixer.music.load(r'sokoban-music.mp3')
# pg.mixer.music.play(-1)
# pg.mixer.music.set_volume(0.3)

#  Charger notre grille
grille = Grille('level/lv1')

# Charger position du joueur
player = Player(grille)

# Charge l'état du jeu
game = Game()

done = False
while not done:
    screen.blit(screen, (0, 0))

    # Vérifier si le jeu est lancé ou non
    if game.is_playing:
        grille.draw_map(screen)
    else:
        screen.blit(name_game, name_game_rect)
        screen.blit(play_button, play_button_rect)

    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
            pg.quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.is_playing = True
        elif event.type == pg.KEYDOWN:
            player.move_player(event.key)
            if event.key == pg.K_r:
                game.restart = True
                game.restart_game('level/lv1')

