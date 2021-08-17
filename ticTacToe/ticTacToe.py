from tkinter import *
from tkinter import messagebox as MSG, Button
from PIL import Image, ImageTk

count = 0


def withAI():
    # Window
    root1 = Tk()
    root1.geometry("550x390")
    root1.title("Tic Tac Toe with PC")
    root1.resizable(False, False)
    root1.config(bg="#CAFAFE")
    # root1.iconbitmap("tic-tac-toe-icon.ico")

    # image1 = Image.open('tic-tac-toe.png')
    # test = ImageTk.PhotoImage(image1)
    # Label(image=test, bg="#CAFAFE").place(x=370, y=10)

    global playerX, playerO, clicked
    clicked = True
    bot = 'X'
    player = 'O'
    playerO = 0
    playerX = 0
    playerX_var = StringVar()
    playerO_var = StringVar()

    # Return True if PC is win otherwise return false if player is win
    def checkWhichMarkWon(mark):
        global board
        if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
            return True
        elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
            return True
        elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
            return True
        elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
            return True
        elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
            return True
        elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
            return True
        elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
            return True
        elif board[7] == board[5] and board[7] == board[3] and board[7] == mark:
            return True
        else:
            return False

    # Check Match is draw or not
    def checkDraw():
        global board
        for key in board.keys():
            if board[key] == ' ':
                return False
        return True

    # Check which player is win
    def checkWin():
        global board
        if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
            b1.config(bg='red')
            b2.config(bg='red')
            b3.config(bg='red')
            return True
        elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
            b4.config(bg='red')
            b5.config(bg='red')
            b6.config(bg='red')
            return True
        elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
            b7.config(bg='red')
            b8.config(bg='red')
            b9.config(bg='red')
            return True
        elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
            b1.config(bg='red')
            b4.config(bg='red')
            b7.config(bg='red')
            return True
        elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
            b2.config(bg='red')
            b5.config(bg='red')
            b8.config(bg='red')
            return True
        elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
            b3.config(bg='red')
            b6.config(bg='red')
            b9.config(bg='red')
            return True
        elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
            b1.config(bg='red')
            b5.config(bg='red')
            b9.config(bg='red')
            return True
        elif board[7] == board[5] and board[7] == board[3] and board[7] != ' ':
            b7.config(bg='red')
            b5.config(bg='red')
            b3.config(bg='red')
            return True
        else:
            return False

    # Disable all buttons
    def disableButtons():
        Label(root1, text='Reset Game', font='Helvetica 15 bold', height=1, width=14, bg="#CAFAFE").place(x=85, y=360)
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)

    # insert marker on button and display
    def insertMarker(marker, position):
        global board, playerX, playerO
        if board[position] == ' ':
            board[position] = marker
            if position == 1:
                b1.config(text='X')
            elif position == 2:
                b2.config(text='X')
            elif position == 3:
                b3.config(text='X')
            elif position == 4:
                b4.config(text='X')
            elif position == 5:
                b5.config(text='X')
            elif position == 6:
                b6.config(text='X')
            elif position == 7:
                b7.config(text='X')
            elif position == 8:
                b8.config(text='X')
            elif position == 9:
                b9.config(text='X')

            if checkDraw():
                disableButtons()
            elif checkWin():
                if marker == 'X':
                    MSG.showinfo('AI Tic Tac Toe', 'Player X is winner')
                    playerX += 1
                    playerX_var.set('Player X: ' + str(playerX))
                    disableButtons()
                else:
                    MSG.showinfo('AI Tic Tac Toe', 'Player O is winner')
                    playerO += 1
                    playerO_var.set('Player O: ' + str(playerO))
                    disableButtons()
        else:
            MSG.showwarning('AI Tic Tac Toe', 'Please choose other position')
        return

    # AI move
    def botMove():
        global clicked, board
        if clicked == False:
            clicked = True
            bestScore = -800
            bestMove = 0
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = 'X'
                    score = minimax(board, 0, False)
                    board[key] = ' '
                    if score > bestScore:
                        bestScore = score
                        bestMove = key
            insertMarker(bot, bestMove)
            return

    # minimax algorithm for best move
    def minimax(board, depth, isMax):
        if checkWhichMarkWon(bot):
            return 1
        elif checkWhichMarkWon(player):
            return -1
        elif checkDraw():
            return 0

        if isMax:
            bestScore = -800
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[key] = ' '
                    if score > bestScore:
                        bestScore = score
            return bestScore
        else:
            bestScore = 800
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[key] = ' '
                    if score < bestScore:
                        bestScore = score
            return bestScore

    # function for button
    def buttonClick(b, num):
        global clicked, board
        Label(root1, text='Game is started', font='Helvetica 15 bold', height=1, width=14, bg='#CAFAFE').place(x=85, y=360)
        if b['text'] == ' ' and clicked == True:
            b['text'] = 'O'
            board[num] = 'O'
            clicked = False
            if checkDraw():
                disableButtons()
                MSG.showinfo('AI Tic Tac Toe', 'Matc is draw')
                clicked = True
            else:
                botMove()
        else:
            MSG.showwarning('AI Tic Tac Toe', 'Please choose another position')

    # Design game
    def reset():
        global board
        board = {1: ' ', 2: ' ', 3: ' ',
                 4: ' ', 5: ' ', 6: ' ',
                 7: ' ', 8: ' ', 9: ' '}
        global b1, b2, b3, b4, b5, b6, b7, b8, b9, resetButton
        Label(root1, text='Start Game', font='Helvetica 15 bold', height=1, width=14, bg='#CAFAFE').place(x=85, y=360)
        b1 = Button(root1, text=' ', font='Helvetica 20', height=3, width=6, bg='grey',
                    command=lambda: buttonClick(b1, 1))
        b2 = Button(root1, text=' ', font='Helvetica 20', height=3, width=6, bg='grey',
                    command=lambda: buttonClick(b2, 2))
        b3 = Button(root1, text=' ', font='Helvetica 20', height=3, width=6, bg='grey',
                    command=lambda: buttonClick(b3, 3))
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        b4 = Button(root1, text=' ', font='Helvetica 20', height=3, width=6, bg='grey',
                    command=lambda: buttonClick(b4, 4))
        b5 = Button(root1, text=' ', font='Helvetica 20', height=3, width=6, bg='grey',
                    command=lambda: buttonClick(b5, 5))
        b6 = Button(root1, text=' ', font='Helvetica 20', height=3, width=6, bg='grey',
                    command=lambda: buttonClick(b6, 6))
        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)

        b7 = Button(root1, text=' ', font='Helvetica 20', height=3, width=6, bg='grey',
                    command=lambda: buttonClick(b7, 7))
        b8 = Button(root1, text=' ', font='Helvetica 20', height=3, width=6, bg='grey',
                    command=lambda: buttonClick(b8, 8))
        b9 = Button(root1, text=' ', font='Helvetica 20', height=3, width=6, bg='grey',
                    command=lambda: buttonClick(b9, 9))
        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

    reset()
    resetButton = Button(root1, text='RESET', font='Helvetica 13 bold', height=1, width=15, bg='#4e5153', fg='#ffffff',
                         command=reset)
    resetButton.place(x=360, y=260)
    Button(root1, text='EXIT', font='Helvetica 13 bold', height=1, width=15, bg='#4e5153', fg='#ffffff',
           command=root1.destroy).place(x=360, y=310)
    playerX_var.set('Player X : ' + str(playerX))
    playerO_var.set('Player O : ' + str(playerO))
    Label(root1, text='SCORE', font='Helvetica 20 bold', height=1, width=10, bg="#CAFAFE", fg='#FC0445').place(x=380, y=140)
    Label(root1, textvariable=playerX_var, font='Helvetica 15 bold', height=1, width=15, bg="#CAFAFE").place(x=375, y=180)
    Label(root1, textvariable=playerO_var, font='Helvetica 15 bold', height=1, width=15, bg="#CAFAFE").place(x=375, y=210)

    root1.mainloop()


withAI()
