import pygame
import board
import time

reversi = board.Board(100)

reversi.draw()

while True:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            reversi.click_event(x, y)