#! /usr/bin/env python3
# coding; utf-8

import os
import pygame


class Display():

    def __init__(self):
        
        self.directory = os.path.dirname(__file__)
        self.img_floor = os.path.join(self.directory, "../../ressource/img", "sol.png")
        self.img_wall = os.path.join(self.directory, "../../ressource/img", "mur.png")
        self.img_playeur = os.path.join(self.directory, "../../ressource/img", "MacGyver.png")
        self.img_guardian = os.path.join(self.directory, "../../ressource/img", "Gardien.png")
        self.img_aiguille = os.path.join(self.directory, "../../ressource/img", "aiguille.png")
        self.img_ether = os.path.join(self.directory, "../../ressource/img", "ether.png")
        self.img_tube = os.path.join(self.directory, "../../ressource/img", "tube.png")
        self.img_home = os.path.join(self.directory, "../../ressource/img", "startscreen.png")
        self.img_counter = os.path.join(self.directory, "../../ressource/img", "wood.png")
        self.file_map = os.path.join(self.directory, "../../ressource/", "map.txt")
        self.background1 = pygame.Surface((600, 700))
        self.background2 = pygame.Surface((600, 700))
        #self.type_text = None
        #self.text = None
        #self.text_pos = None

        self.COLOR = 0, 0, 0
        pygame.init()
        pygame.font.init()

        self.window = pygame.display.set_caption("MacGyver escapes")
        self.window = pygame.display.set_mode((600, 700))

        self.floor = pygame.image.load(self.img_floor).convert()
        self.wall = pygame.image.load(self.img_wall).convert()
        self.playeur = pygame.image.load(self.img_playeur).convert_alpha()
        self.guardian = pygame.image.load(self.img_guardian).convert_alpha()
        self.aiguille = pygame.image.load(self.img_aiguille).convert_alpha()
        self.ether = pygame.image.load(self.img_ether).convert_alpha()
        self.tube = pygame.image.load(self.img_tube).convert_alpha()
        self.startscreen = pygame.image.load(self.img_home).convert()
        self.counter_ob = pygame.image.load(self.img_counter).convert_alpha()

        
    def home_page(self):

            self.background1.blit(self.startscreen, (0, 0))
            self.window.blit(self.background1, (0, 0))

    
    def object_counter(self, ob):
        
            self.background2.blit(self.counter_ob, (0, 600))
            self.type_text = pygame.font.SysFont('ani', 56)
            self.text = self.type_text.render("Objects in pocket: {}".format(ob), True, self.COLOR)
            self.text_pos = self.text.get_rect()
            self.text_pos.centerx = self.window.get_rect().centerx
            self.text_pos.centery = 650
            self.background2.blit(self.text, self.text_pos)
            self.window.blit(self.background2, (0, 0))
