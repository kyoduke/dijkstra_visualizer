import pygame
from .colors import DARK_GREY, BLACK

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.current_color = color
        self.font = pygame.font.SysFont('arial', 16)

    def draw(self, win):
        pygame.draw.rect(win, self.current_color, self.rect)
        pygame.draw.rect(win, DARK_GREY, self.rect, 2)  # Border

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        win.blit(text_surface, text_rect)

    def check_hover(self, pos):
        if self.rect.collidepoint(pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color

    def is_clicked(self, pos, click):
        if self.rect.collidepoint(pos) and click:
            return True
        return False
