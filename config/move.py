#! /usr/bin/env python3
# coding: utf-8
from .maping import Laby

class Move:

    def __init__(self):
        self.playeur_pos = []
        self.map = Laby()

    def take_playeur_pos(self):
        for y, line in enumerate(self.map.laby_complet):
            for x, colonne in enumerate(line):
                if colonne == "P":
                    self.playeur_pos.append((y, x))
        #print("position avant mouvement du joueur {}".format(self.playeur_pos))

    def move_right(self):
        self.playeur_pos[0] = list(self.playeur_pos[0])
        self.playeur_pos[0][1] = self.playeur_pos[0][1]+1
        self.playeur_pos[0] = tuple(self.playeur_pos[0])
        #print("position après mouvement vers la droite {}".format(self.playeur_pos))
        if self.playeur_pos[0] not in self.map.murs:
            print("Vous avancez de une case")
        else:
            print("il y a un mur")
        return self.playeur_pos[0]

    def move_left(self):
        self.playeur_pos[0] = list(self.playeur_pos[0])
        self.playeur_pos[0][1] = self.playeur_pos[0][1]-1
        self.playeur_pos[0] = tuple(self.playeur_pos[0])
        #print("position après mouvement vers la gauche {}".format(self.playeur_pos))
        if self.playeur_pos[0] not in self.map.murs:
            print("Vous avancez de une case")
        else:
            print("il y a un mur")
        return self.playeur_pos[0]

    def move_up(self):
        self.playeur_pos[0] = list(self.playeur_pos[0])
        self.playeur_pos[0][0] = self.playeur_pos[0][0]-1
        self.playeur_pos[0] = tuple(self.playeur_pos[0])
        #print("position après mouvement vers le haut {}".format(self.playeur_pos))
        if self.playeur_pos[0] not in self.map.murs:
            print("Vous avancez de une case")
        else:
            print("il y a un mur")
        return self.playeur_pos[0]

    def move_down(self):
        self.playeur_pos[0] = list(self.playeur_pos[0])
        self.playeur_pos[0][0] = self.playeur_pos[0][0]+1
        self.playeur_pos[0] = tuple(self.playeur_pos[0])
        #print("position après mouvement vers le haut {}".format(self.playeur_pos))
        if self.playeur_pos[0] not in self.map.murs:
            print("Vous avancez de une case")
        else:
            print("il y a un mur")
        return self.playeur_pos[0]