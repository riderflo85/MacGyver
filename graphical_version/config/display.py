#! /usr/bin/env python3
# coding; utf-8

import os
import pygame


class Display():

    def __init__(self):
        
        self.directory = os.path.dirname(__file__)
        self.path_to_file_floor = os.path.join(self.directory, "../../ressource/img", "sol.png")
        self.path_to_file_mur = os.path.join(self.directory, "../../ressource/img", "mur.png")
        self.path_to_file_playeur = os.path.join(self.directory, "../../ressource/img", "MacGyver.png")
        self.path_to_file_gardien = os.path.join(self.directory, "../../ressource/img", "Gardien.png")
        self.path_to_file_aiguille = os.path.join(self.directory, "../../ressource/img", "aiguille.png")
        self.path_to_file_ether = os.path.join(self.directory, "../../ressource/img", "ether.png")
        self.path_to_file_tube = os.path.join(self.directory, "../../ressource/img", "tube.png")
        self.path_to_file_map = os.path.join(self.directory, "../../ressource/", "map.txt")


        pygame.init()
        pygame.font.init()

        self.window = pygame.display.set_mode((600, 600), pygame.RESIZABLE)

        self.floor = pygame.image.load(self.path_to_file_floor).convert()
        self.wall = pygame.image.load(self.path_to_file_mur).convert()
        self.playeur = pygame.image.load(self.path_to_file_playeur).convert_alpha()
        self.gardien = pygame.image.load(self.path_to_file_gardien).convert_alpha()
        self.aiguille = pygame.image.load(self.path_to_file_aiguille).convert()
        self.ether = pygame.image.load(self.path_to_file_ether).convert_alpha()
        self.tube = pygame.image.load(self.path_to_file_tube).convert_alpha()