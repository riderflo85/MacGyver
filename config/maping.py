#! /usr/bin/env python3
# coding: utf-8

import random
import os

file_name = "map.txt"
directory = os.path.dirname(__file__)
path_to_file = os.path.join(directory, "../ressource", file_name)

class Laby:

    def __init__(self):
        self.laby_complet = []
        self.murs = []
        self.passages = []
        self.personnage = []
        self.arrive = []
        self.local_x = int
        self.local_y = int
        self.object_in_pocket = 0
        self.game_exit = False

        self.load_map_file()
        self.create_white_map()

    def load_map_file(self):
        with open(path_to_file, 'r') as lab:
            for y, line in enumerate(lab):
                for x, colonne in enumerate(line):
                    self.local_x = x
                    self.local_y = y
                    if colonne == "x":
                        self.murs.append((y, x))
                    elif colonne == ".":
                        self.passages.append((y, x))
                    elif colonne == "d":
                        self.personnage.append((y, x))
                    elif colonne == "a":
                        self.arrive.append((y, x))
                    else:
                        pass

    def create_white_map(self):
        self.laby_complet = [[""]] * (self.local_y+1)
        nb_colone = 0
        while nb_colone < (self.local_x+1):
            self.laby_complet[nb_colone] = [[""]] * (self.local_x+1)
            nb_colone += 1

    def place_objet(self):
        self.pos_object = []
        nb_object = 0
        while nb_object <= 2:  # 2 car en programmation on compte a partir de 0
            self.pos_object.append(random.choice(self.passages))
            nb_object += 1

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
                if self.object_in_pocket < 3:
                    self.game_exit = True
                    print(
                        "Vous n'avez pas récuperer tout les objets! Le gardiens vous tue !!!")
            else:
                self.laby_complet[y][x] = "A"

        for ob in self.pos_object:
            y, x = ob
            if pos == ob:
                self.laby_complet[y][x] = "P"
                self.pos_object.remove(ob)
                self.object_in_pocket += 1
            else:
                self.laby_complet[y][x] = "O"

    
    def print_laby(self, *end):
        for part_of_lab in self.laby_complet:
            print(part_of_lab)
        if end:
            self.game_exit = True