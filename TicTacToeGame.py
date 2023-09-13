# Import the tkinter GUI library and using it as 'tk'
import tkinter as tk
# Creating the main window
storage = tk.Tk()
# Setting the window size
storage.geometry('800x500')
# Setting the title of the window
storage.title("Tic Tac Toe - GAME")

# Designing the GUI components
# Label for "TIC-TAC-TOE" with custom font and red text color
tk.Label(storage, text="TIC-TAC-TOE", font=('ariel', 45,), fg='red').pack()
# Labeling for "GAME" with custom font
tk.Label(storage, text="GAME", font=('Ariel', 25)).pack()
# Creating a label to display the current player's turn ("X's turn")
status_label = tk.Label(storage, text="X's turn", font=('Ariel', 15), bg='blue', fg='snow')
# Adding the status_label to the window and make it fill the horizontal space
status_label.pack(fill=tk.X)

# Function to reset the game
def playAgain():
    #Accessing the global varriable to reset x
    global currentChar
    currentChar = 'X'
    #loop through each point in xoPointCountr
    for point in xoPointCountr:
        #setting the state of the button associated with the point to normal which is enabled
        point.button.configure(state=tk.NORMAL)
        #reset the point to clear text and value
        point.reset()
    #Updating the status_label to indicate it's x's turn again
    status_label.configure(text="X's turn")
    #hide the play again button from display
    playAgain.pack_forget()

# Create a "Play again" button
playAgain = tk.Button(storage, text='Play again', font=('Ariel', 15), fg='red', command=playAgain)
# Initialize the current player character
currentChar = "X"
# Create the play area frame with a white background
play_area = tk.Frame(storage, width=500, height=300, bg='white')
# Lists to store X and O points
# xoPointCountr is a list to store all the points (cells) on the game board
xoPointCountr = []
#Store all the X points
xPointCountr = []
#Store all the 0 points
oPointCountr = []

# Class to represent each cell on the game board
class XOPoint:
    def __init__(self, x, y):
        #initialize x and y coordinates of the cell
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

    def set(self):
        global currentChar
        if not self.value:
            self.button.configure(text=currentChar, bg='snow', fg='black')
            self.value = currentChar
            if currentChar == "X":
                xPointCountr.append(self)
                currentChar = "O"
                status_label.configure(text="O's turn")
            elif currentChar == "O":
                oPointCountr.append(self)
                currentChar = "X"
                status_label.configure(text="X's turn")
        check_win()

    def reset(self):
        self.button.configure(text="", bg='lightgray')
        if self.value == "X":
            xPointCountr.remove(self)
        elif self.value == "O":
            oPointCountr.remove(self)
        self.value = None

# Create the game board (3x3 grid) and store points in xoPointCountr
for x in range(1, 4):
    for y in range(1, 4):
        xoPointCountr.append(XOPoint(x, y))

# Class to represent winning possibilities
class WinningPossibility:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def check(self, for_chr):
        p1_satisfied = False
        p2_satisfied = False
        p3_satisfied = False
        if for_chr == 'X':
            for point in xPointCountr:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        elif for_chr == 'O':
            for point in oPointCountr:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        return all([p1_satisfied, p2_satisfied, p3_satisfied])

# List of winning possibilities
winning_possibilities = [
    WinningPossibility(1, 1, 1, 2, 1, 3),
    WinningPossibility(2, 1, 2, 2, 2, 3),
    WinningPossibility(3, 1, 3, 2, 3, 3),
    WinningPossibility(1, 1, 2, 1, 3, 1),
    WinningPossibility(1, 2, 2, 2, 3, 2),
    WinningPossibility(1, 3, 2, 3, 3, 3),
    WinningPossibility(1, 1, 2, 2, 3, 3),
    WinningPossibility(3, 1, 2, 2, 1, 3)
]

# Function to disable the game
def disable_game():
    for point in xoPointCountr:
        point.button.configure(state=tk.DISABLED)
    playAgain.pack()

# Function to check for a winner
def check_win():
    for possibility in winning_possibilities:
        if possibility.check('X'):
            status_label.configure(text="Result: X won!")
            disable_game()
            return
        elif possibility.check('O'):
            status_label.configure(text="Result: O won!")
            disable_game()
            return
    if len(xPointCountr) + len(oPointCountr) == 9:
        status_label.configure(text="Result: Draw!")
        disable_game()

# Pack the play area frame with some padding
play_area.pack(pady=10, padx=10)

# Start the Tkinter main loop
storage.mainloop()
