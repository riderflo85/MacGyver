#! /usr/bin/env python3
# coding: utf-8

import os
import pygame


class Laby:

    def __init__(self):
        self.wall_list = []
        self.passages = []
        self.init_playeur_pos = []
        self.pos_start = []
        self.guardian_pos = []
        self.object_in_pocket = 0
        self.guardian_radius = []


    def load_map_file(self, file_map, wall, window, floor, guardian):
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

                    elif colomn == "d":
                        self.pos_start.append((x, y))
                        window.blit(floor, (x, y))
                        pygame.display.flip()

                    elif colomn == "a":
                        self.passages.append((x, y))
                        self.guardian_pos.append((x, y))
                        window.blit(floor, (x, y))
                        window.blit(guardian, (x, y))
                        pygame.display.flip()

                    else:
                        pass

                    self.nb_line += 1
                self.nb_colomn += 1


    def refresh_map(self, wall, floor, gard, pos_objects, window):

        for pos_wall in self.wall_list:
            window.blit(wall, pos_wall)
    
        for pos_passage in self.passages:
            window.blit(floor, pos_passage)

        for keys, value in pos_objects.items():
            window.blit(value, keys)

        window.blit(floor, self.pos_start[0])
        window.blit(gard, self.guardian_pos[0])
        
        pygame.display.flip()

    
    def guardian_zone_calculation(self):

        self.x = self.guardian_pos[0][0]
        self.y = self.guardian_pos[0][1]
        # Upleft
        self.guardian_radius.append((self.x-40, self.y-40))
        # Up
        self.guardian_radius.append((self.x, self.y-40))
        # Upright
        self.guardian_radius.append((self.x+40, self.y-40))
        # Left
        self.guardian_radius.append((self.x-40, self.y))
        # Right
        self.guardian_radius.append((self.x+40, self.y))
        # Downleft
        self.guardian_radius.append((self.x-40, self.y+40))
        # Down
        self.guardian_radius.append((self.x, self.y+40))
        # Downright
        self.guardian_radius.append((self.x+40, self.y+40))