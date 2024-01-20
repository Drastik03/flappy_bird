import random
import pygame
import pygame.mixer
from code.bird import Bird
from code.game import DrawGame
from code.pipe import Pipe
from code.start import Button

class Windows:
    def __init__(self):
        self.initComponents()

    def initComponents(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Flappy bird")
        self.max_width = 650
        self.max_height = 640
        self.score = 0
        self.screen = pygame.display.set_mode((self.max_width, self.max_height))  
        self.clock = pygame.time.Clock()
        self.game_drawer = DrawGame(self.screen)  
        self.bird_group = pygame.sprite.Group()
        self.pip_group = pygame.sprite.Group()
        self.flappy = Bird(self.screen, 90, int(self.max_height / 2))
        self.bird_group.add(self.flappy)

        # Inicializar variables de score y paso de tubería
        self.score = 0
        self.pass_pipe = False

        # Inicializar sonido de aleteo y colisión
        self.collision_sound = pygame.mixer.Sound("assets/audio/collision_sound.wav")
        self.score_sound = pygame.mixer.Sound("assets/audio/point.wav")

        # Variables para controlar la repetición de sonidos
        self.collision_sound_played = False

        self.run_game()

    def run_game(self):
        run = True
        self.restart = pygame.image.load("assets/img/restart.png")
        self.screen.blit(self.restart, (100, 530))
        self.button = Button(self.screen, self.max_width // 2 - 50, self.max_height // 2 - 100, self.restart)

        self.last_pipe = pygame.time.get_ticks()
        self.pipe_frequency = 1500  

        while run:
            self.clock.tick(60)
            if self.pip_group:
                bird_rect = self.bird_group.sprites()[0].rect
                pipe_rect = self.pip_group.sprites()[0].rect

                if bird_rect.left > pipe_rect.left and bird_rect.right < pipe_rect.right and not self.pass_pipe:
                    self.pass_pipe = True

                if self.pass_pipe and bird_rect.right > pipe_rect.right:
                    self.score += 1
                    self.score_sound.play()
                    self.pass_pipe = False
                    print(str(self.score))
                font = pygame.font.SysFont('Bauhaus 93', 60)
                white = (255, 255, 255)
                self.draw_text(str(self.score), font, white, int(self.max_width / 2), 20)

            # Colisiones
            if pygame.sprite.groupcollide(self.bird_group, self.pip_group, False, False) or self.flappy.rect.top < 0:
                self.flappy.game_over = True
                if not self.collision_sound_played:
                    self.collision_sound.play()
                    self.collision_sound_played = True
            if self.flappy.rect.bottom >= 530:
                self.flappy.game_over = True
                self.flappy.flying = False
                if not self.collision_sound_played:
                    self.collision_sound.play()
                    self.collision_sound_played = True
            if not self.flappy.game_over and self.flappy.flying:
                time_now = pygame.time.get_ticks()
                if time_now - self.last_pipe > self.pipe_frequency:
                    pipe_height = random.randint(-100, 100)
                    btm_pipe = Pipe(self.screen, self.max_width, int(self.max_width / 2) + pipe_height, position=-1)
                    top_pipe = Pipe(self.screen, self.max_width, int(self.max_height / 2) + pipe_height, position=1)
                    self.pip_group.add(top_pipe)
                    self.pip_group.add(btm_pipe)
                    self.last_pipe = time_now




            if self.flappy.game_over == True:
                if self.button.draw_button() == True:
                    self.flappy.game_over = False
                    self.score = self.reset_game()
                    self.collision_sound_played = False


            if not self.flappy.game_over:
                self.game_drawer.update_ground()
                self.game_drawer.draw_background()
                self.game_drawer.draw_ground()

                for pipe in self.pip_group.sprites():
                    self.game_drawer.draw_pipe(pipe)
                self.pip_group.update()

                self.bird_group.update() 
                self.bird_group.draw(self.screen)

                self.flappy.update_bird()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and not self.flappy.flying and not self.flappy.game_over:
                    self.flappy.flying = True

            # Actualizar pantalla
            pygame.display.update()

        pygame.quit()

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x - img.get_width() / 2, y - img.get_height() / 2))

    def reset_game(self):
        self.pip_group.empty()
        self.flappy.rect.x = 100
        self.flappy.rect.y = int(self.max_height / 2)
        self.score = 0
        return self.score