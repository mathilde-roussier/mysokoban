from grille import Grille

class Game:

    def __init__(self):
        # Défini si notre jeu est lancé ou pas
        self.is_playing = False
        self.restart = False

    def restart_game(self, fichier):
        if self.restart:
            with open(fichier, 'r') as fich:
                Grille.lvtest = [[int(l) for l in line.strip().split(" ")] for line in fich]
