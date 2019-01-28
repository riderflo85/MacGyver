#! /usr/bin/env python3
# coding; utf-8

# Module Python
import os
import pygame


class Display():
    """This class manages the graphic part of the game"""

    def __init__(self):
        """Initializes all images as well as the window"""

        self.directory = os.path.dirname(__file__)
        self.folder = "../ressource/img"
        self.img_floor = os.path.join(self.directory, self.folder, "sol.png")
        self.img_wall = os.path.join(self.directory, self.folder, "mur.png")
        self.img_player = os.path.join(self.directory, self.folder, "MacGyver.png")
        self.img_guardian = os.path.join(self.directory, self.folder, "Gardien.png")
        self.img_aiguille = os.path.join(self.directory, self.folder, "aiguille.png")
        self.img_ether = os.path.join(self.directory, self.folder, "ether.png")
        self.img_tube = os.path.join(self.directory, self.folder, "tube.png")
        self.img_home = os.path.join(self.directory, self.folder, "startscreen.png")
        self.img_counter = os.path.join(self.directory, self.folder, "wood.png")
        self.file_map = os.path.join(self.directory, "../ressource", "map.txt")
        self.background1 = pygame.Surface((600, 700))
        self.background2 = pygame.Surface((600, 700))
        self.text_status = "Objects in pocket:"

        self.COLOR = 81, 25, 0
        pygame.init()
        pygame.font.init()

        self.window = pygame.display.set_caption("MacGyver escapes")
        self.window = pygame.display.set_mode((600, 700))

        self.floor = pygame.image.load(self.img_floor).convert()
        self.wall = pygame.image.load(self.img_wall).convert()
        self.player = pygame.image.load(self.img_player).convert_alpha()
        self.guardian = pygame.image.load(self.img_guardian).convert_alpha()
        self.aiguille = pygame.image.load(self.img_aiguille).convert_alpha()
        self.ether = pygame.image.load(self.img_ether).convert_alpha()
        self.tube = pygame.image.load(self.img_tube).convert_alpha()
        self.startscreen = pygame.image.load(self.img_home).convert()
        self.counter_ob = pygame.image.load(self.img_counter).convert_alpha()

    def home_page(self):
        """Show the homepage"""

        self.background1.blit(self.startscreen, (0, 0))
        self.window.blit(self.background1, (0, 0))

    def object_counter(self, ob, the_end):
        """Displays and manages text on object counter"""

        self.background2.blit(self.counter_ob, (0, 600))
        self.type_text = pygame.font.SysFont('ani', 56)
        if the_end:
            self.text_status = "YOU WINNER !!!"
            self.text = self.type_text.render("{}".format(self.text_status), True, self.COLOR)
        else:
            self.text = self.type_text.render("{}{}/3".format(self.text_status, ob), True, self.COLOR)

        self.text_pos = self.text.get_rect()
        self.text_pos.centerx = self.window.get_rect().centerx
        self.text_pos.centery = 650
        self.background2.blit(self.text, self.text_pos)
        self.window.blit(self.background2, (0, 0))
