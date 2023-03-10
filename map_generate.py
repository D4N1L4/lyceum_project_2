import pygame
import os
import sys
import random
from person import Person

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
clock = pygame.time.Clock()

scores = 1000  # баллы

rand_gen_for_patern = [random.randint(0, 9) for i in range(162)]
player = Person()
x_pers_g = player.x_coodr_person_osn
y_pers_g = player.y_coodr_person_osn


class Tree_class:  # это что, елка?
    def __init__(self, min_x_tree, max_x_tree, min_y_tree, max_y_tree):
        global x_pers_g, y_pers_g

        self.cal_tree_max = random.randint(70, 140)  # количество елок

        self.col_p_pl_11111 = 0
        Tree_class.col_proverka.col_p_pl = self.col_p_pl_11111

        self.min_x_tree = min_x_tree
        self.max_x_tree = max_x_tree
        self.min_y_tree = min_y_tree
        self.max_y_tree = max_y_tree

        self.speed_pers = player.speed_pers
        self.x_coord_person = player.x_coodr_person_osn
        self.y_coord_person = player.y_coodr_person_osn
        print(self.x_coord_person, self.y_coord_person)

    def tree(self, screen):
        # большой и разнообразный выбор
        tree_image = [pygame.image.load('image/low_settings/tree/el0001.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0002.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0003.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0004.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0005.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0006.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0007.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0008.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0009.png').convert_alpha(),
                      pygame.image.load('image/low_settings/tree/el0010.png').convert_alpha(),
                      ]

        self.cal_tree_now = 0
        self.tree_image_random_scale = []
        self.random_x_cooord = []
        self.random_y_cooord = []
        generation_of_trees = []

        self.num_el = 0
        while self.cal_tree_now < self.cal_tree_max:
            tree_image_random = tree_image[random.randint(0, 9)]
            a = random.randint(200, 270)
            self.tree_image_random_scale.append(
                pygame.transform.scale(tree_image_random, (a, a * 1.3)))  # рандомный размер елок

            proverka = 0
            while proverka == 0:
                random_x_cooord_1 = random.randint(-100, 1920)
                random_y_cooord_1 = random.randint(-100, 1080)

                if 570 < random_x_cooord_1 < 1220 and 150 < random_y_cooord_1 < 720:  # область для костра
                    proverka = 0
                else:
                    proverka = 1
                    self.random_x_cooord.append(random_x_cooord_1)
                    self.random_y_cooord.append(random_y_cooord_1)
                self.num_el += 1

            self.cal_tree_now += 1

    def render_tree(self):
        n = 0

        while n < self.cal_tree_max:
            screen.blit(self.tree_image_random_scale[n],
                        (self.random_x_cooord[n], self.random_y_cooord[n]))  # отрисовка ёлок
            n += 1

    def col_proverka(self, x, y, x_rect, y_rect):
        n = 0
        self.x_coord_person = x
        self.y_coord_person = y
        self.x_rect = x_rect
        self.y_rect = y_rect

        while n < self.cal_tree_max:
            print(self.x_coord_person, self.y_coord_person)
            pers_rect = pygame.Rect(self.x_rect, self.y_rect, 90, 90)
            el_rect = self.tree_image_random_scale[n].get_rect(
                topleft=(self.random_x_cooord[n], self.random_y_cooord[n]))

            if pygame.Rect.colliderect(pers_rect, el_rect):  # коллизия елки пересеккает персонажа то
                self.tree_image_random_scale.pop(n)  # вычеркиваем всё о этой ёлке из списка
                self.random_x_cooord.pop(n)
                self.random_y_cooord.pop(n)
                self.cal_tree_max -= 1
                self.col_p_pl_11111 = 1
                Tree_class.col_proverka.col_p_pl = self.col_p_pl_11111
                sound_of_taking()
                break
            n += 1


class Board:  # доска?
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        # картинки из которых делается выбор
        sp_ground = (pygame.image.load('image/low_settings/new_ground/ground0000.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0001.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0002.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0003.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0004.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0005.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0006.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0007.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0008.png').convert_alpha(),
                     pygame.image.load('image/low_settings/new_ground/ground0009.png').convert_alpha(),
                     )
        for y in range(self.height):
            for x in range(self.width):
                # случайно выбираем картинку
                img_ground = sp_ground[rand_gen_for_patern[y * 18 + x]]
                # подгоняем размеры
                self.small_img_ground = pygame.transform.scale(img_ground, (155, 155))
                # выстраиваем из них сетку
                screen.blit(self.small_img_ground, (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                                    self.cell_size, self.cell_size))


def sound_of_taking():
    take_s = pygame.mixer.Sound('other/sounds/take-throw.mp3')
    take_s.play()


def main():
    global which_way, scores, x_pers_g, y_pers_g
    which_way = 'down'
    speed_pers = 3

    screen = pygame.display.set_mode(size)
    number_while = 0
    number_event = 0
    number_clikov = 0

    board = Board(18, 9)
    # clouds = Clouds()

    board.set_view(0, 0, 150)
    treeeeee = Tree_class(0, 1920, 1080, 0)

    treeeeee.tree(screen)

    running = True
    pygame.init()

    run_gr = True
    while run_gr:
        treeeeee.tree(screen)
        run_gr = False
    while running:
        number_while += 1
        for event in pygame.event.get():
            number_event += 1
            if event.type == pygame.QUIT:
                running = False

            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_UP):
                y_pers_g -= speed_pers
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_DOWN):
                y_pers_g += speed_pers
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_LEFT):
                x_pers_g -= speed_pers
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_RIGHT):
                x_pers_g += speed_pers

            # что то на подобии ускорения, нужно допиливать
            if number_clikov > 10:
                speed_pers = 5
            else:
                speed_pers = 3
            if number_clikov > 17:
                number_clikov = 0

        board.render(screen)

        # clouds.render()
        treeeeee.render_tree()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
