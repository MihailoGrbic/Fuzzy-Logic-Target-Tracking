import numpy as np
import pygame

from common import window, colors, DEFAULT_FONT, quitProgram
from drawing import drawTarget, drawTracker, writeText
from fuzzy_tracker import FuzzyTracker

pygame.display.set_caption("Fuzzy Logic Target Tracking by Jelena Ristić and Mihailo Grbić")


window_dim = np.array(window.get_size())
freeze = False

tracker = FuzzyTracker(position=window_dim / 2)

while True:
    window.fill(colors['White'])

    # Event handling
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quitProgram()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitProgram()

        if event.type == pygame.MOUSEBUTTONDOWN:
            freeze = not freeze

    # Make target follow mouse pointer if not frozen
    if not freeze:
        target_pos = np.array(pygame.mouse.get_pos())

    tracker.updateTrackerPos(target_pos)

    drawTarget(target_pos)
    drawTracker(tracker.position)
    writeText()

    # Draw everything on the screen
    pygame.display.update()
