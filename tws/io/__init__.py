class InputParser:
    def __init__(self, i):
        self.elements = i.strip().split("\n")

    def parse(self):
        grid_dimensions = tuple(e for e in self.elements.pop(0).split())
        instructions = [(e, e1) for e, e1 in zip(self.elements[::2], self.elements[1::2])]

        return grid_dimensions, instructions
