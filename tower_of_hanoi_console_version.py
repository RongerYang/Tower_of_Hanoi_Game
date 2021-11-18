def move_validation(disks, source, dest):
    if source in [0, 1, 2] and dest in [0, 1, 2] and len(disks[source]) > 0:
        if disks[dest] == []:
            return True
        elif disks[source][0] < disks[dest][0]:
            return True
    return False

def is_game_success(disks):
    return len(disks[0]) == 0 and len(disks[1]) == 0

def hanoi_move(disks, source, dest):
    if move_validation(disks, source, dest):
        disks[dest].insert(0, disks[source].pop(0))

    return disks


def tower_of_hanoi_sol(disks, disk_num, source, auxiliary, dest):
    if (disk_num == 1):
        print('Move disk {} from rod {} to rod {}.'.format(disks[source][0], source, dest))
        disks = hanoi_move(disks, source, dest)
        print(disks)
        return disks
    tower_of_hanoi_sol(disks, disk_num - 1, source, dest, auxiliary)
    print('Move disk {} from rod {} to rod {}.'.format(disks[source][0], source, dest))
    disks = hanoi_move(disks, source, dest)
    print(disks)
    tower_of_hanoi_sol(disks, disk_num - 1, auxiliary, source, dest)

def start_game():
    disk_num = int(input('Enter the number of disks: '))
    disks = [[i for i in range(1, disk_num + 1)], [], []]
    min_moves = 2 ** disk_num - 1
    count_moves = 0
    print(disks)

    reader = input('Would you like to play the game or check the solution? \n'
                   'Enter p for playing the game, enter s for checking the solution, enter q to quit: ')

    while reader != 'p' and reader != 's' and reader != 'q':
        print("Sorry, your input is invalid, please try again.")
        reader = input('Would you like to play the game or check the solution? \n'
                       'Enter p for playing the game, enter s for checking the solution, enter q to quit: ')
    else:
        if reader == 's':
            tower_of_hanoi_sol(disks, disk_num, 0, 1, 2)
            print('Minimum Number of Moves: {}'.format(min_moves))
            reader = input('Enter s to restart the game, otherwise quit the game: ')
            if reader == 's':
                start_game()
            else:
                exit(0)
        elif reader == 'p':
            user_play_version(count_moves, min_moves, disks)
        elif reader == 'q':
            exit(0)

def user_play_version(count_moves, min_moves, disks):
    source = input(
        'Enter the source rod where the top disk will be moved \n'
        '(rods named 0, 1, 2 respectively from left to right): ')
    while source != '0' and source != '1' and source != '2':
        print('The source rod should be an interger from 0, 1, 2. Try again!')
        source = input(
            'Enter the source rod where the top disk will be moved \n'
            '(rods named 0, 1, 2 respectively from left to right): ')

    dest = input(
        'Enter the destination rod where the top disk will moved \n'
        '(rods named 0, 1, 2 respectively from left to right): ')
    while dest != '0' and dest != '1' and dest != '2':
        print('The destination rod should be an interger from 0, 1, 2. Try again!')
        dest = input(
            'Enter the destination rod where the top disk will moved \n'
            '(rods named 0, 1, 2 respectively from left to right): ')

    else:
        disks = hanoi_move(disks, int(source), int(dest))
        count_moves += 1
        print("Move # {}:".format(count_moves))
        print(disks)
        print("Minimum Moves: {}".format(min_moves))
        success = is_game_success(disks)

        if success == True:
            print("Solved! Congratulations!")
            reader = input('Enter s to restart the game, otherwise quit the game: ')
            if reader == 's':
                start_game()
            else:
                exit(0)
        else:
            user_play_version(count_moves, min_moves, disks)



if __name__ == '__main__':
    start_game()