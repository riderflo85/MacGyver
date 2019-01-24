#! /usr/bin/env python3
# coding: utf-8

class Move:


    def __init__(self):

        self.move_valide = False
    

    def move_up(self, ply_pos, wall_list):

        self.predict_playeur_pos = (ply_pos[0], ply_pos[1]-40)

        if self.predict_playeur_pos not in wall_list:
            self.move_valide = True

        else:
            self.move_valide = False
        
        return self.move_valide


    def move_down(self, ply_pos, wall_list):

        self.predict_playeur_pos = (ply_pos[0], ply_pos[1]+40)

        if self.predict_playeur_pos not in wall_list:
            self.move_valide = True

        else:
            self.move_valide = False

        return self.move_valide


    def move_left(self, ply_pos, wall_list):

        self.predict_playeur_pos = (ply_pos[0]-40, ply_pos[1])

        if self.predict_playeur_pos not in wall_list:
            self.move_valide = True

        else:
            self.move_valide = False

        return self.move_valide


    def move_right(self, ply_pos, wall_list):

        self.predict_playeur_pos = (ply_pos[0]+40, ply_pos[1])

        if self.predict_playeur_pos not in wall_list:
            self.move_valide = True

        else:
            self.move_valide = False

        return self.move_valide