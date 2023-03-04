import random
import pygame
from display_images import *
from settings import *
from os import listdir
from os.path import isfile, join
import pygame_gui

class Flag:

    def __init__(self):
        self.FLAG_FILES = [f for f in listdir('Flags/') if isfile(join('Flags/', f))]
        self.displayed_files = []
        self.correction = []
        self.number = 0
        self.txt = ''
        self.manag = 0
        self.txt_input = 0

    def set_manag(self, width, height):
        self.manag = pygame_gui.UIManager((width, height))

    def set_txt(self, width, height):
        self.txt_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((0.3333*width, 0.64*height), (width*0.33333, 0.040*height)), manager=self.manag,
                                                object_id='#main_text_entry')

    def clear(self):
        self.txt = ''

    def reset(self):
        self.FLAG_FILES = [f for f in listdir('Flags/') if isfile(join('Flags/', f))]
        self.displayed_files = []
        self.correction = []
        self.number = 0
        self.txt = ''

    def choice(self):
        flag_name = random.choice([name for name in self.FLAG_FILES if name not in self.displayed_files])
        self.displayed_files.append(flag_name)
        self.number+=1
        return flag_name
    
    def display_flags(self, screen, width, height, flag_name, timer):

        font = pygame.font.SysFont(None, 24)
        little_font = pygame.font.SysFont(None, 19)

        # Votre réponse
        votre_reponse = little_font.render('Votre réponse', True, COLOR_BLUE_SKY)
        screen.blit(votre_reponse, (width/3, 0.615*height))

        # Barre en dessous
        pygame.draw.line(screen, COLOR_BLUE_SKY, (width/3, 0.69*height), (2*width/3, 0.69*height), 1)

        # flag display
        display_flag(screen, width, height, flag_name)
        pygame.draw.line(screen, COLOR_RED, (0.33333*width, 0.23*height), (0.333333*width + 0.333333*width* timer/1200, 0.23*height), 5)

    def display_first_correction(self, screen, width, height):

        gap = (3/140)*height
        thickness = 1
        # Lignes horizontales
        pygame.draw.line(screen, COLOR_GOLD, (width/14, height/7 - gap), (13*width/14, height/7 - gap), thickness)
        pygame.draw.line(screen, COLOR_GOLD, (width/14, 2*height/7 - gap), (13*width/14, 2*height/7 - gap), thickness)
        pygame.draw.line(screen, COLOR_GOLD, (width/14, 3*height/7 - gap), (13*width/14, 3*height/7 - gap), thickness)
        pygame.draw.line(screen, COLOR_GOLD, (width/14, 4*height/7 - gap), (13*width/14, 4*height/7 - gap), thickness)
        pygame.draw.line(screen, COLOR_GOLD, (width/14, 5*height/7 - gap), (13*width/14, 5*height/7 - gap), thickness)
        pygame.draw.line(screen, COLOR_GOLD, (width/14, 6*height/7 - gap), (13*width/14, 6*height/7 - gap), thickness)

        font = pygame.font.SysFont(None, 24)
        big_font = pygame.font.SysFont(None, 29)
        
        for i in range(1,6):
            tuple = self.correction[i-1]
            ma_reponse = tuple[0]
            ma_correction = tuple[1]
            bonne_reponse = tuple[2]

            flag_size = int(0.10*width),int(0.10*height)
            flag_init = pygame.image.load(f'Flags/{ma_correction}')
            flag = pygame.transform.scale(flag_init, flag_size)
            screen.blit(flag, (width/7, i*height/7))
            
            if bonne_reponse:
                display_txt = font.render(ma_reponse, True, COLOR_GREEN)
                screen.blit(display_txt, (width/2.8, (i*height/7) + 0.03*height))
            else:
                if ma_reponse=='':
                    display_txt = big_font.render(int(width/250)*' '+'X', True, COLOR_RED)
                    screen.blit(display_txt, (width/2.8, (i*height/7) + 0.03*height))
                else:
                    display_txt = font.render(ma_reponse, True, COLOR_RED)
                    screen.blit(display_txt, (width/2.8, (i*height/7) + 0.03*height))

            display_txt = font.render(ma_correction[:len(ma_correction)-4], True, COLOR_BLACK)
            screen.blit(display_txt, (2*width/3, (i*height/7) + 0.03*height))

    def display_second_correction(self, screen, width, height):

        gap = (3/140)*height
        thickness = 1
        # lignes horizontales
        pygame.draw.line(screen, COLOR_GOLD, (width/14, height/7 - gap), (13*width/14, height/7 - gap), thickness)
        pygame.draw.line(screen, COLOR_GOLD, (width/14, 2*height/7 - gap), (13*width/14, 2*height/7 - gap), thickness)
        pygame.draw.line(screen, COLOR_GOLD, (width/14, 3*height/7 - gap), (13*width/14, 3*height/7 - gap), thickness)
        pygame.draw.line(screen, COLOR_GOLD, (width/14, 4*height/7 - gap), (13*width/14, 4*height/7 - gap), thickness)
        pygame.draw.line(screen, COLOR_GOLD, (width/14, 5*height/7 - gap), (13*width/14, 5*height/7 - gap), thickness)
        pygame.draw.line(screen, COLOR_GOLD, (width/14, 6*height/7 - gap), (13*width/14, 6*height/7 - gap), thickness)
        
        font = pygame.font.SysFont(None, 24)
        big_font = pygame.font.SysFont(None, 29)

        for i in range(1,6):
            tuple = self.correction[i+4]
            ma_reponse = tuple[0]
            ma_correction = tuple[1]
            bonne_reponse = tuple[2]

            flag_size = int(0.10*width),int(0.10*height)
            flag_init = pygame.image.load(f'Flags/{ma_correction}')
            flag = pygame.transform.scale(flag_init, flag_size)
            screen.blit(flag, (width/7, i*height/7))

            if bonne_reponse:
                display_txt = font.render(ma_reponse, True, COLOR_GREEN)
                screen.blit(display_txt, (width/2.8, (i*height/7) + 0.03*height))
            else:
                if ma_reponse=='':
                    display_txt = big_font.render(int(width/250)*' '+'X', True, COLOR_RED)
                    screen.blit(display_txt, (width/2.8, (i*height/7) + 0.03*height))
                else:
                    display_txt = font.render(ma_reponse, True, COLOR_RED)
                    screen.blit(display_txt, (width/2.8, (i*height/7) + 0.03*height))

            correction_flag = font.render(ma_correction[:len(ma_correction)-4], True, COLOR_BLACK)
            screen.blit(correction_flag, (2*width/3, (i*height/7) + 0.03*height))

    

    