class ConnectFour(object):

    def __init__(self, game_state):
        self.game_state = game_state
        self.player = None
        self.turns = 0

    def get_game_state(self):
        return self.game_state

    def get_player(self):
        return self.player

    def get_num_moves(self):
        return self.turns

    def count_discs(self):
        """
        Returns a list which contains the number of "y" discs and "r" discs inn the game state.
        """
        num_y = 0
        num_r = 0
        for row in self.game_state:
            for column in row:
                if column == 'y':
                    num_y += 1
                if column == 'r':
                    num_r += 1

        self.turns = num_y + num_r
        return [num_y, num_r]

    def drop_disc_into_column(self, column, player):
        """
        Traverse the game_state starting from the bottom
            Checking each column of that specific row has a None value
                f there is change that value to the players value and break.
        :param column: - A column index starting with 0 to len(game_state[0])
        :param player: - "Y" or "r"
        :return:
        """

        for i in reversed(range(len(self.game_state))):
            if self.game_state[i][column] is None:
                self.game_state[i][column] = player
                break
        else:
            raise Exception("No more available slots in column : {}!".format(column))

    def forward_diagonals(self):
        """
        Return a list of lists of every forward diagonals on the game state.
        :return:
        """
        h, w = len(self.game_state), len(self.game_state[0])
        diagonals = []
        for i in range(h + w - 1):
            temp_list = []
            for j in range(max(i - h + 1, 0), min(i + 1, w)):
                x = j
                y = h - i + j - 1
                temp_list.append(self.game_state[y][x])
            diagonals.append(temp_list)
        return diagonals

    def backward_diagonals(self):
        """
        Return a list of lists of every backward diagonals on the game state.
        """
        h, w = len(self.game_state), len(self.game_state[0])
        diagonals = []
        for i in range(h + w - 1):
            temp_list = []
            for q in range(max(i - h + 1, 0), min(i + 1, w)):
                x = q
                y = i - q
                temp_list.append(self.game_state[y][x])
            diagonals.append(temp_list)
        return diagonals

    def columns(self):
        """
        Return a list of lists of every column on the game state.
        """

        columns = []
        for i in range(len(self.game_state[0])):
            temp_list = []
            for j in range(len(self.game_state)):
                temp_list.append(self.game_state[j][i])
            columns.append(temp_list)
        return columns
