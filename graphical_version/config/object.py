#! /usr/bin/env python3
# conding: utf-8
import pygame
import random

class Objects():

    def __init__(self):

        self.pos_objects = {}
        self.objects_in_pocket = 0

    
    def place_objects(self, list_objects, passage, window):
        
        for ob in list_objects:
            self.pos_objects[random.choice(passage)] = ob

        for keys, value in self.pos_objects.items():
            window.blit(value, keys)
            pygame.display.flip()

    
    def take_objects(self, ply_pos):

        self.tuple_playeur_pos = (ply_pos[0], ply_pos[1])
        self.dict_temp = self.pos_objects.copy()

        for pos_ob in self.dict_temp.keys():
            if self.tuple_playeur_pos == pos_ob:
                self.pos_objects.pop(pos_ob)
                self.objects_in_pocket += 1