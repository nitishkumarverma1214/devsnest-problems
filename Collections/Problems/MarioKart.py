from cmath import inf


def solve(mat):
    least= inf
    sec_least = inf
    players_with_sec_least = []

    for player in mat:
        if player[1]<least:
            sec_least = least
            least = player[1]
        elif player[1] < sec_least and player[1] != least:
            sec_least = player[1]
    
    for pl,sc in mat:
        if sc== sec_least:
            players_with_sec_least.append(pl)
    return sorted(players_with_sec_least)


print(solve([[3 ,37],[1 ,41],[2, 37],[5 ,41],[4 ,35]]))