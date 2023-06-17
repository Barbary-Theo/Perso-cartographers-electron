from model.cell import Cell


class Map:

    def __init__(self, nb_rows: int = 1, nb_cols: int = 1, cells=None):
        if cells is None:
            cells = [[Cell()]]
        self.nb_rows = nb_rows
        self.nb_cols = nb_cols
        self.cells = cells

    def print(self):
        print("", end="\t")
        for index_col in range(self.nb_cols):
            print(" "*5 + str(index_col), end=" "*4)
        print()
        print("", end="\t")
        for index_col in range(self.nb_cols):
            print((" " if index_col == 0 else "") + "_"*10 + " ", end="")
        print()
        for index_row, row in enumerate(self.cells):
            print(index_row, end="\t|")
            for index_col, cell in enumerate(row):
                padding = " " if not ((8 - len(str(cell))) / 2).is_integer() else ""
                print(" " + " "*((8 - len(str(cell))) // 2) + str(cell) + " " + " "*((8 - len(str(cell))) // 2) + padding, end="|")
            print()