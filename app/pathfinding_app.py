import pygame as pg
from math import gcd

pg.init()


class PathfindingApp:
    def __init__(self, app_name):
        self.name = app_name
        self.fps = 60
        self.width = 1280
        self.height = 720
        self.size = [self.width, self.height]
        self.clock = pg.time.Clock()
        self.main_screen = pg.display.set_mode(self.size)
        self.map_screen = pg.Surface((880, 640))
        self.ui_screen = pg.Surface((280, 640))

        self.cell_size = gcd(self.width, self.height)
        self.cell_border_width = 4
        self.width_in_cells = self.map_screen.get_width() // self.cell_size
        self.height_in_cells = self.map_screen.get_height() // self.cell_size

        self.map = self.height_in_cells * [self.width_in_cells * [" "]]

        self.running = False

        pg.display.set_caption(self.name)

    def _process_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def _draw(self):
        self.main_screen.fill("dark gray")
        self.ui_screen.fill("gray")
        self.map_screen.get_width() + self.cell_border_width

        self._draw_map_screen()
        self.main_screen.blit(self.map_screen, (40, 40))
        self.main_screen.blit(self.ui_screen, (80 + 880, 40))

        pg.display.flip()

    def _draw_map_screen(self):
        self.map_screen.fill("black")
        edited_cell_size = self.cell_size - self.cell_border_width
        margin = self.cell_border_width
        full_size = edited_cell_size + margin

        for row, _ in enumerate(self.map):
            for col, cell in enumerate(self.map[row]):
                pg.draw.rect(self.map_screen, (255, 255, 255),
                             pg.Rect(
                                 full_size * col + margin/2,
                                 full_size * row + margin/2,
                                 edited_cell_size,
                                 edited_cell_size))

    def run(self):
        if self.running:
            Exception(f"App: {self.name} is already running!")

        self.running = True
        while self.running:
            self._process_events()
            self._draw()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    app = PathfindingApp("Pathfinding App")
    app.run()
    print(len(app.map), len(app.map[0]))
