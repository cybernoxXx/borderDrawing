def drawBorder(width, heigth):
    if width < 2 or heigth < 2:
        return None
    # range stop at end-1, i want to print exactly height lines
    for h in range(1, heigth+1):
        # first and last lines should be print different
        if h == 1 or h == heigth:
            print("+", end='')
            for w in range(2, width):
                print("-", end='')
            print("+")
        # print the other lines
        else:
            print("|", end='')
            for w in range(2, width):
                print(" ", end='')
            print("|")

drawBorder(16,4)