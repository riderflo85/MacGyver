#! /usr/bin/env python3
# coding: utf-8

import random
import os

os.chdir("../ressource/")
file_name = "map.txt"

class Laby:


    def __init__(self):
        self.laby_complet = []
        self.murs = []
        self.passages = []
        self.personnage = []
        self.arrive = []
        self.local_x = int
        self.local_y = int
        self.is_arriver = False
        self.objet_in_pocket = 0

        self.load_map_file()
        self.create_white_map()


    def load_map_file(self):
        with open(file_name, 'r') as lab:
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
        self.pos_objet = []
        nb_objet = 0
        while nb_objet <= 2: # 2 car en programmation on compte a partir de 0
            self.pos_objet.append(random.choice(self.passages))
            nb_objet += 1

    def complet_map(self, pos):
        for m in self.murs:
            y, x = m
            self.laby_complet[y][x] =  "#"
        
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
                self.is_arriver = True
            else:
                self.laby_complet[y][x] = "A"

        for ob in self.pos_objet:
            y, x = ob
            if pos == ob:
                self.laby_complet[y][x] = "P"
                self.objet_in_pocket += 1
            else:
                self.laby_complet[y][x] = "O"


    def take_playeur_pos(self):
        self.playeur_pos = []
        for y, line in enumerate(self.laby_complet):
            for x, colonne in enumerate(line):
                if colonne == "P":
                    self.playeur_pos.append((y, x))
        print(self.playeur_pos[0][1])


    def move_right(self):
        self.playeur_pos[0]


    def print_laby(self):
        for part_of_lab in self.laby_complet:
            print(part_of_lab)
        if self.is_arriver:
            print("Bien jouer vous etes arriver !!!")




def main():
    my_lab = Laby()
    local_player = (1, 2)
    my_lab.place_objet()
    my_lab.complet_map(local_player)
    my_lab.take_playeur_pos()
    my_lab.print_laby()
    

main()