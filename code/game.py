import pygame
import random

class DrawGame:
    def __init__(self, screen):
        self.screen = screen 
        self.ground_move = 0
        self.pipe_move = 0  
        self.move_speed = 4
        self.bg_image = pygame.image.load("assets/img/bg.png")
        self.ground = pygame.image.load("assets/img/ground.png")
        
        
    def draw_background(self):
        self.screen.blit(self.bg_image, (0, 0))

    def draw_ground(self):
        self.screen.blit(self.ground, (self.ground_move, 530))

    def draw_pipe(self, pipe):
        self.screen.blit(pipe.image, (pipe.rect.x + self.pipe_move, pipe.rect.y))
        
        
    def update_ground(self):
        self.ground_move -= self.move_speed
        if abs(self.ground_move) > 35:
            self.ground_move = 0
