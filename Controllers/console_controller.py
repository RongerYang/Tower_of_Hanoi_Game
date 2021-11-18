from Models.tohg_model import ToHG, IllegalMoveError

"""
Apply move from origin to destination in model.

@param ToHG model: model to modify
@param int origin: rod number (index from 0) of disk to move
@param int dest: rod number you want to move disk to
@rtype: None
"""
def move(model, origin, dest):
    if dest == origin:
        print("Invalid movement.")
    elif dest not in model.rods.keys() \
            or origin not in model.rods.keys():
        if dest not in model.rods.keys():
            print("Destination rod is out of range.")
        if origin not in model.rods.keys():
            print("Source rod is out of range.")
    elif model.rods[origin] == []:
            print("Source rod is empty.")
    elif model.rods[dest] != [] \
            and model.get_top_disk(origin).size \
                    > model.get_top_disk(dest).size:
        print("Cannot stack larger disk on smaller.")
    else:
        return model.move(origin, dest)


"""
Return the solution for the Tower of Hanoi Game 
(explicitly indicate number of rods = 3)

@param ToHG model: the ToHG model to solve
@param int disk_num: the number of disks
@param int source: the index of the origin rod
@param int auxiliary: the index of the auxiliary rod
@param int dest: the index of the destination rod
@rtype: None
"""
def tower_of_hanoi_sol(model, disk_num, source, auxiliary, dest):
    if (disk_num == 1):
        print('Move # {}: Move disk from rod {} to rod {}.'.format(model.number_of_moves() + 1, source, dest))
        move(model, source, dest)
        print(model.__str__())
    else:
        tower_of_hanoi_sol(model, disk_num - 1, source, dest, auxiliary)
        print('Move # {}: Move disk from rod {} to rod {}.'.format(model.number_of_moves() + 1, source, dest))
        move(model, source, dest)
        print(model.__str__())
        tower_of_hanoi_sol(model, disk_num - 1, auxiliary, source, dest)


"""
Controller for text console

=== Attributes ===
    @param ToHG model: an ToHG model
"""
class ConsoleController:
    """
    Initialize a new ConsoleController self.

    @param ConsoleController self: this ConsoleController self
    @param int rod_num: initial number of rods in ToHG
    @param int disk_num:
        initial number of disks filled in the first rod in ToHG
    @rtype: None
    """
    def __init__(self, rod_num = 3, disk_num = 3):
        self.model = ToHG(rod_num, disk_num)

    """
    Play Console-based game.

    @param ConsoleController self: this ConsoleController self
    @rtype: None
    """
    def play_game(self):
        print("Instructions: '1 3' means move top disk from the first rod to the third rod.")
        print("Enter 'e' to exit the game, enter 's' to see the solution.")
        print(self.model.__str__())
        print("Minimal Number of Moves: {}".format(2 ** self.model.get_number_of_disks() - 1))
        potential_move = input("Please Enter Move {}: ".format(self.model.number_of_moves() + 1))
        success = self.model.check_success()
        while (not potential_move == "e") and (not potential_move == "s") and (not success):
            str_list = potential_move.split()
            num_list = [int(x) - 1 for x in str_list]
            if len(num_list) != 2:
                print("Illegal input. Please read instructions.")
            else:
                move(self.model, num_list[0], num_list[1])
            print(self.model.__str__())
            print("Minimal Number of Moves: {}".format(2 ** self.model.get_number_of_disks() - 1))
            success = self.model.check_success()
            if not success:
                potential_move = input("Please Enter Move {}: ".
                                   format(self.model.number_of_moves() + 1))

        if potential_move == "e":
            exit("You have successfully exit the game.")
        elif potential_move == "s":
            tower_of_hanoi_sol(self.model, self.model.get_number_of_disks(), 0, 1, 2)
            print("Minimal Number of Moves: {}".format(2 ** self.model.get_number_of_disks() - 1))
        if self.model.check_success():
            print("Your Number of Moves: {}".format(self.model.number_of_moves()))
            print("Solved! Congratulations!")
