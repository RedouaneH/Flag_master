import asyncio
import pygame
import random
from display_images import *
from degrade import *
from settings import *
from flags import *
from os import listdir
from os.path import isfile, join

async def main():
    pygame.init()
    clock = pygame.time.Clock()
    # genere la fenetre du jeu
    pygame.display.set_caption(GAME_NAME)
    screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
    logo = pygame.image.load('Images/logo.ico')
    pygame.display.set_icon(logo)
    background_color = COLOR_BLUE
    # Initialisation
    cur_page = 'menu'
    # Drapeaux 
    FLAG=Flag()
    color_menu = color()
    timer = 0 #20 sec

    # boucle du jeux 
    while True:

        pygame.display.flip()
        clock.tick(FPS)
        screen.fill(background_color)
        width, height = pygame.display.get_surface().get_size()

        if cur_page == 'menu':
            color_menu.update()
            background_color = (color_menu.get(),111,204)
            display_menu_image(screen, width, height)

        if cur_page == 'game':
            if timer == 0 :
                FLAG.clear()
                if FLAG.number == 10 :
                    cur_page = 'first_correction'
                else:
                    flag_name = FLAG.choice()
                    timer = 1200

            FLAG.display_flags(screen, width, height, flag_name, timer)
            background_color = (color_menu.get(),111,204)
            timer = timer - 1

        if cur_page == 'first_correction':
            FLAG.display_first_correction(screen, width, height)

        if cur_page == 'second_correction':
            FLAG.display_second_correction(screen, width, height)


        # Gestion des évènements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if cur_page == 'game':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        FLAG.txt = FLAG.txt[:-1]
                    elif event.key == pygame.K_RETURN:
                        if flag_name.lower() == FLAG.txt.lower()+'.png':
                            FLAG.correction.append([FLAG.txt,flag_name,True])
                        else:
                            FLAG.correction.append([FLAG.txt,flag_name,False])

                        timer = 0
                        FLAG.clear()
                    else:
                        FLAG.txt += event.unicode

            

            if cur_page == 'second_correction':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    cur_page = 'menu'
                    timer = 0
                    FLAG.reset()
            
            elif cur_page == 'first_correction':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    cur_page = 'second_correction'

            elif cur_page == 'menu':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    cur_page = 'game'



        await asyncio.sleep(0)
                       
asyncio.run(main())