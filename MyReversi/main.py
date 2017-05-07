import pygame
import board
import time

if __name__=="__main__":
    reversi = board.Board(100, 8)
    reversi.draw()

    while True:

        reversi.make_candidate()

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                reversi.click_event(x, y)