#! /usr/bin/env python3
# coding: utf-8

class Move:
    """This class manages the player’s movements"""


    def __init__(self):

        self.move_valide = False
    

    def move_up(self, ply_pos, wall_list):
        """Movement of playing upward by calculating its future position.
        Verifies that future position is possible"""

        self.predict_player_pos = (ply_pos[0], ply_pos[1]-40)

        if self.predict_player_pos not in wall_list:
            self.move_valide = True

        else:
            self.move_valide = False
        
        return self.move_valide


    def move_down(self, ply_pos, wall_list):
        """Move the player down by calculating its future position.
        Verifies that future position is possible"""

        self.predict_player_pos = (ply_pos[0], ply_pos[1]+40)

        if self.predict_player_pos not in wall_list:
            self.move_valide = True

        else:
            self.move_valide = False

        return self.move_valide


    def move_left(self, ply_pos, wall_list):
        """Movement of the player to the left by calculating his future position.
        Verifies that future position is possible"""

        self.predict_player_pos = (ply_pos[0]-40, ply_pos[1])

        if self.predict_player_pos not in wall_list:
            self.move_valide = True

        else:
            self.move_valide = False

        return self.move_valide


    def move_right(self, ply_pos, wall_list):
        """Movement of the player to the right by calculating his future position.
        Verifies that future position is possible"""

        self.predict_player_pos = (ply_pos[0]+40, ply_pos[1])

        if self.predict_player_pos not in wall_list:
            self.move_valide = True

        else:
            self.move_valide = False

        return self.move_valide