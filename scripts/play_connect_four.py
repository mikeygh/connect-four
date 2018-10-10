from app.ConnectFour import ConnectFour


def get_current_player(game_state):
    """
    To determine the current player, we would need to count up
        all the  discs already played in the current game_state.
    :param game_state: - a 2 Dimensional list
    :return:  return "r" or "y" depending on which players turn it is.
    """
    cf = ConnectFour(game_state)
    num_y, num_r = cf.count_discs()

    if num_y > num_r:
        return "r"
    if num_y == num_r:
        return "y"


def is_state_valid(game_state):
    """
    Determine if the state of the game_state is valid.

    :param game_state: - a 2 Dimensional list
    :return: - return True if the state is valid Falise if it is not.
    """
    cf = ConnectFour(game_state)
    num_y, num_r = cf.count_discs()

    # If there are two many discs of either color return false. The state is invalid.
    if num_r > num_y or (num_y - num_r) > 1:
        return False
    return True


def play(game_state, column, player):
    """
    Based on the game state try to  drop a disc in a particular column
    :param game_state:  - a 2 Dimensional list
    :param column:  - A column index starting with 0 to len(game_state[0])
    :param player: - "Y" or "r"
    :return:  - Return the game_state if successful in playing a piece.
    """
    cf = ConnectFour(game_state)
    try:
        cf.drop_disc_into_column(column, player)
        return game_state
    except Exception:
        return "Bad selection, please try another column!"


def get_winner(game_state):
    """
    Check the game state for any four diagonals or across for one color.

    :param game_state: - a 2 Dimensional list
    :return: - True if there is a winner. False if there is not one.
    """
    cf = ConnectFour(game_state)
    game_state_lists = [cf.forward_diagonals(), cf.backward_diagonals(), cf.columns(), game_state]
    for game_state in game_state_lists:
        result = check_connect_four(game_state)
        if result:
            return True
    return False


def check_connect_four(lists):
    """
    Check the lists within the 2D lists and check for four contiguous y's or r's.
    :param lists: -
    :return:
    """
    for list in lists:
        if len(list) < 4:
            continue
        joined_list = "".join(item for item in list if item)
        if "yyyy" in joined_list or "rrrr" in joined_list:
            print("The winning Row -> {}".format(list))
            return True
    return False
