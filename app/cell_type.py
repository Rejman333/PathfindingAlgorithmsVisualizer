from enum import Enum


class CellType(Enum):
    EMPTY = " "
    WALL = "#"
    START = "S"
    END = "E"
