#! /usr/bin/env python3
# coding: utf-8

import os
import pygame


class Laby:

    def __init__(self):
        self.wall_list = []
        self.passages = []
        self.init_playeur_pos = []
        self.gardien_pos = []
        self.object_in_pocket = 0

        #self.load_map_file()

    def load_map_file(self, file_map, wall, window, floor, gardien):
        with open(file_map, 'r') as lab:
            self.nb_colomn = 0

            for line in lab:
                self.nb_line = 0

                for colomn in line:
                    x = self.nb_line * 40
                    y = self.nb_colomn * 40

                    if colomn == "x":
                        self.wall_list.append((x, y))
                        window.blit(wall, (x, y))
                        pygame.display.flip()

                    elif colomn == ".":
                        self.passages.append((x, y))
                        window.blit(floor, (x, y))
                        pygame.display.flip()

                    elif colomn == "a":
                        self.gardien_pos.append((x, y))
                        window.blit(gardien, (x, y))
                        pygame.display.flip()

                    else:
                        pass

                    self.nb_line += 1
                self.nb_colomn += 1


    def refresh_map(self, wall, pos_passage, pos_objects, window):

        for pos_wall in self.wall_list:
            window.blit(wall, pos_wall)
    
        for pos_passage in self.passages:
            window.blit(floor, pos_passage)

        for keys, value in pos_objects.items():
            window.blit(value, keys)