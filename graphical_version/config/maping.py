#! /usr/bin/env python3
# coding: utf-8

import random
import os

file_name = "map.txt"
directory = os.path.dirname(__file__)
path_to_file = os.path.join(directory, "../../ressource", file_name)

class Laby:

    def __init__(self):
        self.laby_complet = []
        self.murs = []
        self.passages = []
        self.init_playeur_pos = []
        self.gardien_pos = []
        self.nb_colomn = int
        self.nb_line = int
        self.object_in_pocket = 0
        self.game_exit = False

        self.load_map_file()

    def load_map_file(self):
        with open(path_to_file_map, 'r') as lab:
            self.nb_colomn = 0
            for line in lab:
                self.nb_line = 0
                for colomn in line:
                    x = self.nb_line * 40
                    y = self.nb_colomn * 40
                    if colomn == "x":
                        self.murs.append((x, y))
                        fenetre.blit(mur, (x, y))
                        pygame.display.flip()
                    elif colomn == ".":
                        self.passages.append((x, y))
                        fenetre.blit(sol, (x, y))
                        pygame.display.flip()
                    elif colomn == "d":
                        self.init_playeur_pos.append((x, y))
                        fenetre.blit(playeur, (x, y))
                        pygame.display.flip()
                    elif colomn == "a":
                        self.gardien_pos.append((x, y))
                        fenetre.blit(gardien, (x, y))
                        pygame.display.flip()
                    else:
                        pass
                    self.nb_line += 1
                self.nb_colomn += 1


    def place_objet(self):
        self.pos_object = []
        nb_object = 0
        while nb_object <= 2:  # 2 car en programmation on compte a partir de 0
            self.pos_object.append(random.choice(self.passages))
            nb_object += 1

        fenetre.blit(aiguille, pos_object[0])
        fenetre.blit(ether, pos_object[1])
        fenetre.blit(tube, pos_object[2])
        pygame.display.flip()


    def complet_map(self, pos):
        for m in self.murs:
            y, x = m
            self.laby_complet[y][x] = "#"

        for pa in self.passages:
            y, x = pa
            if pos == pa:
                self.laby_complet[y][x] = "P"
            else:
                self.laby_complet[y][x] = " "

        for pe in self.personnage:
            y, x = pe
            if pos == pe:
                self.laby_complet[y][x] = "P"
            else:
                self.laby_complet[y][x] = " "

        for ar in self.arrive:
            y, x = ar
            if pos == ar:
                self.laby_complet[y][x] = "P"
            else:
                self.laby_complet[y][x] = "A"

        for ob in self.pos_object[:]:
            y, x = ob
            if pos == ob:
                self.laby_complet[y][x] = "P"
                self.pos_object.remove(ob)
                self.object_in_pocket += 1
            else:
                self.laby_complet[y][x] = "O"
