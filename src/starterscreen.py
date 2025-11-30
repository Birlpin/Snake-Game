import pygame

class start():
    def __init__(self):
        self.startin = True
        self.start_button = pygame.Rect((720//2)-150, (500//2)-50, 300, 100)
        self.exit_button = pygame.Rect(720//2-150, 500//2+100, 300, 100)
        self.starting_background = pygame.image.load("img/snake.xcf")
        self.starting_background = pygame.transform.scale(self.starting_background, (1200, 800))
        with open("top_score", "r") as file:
            self.score = file.read()

    def game_over(self):
        self.startin = True

    def change_high_score(self):
        pass

    def draw_screen(self, window):
        # drawing rectangles for the title screen
        self.logo = window.blit(start().starting_background, (-240, -300))
        pygame.draw.rect(window, (127, 181,48), (720//2-150, 500//2-50, 300, 100))
        pygame.draw.rect(window, (127,181,48), (720//2-150, 500//2+100, 300, 100))

        # text on screen
        text_font = pygame.font.SysFont("Arial", 85)
        play_text = text_font.render("Play", True, (0,0,0))
        exit_text = text_font.render("Exit", True, (0,0,0))
        score_text = text_font.render("Score:"+self.score, True, (128, 128, 128))
        score = text_font.render(self.score, False, (128,128,128))
        window.blit(play_text, (720//2 - 80, 500//2 - 50))
        window.blit(exit_text, (720//2 - 75, 500//2 + 100, 10, 10))
        window.blit(score_text, (720//2 - 175, 500//2 + 225))

