def drawRect(fromX, fromY, width, height, content, map):
    for w in range(width):
        for h in range(height):
            x = fromX + w
            y = fromY + h

            map.setCell(x, y, content)

def drawHorizontalLine(fromX, toX, y, content, map):
    """from x1 to x2 both inclusive
       drawHorizontalLine(1, 5, 0, "X") -> .XXXXX """

    distance = abs(fromX - toX)
    if fromX > toX:
        direction = 1
    else:
        direction = -1
    for x in range(fromX, toX + 1):
        map.setCell(x, y, content)

def drawVerticalLine(fromY, toY, x, content, map):
    """from y1 to y2 both inclusive"""
    for y in range(fromY, toY + 1):
        map.setCell(x, y, content)
