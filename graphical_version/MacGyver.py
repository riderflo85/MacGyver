#! /urs/bin/env python3
# coding: utf-8

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
    objects = Objects()
    state = Game()

    list_objects = [display.aiguille, display.ether, display.tube]

    state.start_screen(display.home_page())

    my_lab.load_map_file(display.file_map ,display.wall, display.window, display.floor, display.guardian)
    
    objects.place_objects(list_objects, my_lab.passages, display.floor, display.window)

    state.init_game(display.playeur, my_lab.pos_start, display.window)

    my_lab.guardian_zone_calculation()

    while state.start_game:
        state.play_game(moving, my_lab.refresh_map(display.wall, display.floor, objects.pos_objects, display.window), objects, my_lab.wall_list, display.counter)
        state.end_game(objects.in_pocket, my_lab.guardian_radius, display.playeur)


main()