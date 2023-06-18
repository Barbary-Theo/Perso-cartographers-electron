from model.map import Map
from model.cell import Cell
from model.cell_type import CellType


class Player:

    def __init__(self, name: str, description: str, player_map: Map = None):
        if map is None:
            player_map = Map()
        self.name = name
        self.description = description
        self.player_map = player_map

    def print_map(self):
        self.player_map.print()

    def init_map(self):
        player_map = Map(nb_rows = 11, nb_cols = 11)
        cells = []
        for index_row in range(11):
            row = []
            for index_col in range(11):
                row.append(Cell(x = index_row, y = index_col))
            cells.append(row)

        indexes_of_mountain = [{"x": 3, "y": 1}, {"x": 8, "y": 2},  {"x": 5, "y": 5}, {"x": 2, "y": 8}, {"x": 7, "y": 9}]
        indexes_of_temple = [{"x": 1, "y": 2}, {"x": 5, "y": 1},  {"x": 9, "y": 2}, {"x": 1, "y": 8}, {"x": 5, "y": 9}, {"x": 9, "y": 8}]
        for indexes in indexes_of_mountain:
            cells[indexes.get("y")][indexes.get("x")] = Cell(indexes.get("x"), indexes.get("y"), CellType.MOUNTAIN)
        for indexes in indexes_of_temple:
            cells[indexes.get("y")][indexes.get("x")] = Cell(indexes.get("x"), indexes.get("y"), CellType.TEMPLE)

        player_map.cells = cells
        self.player_map = player_map
