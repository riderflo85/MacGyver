#! /usr/bin/env python3
# coding: utf-8

# Module Python
import pygame


class Game:
    """This class manages the behavior of the game"""

    def __init__(self):
        """Initializes end of game launch variables"""

        self.start_game = True
        self.launch_partie = False
        self.the_end = False

    def init_game(self, player, pos_start, window):
        """Initializes the starting position of the player"""

        self.window = window
        self.pos_start = pos_start
        self.player_pos = player.get_rect(x=self.pos_start[0][0],
            y=self.pos_start[0][1]) # noqa
        self.player_img = player

    def play_game(self, moving, counter, obj, wall_list, refresh_map):
        """Manages game events and player position display"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.start_game = False

            if self.launch_partie:

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        moving.move_right(self.player_pos, wall_list)
                        if moving.move_valide:
                            self.player_pos = self.player_pos.move(40, 0)
                            obj.take_objects(self.player_pos)
                            refresh_map

                    if event.key == pygame.K_LEFT:
                        moving.move_left(self.player_pos, wall_list)
                        if moving.move_valide:
                            self.player_pos = self.player_pos.move(-40, 0)
                            obj.take_objects(self.player_pos)
                            refresh_map

                    if event.key == pygame.K_UP:
                        moving.move_up(self.player_pos, wall_list)
                        if moving.move_valide:
                            self.player_pos = self.player_pos.move(0, -40)
                            obj.take_objects(self.player_pos)
                            refresh_map

                    if event.key == pygame.K_DOWN:
                        moving.move_down(self.player_pos, wall_list)
                        if moving.move_valide:
                            self.player_pos = self.player_pos.move(0, 40)
                            obj.take_objects(self.player_pos)
                            refresh_map

                    if event.key == pygame.K_q:
                        self.start_game = False

        counter
        self.window.blit(self.player_img, self.player_pos)
        pygame.display.flip()

    def start_screen(self, homepage):
        """Load the homepage"""

        while self.launch_partie == False:
            homepage

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_c:
                        self.launch_partie = True

            pygame.display.flip()

    def end_game(self, nb_object, pos_arrived, player):
        """Condition of the end of game"""

        self.tuple_player_pos = (self.player_pos[0], self.player_pos[1])

        if self.tuple_player_pos in pos_arrived:
            if nb_object == 3:
                self.launch_partie = False
                self.the_end = True

            else:
                self.player_pos = player.get_rect(x=self.pos_start[0][0],
                    y=self.pos_start[0][1]) # noqa

        else:
            pass
