import pygame
from enum import Enum
from collections import deque
import player

class Color:
    green   = (0, 255, 0)
    red     = (255, 0, 0)
    blue    = (0, 0, 255)
    white   = (255, 255, 255)
    gray    = (128, 128, 128)
    black   = (0, 0, 0)


class State(Enum):
    BOARD = Color.gray
    WHITE = Color.white
    BLACK = Color.black
    CANDIDATE = Color.green
    PANEL = Color.blue


class Block:
    def __init__(self, screen, x, y, w, h):
        self.screen = screen
        self.color = State.BOARD.value
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))


class StatusPanel(Block):
    def __init__(self, screen, font_color, x, y, w, h):
        super(StatusPanel, self).__init__(screen, x, y, w, h)
        self.font_color = font_color
        self.color = State.PANEL.value

    def draw(self):
        super(StatusPanel, self).draw()


class Item(Block):

    def __init__(self, screen, x, y, w, h, x_idx, y_idx):
        super(Item, self).__init__(screen, x, y, w, h)
        self.state = State.BOARD
        self.color = self.state.value
        self.call_draw = {
            State.BOARD : self.draw_board ,
            State.WHITE : self.draw_white,
            State.BLACK: self.draw_black,
            State.CANDIDATE : self.draw_candidate,
        }
        self.x_idx = x_idx
        self.y_idx = y_idx

    def draw(self):
        super(Item, self).draw()
        print(self.x, self.y)
        self.call_draw[self.state]()

    def draw_board(self):
        print('draw board')

    def draw_white(self):
        print('draw white')

    def draw_black(self):
        print('draw black')

    def draw_candidate(self):
        print('draw candidate')

    def set_candidate(self):
        if not self.state == State.BOARD:
            raise ValueError
        self.state = State.CANDIDATE
        self.color = self.state.value

    def set_board(self):
        if self.state is State.CANDIDATE:
            self.state = State.BOARD
            self.color = self.state.value

    def set_white(self):
        self.state = State.WHITE
        self.color = self.state.value

    def set_black(self):
        self.state = State.BLACK
        self.color = self.state.value

    def toggle_state(self):
        if self.state is State.WHITE:
            self.set_black()
        elif self.state is State.BLACK:
            self.set_white()


class Board:
    def __init__(self, block_width, reversi_width=8):
        self.REVERSI_WIDTH = reversi_width
        self.block_width = block_width
        self.total_width = block_width * self.REVERSI_WIDTH
        self.total_height = block_width * (self.REVERSI_WIDTH+1)

        self.screen = pygame.display.set_mode((self.total_width, self.total_height))
        self.status_panel = StatusPanel(self.screen, (0, 0, 0), 0, 0, self.total_width, self.block_width)
        self.items = [Item(self.screen, (x)*self.block_width, (y+1)*self.block_width, self.block_width, self.block_width, x, y) for x in range(self.REVERSI_WIDTH) for y in range(self.REVERSI_WIDTH)]

        self.set_white(3, 3)
        self.set_white(4, 4)
        self.set_black(3, 4)
        self.set_black(4, 3)

        self.colors = [State.BLACK, State.WHITE]
        self.players = deque([player.Player(c) for c in self.colors])


    def make_candidate(self):
        print('make_candidate')
        player = self.players[0].get_color()
        opponent = self.players[1].get_color()

        items = [item for item in self.items if item.state == player]

        for item in items:
            x_idx = item.x_idx
            y_idx = item.y_idx

    def draw(self):
        self.status_panel.draw()
        for item in self.items:
            item.draw()

        starts = [(0, (y + 1) * self.block_width) for y in range(self.REVERSI_WIDTH+1)]
        starts.extend([(x * self.block_width, self.block_width) for x in range(self.REVERSI_WIDTH+1)])
        ends = [(self.total_width-1, (y + 1) * self.block_width) for y in range(self.REVERSI_WIDTH+1)]
        ends.extend([(x * self.block_width, self.total_height) for x in range(self.REVERSI_WIDTH+1)])

        for start, end in zip(starts, ends):
            pygame.draw.line( self.screen, Color.black, start, end, 5)

        pygame.display.flip()

    def set_candidate(self, x, y):
        try:
            self.items[y * self.REVERSI_WIDTH + x].set_candidate()
        except ValueError:
            print('error detected, your codes are wrong')

    def set_board(self, x, y):
        self.items[y * self.REVERSI_WIDTH + x].set_board()

    def set_white(self, x, y):
        self.items[y * self.REVERSI_WIDTH + x].set_white()

    def set_black(self, x, y):
        self.items[y * self.REVERSI_WIDTH + x].set_black()

    def toggle_state(self, x, y):
        self.items[y * self.REVERSI_WIDTH + x].toggle_state()

    def _abs2coor(self,x, y):
        y = y - self.block_width
        coor_x = (int)(x / self.block_width)
        coor_y = (int)(y / self.block_width)
        return coor_x, coor_y

    def click_event(self, x, y):
        cx, cy = self._abs2coor(x, y)
        print('clicked: ', cx, cy)

