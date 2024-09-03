import pygame
from pygame.locals import *
import random

pygame.init()

die_sound = pygame.mixer.Sound('sounds/die.wav')
hit_sound = pygame.mixer.Sound('sounds/hit.wav')
point_sound = pygame.mixer.Sound('sounds/point.wav')
wing_sound = pygame.mixer.Sound('sounds/wing.wav')

clock = pygame.time.Clock()
fps = 60

screen_width = 665
screen_height = 735

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

font = pygame.font.Font('ArcadeClassic.ttf', 60)
white = (255, 255, 255)

background = pygame.image.load('img/bg.png')
background = pygame.transform.scale(background, (screen_width, screen_height))
ground_image = pygame.image.load('img/ground.png')
button_image = pygame.image.load('img/restart.png')
game_over_image = pygame.image.load('img/gameover.png')
message = pygame.image.load('img/message.png')
message = pygame.transform.scale(message, (int(message.get_width() * 1.2), int(message.get_height() * 1.2)))

ground_scroll = 0
scrolling_speed = 4
flying = False
pipe_gap = 150
pipe_freq = 1500
last_pipe = pygame.time.get_ticks() - pipe_freq
score = 0
pass_pipe = False
game_over = False
show_message = True
sound_played = False

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'img/bird{num}.png')
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):
        if flying:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 625:
                self.rect.y += int(self.vel)

        if not game_over:
            keys = pygame.key.get_pressed()
            if (pygame.mouse.get_pressed()[0] == 1 or keys[K_SPACE]) and not self.clicked:
                self.clicked = True
                self.vel = -10
                if not game_over:
                    wing_sound.play()
            if pygame.mouse.get_pressed()[0] == 0 and not keys[K_SPACE]:
                self.clicked = False

            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/pipe.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height()))
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    def update(self):
        self.rect.x -= scrolling_speed
        if self.rect.right < 0:
            self.kill()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return self.check_click()

    def check_click(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        return action

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))
bird_group.add(flappy)

button = Button(screen_width // 2 - 50, screen_height // 2 + 75, button_image)

run = True
while run:
    clock.tick(fps)

    screen.blit(background, (0, 0))
    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)
    screen.blit(ground_image, (ground_scroll, 600))

    if not flying and not game_over and show_message:
        screen.blit(message, (screen_width // 2 - message.get_width() // 2, screen_height // 2 - message.get_height() // 2))

    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                point_sound.play()
                pass_pipe = False

    draw_text(str(score), font, white, int(screen_width / 2), 20)

    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True
        if not sound_played:
            hit_sound.play()
            die_sound.play()
            sound_played = True

    if flappy.rect.bottom >= 590:
        game_over = True
        flying = False
        if not sound_played:
            die_sound.play()
            sound_played = True

    if not game_over and flying:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_freq:
            pipe_height = random.randint(-100, 100)
            bottom_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
            upper_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
            pipe_group.add(bottom_pipe)
            pipe_group.add(upper_pipe)
            last_pipe = time_now

        ground_scroll -= scrolling_speed
        if abs(ground_scroll) > ground_image.get_width():
            ground_scroll = 0
        screen.blit(ground_image, (ground_scroll + ground_image.get_width(), 600))
        if abs(ground_scroll) > 35:
            ground_scroll = 0

        pipe_group.update()

    if game_over:
        screen.blit(game_over_image, (screen_width // 2 - game_over_image.get_width() // 2, screen_height // 2 - 180))
        if button.draw():
            game_over = False
            score = 0
            pipe_group.empty()
            flappy.rect.center = (100, int(screen_height / 2))
            flappy.vel = 0
            flying = False
            show_message = True
            sound_played = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN and event.key == K_SPACE) and flying == False and game_over == False:
            flying = True
            show_message = False

    pygame.display.update()

pygame.quit()