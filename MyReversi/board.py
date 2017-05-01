import pygame
from enum import Enum


class Block:
    def __init__(self, screen, color, x, y, w, h):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))


class StatusPanel(Block):
    def __init__(self, screen, color, font_color, x, y, w, h):
        super(StatusPanel, self).__init__(screen, color, x, y, w, h)
        self.font_color = font_color

    def draw(self):
        super(StatusPanel, self).draw()

class State(Enum):
    BOARD = 'board',
    WHITE = 'white',
    BLACK = 'black',
    CANDIDATE = 'candidate',


class Item(Block):
    def __init__(self, screen, color, x, y, w, h):
        super(Item, self).__init__(screen, color, x, y, w, h)
        self.state = State.BOARD
        self.call_draw = {
            State.BOARD : self.draw_board ,
            State.WHITE : self.draw_white,
            State.BLACK: self.draw_black,
            State.CANDIDATE : self.draw_candidate,
        }
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

    def set_board(self):
        if self.state is State.CANDIDATE:
            self.state = State.BOARD

    def set_white(self):
        self.state = State.WHITE

    def set_black(self):
        self.state = State.BLACK

    def toggle_state(self):
        if self.state is State.WHITE:
            self.state = State.BLACK
        elif self.state is State.BLACK:
            self.state = State.WHITE


class Rule:
    def __init__(self):
        self.states = [State.BOARD for _ in range(64)]
        self.set_state(3, 3, State.WHITE)
        self.set_state(3, 4, State.BLACK)
        self.set_state(4, 3, State.BLACK)
        self.set_state(4, 4, State.WHITE)

    def set_state(self, x, y, state):
        self.states[y*8 + x] = state

    def get_state(self, x=None, y=None):
        if x is not None and y is not None:
            return self.states[y * 8 + x]
        else:
            return self.states

    def make_candidate(self):
        print('a')


class Board:
    def __init__(self, block_width):
        self.block_width = block_width
        self.total_width = block_width * 8
        self.total_height = block_width * 9
        self.color = {
            'green':(0, 255, 0),
            'red': (255, 0, 0),
            'blue': (0, 0, 255),
            'white': (255, 255, 255),
            'gray': (128, 128, 128),
            'black': (0, 0, 0),
        }
        self.screen = pygame.display.set_mode((self.total_width, self.total_height))
        self.status_panel = StatusPanel(self.screen, self.color['blue'], (0, 0, 0), 0, 0, self.total_width, self.block_width)
        self.items = [Item(self.screen, self.color['gray'], (x)*self.block_width, (y+1)*self.block_width, self.block_width, self.block_width) for x in range(8) for y in range(8)]
        self.rule = Rule


    def draw(self):
        self.status_panel.draw()
        for item in self.items:
            item.draw()

        starts = [(0, (y + 1) * self.block_width) for y in range(9)]
        starts.extend([(x * self.block_width, self.block_width) for x in range(9)])
        ends = [(self.total_width-1, (y + 1) * self.block_width) for y in range(9)]
        ends.extend([(x * self.block_width, self.total_height) for x in range(9)])

        for start, end in zip(starts, ends):
            pygame.draw.line( self.screen, self.color['black'], start, end, 5)

        pygame.display.flip()

    def set_candidate(self, x, y):
        try:
            self.items[y * 8 + x].set_candidate()
        except ValueError:
            print('error detected, your codes are wrong')

    def set_board(self, x, y):
        self.items[y * 8 + x].set_board()

    def set_white(self, x, y):
        self.items[y*8+x].set_white()

    def set_black(self, x, y):
        self.items[y * 8 + x].set_black()

    def toggle_state(self, x, y):
        self.items[y * 8 + x].toggle_state()

    def abs2coor(self,x, y):
        y = y - self.block_width
        coor_x = (int)(x / self.block_width)
        coor_y = (int)(y / self.block_width)
        return coor_x, coor_y

    def click_event(self, x, y):
        cx, cy = self.abs2coor(x, y)
        print('clicked: ' , cx, cy)

