import pygame
from image import Photo


class Group:
    def __init__(self):
        self.images = []
        self.i = 0
        self.next = Photo('graphics/next.png')
        self.is_burst = False

    def add(self, image):
        if len(self.images) > 0:
            self.is_burst = True
        self.images.append(image)

    def setup_next(self):
        self.max_first()
        self.next.set_x(self.images[0].rect.left - 150)

    def get_next(self, vis_image_group):
        vis_image_group.remove(self.images[self.i])
        self.i += 1
        if self.i == len(self.images):
            self.i = 0
        vis_image_group.add(self.images[self.i])

    def display(self, vis_image_group):
        vis_image_group.add(self.images[self.i])
        if self.is_burst:
            vis_image_group.add(self.next)

    def max_first(self):
        max_pos = 0
        for i in range(1, len(self.images)):
            if self.images[i] >= self.images[max_pos]:
                max_pos = i
        temp = self.images[0]
        self.images[0] = self.images[max_pos]
        self.images[max_pos] = temp
