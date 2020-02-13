import heapq
from game import Game
#import numpy as np


def a_star(start, h, goal, open):
    closed_set = set()
    open_set = set()
    g_value = {}
    f_value = []
    parent = {}

    # initialization
    f_start = h(start)
    g_value[start] = 0
    open_set.add(start)
    heapq.heappush(f_value, (f_start, start))

    while open_set:
        cost, node = heapq.heappop(f_value)

        if goal(node):
            return make_path(node, parent)

        closed_set.add(node)
        open_set.remove(node)

        for n in open(node):
            tentative_g_score = g_value[node] + 1

            # only works if your heuristic is consistent (monotonic)
            if n in closed_set:
                continue

            if n not in open_set or tentative_g_score < g_value[n]:
                parent[n] = node
                g_value[n] = tentative_g_score
                actual_f_value = tentative_g_score + h(n)

                if n in open_set:
                    # O(N) rebuild of the heap (Python heap doesn't have decrease-key operation)
                    for i, (p, x) in f_value:
                        if x == n:
                            f_value[i] = (actual_f_value, n)
                            break
                    heapq.heapify(f_value)
                else:
                    open_set.add(n)
                    heapq.heappush(f_value, (actual_f_value, n))


def make_path(node, parent):
    path = [node]

    while node in parent:
        node = parent[node]
        path.insert(0, node)

    return path


if __name__ == '__main__':
    import time

    start = time.time()

    from game import Game

    def goal(game):
        return game.is_game_finished()

    def open(game):
        if game.is_game_finished():
            return

        for move in "nsew":
            new_game = game.play(move)

            if (new_game != game):
                yield new_game

    def trivial_heuristic(game):
        return 0

    def numberOfTiles_heuristic(game):
        numberOfTiles = 0
        for i in range(len(game.board)):
            for j in range(len(game.board)):
                if game.board[i][j]  > 0:
                    numberOfTiles += 1
        return numberOfTiles

    def h1(game):
        board = game.board

        Weighted_sum = [[1, 1, 2, 4],
                        [1, 2, 8, 256],
                        [2, 16, 128, 512],
                        [32, 64, 1024, 2048]]
        cells = 0

        for i in range(len(board)):
            for j in range(len(board)):
                cells += board[i][j] * Weighted_sum[i][j]

        return cells

    def h2(game):
        Max_tile = 0
        row = 4
        col = 4
        map = [[0] * row for i in range(col)]
        
        for x in range(row):
            for y in range(col):
                Max_tile = max(Max_tile, map[x][y])

        return Max_tile

    def h3(game):
        board = game.board
        empty_tiles = []
        row  = 4
        col = 4
        for y in range(row):
            for x in range(col):
                if trivial_heuristic(board[y][x]):
                    empty_tiles.append([y, x])

        return len(empty_tiles)

    game = Game(4, 32)
    path = a_star(game, trivial_heuristic, goal, open)
    path1 = a_star(game, numberOfTiles_heuristic, goal, open)
    path2 = a_star(game, h1, goal, open)
    path3 = a_star(game, h2,goal,open)
    path4 = a_star(game, h3,goal,open)

    #print(path)
    #print(len(path))
    #print(time.time() - start)

    #print(" ")

    #print(path1)
    #print(len(path1))
    #print(time.time() - start)

    #print(" ")

    #print(path2)
    #print(len(path2))
    #print(time.time() - start)

    #print(" ")

    #print(path3)
    #print(len(path3))
    #print(time.time() - start)

    #print(" ")

    print(path4)
    print(len(path4))
    print(time.time() - start)
