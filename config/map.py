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
        #print("position avant mouvement du joueur {}".format(self.playeur_pos))


    def move_right(self):
        self.playeur_pos[0] = list(self.playeur_pos[0])
        self.playeur_pos[0][1] = self.playeur_pos[0][1]+1
        self.playeur_pos[0] = tuple(self.playeur_pos[0])
        #print("position après mouvement vers la droite {}".format(self.playeur_pos))
        if self.playeur_pos[0] not in self.murs:
            print("tu peut avancer")
        else:
            print("il y a un mur")
        return self.playeur_pos[0]
    

    def move_left(self):
        self.playeur_pos[0] = list(self.playeur_pos[0])
        self.playeur_pos[0][1] = self.playeur_pos[0][1]-1
        self.playeur_pos[0] = tuple(self.playeur_pos[0])
        #print("position après mouvement vers la gauche {}".format(self.playeur_pos))
        if self.playeur_pos[0] not in self.murs:
            print("tu peut avancer")
        else:
            print("il y a un mur")
        return self.playeur_pos[0]
    

    def move_up(self):
        self.playeur_pos[0] = list(self.playeur_pos[0])
        self.playeur_pos[0][0] = self.playeur_pos[0][0]-1
        self.playeur_pos[0] = tuple(self.playeur_pos[0])
        #print("position après mouvement vers le haut {}".format(self.playeur_pos))
        if self.playeur_pos[0] not in self.murs:
            print("tu peut avancer")
        else:
            print("il y a un mur")
        return self.playeur_pos[0]


    def move_down(self):
        self.playeur_pos[0] = list(self.playeur_pos[0])
        self.playeur_pos[0][0] = self.playeur_pos[0][0]+1
        self.playeur_pos[0] = tuple(self.playeur_pos[0])
        #print("position après mouvement vers le haut {}".format(self.playeur_pos))
        if self.playeur_pos[0] not in self.murs:
            print("tu peut avancer")
        else:
            print("il y a un mur")
        return self.playeur_pos[0]


    def print_laby(self):
        for part_of_lab in self.laby_complet:
            print(part_of_lab)
        if self.is_arriver:
            print("Bien jouer vous etes arriver !!!")




def main():
    my_lab = Laby()
    start_local_player = (1, 0) # On place le joueur au point de départ avant de lancer la boucle principale (le jeu)
    my_lab.place_objet()
    my_lab.complet_map(start_local_player) # A mettre dans la boucle principale du jeu
    game_exit = False
    start_game = True
    print("\tBienvenu dans le jeux !!!\nVoici les commandes que vous pouvez tapez:\n  - x => quitte la parti\n  - z => aller vers le haut\n  - q => aller vers la gauche\n  - s => aller vers le bas\n  - d => aller vers la droite\n\n Bonne chance!!! ")
    while game_exit == False:
        my_lab.take_playeur_pos()
        if start_game:
            my_lab.print_laby()
            start_game = False
        print("Que voulez-vous faire? Avancer? Quitter? (utilisez les commandes indiquer plus haut)")
        reponse = input(" ")
        if reponse.lower() == "z":
            my_lab.complet_map(my_lab.move_up())
            my_lab.print_laby()
        elif reponse.lower() == "q":
            my_lab.complet_map(my_lab.move_left())
            my_lab.print_laby()
        elif reponse.lower() == "s":
            my_lab.complet_map(my_lab.move_down())
            my_lab.print_laby()
        elif reponse.lower() == "d":
            my_lab.complet_map(my_lab.move_right())
            my_lab.print_laby()
        elif reponse.lower() == "x":
            print("Vous quittez la partie")
            game_exit = True
        else:
            print("Merci d'indiquer une commande valide")
    

main()