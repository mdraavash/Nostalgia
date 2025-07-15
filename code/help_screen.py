import pygame
from .buttons import Button
from .settings import *

class HelpScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load(HELP_SCREEN_BG).convert()
        self.back_button = Button(50, 50, pygame.image.load(BACK_BUTTON_IMAGE).convert_alpha(), 0.5)

    def run(self):
        self.screen.blit(self.background, (0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'exit'
            if self.back_button.draw(self.screen):
                return 'back'
            pygame.display.update()