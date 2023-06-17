from model.cell_type import CellType


class Cell:

    def __init__(self, x: int = 0, y: int = 0, cell_type: CellType = CellType.EMPTY):
        self.x = x
        self.y = y
        self.cell_type = cell_type

    def __str__(self):
        return self.cell_type.value
