import numpy as np

'''
 1 2
[0 0]
'''


def tournament_schedule(players, schedule=None, day=None, i=None, j=None):
    number_of_players = len(players)
    if day is None:
        day = number_of_players - 1
    else:
        day -= 1

    if i is None and j is None:
        i = 0
        j = number_of_players - 1

    if schedule is None:
        schedule = []
        for _ in range(number_of_players - 1):
            schedule.append([0] * number_of_players)

    if number_of_players == 2:
        schedule[day][j] = players[i]
        schedule[day][i] = players[j]
    else:
        half = int((i + j) / 2) + 1
        fir_half = tournament_schedule(players[:half], day=day, i=i, j=half, schedule=schedule)
        sec_half = tournament_schedule(players[:half], day=day, i=half, j=j, schedule=schedule)

    print(np.matrix(schedule))
    return 0


if __name__ == "__main__":
    players = [1, 2, 3, 4]
    print(' ', end='')
    print(players)
    result = tournament_schedule(players)
    print('Schedule')

    print(result)
