#! /usr/bin/env python3
# coding: utf-8

# Module Python
import pygame


class Game:

    def __init__(self):

        self.start_game = True
        self.launch_partie = False

    
    def init_game(self, playeur, pos_start, window):

        self.window = window
        self.pos_start = pos_start
        self.playeur_pos = playeur.get_rect(x=self.pos_start[0][0], y=self.pos_start[0][1])
        self.playeur_img = playeur


    def play_game(self, moving, refresh_map, obj, wall_list, counter):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.start_game = False

            if self.launch_partie:

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        moving.move_right(self.playeur_pos, wall_list)
                        if moving.move_valide:
                            self.playeur_pos = self.playeur_pos.move(40, 0)
                            obj.take_objects(self.playeur_pos)
                            refresh_map

                    if event.key == pygame.K_LEFT:
                        moving.move_left(self.playeur_pos, wall_list)
                        if moving.move_valide:
                            self.playeur_pos = self.playeur_pos.move(-40, 0)
                            obj.take_objects(self.playeur_pos)
                            refresh_map

                    if event.key == pygame.K_UP:
                        moving.move_up(self.playeur_pos, wall_list)
                        if moving.move_valide:
                            self.playeur_pos = self.playeur_pos.move(0, -40)
                            obj.take_objects(self.playeur_pos)
                            refresh_map

                    if event.key == pygame.K_DOWN:
                        moving.move_down(self.playeur_pos, wall_list)
                        if moving.move_valide:
                            self.playeur_pos = self.playeur_pos.move(0, 40)
                            obj.take_objects(self.playeur_pos)
                            refresh_map

                    if event.key == pygame.K_q:
                        self.start_game = False
                
        counter
    
        self.window.blit(self.playeur_img, self.playeur_pos)
        pygame.display.flip()


    def start_screen(self, homepage):
        
        while self.launch_partie == False:
            homepage

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_c:
                        self.launch_partie = True

            pygame.display.flip()


    def end_game(self, nb_object, pos_arrived, playeur):

        self.tuple_playeur_pos = (self.playeur_pos[0], self.playeur_pos[1])

        if self.tuple_playeur_pos in pos_arrived:
            if nb_object == 3:
                self.start_game = False
                print("BIEN JOUER VOUS AVEZ GAGNER !!!!")

            else:
                self.playeur_pos = playeur.get_rect(x=self.pos_start[0][0], y=self.pos_start[0][1])
                print("Vous n'avez pas tout les objets dans votre sac, le guardian vous tue !!!")
                
        else:
            pass