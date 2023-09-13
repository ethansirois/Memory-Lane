import pygame
# import tkinter.filedialog
import os
from PIL import Image
from sys import exit
from person import Person
from image import Photo
from group import Group
import photo_resize


pygame.init()
screen = pygame.display.set_mode((1504, 800))
pygame.display.set_caption('Memory Lane')
clock = pygame.time.Clock()
photo_select = True



# person
player = pygame.sprite.GroupSingle()
person = Person()
player.add(person)

# images
vis_image_group = pygame.sprite.Group()
images = []
groups = []
groups_left_pos = []
closest_group = 1
next_timer = pygame.USEREVENT + 1
pygame.time.set_timer(next_timer, 200)

# all static surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
memory_lane = pygame.image.load('graphics/memory_lane.png').convert()
add_image_surface = pygame.image.load('graphics/add_image.png').convert()
add_image_rect = add_image_surface.get_rect(topleft=(0, 0))
end_surf = pygame.Surface((1504, 800))
end_surf.fill((255, 255, 255))


def draw_bg(pos):
    screen.blit(sky_surface, (-1504 + (pos % 1504), 0))
    screen.blit(sky_surface, (pos % 1504, 0))
    screen.blit(ground_surface, (-1504 + (pos % 1504), 700))
    screen.blit(ground_surface, (pos % 1504, 700))
    if pos >= -300:
        screen.blit(memory_lane, (pos, 500))


def update_vis(pos):
    global closest_group
    prev_closest = closest_group
    if abs(groups_left_pos[closest_group] + pos) > abs(groups_left_pos[closest_group + 1] + pos):
        closest_group += 1
        if closest_group > len(groups_left_pos) - 2:
            closest_group = len(groups_left_pos) - 2
        else:
            vis_image_group.remove(groups[closest_group - 2])
            groups[closest_group + 1].display(vis_image_group)
    if abs(groups_left_pos[closest_group] + pos) > abs(groups_left_pos[closest_group - 1] + pos):
        closest_group -= 1
        if closest_group < 1:
            closest_group = 1
        else:
            vis_image_group.remove(groups[closest_group + 2])
            groups[closest_group - 1].display(vis_image_group)

    for image in vis_image_group:
        image.update_x(pos)


def load_images(folder):
    old_dir = os.getcwd()
    new_image_path = photo_resize.resize_photos(folder)
    os.chdir(old_dir)
    for f in os.listdir(new_image_path):
        group = Group()
        if os.path.isdir(new_image_path + '/' + f):
            for image in os.listdir(new_image_path + '/' + f):
                group.add(Photo(new_image_path + '/' + f + '/' + image))
            groups.append(group)
        else:
            group.add(Photo(new_image_path + '/' + f))
            groups.append(group)


def set_images():
    groups_left_pos.append(groups[0].images[0].rect.left)
    groups[0].setup_next()
    for i in range(1, len(groups)):
        new_left = groups[i - 1].images[0].get_right() + 300
        for image in groups[i].images:
            image.set_x(new_left)
        groups_left_pos.append(new_left)
        groups[i].setup_next()
    for ind in range(3):
        groups[ind].display(vis_image_group)


def display_previews():
    #for i in range(len(groups)):
    #    image = groups[i][0]
    #    screen.blit(pygame.transform.scale_by(image.image, 0.125), (i % 15 * 100, i / 15))
    screen.blit(add_image_surface, add_image_rect.topleft)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif not photo_select:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                for ind in range(3):
                    if groups[closest_group + ind - 1].next.rect.collidepoint(mouse_pos):
                        groups[closest_group + ind - 1].get_next(vis_image_group)
                        groups[closest_group + ind - 1].display(vis_image_group)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    person.speed = 3 * 1
                if event.key == pygame.K_2:
                    person.speed = 3 * 2
                if event.key == pygame.K_3:
                    person.speed = 3 * 3
                if event.key == pygame.K_4:
                    person.speed = 3 * 4
                if event.key == pygame.K_5:
                    person.speed = 3 * 5
                if event.key == pygame.K_6:
                    person.speed = 3 * 8
                if event.key == pygame.K_7:
                    person.speed = 3 * 10
                if event.key == pygame.K_8:
                    person.speed = 3 * 15
                if event.key == pygame.K_9:
                    person.speed = 3 * 20
                if event.key == pygame.K_0:
                    person.speed = 3 * 30

    if photo_select:
        screen.fill((249, 249, 249))
        display_previews()
        mouse_pos = pygame.mouse.get_pos()
        if add_image_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            # /Users/ethansirois/Desktop/Memory Lane/graphics/memory_lane_photos
            image_folder = "/Users/ethansirois/Desktop/Memory Lane/graphics/memory_lane_photos"     # input()
            load_images(image_folder)
            set_images()
            photo_select = False

    else:
        shift = person.shift
        draw_bg(shift)

        update_vis(shift)
        vis_image_group.draw(screen)

        player.draw(screen)
        player.update()

        if -shift > groups_left_pos[-1]:
            end_surf.set_alpha(min(abs((groups_left_pos[-1] + shift) / 10), 255))       # (groups_left_pos[-1] + 700 + shift) / 10)
            screen.blit(end_surf, (0, 0))

    pygame.display.update()
    clock.tick(60)
