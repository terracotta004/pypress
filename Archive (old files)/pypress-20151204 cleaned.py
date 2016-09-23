# pypress.py# A version of Letterpress for Python# Original game designed and published by atebitsfrom graphics import *import stringimport randomimport lib_button as buttondef drawBoard():    win = GraphWin("pypress.py", 700, 600)    win.setCoords(0, 0, 700, 600)    box = [""] * 25    letters = []    upLeft = Point(100, 500)    downRight = Point(150, 450)    width = 100# downRight.getX() - upLeft.getX()    height = 100# upLeft.getY() - downRight.getY()    center = Point(150, 50) ##Revert if needed##    for i in range(25): # Draw Buttons        box[i] = button.Button(win, center, width, height, str(box[i])) ##        box[i] = Rectangle(upLeft, Point(200, 400))##        box[i].draw(win)        if not i in [4, 9, 14, 19]:            if round(center.getX()) in [150, 350, 550]:                center.move(0, 100)            else:                center.move(0, -100)        else:            center.move(100, 0)        #center.move(dx, dy)                return win, box, lettersdef initTiles(box, letters, win):    for i in range(25): # Label buttons        letters.append(random.choice(string.ascii_uppercase))        box[i].label.setSize(20)        box[i].label.setText(letters[i])        box[i].activate()    submit = False    submitButton = button.Button(win, Point(650, 550), 70, 30, "submit!")    submitButton.activate()    return submit, submitButtondef drawChosenLettersStr(win, box, letters, click, chosenLetters, drawChosenLetters): # no longer necessary, included in main()    boxIndex = list(range(25))    for i in range(25):        if box[i].clicked(click):            chosenLetters = chosenLetters + letters[i]            letters[i] = ""            drawChosenLetters.setText(chosenLetters)                return letters, chosenLettersdef drawChosenLetterBoxes(win, box, letters, click, chosenLetters, drawChosenLetters): # will create buttons as chosen letters    passdef main():    win, box, letters  = drawBoard()    submit, submitButton = initTiles(box, letters, win)    chosenLetters = ""    drawChosenLetters = Text(Point(350, 550), chosenLetters)    drawChosenLetters.setSize(20)    drawChosenLetters.draw(win)    while submit == False:        click = win.getMouse()        if submitButton.clicked(click):            submitButton.deactivate()            print("Breaking...")            break        for i in range(25):            if box[i].clicked(click):                chosenLetters = chosenLetters + letters[i]                letters[i] = ""                drawChosenLetters.setText(chosenLetters)                #       letters, chosenLetters = drawChosenLettersStr(win, box, letters, click, chosenLetters, drawChosenLetters)        print(letters, chosenLetters)    win.getMouse()    win.close()if __name__ == "__main__":    main()