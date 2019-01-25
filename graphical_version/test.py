#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import os

path_to_file = os.path.join("../ressource/img", "wood.png")

pygame.init()
pygame.font.init()
#clock = pygame.time.Clock()


ob = 2

CIEL = 0, 200, 255
ORANGE = 255, 100, 0


fenetre = pygame.display.set_mode((600, 700), pygame.RESIZABLE)

my_img = pygame.image.load(path_to_file).convert()

def main():

    loop = True
    while loop:
        background = pygame.Surface((600, 700))
        background.blit(my_img, (0, 600))

        # Définition de la police
        bigText = pygame.font.SysFont('ani', 36)

        # Définition du texte
        # render(text, antialias, rgb color tuple)
        title_text = bigText.render("\
Object in pocket: {}\
 autre text\
 essai ".format(ob), True, ORANGE)

        # Position: horizontal au centre , vertical = 50
        # Le centre du texte est au centre quelque soit le texte
        # Le texte est inscrit dans un rectangle
        textpos = title_text.get_rect()

        # Placement du texte en x et y
        textpos.centerx = fenetre.get_rect().centerx
        textpos.centery = 650

        # Collage du texte sur le fond
        background.blit(title_text, textpos)

        # Ajout du fond dans la fenêtre
        fenetre.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        # Actualisation de l'affichage
        pygame.display.flip()
        # 10 fps
        #clock.tick(10)

if __name__ == '__main__':
    main()