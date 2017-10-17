class MapDrawer():
    def __init__(self, map):
        self.map = map

    def drawRect(self, fromX, fromY, width, height, content):
        for w in range(width):
            for h in range(height):
                x = fromX + w
                y = fromY + h

                self.map.setCell(x, y, content)

    def drawHorizontalLine(self, fromX, toX, y, content):
        """from x1 to x2 both inclusive
           drawHorizontalLine(1, 5, 0, "X") -> .XXXXX """
        for x in range(fromX, toX + 1):
            self.map.setCell(x, y, content)

    def drawVerticalLine(self, fromY, toY, x, content):
        """from y1 to y2 both inclusive"""
        for y in range(fromY, toY + 1):
            self.map.setCell(x, y, content)
