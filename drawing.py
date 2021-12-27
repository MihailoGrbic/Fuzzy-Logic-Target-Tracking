import pygame

from common import window, colors, DEFAULT_FONT


def drawTarget(target_pos):
    pygame.draw.circle(window, colors['Black'], target_pos, 53)
    pygame.draw.circle(window, colors['Red'], target_pos, 50)
    pygame.draw.circle(window, colors['White'], target_pos, 40)
    pygame.draw.circle(window, colors['Red'], target_pos, 30)
    pygame.draw.circle(window, colors['White'], target_pos, 20)
    pygame.draw.circle(window, colors['Red'], target_pos, 10)

def drawTracker(tracker_pos):
    pygame.draw.line(window, colors['Blue'], tracker_pos - [8, 0], tracker_pos + [8, 0], 3)
    pygame.draw.line(window, colors['Blue'], tracker_pos - [0, 8], tracker_pos + [0, 8], 3)

def writeText():
    font = pygame.font.SysFont(DEFAULT_FONT, 25)
    text = font.render("Left click to freeze the target. Exit program with the escape button.", True, colors['Black'])
    text_rect = text.get_rect()
    text_rect.center = (330, 1060)
    window.blit(text, text_rect)
    pygame.display.update(text_rect)

    font = pygame.font.SysFont(DEFAULT_FONT, 25)
    text = font.render("by Jelena Ristić and Mihailo Grbić", True, colors['Black'])
    text_rect = text.get_rect()
    text_rect.center = (1750, 1060)
    window.blit(text, text_rect)
    pygame.display.update(text_rect)
