import pygame
from code.settings import *

BG_COLOR = (173, 216, 230)         # Light sky blue
HIGHLIGHT_COLOR = (255, 140, 0)    # Orange
TEXT_COLOR = (255, 255, 255)       # White

class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(UI_FONT, 40)
        self.options = ["Resume", "Main Menu", "Exit"]
        self.selected = 0

    def draw(self):
        self.screen.fill(BG_COLOR)

        # Title
        title = self.font.render("PAUSED", True, HIGHLIGHT_COLOR)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 80))

        # Options
        for index, option in enumerate(self.options):
            is_selected = index == self.selected
            color = TEXT_COLOR
            bg_color = HIGHLIGHT_COLOR if is_selected else None

            text_surface = self.font.render(option.upper(), True, color)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, 200 + index * 70))

            if bg_color:
                pygame.draw.rect(self.screen, bg_color, text_rect.inflate(30, 20), border_radius=8)

            self.screen.blit(text_surface, text_rect)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected]
        return None
