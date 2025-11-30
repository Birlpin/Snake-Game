import snake
import pygame
import random


class game():
    def __init__(self):
        self.gaming = False
        self.apple_exi = False
        self.apple_row = 0
        self.apple_tile = 0
        self.snake = snake.snake()
        self.current = -10

    def high_score_check(self, high_score):
        if self.current > high_score:
            return True
        else:
            return False


    def random_select(self):
        self.apple_row = random.randint(0,24)
        self.apple_tile = random.randint(0,24)


    def add_apple(self):
        #! adds new apple if last is deleted
        # * Reruns random apple spot if it tries to place where snake body is
        # * Until apple placement is found that is unoccupied by snake
        while True:
            self.random_select()
            length = 0
            for tail in self.snake.body:
                if [self.apple_tile, self.apple_row] != tail:
                    length += 1
                    if length == len(self.snake.body):
                        self.current += 10
                        return
            self.add_apple()




    def draw_board(self, window, window_len):
        # When snake and apple render they can only render on a 25 by 25 tile
        window.fill((0,0,0))

        # * 25 tiles but 26 lines
        tile_size = window_len / 25

        pygame.draw.rect(window, (255, 0, 0), (self.apple_tile * tile_size, self.apple_row * tile_size, tile_size, tile_size))


    def apple_collision(self):
        # * checks if head passes over the apple
        if [self.apple_tile, self.apple_row] == self.snake.body[0]:
            # * IF yes main executes self.game.add_apple
            self.apple_exi = False
            self.snake.add_tail = True




