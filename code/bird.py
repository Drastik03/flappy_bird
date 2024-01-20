import pygame
class Bird(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.index = 0
        self.counter = 0
        self.images = []
        self.vel = 0
        self.flying = False
        self.game_over = False
        self.clicked = False
        self.flap_cooldown = 2
        self.last_flap_time = 0  
        self.flap_sound = pygame.mixer.Sound("assets/audio/FlappyBird_audio_wing.wav")

        for num in range(1, 4):
            self.img = pygame.transform.scale(pygame.image.load(f'assets/img/bird{num}.png'), (30, 60))
            self.images.append(self.img)
        self.image = self.images[self.index]
        self.rect = self.img.get_rect()
        self.rect.center = [x, y]

    def update_bird(self):
        if self.flying == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 530:
                self.rect.y += int(self.vel)

        if self.game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
                current_time = pygame.time.get_ticks()
                self.flap_sound.play()  
                
                if current_time - self.last_flap_time > self.flap_cooldown * 1000:
                    self.flap_sound.play()  
                    self.last_flap_time = current_time 

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                self.counter += 1
                self.flap_cooldown = 5
                self.last_flap_time = 0 
            if self.counter > self.flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -1)

        else:
            self.image = pygame.transform.rotate(self.images[self.index], -70)