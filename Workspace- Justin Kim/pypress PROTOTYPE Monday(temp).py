# pypress.py# Designed by Ben Underwood and Justin Kim# A version of Letterpress for Python# Original game designed and published by atebitsfrom graphics import *import stringimport randomimport lib_button as buttonfrom time import sleepPLAYER_ONE_COLOR = "cyan"PLAYER_TWO_COLOR = "goldenrod"def drawBoard():    win = GraphWin("PyPress.py", 700, 600)    win.setCoords(0, 0, 700, 600)        box = [""] * 25    upLeft = Point(100, 500)    downRight = Point(150, 450)    width = 100# downRight.getX() - upLeft.getX()    height = 100# upLeft.getY() - downRight.getY()    center = Point(150, 50) ##Revert if needed##    for i in range(25): # Draw Buttons        box[i] = button.Button(win, center, width, height, str(box[i]))         if not i in [4, 9, 14, 19]:            if round(center.getX()) in [150, 350, 550]:                center.move(0, 100)            else:                center.move(0, -100)        else:            center.move(100, 0)    return win, boxdef initTiles(win, box):    global letters    letters = []    for i in range(25): # Label buttons        letters.append(random.choice(string.ascii_uppercase))        box[i].label.setSize(20)        box[i].label.setText(letters[i])        box[i].activate()    print(letters, "\n")def setAllActive(ButtonList):    for i in ButtonList:        i.activate()def turnSwitch():    global color    global lastColor        if color == PLAYER_ONE_COLOR:        color = PLAYER_TWO_COLOR        lastColor = PLAYER_ONE_COLOR    elif color == PLAYER_TWO_COLOR:        color = PLAYER_ONE_COLOR        lastColor = PLAYER_TWO_COLOR    time.sleep(1)def makeScore(chosenLetters):    letterList = []    for i in range(len(chosenLetters)):        letterList.append(chosenLetters[i])    return letterListdef isClicked(click, box):    boxClicked = None    global oldColor    print("Old Colors:\n\n", oldColor, "\n\n")    totalButtonClicks = [0] * 25  #\ What are these for?    wasClicked = [False] * 25     #/    #global lastColor    #print(lastColor)    for i in range(25):        if box[i].clicked(click):            letter = box[i].getLabel()            box[i].deactivate()            oldColor[i] = lastColor            box[i].setFill(color, color)            boxClicked = i    if boxClicked == None:        letter = None    return letter, boxClickeddef main():    win, box = drawBoard()    initTiles(win, box)    submitButton = button.Button(win, Point(650, 550), 70, 30, "submit!")    submitButton.activate()    chosenLetters = ""    drawChosenLetters = Text(Point(350, 550), chosenLetters)    drawChosenLetters.setSize(20)    drawChosenLetters.draw(win)#######    #boxIndex = list(range(25))    global color    global lastColor    global oldColor    color = PLAYER_ONE_COLOR    lastColor = "light gray"    oldColor = [None] * 25    ## LEGACY CODE ##    testCount = 0 #Used for testing the loop structure, can remove, or keep                    # if we want to display the number of turns taken.##    submit = False    invalidText = Text(Point(650, 515), "Not a valid word!")    redLetters = []    blueLetters = []    wordlist = open("wordlist.txt")    testlist = open("wordlist(test).txt", "w")        while (len(redLetters) + len(blueLetters)) < 25:        while True:            invalidText.undraw()            click = win.getMouse()            if submitButton.clicked(click):                if True: #drawChosenLetters.getText().lower() in wordlist.read():                    print(wordlist.read(), file=testlist)                                        print(drawChosenLetters.getText())                    invalidText.setText("Valid word!")                    invalidText.draw(win)                else:                    invalidText.setText("Invalid word!")                    invalidText.draw(win)###     Removed to prevent bugs in prototype. Must indent statements beginning###         with 'submitButton.deactivate()' and ending with 'break'.                ##                if chosenLetters.lower() not in wordlist.read():##                    invalidText.draw(win)##                    print(chosenLetters)##                else:                submitButton.deactivate()                print("\nSubmitting and Ending Turn...\n")                break            letter, boxClicked = isClicked(click, box)            if letter != None:                chosenLetters = chosenLetters + letter                                try:                    if letters[boxClicked] != None:                        print("Removing", letters[boxClicked], "from 'letters'")                        print("Location:", boxClicked)                        letters[boxClicked] = None                                                        else:                        print("valueError... Redirecting...")                        if color == PLAYER_ONE_COLOR:                            try:                                if oldColor[boxClicked] == color:                                    blueLetters.remove(letter)                                    print("First Player clicked their own letter.")                                else:                                    print("Removing {0} @ Location {1} from Second Player".format(                                        letters[boxClicked], boxClicked))                                    redLetters.remove(letter)                                    print("Removed letter from Second Player")                            except ValueError:                                if letter in blueLetters:                                    print("Never mind")                                    blueLetters.remove(letter) # See below comment                                    pass                        elif color == PLAYER_TWO_COLOR:                            try:                                if oldColor[boxClicked] == color:                                    redLetters.remove(letter)                                    print("Second Player clicked their own letter.")                                else:                                    print("Removing {0} @ Location {1} from First Player".format(                                        letters[boxClicked], boxClicked))                                    blueLetters.remove(letter)                                    print("Removed letter from First Player")                            except ValueError:                                if letter in redLetters:                                    print("Never mind")                                    redLetters.remove(letter) #At this point, the                                                        # letter has already been                                                        # added to 'chosenLetters'.                                                        # Removing the existing                                                        # letter from the list                                                        # prevents the program from                                                        # duplicating the letter,                                                        # as the letter will be                                                        # re-added as part of the                                                        # new word.                                    pass                        else: print('\nWhat? Neither team registered...\n',letters, '\n')                except IndexError:                    print("\nIndex Error, Redirecting...")                    print()                    print(letters)                    print()                    print(len(letters))                    print()                                                          drawChosenLetters.setText(chosenLetters)        letterList = makeScore(chosenLetters)        if color == PLAYER_ONE_COLOR:             blueLetters = blueLetters + letterList        elif color == PLAYER_TWO_COLOR:            redLetters = redLetters + letterList        print(blueLetters, redLetters)                    turnSwitch()        chosenLetters = ""        drawChosenLetters.setText(chosenLetters)        print("\n" + "-" * 20, "Switching Turns", "-" * 20 + "\n")        if color == PLAYER_ONE_COLOR:            print(" " * 20, "Player 1", " " * 20)        else: print(" " * 20, "Player 2", " " * 20)        testCount = testCount + 1        submit = True        submitButton.activate()        setAllActive(box)    print("Finished!")    print(letters)    print("Player 1 Score:",len(blueLetters),"\nPlayer 2 Score:", len(redLetters))    print("\n Total letters claimed:", len(letters))    print("\n\n\nClick to Close...")    win.getMouse()    win.close()if __name__ == "__main__":    main()