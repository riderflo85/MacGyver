#! /urs/bin/env python3
# coding: utf-8

# My module
from config.maping import Laby
from config.move import Move
from config.game import Game
from config.display import Display
from config.object import Objects


def main():

    # Initialize objects
    my_lab = Laby()
    moving = Move()
    display = Display()
    objects = Objects()
    state = Game()

    list_objects = [display.aiguille, display.ether, display.tube]

    # Launch the welcome screen
    state.start_screen(display.home_page())

    # Load in memory the map of the game
    my_lab.load_map_file(display.map, display.wall,
        display.window, display.floor, display.guardian) # noqa

    # Place objects
    objects.place_objects(list_objects, my_lab.passages,
        display.floor, display.window) # noqa

    # Place the player on the starting position
    state.init_game(display.player, my_lab.pos_start, display.window)

    # Calculating the guardian’s field of action
    my_lab.guardian_zone_calculation()

    # Loop main of the game
    while state.start_game:

        state.play_game(moving, # noqa
            display.object_counter(objects.in_pocket, state.the_end, # noqua
                state.death), # noqa
            objects, my_lab.wall_list, # noqa
            my_lab.refresh_map(display.wall, display.floor, # noqa
                display.guardian, objects.pos_objects, display.window)) # noqa

        state.end_game(objects.in_pocket,
            my_lab.guardian_radius, display.player) # noqa


main()
