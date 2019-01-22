#! /usr/bin/env python3
# coding: utf-8

import pygame

import os

file_name = "floor-tiles-20x20.png"
path_to_file = os.path.join("../ressource/img", file_name)

pygame.init()
pygame.font.init()

fenetre = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

fond = pygame.image.load(path_to_file).convert()

fenetre.blit(fond, (0, 0))
pygame.display.flip()

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False