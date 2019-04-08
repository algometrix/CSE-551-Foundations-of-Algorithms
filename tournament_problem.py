

def tournament_schedule(players, schedule=None, day=None, i=None, j=None):
    number_of_players = j - i + 1
    if day is None:
        day = number_of_players - 1

    if i is None and j is None:
        i = 0
        j = number_of_players - 1

    if schedule is None:
        schedule = []
        for _ in range(number_of_players - 1):
            schedule.append([0] * number_of_players)

    if number_of_players == 2:
        schedule[day - 1][j] = players[i]
        schedule[day - 1][i] = players[j]
    else:
        half = int((j + i) / 2) + 1
        tournament_schedule(players, day=int(day/2), i=i,
                            j=half-1, schedule=schedule)
        tournament_schedule(players, day=int(
            day/2), i=half, j=j, schedule=schedule)
        start_day = int(day/2)
        end_day = day
        #print(schedule[start_day - 1])
        #print('Day : {} | {} : {}'.format(day, i+1, j+1))
        #print('Start Day : {}'.format(start_day + 1))
        for _day in range(start_day, end_day):
            for _player in range(i, half):
                p_index = _player + _day + 1
                if p_index >= number_of_players + i:
                    p_index = (p_index % number_of_players) + half
                schedule[_day][_player] = players[p_index]
                schedule[_day][p_index] = players[_player]

    return schedule

def print_result(schedule, players):
    n_days = len(schedule)
    n_players = len(players)
    for _day in range(n_days):
        print_memory = []
        for _player in range(n_players):
            if players[_player] in print_memory:
                continue
            opponent = schedule[_day][_player]
            print_memory.append(opponent)
            print('Day {} \t: {} \tvs\t {}'.format(_day + 1, _player + 1, opponent))

if __name__ == "__main__":
    players = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13, 14, 15, 16]
    number_of_players = len(players)
    schedule = tournament_schedule(players, i=0, j=number_of_players - 1)
    print_result(schedule, players)
