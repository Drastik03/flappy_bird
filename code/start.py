import pygame
class Button:
    def __init__(self, screen, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen = screen
        
    def draw_button(self):
        self.action = False
        self.position = pygame.mouse.get_pos()
        if self.rect.collidepoint(self.position):
            if pygame.mouse.get_pressed()[0] == 1:
                self.action = True

        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        return self.action