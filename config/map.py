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
        self.object_in_pocket = 0
        self.game_exit = False

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

    def take_playeur_pos(self):
        self.playeur_pos = []
        for y, line in enumerate(self.laby_complet):
            for x, colonne in enumerate(line):
                if colonne == "P":
                    self.playeur_pos.append((y, x))
        #print("position avant mouvement du joueur {}".format(self.playeur_pos))

    def move_right(self):
        self.playeur_pos[0] = list(self.playeur_pos[0])
        self.playeur_pos[0][1] = self.playeur_pos[0][1]+1
        self.playeur_pos[0] = tuple(self.playeur_pos[0])
        #print("position après mouvement vers la droite {}".format(self.playeur_pos))
        if self.playeur_pos[0] not in self.murs:
            print("Vous avancez de une case")
        else:
            print("il y a un mur")
        return self.playeur_pos[0]

    def move_left(self):
        self.playeur_pos[0] = list(self.playeur_pos[0])
        self.playeur_pos[0][1] = self.playeur_pos[0][1]-1
        self.playeur_pos[0] = tuple(self.playeur_pos[0])
        #print("position après mouvement vers la gauche {}".format(self.playeur_pos))
        if self.playeur_pos[0] not in self.murs:
            print("Vous avancez de une case")
        else:
            print("il y a un mur")
        return self.playeur_pos[0]

    def move_up(self):
        self.playeur_pos[0] = list(self.playeur_pos[0])
        self.playeur_pos[0][0] = self.playeur_pos[0][0]-1
        self.playeur_pos[0] = tuple(self.playeur_pos[0])
        #print("position après mouvement vers le haut {}".format(self.playeur_pos))
        if self.playeur_pos[0] not in self.murs:
            print("Vous avancez de une case")
        else:
            print("il y a un mur")
        return self.playeur_pos[0]

    def move_down(self):
        self.playeur_pos[0] = list(self.playeur_pos[0])
        self.playeur_pos[0][0] = self.playeur_pos[0][0]+1
        self.playeur_pos[0] = tuple(self.playeur_pos[0])
        #print("position après mouvement vers le haut {}".format(self.playeur_pos))
        if self.playeur_pos[0] not in self.murs:
            print("Vous avancez de une case")
        else:
            print("il y a un mur")
        return self.playeur_pos[0]

    def print_laby(self, *end):
        for part_of_lab in self.laby_complet:
            print(part_of_lab)
        if end:
            self.game_exit = True


def main():
    my_lab = Laby()
    # On place le joueur au point de départ avant de lancer la boucle principale (le jeu)
    start_local_player = (1, 0)
    my_lab.place_objet()
    # A mettre dans la boucle principale du jeu
    my_lab.complet_map(start_local_player)
    start_game = True
    print("\tBienvenu dans le jeux !!!\nVoici les commandes que vous pouvez tapez:\n  - x => quitte la partie\n  - z => aller vers le haut\n  - q => aller vers la gauche\n  - s => aller vers le bas\n  - d => aller vers la droite\n\n Bonne chance!!! ")
    while my_lab.game_exit == False:
        my_lab.take_playeur_pos()
        if start_game:
            my_lab.print_laby()
            start_game = False
        print("Que voulez-vous faire? Avancer? Quitter? (utilisez les commandes indiquer plus haut)")
        reponse = input(" ")
        if reponse.lower() == "z":
            my_lab.complet_map(my_lab.move_up())
            my_lab.print_laby()
            print("\t\t\t", my_lab.object_in_pocket)
        elif reponse.lower() == "q":
            my_lab.complet_map(my_lab.move_left())
            my_lab.print_laby()
            print("\t\t\t", my_lab.object_in_pocket)
        elif reponse.lower() == "s":
            my_lab.complet_map(my_lab.move_down())
            my_lab.print_laby()
            print("\t\t\t", my_lab.object_in_pocket)
        elif reponse.lower() == "d":
            my_lab.complet_map(my_lab.move_right())
            my_lab.print_laby()
            print("\t\t\t", my_lab.object_in_pocket)
        elif reponse.lower() == "x":
            print("Vous quittez la partie")
            my_lab.game_exit = True
        elif my_lab.object_in_pocket == 3:
            my_lab.print_laby(True)
            print("Bien jouer vous avez gagner la partie")
        else:
            print("Merci d'indiquer une commande valide")


main()
