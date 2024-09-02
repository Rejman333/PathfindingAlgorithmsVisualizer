import pygame
from math import gcd
SCREEN_WIDTH, SCREEN_HEIGHT = WINDOW_SIZE = (1280, 720)

GRID_COLOR = (0, 0, 0)
line_width = 3

pygame.init()
WORLD_MAP = \
    [
        ["", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", ""],
    ]


def draw_world_map_grid(screen, map_height, map_width, offset_width, offset_height):
    tile_size = gcd(map_height, map_width)
    # draw vertical lines
    for x in range(tile_size, map_width, tile_size):
        pygame.draw.line(screen, GRID_COLOR,
                         (x + offset_width, offset_height),
                         (x + offset_width, map_height + offset_height - 1),
                         line_width)
    # draw horizontal lines
    for y in range(tile_size, map_height, tile_size):
        pygame.draw.line(screen, GRID_COLOR,
                         (offset_width, y + offset_height),
                         (map_width + offset_width - 1, y + offset_height),
                         line_width)


def draw_menu(screen):
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(960, 40, 240, 680))


def draw_world_map_bg(screen):
    offset_wight = 40
    offset_height = 40
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(offset_wight, offset_height, 880, 640))
    pygame.draw.rect(screen, GRID_COLOR, pygame.Rect(offset_wight, offset_height, 880, 640), line_width)
    draw_world_map_grid(screen, 640, 880, offset_wight, offset_height)


def draw(screen):
    draw_menu(screen)
    draw_world_map_bg(screen)


def main():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("gray")
        draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
