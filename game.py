import pygame
import random

class game():
    def __init__(self):
        self.gaming = False
        # TODO: use a 0,1 formate for a list in list for food logic for snake game
            # 1. create list in list
            # 2. randomize 1 icon (can only have one 1 at a time)
            # 3. add snake that will represent a 2 in list in list
            # 4. add constant movement in direction last touched (no movement until arrow key pressed)

        self.board = []
        self.rand_tile = None
        self.rand_row = None


    def draw_board(self, window_x, window_y):
        # When snake and apple render they can only render on a 25 by 25 tile
        pass

    def draw_screen(self, window):
        window.fill((0,0,0))

    def make_board(self):
        for i in range(25):
            row = []
            for j in range(25):
                row.append([0])
            self.board.append(row)

    def random_select(self):
        self.rand_tile = random.randint(0,25)
        self.rand_row = random.randint(0,25)
