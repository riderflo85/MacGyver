#! /usr/bin/env python3
# coding: utf-8

class Game:

    def __init__(self):
        self.start_game = True
        self.the_end = False
        self.start_pos_playeur = (1, 0)
    

    def end_game(self, nb_object, pos_playeur, pos_arrived):
        if pos_playeur[0] == pos_arrived[0]:
            if nb_object == 3:
                self.the_end = True
                print("BIEN JOUER VOUS AVEZ GAGNER !!!!")
            else:
                self.the_end = True
                print("Vous n'avez pas tout les objets dans votre sac, le gardien vous tue !!!")
        else:
            pass