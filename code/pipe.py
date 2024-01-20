import pygame
class Pipe(pygame.sprite.Sprite):
    def __init__(self,screen,x,y,position):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("assets/img/pipe.png")
        self.rect = self.image.get_rect()
        pipe_gap = 150
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]
    def update(self):
        scroll_speed = 4
        self.rect.x -= scroll_speed
        if self.rect.right < 100:
            self.kill()