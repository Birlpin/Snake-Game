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
        self.window.fill((6,63,62))

        # init the start class
        self.start = starterscreen.start()
        self.game = game.game()


        main.run(self)


    def run(self):

        run = True
        while run:

            # starter screen draw
            if self.start.startin == True:
                self.start.draw_screen(self.window)

            # game start
            if self.game.gaming == True:
                if not self.game.apple_exi:
                    self.game.add_apple()
                    self.game.apple_exi = True
                self.game.draw_board(self.window, self.window_x, self.window_y)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                # IF in title screen
                if self.start.startin == True:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        click_pos = pygame.mouse.get_pos()

                        if self.start.startbutton.collidepoint(click_pos):
                            self.start.startin = False
                            self.game.gaming = True

            pygame.display.update()
            self.clock.tick(30)

main()
