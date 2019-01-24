#! /usr/bin/env python3
# coding: utf-8

import pygame
import random
import os


path_to_file_sol = os.path.join("../../ressource/img", "sol.png")
path_to_file_mur = os.path.join("../../ressource/img", "mur.png")
path_to_file_playeur = os.path.join("../../ressource/img", "MacGyver.png")
path_to_file_gardien = os.path.join("../../ressource/img", "Gardien.png")
path_to_file_aiguille = os.path.join("../../ressource/img", "aiguille.png")
path_to_file_ether = os.path.join("../../ressource/img", "ether.png")
path_to_file_tube = os.path.join("../../ressource/img", "tube.png")
path_to_file_map = os.path.join("../../ressource/", "map.txt")

passages = []
list_murs = []
gardien_pos = []
pos_object = {}

pygame.init()
pygame.font.init()

fenetre = pygame.display.set_mode((600, 600), pygame.RESIZABLE)

sol = pygame.image.load(path_to_file_sol).convert()
mur = pygame.image.load(path_to_file_mur).convert()
playeur = pygame.image.load(path_to_file_playeur).convert_alpha()
gardien = pygame.image.load(path_to_file_gardien).convert_alpha()
aiguille = pygame.image.load(path_to_file_aiguille).convert()
ether = pygame.image.load(path_to_file_ether).convert_alpha()
tube = pygame.image.load(path_to_file_tube).convert_alpha()

playeur_pos = playeur.get_rect(x=0, y=40)

object_in_pocket = 0
list_object = [aiguille, ether, tube]

#-------------------------------------------------
#--------------------Fonctions--------------------
#-------------------------------------------------

def load_map_file():
    
    with open(path_to_file_map, 'r') as lab:

        nb_colomn = 0

        for line in lab:
            nb_line = 0

            for colomn in line:
                x = nb_line * 40
                y = nb_colomn * 40

                if colomn == "x":
                    list_murs.append((x, y))
                    fenetre.blit(mur, (x, y))
                    pygame.display.flip()

                elif colomn == ".":
                    passages.append((x, y))
                    fenetre.blit(sol, (x, y))
                    pygame.display.flip()

                elif colomn == "a":
                    gardien_pos.append((x, y))
                    fenetre.blit(gardien, (x, y))
                    pygame.display.flip()

                else:
                    pass

                nb_line += 1
            nb_colomn += 1


def place_objet():
        
    for ob in list_object:
        pos_object[random.choice(passages)] = ob

    for keys, value in pos_object.items():
        fenetre.blit(value, keys)
        pygame.display.flip()


def refresh_map():

    for pos_mur in list_murs:
        fenetre.blit(mur, pos_mur)
    
    for pos_passages in passages:
        fenetre.blit(sol, pos_passages)

    for keys, value in pos_object.items():
        fenetre.blit(value, keys)
        pygame.display.flip()


def take_object(ply_pos):

    tuple_playeur_pos = (ply_pos[0], ply_pos[1])
    dict_temp = pos_object.copy()

    for pos_ob in dict_temp.keys():
        
        if tuple_playeur_pos == pos_ob:

            pos_object.pop(pos_ob)
            global object_in_pocket
            object_in_pocket += 1


class Move:


    def __init__(self):

        self.move_valide = False
    

    def move_up(self, ply_pos):

        self.predict_playeur_pos = (ply_pos[0], ply_pos[1]-40)

        if self.predict_playeur_pos not in list_murs:
            self.move_valide = True

        else:
            self.move_valide = False
        
        return self.move_valide


    def move_down(self, ply_pos):

        self.predict_playeur_pos = (ply_pos[0], ply_pos[1]+40)

        if self.predict_playeur_pos not in list_murs:
            self.move_valide = True

        else:
            self.move_valide = False

        return self.move_valide


    def move_left(self, ply_pos):

        self.predict_playeur_pos = (ply_pos[0]-40, ply_pos[1])

        if self.predict_playeur_pos not in list_murs:
            self.move_valide = True

        else:
            self.move_valide = False

        return self.move_valide


    def move_right(self, ply_pos):

        self.predict_playeur_pos = (ply_pos[0]+40, ply_pos[1])

        if self.predict_playeur_pos not in list_murs:
            self.move_valide = True

        else:
            self.move_valide = False

        return self.move_valide
    

#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------


moving = Move()

load_map_file()
place_objet()


pygame.display.flip()

#print(passages,"\n",pos_object)

continuer = True

while continuer:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            continuer = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                moving.move_right(playeur_pos)
                if moving.move_valide:
                    playeur_pos = playeur_pos.move(40, 0)
                    take_object(playeur_pos)
                    refresh_map()

            if event.key == pygame.K_LEFT:
                moving.move_left(playeur_pos)
                if moving.move_valide:
                    playeur_pos = playeur_pos.move(-40, 0)
                    take_object(playeur_pos)
                    refresh_map()

            if event.key == pygame.K_UP:
                moving.move_up(playeur_pos)
                if moving.move_valide:
                    playeur_pos = playeur_pos.move(0, -40)
                    take_object(playeur_pos)
                    refresh_map()

            if event.key == pygame.K_DOWN:
                moving.move_down(playeur_pos)
                if moving.move_valide:
                    playeur_pos = playeur_pos.move(0, 40)
                    take_object(playeur_pos)
                    refresh_map()

            if event.key == pygame.K_q:
                continuer = False
    
    fenetre.blit(playeur, playeur_pos)
    pygame.display.flip()
    