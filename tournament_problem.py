# Author : Ashish Nagar

def tournament_schedule(players, schedule=None, day=None, i=None, j=None):
    # Count the number of players
    number_of_players = j - i + 1

    # Create matrix to store the schedule
    if schedule is None:
        schedule = []
        for _ in range(number_of_players - 1):
            schedule.append([0] * number_of_players)

    # If only 2 players in the group then they play against each other
    if number_of_players == 2:
        schedule[day - 1][j] = players[i]
        schedule[day - 1][i] = players[j]
    else:
        # Else arrange match between 2 groups
        half = int((j + i) / 2) + 1
        # Divide the groups into 2 halves
        tournament_schedule(players, day=int(day/2), i=i,
                            j=half-1, schedule=schedule)
        tournament_schedule(players, day=int(
            day/2), i=half, j=j, schedule=schedule)

        # After dividing arrange match between the 2 groups
        start_day = int(day/2)  # Games before day/2 have already been scheduled by divide and conquer
        end_day = day
        # Loop through each day of the remaining slots and arrange match between the players
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

def print_table(schedule, players):
    n_days = len(schedule)
    n_players = len(players)
    print('Player\t',end='')
    for _player in range(n_players):
        print('\t{} '.format(players[_player]), end=' ')
    print('\n')
    for _day in range(n_days):
        print('Day {}'.format(_day + 1), end='\t')
        for _player in range(n_players):
            print('\t{} '.format(schedule[_day][_player]), end=' ')
        print('\n')

if __name__ == "__main__":
    players = [1, 2, 3, 4, 5, 6, 7, 8 ]
    number_of_players = len(players)
    schedule = tournament_schedule(players, i=0, j=number_of_players - 1, day = number_of_players - 1)
    print_table(schedule, players)
