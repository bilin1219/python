import copy

class TicTacToe:
    """
    Rules for Tic-Tac-Toe
    The game is played on a grid that's 3 squares by 3 squares.
    You are X , your friend (or the computer in this case) is O . Players take turns putting their marks in empty squares.
    The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
    When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
    """

    class State:
        pass

    def __init__(self):
        self.state = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]


    def player(self, state):
        # - player(s) : returns which player to move in state s
        num_x = 0
        num_o = 0
        for row in state:
            for cell in row:
                if cell == "X":
                    num_x += 1
                elif cell == "O":
                    num_o += 1

        return "X" if num_o >= num_x else "O"

    def actions(self, state):
        # - actions(s) : return legal moves in state s
        legal_moves = []
        for i, row in enumerate(state):
            for j, cell in enumerate(row):
                if not (cell == "X" or cell == "O"):
                    legal_moves.append((i, j))

        return legal_moves

    def result(self, state, action):
        # - result(s, a) : return state after action a taken in state s
        result = copy.deepcopy(state)
        i, j = action
        result[i][j] = self.player(state)
        return result

    def terminal(self, state):
        # - terminal(s) : checks if state s is a terminal state
        if len(self.actions(state)) == 0:
            return True

        for player in "XO":
            for index in range(0, 3):
                # row test
                if state[index][0] == player and state[index][1] == player and state[index][2] == player:
                    return True
                # col test
                if state[0][index] == player and state[1][index] == player and state[2][index] == player:
                    return True

            d1 = state[0][0] == player and state[1][1] == player and state[2][2] == player
            d2 = state[0][2] == player and state[1][1] == player and state[2][0] == player
            if d1 or d2:
                return True

        return False

    def utility(self, state):
        # - utility(s) : final numerical value for terminal state s
        for player in "XO":
            for index in range(0, 3):
                # row test
                if state[index][0] == player and state[index][1] == player and state[index][2] == player:
                    return 1 if player == "X" else -1
                # col test
                if state[0][index] == player and state[1][index] == player and state[2][index] == player:
                    return 1 if player == "X" else -1

            d1 = state[0][0] == player and state[1][1] == player and state[2][2] == player
            d2 = state[0][2] == player and state[1][1] == player and state[2][0] == player
            if d1 or d2:
                return 1 if player == "X" else -1

        return 0

    def max_value(self, state):
        if self.terminal(state):
            return self.utility(state)

        v = -10
        for action in self.actions(state):
            v = max(v, self.min_value(self.result(state, action)))
        return v

    def min_value(self, state):
        if self.terminal(state):
            return self.utility(state)

        v = +10
        for action in self.actions(state):
            v = min(v, self.max_value(self.result(state, action)))
        return v

    def play(self):
        while not self.terminal(self.state):
            if self.player(self.state) == "X":
                move = int(input("Please enter your move: ")) - 1
                row = move // 3
                col = move % 3
                self.state = self.result(self.state, tuple(row, col))
            else:
                v = +10
                move = ()
                for action in self.actions(self.state):
                    vp = self.max_value(self.result(self.state, action))
                    if v > vp:
                        v = vp
                        move = action

                self.state = self.result(self.state, move)

            self.display()

    def display(self):
        # The function draws the computer's move and updates the board.
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|   ' + self.state[0][0] + '   |   ' + self.state[0][1] + '   |   ' + self.state[0][2] + '   |')
        print('|       |       |       |')
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|   ' + self.state[1][0] + '   |   ' + self.state[1][1] + '   |   ' + self.state[1][2] + '   |')
        print('|       |       |       |')
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|   ' + self.state[2][0] + '   |   ' + self.state[2][1] + '   |   ' + self.state[2][2] + '   |')
        print('|       |       |       |')
        print('+-------+-------+-------+')


game = TicTacToe()
game.display()
game.play()
