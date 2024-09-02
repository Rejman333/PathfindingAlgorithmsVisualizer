import pygame
from math import gcd

SCREEN_WIDTH, SCREEN_HEIGHT = WINDOW_SIZE = (1280, 720)

GRID_COLOR = (0, 0, 0)
line_width = 3

pygame.init()


def draw_menu(screen):
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(960, 40, 240, 640))



def draw(screen):
    draw_menu(screen)


def main():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    grid_image = pygame.Surface((880, 640))
    print(type(screen))
    clock = pygame.time.Clock()
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("gray")
        # draw(screen)
        grid_image.fill("white")
        screen.blit(grid_image,(40,40))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
