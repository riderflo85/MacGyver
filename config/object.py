#! /usr/bin/env python3
# conding: utf-8

# Module Python
import pygame
import random


class Objects():
    """This class manages the actions of objects"""

    def __init__(self):
        """Initializes variables useful to objects"""

        self.pos_objects = {}
        self.in_pocket = 0

    def place_objects(self, list_objects, passage, floor, window):
        """Place objects randomly"""

        # Browse and also store the position 
        #  of objects as their names in a dictionary
        for ob in list_objects:
            self.pos_objects[random.choice(passage)] = ob

        for keys, value in self.pos_objects.items():
            window.blit(floor, keys)
            window.blit(value, keys)
            pygame.display.flip()

    def take_objects(self, ply_pos):
        """Recovers an object if the player passes on it"""

        self.tuple_player_pos = (ply_pos[0], ply_pos[1])
        self.dict_temp = self.pos_objects.copy()

        for pos_ob in self.dict_temp.keys():
            if self.tuple_player_pos == pos_ob:
                self.pos_objects.pop(pos_ob)
                self.in_pocket += 1
