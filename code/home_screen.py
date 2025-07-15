from .buttons import Button
import pygame
from .settings import *
from .level import *
from .help_screen import HelpScreen

class HomeScreen:
    def __init__(self,screen):
        self.screen = screen
        self.background = pygame.image.load(START_SCREEN_BG).convert()
        self.start_button = Button(100, 200, pygame.image.load(START_BUTTON_image).convert_alpha(), 0.75)
        self.help_button = Button(100, 300, pygame.image.load(HELP_BUTTON_IMAGE).convert_alpha(), 0.75)
        self.exit_button = Button(100, 400, pygame.image.load(EXIT_BUTTON_IMAGE).convert_alpha(), 0.75)

    def run(self):
        self.screen.blit(self.background, (0, 0))
        if self.start_button.draw(self.screen):
            return 'game_start'
        if self.help_button.draw(self.screen):
            help_screen = HelpScreen(self.screen)
            if help_screen.run() == 'back':
                return None
        if self.exit_button.draw(self.screen):
            return 'exit'
        return None