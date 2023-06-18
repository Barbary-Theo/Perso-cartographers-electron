import numpy
from model.cell import Cell
from model.cell_type import CellType


class Map:

    def __init__(self, nb_rows: int = 1, nb_cols: int = 1, cells=None):
        if cells is None:
            cells = [[Cell()]]
        self.nb_rows = nb_rows
        self.nb_cols = nb_cols
        self.cells = cells

    def print(self):
        print("", end="    ")
        for index_col in range(self.nb_cols):
            print(" "*5 + str(index_col), end=" "*5)
        print()
        print("", end="    ")
        for index_col in range(self.nb_cols):
            print((" " if index_col == 0 else "") + "_"*10 + " ", end="")
        print()
        for index_row, row in enumerate(self.cells):
            print(index_row, end="   |")
            for index_col, cell in enumerate(row):
                padding = " " if not ((8 - len(str(cell))) / 2).is_integer() else ""
                print(" " + " "*((8 - len(str(cell))) // 2) + str(cell) + " " + " "*((8 - len(str(cell))) // 2) + padding, end="|")
            print()

    def change_cell_type(self, x: int, y: int, cell_type: CellType):
        cell = self.cells[y][x]
        print(cell)
        print(cell.x, " ", cell.y)
        self.cells[y][x].change_cell_type(cell_type)

    @staticmethod
    def rotate_cells(cells: list):
        return numpy.rot90(cells)

    def put_cells_on_map(self, x: int, y: int, cells: list):
        is_possible_to_put_cells = True

        for index_row, row in enumerate(cells):
            for index_col, cell_to_put in enumerate(row):
                is_possible_to_put_cells = self.is_possible_to_put_cells(x, y, index_row, index_col, cell_to_put, is_possible_to_put_cells)

        if is_possible_to_put_cells:
            for index_row, row in enumerate(cells):
                for index_col, cell_to_put in enumerate(row):
                    if cell_to_put.cell_type!= CellType.EMPTY:
                        self.cells[index_row + y][index_col + x] = Cell(index_col + x, index_row + y, cell_to_put.cell_type)

        return is_possible_to_put_cells

    def is_possible_to_put_cells(self, x: int, y: int, index_row: int, index_col: int, cell_to_put: Cell, is_possible_to_put_cell: bool):
        try:
            cell_map = self.cells[index_row + y][index_col + x]
            if cell_map.cell_type != CellType.EMPTY and cell_to_put.cell_type != CellType.EMPTY:
                return False
        except IndexError:
            return False
        return is_possible_to_put_cell if is_possible_to_put_cell else False