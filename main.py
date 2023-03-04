import asyncio
import pygame
from display_images import *
from settings import *
from flags import *
import pygame_gui

async def main():

    pygame.init()
    clock = pygame.time.Clock()

    width = WIDTH
    height = HEIGHT

    # Generates the game window
    pygame.display.set_caption(GAME_NAME)
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    logo = pygame.image.load('Images/logo.ico')
    pygame.display.set_icon(logo)
    background_color = COLOR_BLUE

    # Initialisation - main menu
    cur_page = 'menu'

    # Initialisation flag class
    FLAG = Flag()

    # 20 sec
    timer = 0

    FLAG.set_manag(width, height)
    FLAG.set_txt(width, height)

    # game lop 
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000

        pygame.display.flip()
        clock.tick(FPS)
        screen.fill(background_color)
        cur_width = pygame.display.get_surface().get_size()[0]
        cur_height = pygame.display.get_surface().get_size()[1]

        if cur_width != width or cur_height != height:
            width, height = pygame.display.get_surface().get_size()
            if cur_page == 'game':
                FLAG.set_manag(width, height)
                FLAG.set_txt(width, height)

        # main menu
        if cur_page == 'menu':
            display_menu_image(screen, width, height)

        # flag displayed
        if cur_page == 'game':

            
            

            if timer == 0:
                FLAG.clear()
                if FLAG.number == 10 :
                    cur_page = 'first_correction'
                else:
                    flag_name = FLAG.choice()
                    timer = 1200

            FLAG.display_flags(screen, width, height, flag_name, timer)
            timer = timer - 1

            FLAG.manag.update(UI_REFRESH_RATE)
            FLAG.manag.draw_ui(screen)

        # correction for the first five flags
        if cur_page == 'first_correction':
            FLAG.display_first_correction(screen, width, height)

        # correction for the next five flags
        if cur_page == 'second_correction':
            FLAG.display_second_correction(screen, width, height)


        # events management
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if cur_page == 'game':
                if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                    if flag_name.lower() == event.text.lower()+'.png':
                        FLAG.correction.append([event.text, flag_name, True])
                    else:
                        FLAG.correction.append([event.text, flag_name, False])

                    timer = 0
                    FLAG.set_manag(width, height)
                    FLAG.set_txt(width, height)
                           
                FLAG.manag.process_events(event)

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

        pygame.display.update()

        await asyncio.sleep(0)


asyncio.run(main())