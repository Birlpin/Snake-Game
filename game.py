import pygame
import random

class game():
    def __init__(self):
        self.gaming = False
        #! use a 0,1 formate for a list in list for food logic for snake game
            # TODO. create tile allocation for the board for render purposes
            # TODO. add snake that will represent a 2 in list in list
            # TODO. add constant movement in direction last touched (no movement until arrow key pressed)

        self.board = []
        self.apple_exi = False
        self.apple_row = 0
        self.apple_tile = 0
        self.make_board()



    def make_board(self):
        for i in range(25):
            row = []
            for j in range(25):
                row.append(0)
            self.board.append(row)

    def random_select(self):
        self.apple_row = random.randint(0,24)
        self.apple_tile = random.randint(0,24)


    def add_apple(self):
        print(self.apple_row, self.apple_tile)
        # *Reruns random apple spot if it tries to place where snake body is
        while True:
            self.random_select()
            if self.board[self.apple_row][self.apple_tile] == 0:
                self.board[self.apple_row][self.apple_tile] = 1
                break
        self.apple_exi = True
        print(self.apple_row, self.apple_tile)

    # * Make a delete apple



    def draw_board(self, window, window_x, window_y):
        # When snake and apple render they can only render on a 25 by 25 tile
        window.fill((0,0,0))
        # TODO: render apple
        # TODO: render snake (might have to write helper function)
        # 25 tiles but 26 lines


        tile_width = window_x / 26
        tile_height = window_y / 26

        render_apple = pygame.draw.rect(window, (255, 0, 0), (self.apple_tile * tile_width, self.apple_row * tile_height, tile_width, tile_height) )

