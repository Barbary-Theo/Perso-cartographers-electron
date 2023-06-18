from model.map import Map
from model.cell_type import CellType
from model.cell import Cell


test_cell = [
    [Cell(0, 0, CellType.FOREST), Cell(1, 0, CellType.EMPTY), Cell(2, 0, CellType.MOUNTAIN)],
    [Cell(0, 1, CellType.MONSTER), Cell(1, 1, CellType.HOUSE), Cell(2, 1, CellType.EMPTY)],
    [Cell(0, 2, CellType.WATER), Cell(1, 2, CellType.TEMPLE), Cell(2, 2, CellType.MONSTER)]
]

test_cell_to_put = [
    [Cell(0, 0, CellType.EMPTY), Cell(1, 0, CellType.HOUSE)],
    [Cell(0, 1, CellType.HOUSE), Cell(1, 1, CellType.EMPTY)]
]


def main():
    map = Map(3, 3, test_cell)
    map.print()
    map.put_cells_on_map(1, 0, Map.rotate_cells(test_cell_to_put))
    map.print()


if __name__ == '__main__':
    main()
