from model.map import Map
from model.cell_type import CellType
from model.cell import Cell


def main():
    cells = [
        [Cell(0, 0,CellType.FOREST), Cell(1, 0, CellType.MOUNTAIN), Cell(2, 0, CellType.MOUNTAIN)],
        [Cell(0, 1,CellType.MONSTER), Cell(1, 1, CellType.HOUSE), Cell(2, 1, CellType.MOUNTAIN)],
        [Cell(0, 2,CellType.WATER), Cell(1, 2, CellType.TEMPLE), Cell(2, 2, CellType.MONSTER)]
    ]
    map = Map(3, 3, cells)
    map.print()


if __name__ == '__main__':
    main()
