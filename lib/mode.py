"""
mode of play in game
ai: play by ai agent
real: play by real player
"""

def _strBoard():
    "Create a board using string type"
    board = ''
    tmp = 1

    for i in range(3):
        for j in range(3):
            board += str(tmp)
            if j < 2:
                board += ' '
            tmp += 1
        if i < 2:
            board += '\n'
    return board

help = {
    "mode": "1. ai \n2. real",
    "positions": f"play into the board using the numbering in the board\n{_strBoard()}",
}


def _assignPlayMode(players_mode, player, who_play):
    players_mode[player] = who_play


def chooseMode(players_mode):
    # choose mode for each player (real or ai)
    mode_options = ("real", "ai")

    X_player_mode = input("X-player: AI or Real? - ")
    O_player_mode = input("O-player: AI or Real? - ")

    if not (X_player_mode.lower() in mode_options and O_player_mode.lower() in mode_options):
        raise Exception("Invalid mode!")
    
    _assignPlayMode(players_mode, 'X', X_player_mode)
    _assignPlayMode(players_mode, 'O', O_player_mode)
    

def getHelp(cmd):
    if cmd.lower() == "all":
        for key, value in help.items():
            print(f"{key} - \n\t{value}\n")
    else:
        print(help.get(cmd.lower()))