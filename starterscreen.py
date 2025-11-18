import pygame

class start():
    def __init__(self):
        self.startin = True
        self.startbutton = pygame.Rect((720//2-150, 500//2-50), (720//2+150, 500//2+50))
        self.exitbutton = pygame.Rect((720//2-150, 500//2+100), (720//2+150, 500//2+200))
        self.startingbackground = pygame.image.load("img/snake.xcf")
        self.startingbackground = pygame.transform.scale(self.startingbackground, (1200, 800))

    def draw_screen(self, window):
        # drawing rectangles for the title screen
        self.logo = window.blit(start().startingbackground, (-240, -300))
        pygame.draw.rect(window, (127, 181,48), (720//2-150, 500//2-50, 300, 100))
        pygame.draw.rect(window, (127,181,48), (720//2-150, 500//2+100, 300, 100))

        # text on screen
        text_font = pygame.font.SysFont("Arial", 75)
        play_text = text_font.render("Play", True, (128,128,128))
        window.blit(play_text, (720//2 - 50, 720//2 - 50))



    def click_coll(self):
        pass
        #self.startbutton.collidepoint()
