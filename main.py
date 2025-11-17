import game
import starterscreen
import pygame

class main():
    def __init__(self):
        pygame.init()

        window_x =720
        window_y = 500

        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((window_x, window_y))

        # init the start class
        self.start = starterscreen.start()
        self.gaming = game.game().gaming

        main.run(self)


    def run(self):

        run = True
        while run:

            # starter screen draw
            if self.start.startin == True:
                self.start.draw_screen(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                # IF in title screen
                if self.start.startin == True:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        click_pos = pygame.mouse.get_pos()

                        if self.start.startbutton.collidepoint((click_pos)):
                            self.start.startin = False
                            self.gaming = True

            pygame.display.update()
            self.clock.tick(30)

main()
