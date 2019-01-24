#! /urs/bin/env python3
# coding: utf-8

# Module Python
import pygame

# My module
from config.maping import Laby
from config.move import Move
from config.game import Game
from config.display import Display
from config.object import Objects

def main():
    
    my_lab = Laby()
    moving = Move()
    display = Display()
    objects = Objects
    state = Game(display.playeur)

    list_objects = [display.aiguille, display.ether, display.tube]

    my_lab.load_map_file(display.path_to_file_map ,display.wall, display.window, display.floor, display.gardien)
    objects.place_objects(list_objects, my_lab.passages, display.window)

    pygame.display.flip()

    while state.start_game:
        continue



main()