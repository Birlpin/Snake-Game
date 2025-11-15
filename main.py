import starterscreen
import pygame
class main():
    def __init__(self):
        pygame.init()

        window_x =720
        window_y = 500

        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((window_x, window_y))

        main.run(self)

    def run(self):

        run = True
        instart = True
        while run:

            if instart:
                starterscreen.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pass

            pygame.display.update()
            self.clock.tick(30)

main()
