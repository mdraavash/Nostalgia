import pygame
from .settings import *
from .buttons import Button

class GameOverScreen:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.font = pygame.font.Font(UI_FONT, 30)
        self.background = pygame.image.load(GAME_OVER_BG).convert()
        self.restart_button = Button(400, 400, pygame.image.load(RESTART_BUTTON_IMAGE).convert_alpha(), 0.75)
        self.exit_button = Button(750, 400, pygame.image.load(EXIT_BUTTON_IMAGE).convert_alpha(), 0.75)

    def run(self):
        self.screen.blit(self.background, (0, 0))
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() //2, 300))
        if self.restart_button.draw(self.screen):
            return 'restart'
        if self.exit_button.draw(self.screen):
            return 'exit'
        return None