import game
import starterscreen
import pygame



class main():
    def __init__(self):
        pygame.init()

        self.window_x = 720
        self.window_y = 720

        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((self.window_x, self.window_y))

        # init the start class
        self.start = starterscreen.start()
        self.game = game.game()
        self.snake = self.game.snake

        self.k_down_last = False
        self.k_up_last = False
        self.k_right_last = False
        self.k_left_last = False

        self.high_score = self.start.score


        main.run(self)

    def down_key_reset(self):
        self.k_down_last = False
        self.k_up_last = False
        self.k_right_last = False
        self.k_left_last = False

    def game_reset(self):
        self.game.high_score_check(self.high_score)
        self.start = starterscreen.start()
        self.game = game.game()
        self.snake = self.game.snake
        self.down_key_reset()


    def run(self):

        run = True
        while run:
            # * Variable to make sure, no double input per frame
            alr_pressed = False

            # * starter screen draw
            if self.start.startin:
                self.clock.tick(30)
                self.window.fill((6,63,62))
                self.start.draw_screen(self.window)

            # * Game Starts
            if self.game.gaming:
                self.clock.tick(5)
                self.window.fill((0,0,0))

                # * IF apple eaten
                if not self.game.apple_exi:
                    self.game.add_apple()
                    # * State apple exists
                    self.game.apple_exi = True


                # * draws the apple
                self.game.draw_board(self.window, self.window_x)

                # * Draw snake tails
                self.snake.draw_snake(self.window,720)




            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                # * IF in title screen
                if self.start.startin == True:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        click_pos = pygame.mouse.get_pos()

                        if self.start.start_button.collidepoint(click_pos):
                            self.start.startin = False
                            self.game.gaming = True

                        elif self.start.exit_button.collidepoint(click_pos):
                            run = False


                if self.game.gaming == True:
                    # * Move Snake UP
                    if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                        if not self.k_down_last:
                            # * UP pressed last
                            self.down_key_reset()
                            self.k_up_last = True

                            # * no double input
                            alr_pressed = True

                            # * move tail one tile up
                            self.snake.move_snake_up()


                    elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                        if not self.k_up_last:
                            # * DOWN key pressed last
                            self.down_key_reset()
                            self.k_down_last = True

                            # * no double input
                            alr_pressed = True

                            # * move tail down
                            self.snake.move_snake_down()


                    elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                        if not self.k_right_last:
                            # * DOWN key pressed last
                            self.down_key_reset()
                            self.k_left_last = True

                            # * no double input
                            alr_pressed = True

                            # * move tail down
                            self.snake.move_snake_left()


                    elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                        if not self.k_left_last:
                            # * DOWN key pressed last
                            self.down_key_reset()
                            self.k_right_last = True

                            # * no double input
                            alr_pressed = True

                            # * move tail down
                            self.snake.move_snake_right()


            # * Make the snake move in the direction of last press
            if self.k_down_last == True and alr_pressed == False:
                self.snake.move_snake_down()

            elif self.k_up_last == True and alr_pressed == False:
                self.snake.move_snake_up()

            elif self.k_right_last == True and alr_pressed == False:
                self.snake.move_snake_right()

            elif self.k_left_last == True and alr_pressed == False:
                self.snake.move_snake_left()

            pygame.display.update()

            # * collision check, if failed. send to start screen
            if not self.snake.vert_bound_check():
                self.game_reset()
            if not self.snake.hor_bound_check():
                self.game_reset()
            if not self.snake.self_hit_check():
                self.game_reset()
            self.game.apple_collision()



main()
