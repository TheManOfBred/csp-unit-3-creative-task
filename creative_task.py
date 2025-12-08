from cmu_graphics import *
app.playerList = ['x', 'o']
app.playerIndex = 0
app.evilListIndex = 0
#evilList = [
 #   {'name': 1, 'full': False}, {'name': 2, 'full': False}, {'name': 3, 'full': False},
  #  {'name': 4, 'full': False}, {'name': 5, 'full': False}, {'name': 6, 'full': False},
   # {'name': 7, 'full': False}, {'name': 8, 'full': False}, {'name': 9, 'full': False}
    #]
# evilList = [
#     '1', '2', '3', 
#     '4', '5', '6',
#     '7', '8', '9'
#     ]
crosses = Group()
os = Group()
board = Group()
app.square1 = Rect(0, 0, 130, 130, fill = None, border = 'black', borderWidth = 1, visible = False)
app.square1.full = False
app.square1.symbol = None

app.square2 = Rect(130, 0, 140, 130, fill = None, border = 'black', borderWidth = 1, visible = False)
app.square2.full = False
app.square2.symbol = None

app.square3 = Rect(270, 0, 130, 130, fill = None, border = 'black', borderWidth = 1, visible = False)
app.square3.full = False
app.square3.symbol = None

app.square4 = Rect(0, 130, 130, 140, fill = None, border = 'black', borderWidth = 1, visible = False)
app.square4.full = False
app.square4.symbol = None

app.square5 = Rect(130, 130, 140, 140, fill = None, border = 'black', borderWidth = 1, visible = False)
app.square5.full = False
app.square5.symbol = None

app.square6 = Rect(270, 130, 130, 140, fill = None, border = 'black', borderWidth = 1, visible = False)
app.square6.full = False
app.square6.symbol = None

app.square7 = Rect(0, 270, 130, 130, fill = None, border = 'black', borderWidth = 1, visible = False)
app.square7.full = False
app.square7.symbol = None

app.square8 = Rect(130, 270, 140, 130, fill = None, border = 'black', borderWidth = 1, visible = False)
app.square8.full = False
app.square8.symbol = None

app.square9 = Rect(270, 270, 130, 130, fill = None, border = 'black', borderWidth = 1, visible = False)
app.square9.full = False
app.square9.symbol = None

def drawBoard():
    board.add(
        app.square1,
        app.square2,
        app.square3,
        app.square4,
        app.square5,
        app.square6,
        app.square7,
        app.square8,
        app.square9
    )
    board.visible = True
    
def winScreen(winner):
    Label(str(winner) + ' WINS', 200, 200, bold = True, font = 'Comic Sans', size = 50)
    pass
def main():
    for square in board.children:
        square.full = False
        square.symbol = None
        
    
def drawCross(crossX, crossY):
    crosses.add(
        Line(crossX-50, crossY, crossX+50, crossY, fill = 'red', rotateAngle = 45, lineWidth = 5),
        Line(crossX-50, crossY, crossX+50, crossY, fill = 'red', rotateAngle = -45, lineWidth = 5)
    )
    pass
def drawO(oX, oY):
    os.add(
        Circle(oX, oY, 48, fill = None, border = 'blue', borderWidth = 5)
    )
    pass
def clearBoard():
    crosses.visible = False
    os.visible = False
    board.visible = False
main()
drawBoard() 
def onMousePress(mouseX, mouseY):
    
    for square in board.children:
        # print(square.full)

                
        #print(square.symbol)
        app.player = app.playerList[app.playerIndex]
        
        if (square.contains(mouseX, mouseY)):
            if square.full == True:
                return
            if (app.player == 'x'):
                drawCross(square.centerX, square.centerY)
                app.playerIndex+=1
                square.full = True
                square.symbol = 'X'
            if (app.player == 'o'):
                drawO(square.centerX, square.centerY)
                app.playerIndex-=1
                square.full = True
                square.symbol = 'O'
                #win conditions
            if (app.square1.symbol == app.square2.symbol == app.square3.symbol!=None):
                winScreen(app.square1.symbol)
                clearBoard()
            if (app.square1.symbol == app.square4.symbol == app.square7.symbol!=None):
                winScreen(app.square1.symbol)
                clearBoard()
            if (app.square1.symbol == app.square5.symbol == app.square9.symbol!=None):
                winScreen(app.square1.symbol)
                clearBoard()
            if (app.square2.symbol == app.square5.symbol == app.square8.symbol!=None):
                winScreen(app.square2.symbol)
                clearBoard()
            if (app.square3.symbol == app.square6.symbol == app.square9.symbol!=None):
                winScreen(app.square3.symbol)
                clearBoard()
            if (app.square4.symbol == app.square5.symbol == app.square6.symbol!=None):
                winScreen(app.square4.symbol)
                clearBoard()
            if (app.square7.symbol == app.square8.symbol == app.square9.symbol!=None):
                winScreen(app.square7.symbol)
                clearBoard()
            if (app.square7.symbol == app.square5.symbol == app.square3.symbol!=None):
                winScreen(app.square7.symbol)
                clearBoard()

    pass

cmu_graphics.run()
  



    