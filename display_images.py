import pygame

def display_menu_image(screen, cur_width, cur_height):
    
    title_size = int(0.50*cur_width),int(0.22*cur_height)
    title_init = pygame.image.load('Images/title.png')
    title = pygame.transform.scale(title_init, title_size)

    press_to_start_size = int(0.30*cur_width),int(0.15*cur_height)
    press_to_start_init = pygame.image.load('Images/press_to_start.png')
    press_to_start = pygame.transform.scale(press_to_start_init, press_to_start_size)

    screen.blit(press_to_start, ((cur_width-press_to_start_size[0])/2, (1.7*cur_height-press_to_start_size[1])/3))
    screen.blit(title, ((cur_width-title_size[0])/2, (cur_height-title_size[1])/3))

def display_flag(screen, cur_width, cur_height, flag_name):

    flag_size = int(0.33*cur_width),int(0.33*cur_height)
    flag_init = pygame.image.load(f'Flags/{flag_name}')
    flag = pygame.transform.scale(flag_init, flag_size)

    screen.blit(flag, ((cur_width-flag_size[0])/2, (cur_height-flag_size[1])/2.6))
    
    
