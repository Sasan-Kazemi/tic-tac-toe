class tictactoe:
    def __init__(self):
        self.board = [[0, 0, 0], 
                      [0, 0, 0],
                      [0, 0, 0]]
        self.current = 'X'
        self.counter = 0
        self.status = 'on going'
        self.dict = {"X" : "O", "O" : "X"}

    def check(self):
        if self.counter < 5:
            return

        maind, antid = True, True
        for i in range(3):
            row, col = True, True

            if not self.board[i][i] in ["X", "O"] or self.board[i][i] != self.board[0][0]:
                maind = False

            if not self.board[i][2 - i] in ["X", "O"] or self.board[i][2 - i] != self.board[2][0]:
                antid = False

            for j in range(3):

                if not self.board[i][j] in ["X", "O"]  or self.board[i][j] != self.board[i][0]:
                    row = False

                if not self.board[j][i] in ["X", "O"] or self.board[j][i] != self.board[0][i]:
                    col = False

            if row:
                self.status = "ended"
                print(f"The Winner is {self.board[i][0]}")
                return

            if col:
                self.status = "ended"
                print(f"The Winner is {self.board[0][i]}")
                return

        if maind:
                self.status = "ended"
                print(f"The Winner is {self.board[0][0]}")
                return

        if antid:
                self.status = "ended"
                print(f"The Winner is {self.board[2][0]}")
                return

        if self.counter == 9:
            self.status = "ended"
            print("The Game is Tie")

    def move(self, pos):
        if self.counter == 9 or self.status == "ended":
            print("The Game is Over")
            return
        
        i = (pos - 1) // 3
        j = (pos - 1) % 3

        if self.board[i][j] != 0:
            print("Please Choose Another position")
            return

        self.board[i][j] = self.current
        self.current = self.dict[self.current]
        self.counter += 1
        self.check()

    def print(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end=" ")
            print()
        
game = tictactoe()
while game.status != "ended":
    game.print()   
    print()
    game.move(int(input()))
    print()
