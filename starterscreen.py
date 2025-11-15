import pygame

class start():
    def __init__(self):
        self.startin = True
        self.startbutton = pygame.Rect((720//2-50, 500//2-50), (720//2+50, 500//2+50))
        self.exitbutton = pygame.Rect((720//2+100, 500//2+100), (720//2+50+150, 500//2+50+150))
        self.startingbackground = pygame.image.load("img/snake.xcf")
        self.startingbackground = pygame.transform.scale(self.startingbackground, (1200, 800))

    def draw_screen(self, window):
        self.logo = window.blit(start().startingbackground, (-240, -300))
        pygame.draw.rect(window, (255, 255,255), (720//2-150, 500/2-50, 300, 100))
        pygame.draw.rect(window, (255,255,255), (720//2-150, 500//2+100, 300, 100))


    def click_coll(self):
        pass
        #self.startbutton.collidepoint()
