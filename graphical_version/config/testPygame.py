#! /usr/bin/env python3
# coding: utf-8

import pygame

import os


path_to_file_sol = os.path.join("../ressource/img", "sol.png")
path_to_file_mur = os.path.join("../ressource/img", "mur.png")
path_to_file_playeur = os.path.join("../ressource/img", "MacGyver.png")
path_to_file_gardien = os.path.join("../ressource/img", "Gardien.png")
path_to_file_map = os.path.join("../ressource/", "map.txt")

passages = []
murs = []
playeur_pos = []
gardien_pos = []

def load_map_file():
    

    with open(path_to_file_map, 'r') as lab:
        nb_colonne = 0
        for line in lab:
            nb_case = 0
            for colonne in line:
                x = nb_case * 40
                y = nb_colonne * 40
                if colonne == "x":
                    murs.append((x, y))
                    fenetre.blit(mur, (x, y))
                    pygame.display.flip()
                elif colonne == ".":
                    passages.append((x, y))
                    fenetre.blit(sol, (x, y))
                    pygame.display.flip()
                elif colonne == "d":
                    playeur_pos.append((x, y))
                    fenetre.blit(playeur, (x, y))
                    pygame.display.flip()
                elif colonne == "a":
                    gardien_pos.append((x, y))
                    fenetre.blit(gardien, (x, y))
                    pygame.display.flip()
                else:
                    pass
                nb_case += 1
            nb_colonne += 1




pygame.init()
pygame.font.init()

fenetre = pygame.display.set_mode((600, 600), pygame.RESIZABLE)

sol = pygame.image.load(path_to_file_sol).convert()
mur = pygame.image.load(path_to_file_mur).convert()
playeur = pygame.image.load(path_to_file_playeur).convert()
gardien = pygame.image.load(path_to_file_gardien).convert()

#fenetre.blit(fond, (0, 0))
pygame.display.flip()

load_map_file()
print(passages)

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
