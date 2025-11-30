import pygame


class snake():
    def __init__(self):
        self.body = [[12,12]]
        self.add_tail = False



    # ! Collision Checks
    def self_hit_check(self):
        # * if 2 of the same tail is counted == self hit == end.screen
        cou = 0
        for tail in self.body:
            if self.body[0] == tail:
                cou += 1
                if cou == 2:
                    return False
        else:
            return True

    def vert_bound_check(self):
        if self.body[0][1] > 24:
            return False

        if self.body[0][1] < 0:
            return False
        else:
            return True

    def hor_bound_check(self):
        if self.body[0][0] > 24:
            return False

        if self.body[0][0] < 0:
            return False
        else:
            return True


    def snake_movement(self, copy):
        # * moves back each tail by one except for the last tail (-1 bc the first head is alr in copy)
        for tail in range(len(self.body) - 1):
            if not tail == len(self.body):
                copy.append(self.body[tail])
        return copy




    def move_snake_down(self):
        # * moves head 1 down
        copy = [[self.body[0][0], self.body[0][1] + 1]]
        # * rewrite the updated snake to main snake
        if self.add_tail == True:
            self.body = self.add_new_tail(copy)
            # * if tail needs to be added
            self.add_tail = False
        else:
            self.body = self.snake_movement(copy)


    def move_snake_up(self):
        # * moves head 1 up
        copy = [[self.body[0][0], self.body[0][1] - 1]]
        # * rewrite the updated snake to main snake
        if self.add_tail == True:
            self.body = self.add_new_tail(copy)
            # * if tail needs to be added
            self.add_tail = False
        else:
            self.body = self.snake_movement(copy)


    def move_snake_left(self):
        # * moves head one left
        copy = [[self.body[0][0] - 1, self.body[0][1]]]
        # * rewrite the updated snake to main snake
        if self.add_tail == True:
            self.body = self.add_new_tail(copy)
            # * if tail needs to be added
            self.add_tail = False
        else:
            self.body = self.snake_movement(copy)


    def move_snake_right(self):
        # * move head 1 right
        copy = [[self.body[0][0] + 1, self.body[0][1]]]
        # * rewrite the updated snake to main snake
        if self.add_tail == True:
            self.body = self.add_new_tail(copy)
            # * if tail needs to be added
            self.add_tail = False
        else:
            self.body = self.snake_movement(copy)



    def draw_snake(self, surface, window_len):
        for snake_loc in self.body:
            # * pixel correction for snake rendering
            pygame.draw.rect(surface, (0,255,0), ((window_len/25 * snake_loc[0]) - 2, (window_len/25 * snake_loc[1]) - 2, (window_len/25) + 4, (window_len/25) + 4))

    def add_new_tail(self, copy):
        for tail in range(len(self.body)):
            if not tail == len(self.body):
                copy.append(self.body[tail])
        return copy




