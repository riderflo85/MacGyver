#! /urs/bin/env python3
# coding: utf-8

from config.map import Laby

def main():
    
    my_lab = Laby()

    # On place le joueur au point de départ avant de lancer la boucle principale (le jeu)
    start_local_player = (1, 0)
    my_lab.place_objet()

    my_lab.complet_map(start_local_player)
    start_game = True

    # Ce print est uniquement pour le version console du jeux, devras être retirer pour la version graphique
    print("\tBienvenu dans le jeux !!!\nVoici les commandes que vous pouvez tapez:\n  - x => quitte la partie\n  - z => aller vers le haut\n  - q => aller vers la gauche\n  - s => aller vers le bas\n  - d => aller vers la droite\n\n Bonne chance!!! ")
    
    while my_lab.game_exit == False:
        my_lab.take_playeur_pos()

        if start_game:
            my_lab.print_laby()
            start_game = False
        print("Que voulez-vous faire? Avancer? Quitter? (utilisez les commandes indiquer plus haut)")
        reponse = input(" ")

        if reponse.lower() == "z":
            my_lab.complet_map(my_lab.move_up())
            my_lab.print_laby()
            print("\t\t\t", my_lab.object_in_pocket)

        elif reponse.lower() == "q":
            my_lab.complet_map(my_lab.move_left())
            my_lab.print_laby()
            print("\t\t\t", my_lab.object_in_pocket)

        elif reponse.lower() == "s":
            my_lab.complet_map(my_lab.move_down())
            my_lab.print_laby()
            print("\t\t\t", my_lab.object_in_pocket)

        elif reponse.lower() == "d":
            my_lab.complet_map(my_lab.move_right())
            my_lab.print_laby()
            print("\t\t\t", my_lab.object_in_pocket)

        elif reponse.lower() == "x":
            print("Vous quittez la partie")
            my_lab.game_exit = True

        elif my_lab.object_in_pocket == 3:
            my_lab.print_laby(True)
            print("Bien jouer vous avez gagner la partie")

        else:
            print("Merci d'indiquer une commande valide")


main()