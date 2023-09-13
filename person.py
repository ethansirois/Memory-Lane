import pygame


class Person(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.shift = 0
        self.direction = 0
        self.speed = 10
        self.person_stand = pygame.image.load('graphics/person_stand.png').convert_alpha()
        self.person_walk_1 = pygame.image.load('graphics/person_walk1.png').convert_alpha()
        self.person_walk_2 = pygame.image.load('graphics/person_walk2.png').convert_alpha()
        self.person_reverse_1 = pygame.image.load('graphics/person_reverse1.png').convert_alpha()
        self.person_reverse_2 = pygame.image.load('graphics/person_reverse2.png').convert_alpha()
        self.person_walk = [self.person_walk_1, self.person_walk_2]
        self.person_reverse = [self.person_reverse_1, self.person_reverse_2]
        self.animation_index = 0
        self.image = self.person_stand
        self.rect = self.image.get_rect(midbottom=(425, 700))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction = 1
        elif keys[pygame.K_LEFT]:
            self.direction = -1
        else:
            self.direction = 0

    def move(self):
        movement = self.direction * self.speed
        if 352 < movement + self.rect.centerx < 1152:
            self.rect.x += movement
        else:
            self.shift -= movement
        if self.shift >= 120:
            self.shift = 120
        elif self.shift <= -50000:
            self.shift = -50000

    def player_animation(self):
        if self.direction == -1:
            self.animation_index += 0.1
            if int(self.animation_index) >= 2:
                self.animation_index = 0
            self.image = self.person_reverse[int(self.animation_index)]
        elif self.direction == 1:
            self.animation_index += 0.1
            if int(self.animation_index) >= 2:
                self.animation_index = 0
            self.image = self.person_walk[int(self.animation_index)]
        else:
            self.image = self.person_stand

    def update(self):
        self.player_input()
        self.move()
        self.player_animation()


