import pygame


class Photo(pygame.sprite.Sprite):
    def __init__(self, file):
        super().__init__()
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(midleft=(750, 325))
        self.og_left = self.rect.left

    def get_right(self):
        return self.rect.right

    def set_x(self, x):
        self.rect.left = x
        self.og_left = x

    def update_x(self, shift):
        self.rect.left = self.og_left + shift

    def __lt__(self, other):
        return self.rect.right - self.rect.left < other.rect.right - other.rect.left

    def __ge__(self, other):
        return self.rect.right - self.rect.left >= other.rect.right - other.rect.left

