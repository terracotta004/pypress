# pypress.py# Designed by Ben Underwood and Justin Kim# A version of Letterpress for Python# Original game designed and published by atebitsfrom graphics import *import stringimport randomimport lib_button as buttonPLAYER_ONE_COLOR = "cyan"PLAYER_TWO_COLOR = "goldenrod"def setAllActive(ButtonList):    for i in ButtonList:        i.activate()def turnSwitch():    global color    global lastColor        if color == PLAYER_ONE_COLOR:        color = PLAYER_TWO_COLOR        lastColor = PLAYER_ONE_COLOR    elif color == PLAYER_TWO_COLOR:        color = PLAYER_ONE_COLOR        lastColor = PLAYER_TWO_COLORdef makeScore(chosenLetters):    letterList = []    for i in range(len(chosenLetters)):        letterList.append(chosenLetters[i])    return letterListdef isClicked(click, box):    boxClicked = None    global oldColor    print("Old Colors:\n\n", oldColor, "\n\n")    totalButtonClicks = [0] * 25    wasClicked = [False] * 25    #global lastColor    #print(lastColor)    if box[0].clicked(click):            letter = box[0].getLabel()            box[0].deactivate()            oldColor[0] = lastColor            box[0].setFill(color, color)            boxClicked = 0    elif box[1].clicked(click):            letter = box[1].getLabel()            box[1].deactivate()            oldColor[1] = lastColor            box[1].setFill(color, color)            boxClicked = 1    elif box[2].clicked(click):            letter = box[2].getLabel()            box[2].deactivate()            oldColor[2] = lastColor            box[2].setFill(color, color)            boxClicked = 2    elif box[3].clicked(click):            letter = box[3].getLabel()            box[3].deactivate()            oldColor[3] = lastColor            box[3].setFill(color, color)            boxClicked = 3    elif box[4].clicked(click):            letter = box[4].getLabel()            box[4].deactivate()            oldColor[4] = lastColor            box[4].setFill(color, color)            boxClicked = 4    elif box[5].clicked(click):            letter = box[5].getLabel()            box[5].deactivate()            oldColor[5] = lastColor            box[5].setFill(color, color)            boxClicked = 5    elif box[6].clicked(click):            letter = box[6].getLabel()            box[6].deactivate()            oldColor[6] = lastColor            box[6].setFill(color, color)            boxClicked = 6    elif box[7].clicked(click):            letter = box[7].getLabel()            box[7].deactivate()            oldColor[7] = lastColor            box[7].setFill(color, color)            boxClicked = 7    elif box[8].clicked(click):            letter = box[8].getLabel()            box[8].deactivate()            oldColor[8] = lastColor            box[8].setFill(color, color)            boxClicked = 8    elif box[9].clicked(click):            letter = box[9].getLabel()            box[9].deactivate()            oldColor[9] = lastColor            box[9].setFill(color, color)            boxClicked = 9    elif box[10].clicked(click):            letter = box[10].getLabel()            box[10].deactivate()            oldColor[10] = lastColor            box[10].setFill(color, color)            boxClicked = 10    elif box[11].clicked(click):            letter = box[11].getLabel()            box[11].deactivate()            oldColor[11] = lastColor            box[11].setFill(color, color)            boxClicked = 11    elif box[12].clicked(click):            letter = box[12].getLabel()            box[12].deactivate()            oldColor[12] = lastColor            box[12].setFill(color, color)            boxClicked = 12    elif box[13].clicked(click):            letter = box[13].getLabel()            box[13].deactivate()            oldColor[13] = lastColor            box[13].setFill(color, color)            boxClicked = 13    elif box[14].clicked(click):            letter = box[14].getLabel()            box[14].deactivate()            oldColor[14] = lastColor            box[14].setFill(color, color)            boxClicked = 14    elif box[15].clicked(click):            letter = box[15].getLabel()            box[15].deactivate()            oldColor[15] = lastColor            box[15].setFill(color, color)            boxClicked = 15    elif box[16].clicked(click):            letter = box[16].getLabel()            box[16].deactivate()            oldColor[16] = lastColor            box[16].setFill(color, color)            boxClicked = 16    elif box[17].clicked(click):            letter = box[17].getLabel()            box[17].deactivate()            oldColor[17] = lastColor            box[17].setFill(color, color)            boxClicked = 17    elif box[18].clicked(click):            letter = box[18].getLabel()            box[18].deactivate()            oldColor[18] = lastColor            box[18].setFill(color, color)            boxClicked = 18    elif box[19].clicked(click):            letter = box[19].getLabel()            box[19].deactivate()            oldColor[19] = lastColor            box[19].setFill(color, color)            boxClicked = 19    elif box[20].clicked(click):            letter = box[20].getLabel()            box[20].deactivate()            oldColor[20] = lastColor            box[20].setFill(color, color)            boxClicked = 20    elif box[21].clicked(click):            letter = box[21].getLabel()            box[21].deactivate()            oldColor[21] = lastColor            box[21].setFill(color, color)            boxClicked = 21    elif box[22].clicked(click):            letter = box[22].getLabel()            box[22].deactivate()            oldColor[22] = lastColor            box[22].setFill(color, color)            boxClicked = 22    elif box[23].clicked(click):            letter = box[23].getLabel()            box[23].deactivate()            oldColor[23] = lastColor            box[23].setFill(color, color)            boxClicked = 23    elif box[24].clicked(click):            letter = box[24].getLabel()            box[24].deactivate()            oldColor[24] = lastColor            box[24].setFill(color, color)            boxClicked = 24    else: letter = None    return letter, boxClickeddef main():####### Make Function? #####    win = GraphWin("PyPress.py", 700, 600)    win.setCoords(0, 0, 700, 600)    box = ["","","","","","","","","","","","","",           "","","","","","","","","","","",""]        upLeft = Point(100, 500)    downRight = Point(150, 450)        width = 100# downRight.getX() - upLeft.getX()    height = 100# upLeft.getY() - downRight.getY()    center = Point(150, 50) ##Revert if needed##    for i in range(25): # Draw Buttons        box[i] = button.Button(win, center, width, height, str(box[i])) ##        box[i] = Rectangle(upLeft, Point(200, 400))##        box[i].draw(win)        if not i in [4, 9, 14, 19]:            if round(center.getX()) in [150, 350, 550]:                center.move(0, 100)            else:                center.move(0, -100)        else:            center.move(100, 0)        #center.move(dx, dy)##        box[i].move(100 * i - (500 * (int(i/5))), -100 * (int(i/5)))##    for click in range(10):##        x = win.getMouse()##        x.draw(win)##        print(x.getX(), x.getY())##        ################ Make Function? #####    global letters    letters = []    for i in range(25): # Label buttons        letters.append(random.choice(string.ascii_uppercase))        box[i].label.setSize(20)        box[i].label.setText(letters[i])        box[i].activate()    print(letters, "\n")##        tile = Text(downRight, letters[i])####        tile.move(100 * i - (500 * (int(i/5))), -100 * (int(i/5)))####        tile.setSize(20)####        tile.draw(win)########            submitButton = button.Button(win, Point(650, 550), 70, 30, "submit!")    submitButton.activate()    #submitText.draw(win)    #Rectangle(Point(615, 565), Point(685, 535)).draw(win)####### Make Function? ###    chosenLetters = ""    drawChosenLetters = Text(Point(350, 550), chosenLetters)    drawChosenLetters.setSize(20)    drawChosenLetters.draw(win)#######    #boxIndex = list(range(25))    global color    global lastColor    global oldColor    color = PLAYER_ONE_COLOR    lastColor = "light gray"    oldColor = [None] * 25        testCount = 0    submit = False##    invalidText = Text(Point(650, 515), "Not a valid word!") # Removed for prototype    redLetters = []    blueLetters = []##    wordlist = open("wordlist.txt")   # Removed to prevent bugs in prototype    while (len(redLetters) + len(blueLetters)) < 25:        while True:            click = win.getMouse()            if submitButton.clicked(click):                ###     Removed to prevent bugs in prototype. Must indent statements beginning###         with 'submitButton.deactivate()' and ending with 'break'.                ##                if chosenLetters.lower() not in wordlist.read():##                    invalidText.draw(win)##                    print(chosenLetters)##                else:                submitButton.deactivate()                print("\nSubmitting and Ending Turn...\n")                break            letter, boxClicked = isClicked(click, box)            if letter != None:                chosenLetters = chosenLetters + letter                                try:                    if letters[boxClicked] != None:                        print("Removing", letters[boxClicked], "from 'letters'")                        print("Location:", boxClicked)                        letters[boxClicked] = None                                                        else:                        print("valueError... Redirecting...")                        if color == PLAYER_ONE_COLOR:                            try:                                if oldColor[boxClicked] == color:                                    blueLetters.remove(letter)                                    print("First Player clicked their own letter.")                                else:                                    print("Removing {0} @ Location {1} from Second Player".format(                                        letters[boxClicked], boxClicked))                                    redLetters.remove(letter)                                    print("Removed letter from Second Player")                            except ValueError:                                if letter in blueLetters:                                    print("Never mind")                                    blueLetters.remove(letter) # See below comment                                    pass                        elif color == PLAYER_TWO_COLOR:                            try:                                if oldColor[boxClicked] == color:                                    redLetters.remove(letter)                                    print("Second Player clicked their own letter.")                                else:                                    print("Removing {0} @ Location {1} from First Player".format(                                        letters[boxClicked], boxClicked))                                    blueLetters.remove(letter)                                    print("Removed letter from First Player")                            except ValueError:                                if letter in redLetters:                                    print("Never mind")                                    redLetters.remove(letter) #At this point, the                                                        # letter has already been                                                        # added to 'chosenLetters'.                                                        # Removing the existing                                                        # letter from the list                                                        # prevents the program from                                                        # duplicating the letter,                                                        # as the letter will be                                                        # re-added as part of the                                                        # new word.                                    pass                        else: print('\nWhat? Neither team registered...\n',letters, '\n')                except IndexError:                    print("\nIndex Error, Redirecting...")                    print()                    print(letters)                    print()                    print(len(letters))                    print()                                                          drawChosenLetters.setText(chosenLetters)        letterList = makeScore(chosenLetters)        if color == PLAYER_ONE_COLOR:             blueLetters = blueLetters + letterList        elif color == PLAYER_TWO_COLOR:            redLetters = redLetters + letterList        print(blueLetters, redLetters)                    turnSwitch()        chosenLetters = ""        drawChosenLetters.setText(chosenLetters)        print("\n" + "-" * 20, "Switching Turns", "-" * 20 + "\n")        if color == PLAYER_ONE_COLOR:            print(" " * 20, "Player 1", " " * 20)        else: print(" " * 20, "Player 2", " " * 20)        testCount = testCount + 1        submit = True        submitButton.activate()        setAllActive(box)    print("Finished!")    print(letters)    print("Player 1 Score:",len(blueLetters),"\nPlayer 2 Score:", len(redLetters))    print("\n Total letters claimed:", len(letters))    print("\n\n\nClick to Close...")    win.getMouse()    win.close()if __name__ == "__main__":    main()