import random

from lib import winPos


class Agent:
    def __init__(self):
        self.weight = {}
        self.opp = 1
        self.free = 1

    def buildWeight(self, board, cur_player, players):
        win_pos = winPos()
        for i in range(3):
            for j in range(3):
                pos = (i, j)
                pos_move = Agent.getPotMove(board, pos, players)
                if pos_move:
                    pos_list = Agent.joinPotMovesSides(pos_move, pos)
                    self.assignWeight(board, pos, pos_list, cur_player, players)


    @staticmethod
    def getPotMove(board, pos, players):
        """
        getPotMove: get potential/possible best moves of a player

        return: list of win-pos (win-pos is a list of potential win in tuple(x,y))
        """

        x, y = pos
        if board[x][y] in players:
            return None

        else:
            pot = []
            for win_pos in winPos():
                if pos in win_pos:
                    pot.append(win_pos)
            return pot

    @staticmethod
    def joinPotMovesSides(potMoves, cur_pos):
        pos_list = []
        for pos in potMoves:
            pos_list.extend(pos)

        # join all the win pos together in a list and
        # exempt the pos whose weight is being computed

        return list(filter(
            lambda val: val != cur_pos, pos_list
            ))

    def assignWeight(self, board, cur_pos, potMoves, cur_player, players):
        self.weight[cur_pos] = 0
        for pos in potMoves:
            x, y = pos
            if board[x][y] in players:
                self.weight[cur_pos] += self.opp + random.random()
                print(self.weight[cur_pos])

            elif board[x][y] == cur_player:
                self.weight[cur_pos] += self.opp + random.random()
                print(self.weight[cur_pos])
            else:
                print(self.weight[cur_pos])
                self.weight[cur_pos] += self.free
