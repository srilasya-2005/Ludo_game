from tkinter import *  # Tkinter is used as the GUI.
import random

root = Tk()
root.title("LUDO GAME")
root.resizable(width=False, height=False)  # The window size of the game.
root.geometry('1000x750')
root.configure(background="green")

# Loading all the image files that are required in the game.
red_piece = PhotoImage(file="red.gif")
blue_piece = PhotoImage(file="blue.gif")
yellow_piece = PhotoImage(file="yellow.gif")
green_piece = PhotoImage(file="green.gif")
main_board = PhotoImage(file="test.gif")

# initializing variable and flags that are to be used in the game
lx = 0
bb = 0
nc = 0
rollc = 0
rolls = []
RED = True
BLUE = False
GREEN = False
YELLOW = False
TURN = True
REDKILL = False
BLUEKILL = False
GREENKILL = False
YELLOWKILL = False


class Box:  # class of red box
    rap = None

    def __init__(self, num=-1, x=0, y=0, x0=0, y0=0, double=False, ):
        self.num = num  # no of gamepiece acc to box
        self.x = x  # initial and final co-ordinates of the boxes
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.rap = Label(image=red_piece, width=20, height=20)
        self.double = double

    def swap(self):
        self.rap.place(x=self.x0 + 13, y=self.y0 + 14)


class YBox:  # Class of yellow box
    rap = None

    def __init__(self, num=-1, x=0, y=0, x0=0, y0=0, double=False):
        self.num = num
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.rap = Label(image=yellow_piece, width=20, height=20)  # image of game piece.
        self.double = double  # if one game piece on top of another.

    def swap(self):  # Swaps the position of gamepiece according to the number on dice.
        self.rap.place(x=self.x0 + 13, y=self.y0 + 14)


class BBox:  # Class of yellow box
    rap = None

    def __init__(self, num=-1, x=0, y=0, x0=0, y0=0, double=False):
        self.num = num  # no of gamepiece acc to box
        self.x = x  # initial and final co-ordinates of the boxes
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.rap = Label(image=blue_piece, width=20, height=20)  # image of game piece.
        self.double = double  # if one game piece on top of another.

    def swap(self):
        self.rap.place(x=self.x0 + 13, y=self.y0 + 14)


class GBox:  # Class of yellow box
    rap = None

    def __init__(self, num=-1, x=0, y=0, x0=0, y0=0, double=False):
        self.num = num  # no of gamepiece acc to box
        self.x = x  # initial and final co-ordinates of the boxes
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.rap = Label(image=green_piece, width=20, height=20)  # image of game piece.
        self.double = double  # if one game piece on top of another.

    def swap(self):  # Swaps the position of gamepiece according to the number on dice.
        self.rap.place(x=self.x0 + 13, y=self.y0 + 14)


def turn():
    """Prints whose turn is it"""

    if RED == True:
        Label(root, text="  Red's Turn  ", fg='Black', background='green', font=("Arial", 24, "bold")).place(x=770,
                                                                                                             y=50)

    if BLUE == True:
        Label(root, text="  Blue's Turn  ", fg='Black', background='green', font=("Arial", 24, "bold")).place(x=770,
                                                                                                              y=50)
    if YELLOW == True:
        Label(root, text=" Yellow's Turn", fg='Black', background='green', font=("Arial", 24, "bold")).place(x=770,
                                                                                                             y=50)
    if GREEN == True:
        Label(root, text=" Green's Turn  ", fg='Black', background='green', font=("Arial", 24, "bold")).place(x=770,
                                                                                                              y=50)


def roll():
    """ Rolling function that rolls a dice, goes again if its a six"""
    global rollc, dice, dice1, dice2, TURN, rolls
    uni_dice = ("\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685")

    if TURN == True:

        rollc = rollc + 1
        if rollc == 1:
            dice = random.randint(1, 6)
            L1 = Label(root, text=uni_dice[dice - 1], fg='White', background='green', font=("Arial", 50, "bold"))
            L1.place(x=800, y=200)
            rolls.append(dice)
            if dice != 6:
                rollc = 0
                TURN = False

        if rollc == 2:
            if dice == 6:
                dice1 = random.randint(1, 6)
                L3 = Label(root, text=uni_dice[dice1 - 1], fg='White', background='green', font=("Arial", 50, "bold"))
                L3.place(x=800, y=280)
                rolls.append(dice1)
                if dice1 != 6:
                    rollc = 0
                    TURN = False

        if rollc == 3:
            if dice1 == 6:
                dice2 = random.randint(1, 6)
                L4 = Label(root, text=uni_dice[dice2 - 1], fg='White', background='green', font=("Arial", 50, "bold"))
                L4.place(x=800, y=360)
                rolls.append(dice2)
                rollc = 0
                TURN = False


def clear():
    """clears all the variable prior to next player's turn"""
    global nc, rolls, TURN, L1, L3, L4
    nc = 0
    del rolls[:]
    TURN = True
    Label(root, text="        ", fg='Black', background='green', font=("Arial", 50, "bold")).place(x=800, y=200)
    Label(root, text="        ", fg='Black', background='green', font=("Arial", 50, "bold")).place(x=800, y=250)
    Label(root, text="        ", fg='Black', background='green', font=("Arial", 50, "bold")).place(x=800, y=280)
    Label(root, text="        ", fg='Black', background='green', font=("Arial", 50, "bold")).place(x=800, y=310)
    Label(root, text="        ", fg='Black', background='green', font=("Arial", 50, "bold")).place(x=800, y=360)
    turn()


def moveCheck(r, rb, la):
    """Check if the player can make a move"""

    if dice == 6 and dice1 == 6 and dice2 == 6:
        return False

    win = True  # Checking if the game is won or the player can make any moves.
    for j in range(4):
        if (r[j].x0 != rb[56].x) and (r[j].y0 != rb[56].y):
            win = False

    if win == True:  # If all gamepieces home, prints that the player has won

        L2 = Label(root, text=(la + "Wins"), fg='Black', background='green', font=("Arial", 24, "bold"))
        L2.place(x=770, y=500)
        return False

    if win == False and dice != 6:  # if its not a 6 and all game pieces inside home, then next players turn
        for i in range(len(r)):
            if (r[i].num != -1):
                return True
        return False


def kill(a, b, c, d, bh, ch, dh):
    """Function that determine if the other's piece can be killed"""
    if ((a[bb].x0 != box[1].x and a[bb].y0 != box[1].y) and (a[bb].x0 != box[14].x and a[bb].y0 != box[14].y) and
            (a[bb].x0 != box[9].x and a[bb].y0 != box[9].y) and (a[bb].x0 != box[22].x and a[bb].y0 != box[22].y) and
            (a[bb].x0 != box[27].x and a[bb].y0 != box[27].y) and (a[bb].x0 != box[35].x and a[bb].y0 != box[35].y) and
            (a[bb].x0 != box[40].x and a[bb].y0 != box[40].y) and (a[bb].x0 != box[48].x and a[bb].y0 != box[48].y)):

        # if the game piece of another color and its on the same block and it is not a double, a kill is made
        for i in range(len(b)):
            if b[i].x0 == a[bb].x and b[i].y0 == a[bb].y and (b[i].double == False):
                b[i].x0 = bh[i].x
                b[i].y0 = bh[i].y
                b[i].x = bh[i].x + 25
                b[i].y = bh[i].y + 25
                b[i].num = -1
                b[i].swap()
                break

        for i in range(len(c)):
            if c[i].x0 == a[bb].x and c[i].y0 == a[bb].y and (c[i].double == False):
                c[i].x0 = ch[i].x
                c[i].y0 = ch[i].y
                c[i].x = ch[i].x + 25
                c[i].y = ch[i].y + 25
                c[i].num = -1
                c[i].swap()
                break

        for i in range(len(d)):
            if d[i].x0 == a[bb].x and d[i].y0 == a[bb].y and (d[i].double == False):
                d[i].x0 = dh[i].x
                d[i].y0 = dh[i].y
                d[i].x = dh[i].x + 25
                d[i].y = dh[i].y + 25
                d[i].num = -1
                d[i].swap()
                break


def doublecheck(a):
    """Makes a double is two or more game pieces on top of another."""
    for k in range(len(a)):
        a[k].double = False

    for i in range(len(a)):
        for j in range(len(a)):
            if (a[i].num == a[j].num) and (i != j):
                a[j].double = True
                a[i].double = True


def main():  # Main game function.
    global box, redbox, bluebox, greenbox, yellowbox, redhome, bluehome, yellowhome, greenhome, check
    global red, blue, yellow, green, rap, RED, BLUE, GREEN, YELLOW, dice, nc, TURN, bb

    Label(root, image=main_board).place(x=-1, y=-1)
    turn()
    Button(root, text="Roll the Dice!", relief="raised", font=("Arial", 20), command=roll).place(x=800, y=120)

    box = [Box() for i in range(52)]

    redbox = [Box() for i in range(57)]  # list of co-ordinates of all the colored boxes, excluding home and stop.
    bluebox = [Box() for i in range(57)]
    greenbox = [Box() for i in range(57)]
    yellowbox = [Box() for i in range(57)]

    redhome = [Box() for i in range(4)]  # list co-ordinates of all the home positions
    bluehome = [Box() for i in range(4)]
    greenhome = [Box() for i in range(4)]
    yellowhome = [Box() for i in range(4)]

    red = [Box() for i in range(4)]  # list of co-ordinates of all the game pieces in their initial state
    blue = [BBox() for i in range(4)]  # that is equal to their respective home co-ordinates.
    green = [GBox() for i in range(4)]
    yellow = [YBox() for i in range(4)]

    for i in range(2):  # Populates list of homeboxes, colored boxes, gamepieces and white boxes
        redhome[i].x = (100 + (100 * i))
        redhome[i].y = 100
        red[i].x0 = redhome[i].x
        red[i].y0 = redhome[i].y
        red[i].x = red[i].x0 + 25
        red[i].y = red[i].y0 + 25

        bluehome[i].x = (100 + (100 * i))
        bluehome[i].y = 550
        blue[i].x0 = bluehome[i].x
        blue[i].y0 = bluehome[i].y
        blue[i].x = blue[i].x0 + 25
        blue[i].y = blue[i].y0 + 25

        yellowhome[i].x = (550 + (100 * i))
        yellowhome[i].y = 550
        yellow[i].x0 = yellowhome[i].x
        yellow[i].y0 = yellowhome[i].y
        yellow[i].x = yellow[i].x0 + 25
        yellow[i].y = yellow[i].y0 + 25

        greenhome[i].x = (550 + (100 * i))
        greenhome[i].y = (100)
        green[i].x0 = greenhome[i].x
        green[i].y0 = greenhome[i].y
        green[i].x = (green[i].x0) + 25
        green[i].y = (green[i].y0) + 25

    for i in range(2, 4):
        redhome[i].x = (100 + (100 * (i - 2)))
        redhome[i].y = 200
        red[i].x0 = redhome[i].x
        red[i].y0 = redhome[i].y
        red[i].x = (red[i].x0) + 25
        red[i].y = (red[i].y0) + 25

        bluehome[i].x = (100 + (100 * (i - 2)))
        bluehome[i].y = (650)
        blue[i].x0 = bluehome[i].x
        blue[i].y0 = bluehome[i].y
        blue[i].x = (blue[i].x0) + 25
        blue[i].y = (blue[i].y0) + 25

        yellowhome[i].x = (550 + (100 * (i - 2)))
        yellowhome[i].y = (650)
        yellow[i].x0 = yellowhome[i].x
        yellow[i].y0 = yellowhome[i].y
        yellow[i].x = (yellow[i].x0) + 25
        yellow[i].y = (yellow[i].y0) + 25

        greenhome[i].x = (550 + (100 * (i - 2)))
        greenhome[i].y = 200
        green[i].x0 = greenhome[i].x
        green[i].y0 = greenhome[i].y
        green[i].x = (green[i].x0) + 25
        green[i].y = (green[i].y0) + 25

    for i in range(6):
        box[i].x = 300
        box[i].y = (700 - (50 * i))

    for i in range(6, 12):
        box[i].x = (250 - (50 * (i - 6)))
        box[i].y = (400)

    box[12].x = 0
    box[12].y = 350

    for i in range(13, 19):
        box[i].x = (0 + (50 * (i - 13)))
        box[i].y = (300)

    for i in range(19, 25):
        box[i].x = (300)
        box[i].y = (250 - (50 * (i - 19)))

    box[25].x = 350
    box[25].y = 0

    for i in range(26, 32):
        box[i].x = (400)
        box[i].y = (0 + (50 * (i - 26)))

    for i in range(32, 38):
        box[i].x = (450 + (50 * (i - 32)))
        box[i].y = (300)

    box[38].x = 700
    box[38].y = 350

    for i in range(39, 45):
        box[i].x = (700 - (50 * (i - 39)))
        box[i].y = (400)

    for i in range(45, 51):
        box[i].x = (400)
        box[i].y = (450 + (50 * (i - 45)))

    box[51].x = 350
    box[51].y = 700

    # red
    lx = 14
    for i in range(52):
        redbox[i].x = box[lx].x
        redbox[i].y = box[lx].y
        lx = lx + 1
        if lx > 51:
            lx = 0

    lx = 50
    for i in range(7):
        redbox[lx].x = (0 + (50 * i))
        redbox[lx].y = 350
        lx = lx + 1
    # blue
    lx = 1
    for i in range(52):

        bluebox[i].x = box[lx].x
        bluebox[i].y = box[lx].y
        lx = lx + 1
        if lx > 51:
            lx = 0

    lx = 50
    for i in range(7):
        bluebox[lx].x = 350
        bluebox[lx].y = (700 - (50 * i))
        lx = lx + 1
    # yellow
    lx = 40
    for i in range(52):
        yellowbox[i].x = box[lx].x
        yellowbox[i].y = box[lx].y
        lx = lx + 1
        if lx > 51:
            lx = 0

    lx = 50
    for i in range(7):
        yellowbox[lx].x = (700 - (50 * i))
        yellowbox[lx].y = (350)
        lx = lx + 1

    # green
    lx = 27
    for i in range(52):

        greenbox[i].x = box[lx].x
        greenbox[i].y = box[lx].y

        lx = lx + 1
        if lx > 51:
            lx = 0

    lx = 50
    for i in range(7):
        greenbox[lx].x = 350
        greenbox[lx].y = (0 + (50 * i))
        lx = lx + 1

    for i in range(4):
        red[i].swap()
        blue[i].swap()
        green[i].swap()
        yellow[i].swap()


def Instruction():
    sub_root = Tk()
    sub_root.title("Instructions")
    sub_root.geometry("1050x700")
    sub_root.configure(background="gray")
    Label(sub_root, text="Instruction", background="gray", fg="White", font=("Arial", 20)).place(x=400, y=30)
    Label(sub_root, text="Ludo is one of the easiest indoor games one can play.", background="gray", fg="White",
          font=("Arial", 16)).place(x=10, y=70)
    Label(sub_root,
          text="But like every other game there are some ground rules one should know before starting to play:",
          background="gray", fg="White", font=("Arial", 16)).place(x=10, y=110)
    Label(sub_root, text=" 1 . Unless you get a '6' when rolling the dice, your planes can't take off.",
          background="gray", fg="White", font=("Arial", 16)).place(x=10, y=150)
    Label(sub_root, text=" 2 . Press the Enter Button button to roll the dice.", background="gray", fg="White",
          font=("Arial", 16)).place(x=10, y=190)
    Label(sub_root,
          text=" 3 . If there are two planes of the same color on top of each other than that plane cannot be killed.",
          background="gray", fg="White", font=("Arial", 16)).place(x=10, y=230)
    Label(sub_root,
          text=" 4 . To win the game, your planes have to travel around the board and come into the home lane.",
          background="gray", fg="White", font=("Arial", 16)).place(x=10, y=270)
    Label(sub_root,
          text="5 . To kill another color’s plane, you have to make your plane land on that box where other colored "
               "plane is.",
          background="gray", fg="White", font=("Arial", 16)).place(x=10, y=310)

    button_back = Button(sub_root, text="Back to the Main Menu", font=("Arial", 16), command=sub_root.destroy)
    button_back.place(x=400, y=400)
    sub_root.mainloop()


def main_RED(cx, cy):
    global box, redbox, bluebox, greenbox, yellowbox, redhome, bluehome, yellowhome, greenhome
    global red, blue, yellow, green, rap, RED, BLUE, GREEN, YELLOW, dice, nc, TURN, bb
    if RED == True and TURN == False:
        la = "RED"
        if moveCheck(red, redbox, la) == False:  # Checks if player can take a turn.
            BLUE = True
            RED = False
            clear()  # clears variable, next players turn

        if RED == True:
            ''''searches if click is made on a red game piece.'''
            for i in range(len(red)):
                if ((((cx > red[i].x0 + 13) and (cx < red[i].x + 13)) and
                     ((cy > red[i].y0 + 14) and (cy < red[i].y + 14)))
                        and (red[i].x0 == redhome[i].x) and (red[i].y0 == redhome[i].y)):
                    if rolls[0 + nc] == 6:  # If a six occurs and gamepiece is in home
                        # Game piece is moved onto the home box
                        red[i].x0 = redbox[0].x
                        red[i].y0 = redbox[0].y
                        red[i].x = redbox[0].x + 25
                        red[i].y = redbox[0].y + 25
                        red[i].num = 0
                        red[i].swap()
                        nc = nc + 1

                        if nc > len(rolls) - 1:  # check if all moves are made. so next players turn.
                            BLUE = True
                            RED = False
                            clear()
                        break
                # if gamepiece is outside home
                if ((((cx > red[i].x0 + 13) and (cx < red[i].x + 13)) and (
                        (cy > red[i].y0 + 14) and (cy < red[i].y + 14)))
                        and ((red[i].x0 > 270) or (red[i].y0 > 270))):
                    bb = (red[i].num + rolls[0 + nc])  # Winning condition

                    if bb > 57:  # prevents moves greater than allowed number
                        break
                    kill(redbox, blue, yellow, green, bluehome, yellowhome,
                         greenhome)

                    red[i].x0 = redbox[bb].x
                    red[i].y0 = redbox[bb].y
                    red[i].x = redbox[bb].x + 25
                    red[i].y = redbox[bb].y + 25
                    red[i].swap()
                    red[i].num = bb
                    doublecheck(red)  # checks if the gamepiece can be made as a double.

                    nc = nc + 1
                    if bb == 57:
                        red.remove(red[i])

                    if nc > len(rolls) - 1:
                        BLUE = True  # next players turn.
                        RED = False
                        clear()
                    break


def main_BLUE(cx, cy):
    global box, redbox, bluebox, greenbox, yellowbox, redhome, bluehome, yellowhome, greenhome
    global red, blue, yellow, green, rap, RED, BLUE, GREEN, YELLOW, dice, nc, TURN, bb
    if BLUE == True and TURN == False:
        la = "BLUE"
        if moveCheck(blue, bluebox, la) == False:
            BLUE = False
            YELLOW = True
            clear()

        if BLUE == True:

            for i in range(len(blue)):
                if ((((cx > blue[i].x0 + 13) and (cx < blue[i].x + 13)) and (
                        (cy > blue[i].y0 + 14) and (cy < blue[i].y + 14)))
                        and (blue[i].x0 == bluehome[i].x) and (blue[i].y0 == bluehome[i].y)):

                    if rolls[0 + nc] == 6:

                        blue[i].x0 = bluebox[0].x
                        blue[i].y0 = bluebox[0].y
                        blue[i].x = bluebox[0].x + 25
                        blue[i].y = bluebox[0].y + 25
                        blue[i].num = 0
                        blue[i].swap()
                        nc = nc + 1

                        if nc > len(rolls) - 1:
                            YELLOW = True
                            BLUE = False
                            clear()
                        break

                if ((((cx > blue[i].x0 + 13) and (cx < blue[i].x + 13)) and (
                        (cy > blue[i].y0 + 14) and (cy < blue[i].y + 14)))
                        and ((blue[i].x0 > 270) or (blue[i].y0 < 470))):
                    bb = ((blue[i].num) + rolls[0 + nc])
                    if bb > 57:
                        break
                        # bb= ((blue[i].num) + rolls[0 + nc]) - 52

                    kill(bluebox, red, yellow, green, redhome, yellowhome, greenhome)

                    blue[i].x0 = bluebox[bb].x
                    blue[i].y0 = bluebox[bb].y
                    blue[i].x = bluebox[bb].x + 25
                    blue[i].y = bluebox[bb].y + 25
                    blue[i].swap()
                    blue[i].num = bb
                    doublecheck(blue)
                    nc = nc + 1
                    if bb == 57:
                        # del red[i]
                        blue.remove(blue[i])

                    if nc > len(rolls) - 1:
                        YELLOW = True
                        BLUE = False
                        clear()
                    break


def main_YEllOW(cx, cy):
    global box, redbox, bluebox, greenbox, yellowbox, redhome, bluehome, yellowhome, greenhome
    global red, blue, yellow, green, rap, RED, BLUE, GREEN, YELLOW, dice, nc, TURN, bb
    if YELLOW == True and TURN == False:
        la = "YELLOW"
        if moveCheck(yellow, yellowbox, la) == False:
            YELLOW = False
            GREEN = True
            clear()

        if YELLOW == True:
            for i in range(len(yellow)):
                if ((((cx > yellow[i].x0 + 13) and (cx < yellow[i].x + 13)) and (
                        (cy > yellow[i].y0 + 14) and (cy < yellow[i].y + 14)))
                        and (yellow[i].x0 == yellowhome[i].x) and (yellow[i].y0 == yellowhome[i].y)):
                    if rolls[0 + nc] == 6:

                        yellow[i].x0 = yellowbox[0].x
                        yellow[i].y0 = yellowbox[0].y
                        yellow[i].x = yellowbox[0].x + 25
                        yellow[i].y = yellowbox[0].y + 25
                        yellow[i].num = 0
                        yellow[i].swap()
                        nc = nc + 1

                        if nc > len(rolls) - 1:
                            YELLOW = False
                            GREEN = True
                            clear()
                        break

                if ((((cx > yellow[i].x0 + 13) and (cx < yellow[i].x + 13)) and (
                        (cy > yellow[i].y0 + 14) and (cy < yellow[i].y + 14)))
                        and ((yellow[i].x0 < 470) or (yellow[i].y0 < 470))):
                    bb = ((yellow[i].num) + rolls[0 + nc])
                    if bb > 57:
                        break
                        # bb = ((yellow[i].num) + rolls[0 + nc]) - 52

                    kill(greenbox, blue, yellow, red, bluehome, yellowhome, redhome)

                    yellow[i].x0 = yellowbox[bb].x
                    yellow[i].y0 = yellowbox[bb].y
                    yellow[i].x = yellowbox[bb].x + 25
                    yellow[i].y = yellowbox[bb].y + 25
                    yellow[i].swap()
                    yellow[i].num = bb
                    doublecheck(yellow)
                    nc = nc + 1
                    if bb == 57:
                        # del red[i]
                        yellow.remove(yellow[i])

                    if nc > len(rolls) - 1:
                        YELLOW = False
                        GREEN = True
                        clear()
                    break


def main_GREEN(cx, cy):
    global greenbox, redhome, bluehome, yellowhome, greenhome, red, blue, yellow, green, rap, RED, GREEN, BLUE, YELLOW, dice, nc, TURN, bb
    if GREEN == True and TURN == False:
        la = "GREEN"
        if moveCheck(green, greenbox, la) == False:
            GREEN = False
            RED = True
            clear()

        if GREEN == True:

            for i in range(len(green)):
                if ((((cx > green[i].x0 + 13) and (cx < green[i].x + 13)) and (
                        (cy > green[i].y0 + 14) and (cy < green[i].y + 14)))
                        and (green[i].x0 == greenhome[i].x) and (green[i].y0 == greenhome[i].y)):

                    if rolls[0 + nc] == 6:

                        green[i].x0 = greenbox[0].x
                        green[i].y0 = greenbox[0].y
                        green[i].x = greenbox[0].x + 25
                        green[i].y = greenbox[0].y + 25
                        green[i].num = 0
                        green[i].swap()
                        nc = nc + 1

                        if nc > len(rolls) - 1:
                            GREEN = False
                            RED = True
                            clear()
                        break

                if ((((cx > green[i].x0 + 13) and (cx < green[i].x + 13)) and (
                        (cy > green[i].y0 + 14) and (cy < green[i].y + 14)))
                        and ((green[i].x0 < 470) or (green[i].y0 < 470))):
                    bb = ((green[i].num) + rolls[0 + nc])
                    if bb > 57:
                        break

                    kill(greenbox, blue, yellow, red, bluehome, yellowhome, redhome)

                    green[i].x0 = greenbox[bb].x
                    green[i].y0 = greenbox[bb].y
                    green[i].x = greenbox[bb].x + 25
                    green[i].y = greenbox[bb].y + 25
                    green[i].swap()
                    green[i].num = bb
                    nc = nc + 1
                    doublecheck(green)
                    if bb == 57:
                        # del red[i]
                        green.remove(green[i])

                    if nc > len(rolls) - 1:
                        GREEN = False
                        RED = True
                        clear()
                    break


def mouse_poniter():
    """This formula returns the x,y co-ordinates of the mouse pointer relative to the board."""
    mx = root.winfo_pointerx() - root.winfo_rootx()
    my = root.winfo_pointery() - root.winfo_rooty()
    return mx, my


def leftClick(event):
    """Main play function of particular  color is called on every left click."""
    red_m = mouse_poniter()
    main_RED(red_m[0], red_m[1])

    blue_r = mouse_poniter()
    main_BLUE(blue_r[0], blue_r[1])

    yellow_m = mouse_poniter()
    main_YEllOW(yellow_m[0], yellow_m[1])

    green_m = mouse_poniter()
    main_GREEN(green_m[0], green_m[1])


def display_menu():
    Label(root, text="MAIN MENU", font=("Arial", 40)).place(relx=0.49, rely=0.10, anchor=CENTER)

    button_play = Button(root, text="Play", relief="raised", font=("Arial", 30), command=main)
    button_play.place(relx=0.5, rely=0.3, anchor=CENTER)

    button_instruction = Button(root, text="Instruction", relief="raised", font=("Arial", 30), command=Instruction)
    button_instruction.place(relx=0.49, rely=0.50, anchor=CENTER)

    button_quit = Button(root, text="Quit", relief="raised", font=("Arial", 30), command=quit)
    button_quit.place(relx=0.5, rely=0.70, anchor=CENTER)


display_menu()
root.bind("<Button-1>", leftClick)
root.mainloop()
