#! /usr/bin/env python3
# coding: utf-8

# Module Python
import pygame

#My module
from .move import Move

class Game:

    def __init__(self, playeur):

        self.start_game = True
        self.playeur_pos = playeur.get_rect(x=0, y=40)
        #self.moving = Move()
    

    def play_game(self, moving, refresh_map, playeur):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    moving.move_right(self.playeur_pos)
                    if moving.move_valide:
                        self.playeur_pos = self.playeur_pos.move(40, 0)
                        take_objects(self.playeur_pos)
                        refresh_map

                if event.key == pygame.K_LEFT:
                    moving.move_left(self.playeur_pos)
                    if moving.move_valide:
                        self.playeur_pos = self.playeur_pos.move(-40, 0)
                        take_objects(self.playeur_pos)
                        refresh_map

                if event.key == pygame.K_UP:
                    moving.move_up(self.playeur_pos)
                    if moving.move_valide:
                        self.playeur_pos = pself.layeur_pos.move(0, -40)
                        take_objects(self.playeur_pos)
                        refresh_map

                if event.key == pygame.K_DOWN:
                    moving.move_down(self.playeur_pos)
                    if moving.move_valide:
                        self.playeur_pos = self.playeur_pos.move(0, 40)
                        take_objects(self.playeur_pos)
                        refresh_map

                if event.key == pygame.K_q:
                    continuer = False
    
        window.blit(playeur, self.playeur_pos)
        pygame.display.flip()



    def end_game(self, nb_object, pos_arrived):

        if self.playeur_pos[0] == pos_arrived[0]:
            if nb_object == 3:
                self.start_game = False
                print("BIEN JOUER VOUS AVEZ GAGNER !!!!")

            else:
                self.start_game = False
                print("Vous n'avez pas tout les objets dans votre sac, le gardien vous tue !!!")
                
        else:
            pass