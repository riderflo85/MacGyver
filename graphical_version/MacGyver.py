#! /urs/bin/env python3
# coding: utf-8

from config.maping import Laby
from config.move import Move
from config.game import Game

def main():
    
    my_lab = Laby()
    playeur_move = Move()
    state = Game()

    
    my_lab.place_objet()

    my_lab.complet_map(state.start_pos_playeur)
    
    # Ce print est uniquement pour le version console du jeux, devras être retirer pour la version graphique
    print("\tBienvenu dans le jeux !!!\nVoici les commandes que vous pouvez tapez:\n  - x => quitte la partie\n  - z => aller vers le haut\n  - q => aller vers la gauche\n  - s => aller vers le bas\n  - d => aller vers la droite\n\n Bonne chance!!! ")
    
    while state.the_end == False:
        playeur_move.take_playeur_pos(my_lab.laby_complet)

        if state.start_game:
            my_lab.print_laby()
            state.start_game = False

        print("Que voulez-vous faire? Avancer? Quitter? (utilisez les commandes indiquer plus haut)")
        reponse = input(" ")

        if reponse.lower() == "z":
            my_lab.complet_map(playeur_move.move_up(my_lab.murs))
            my_lab.print_laby()
            state.end_game(my_lab.object_in_pocket, playeur_move.playeur_pos, my_lab.arrive)
            print("\t\t\t", my_lab.object_in_pocket)

        elif reponse.lower() == "q":
            my_lab.complet_map(playeur_move.move_left(my_lab.murs))
            my_lab.print_laby()
            state.end_game(my_lab.object_in_pocket, playeur_move.playeur_pos, my_lab.arrive)
            print("\t\t\t", my_lab.object_in_pocket)

        elif reponse.lower() == "s":
            my_lab.complet_map(playeur_move.move_down(my_lab.murs))
            my_lab.print_laby()
            state.end_game(my_lab.object_in_pocket, playeur_move.playeur_pos, my_lab.arrive)
            print("\t\t\t", my_lab.object_in_pocket)

        elif reponse.lower() == "d":
            my_lab.complet_map(playeur_move.move_right(my_lab.murs))
            my_lab.print_laby()
            state.end_game(my_lab.object_in_pocket, playeur_move.playeur_pos, my_lab.arrive)
            print("\t\t\t", my_lab.object_in_pocket)

        elif reponse.lower() == "x":
            print("Vous quittez la partie")
            state.the_end = True

        else:
            print("Merci d'indiquer une commande valide")




main()