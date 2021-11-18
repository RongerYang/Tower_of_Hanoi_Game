from Controllers.console_controller import ConsoleController
from Controllers.gui_controller import GUIController

if __name__ == '__main__':
    disk_input = int(input('Enter the number of disks: '))
    version = input("Choose the game version to start the Tower of Hanoi Game.\n"
                    "Enter 'g' for GUI version, enter 'c' for text console version: ")
    while version != 'g' and version != 'c':
        print("Your input version is invalid, please try again!")
        version = input("Enter the game version to start the Tower of Hanoi Game.\n"
                        "Enter 'g' for GUI version, enter 'c' for text console version: ")
    else:
        if version == 'c':
            cc = ConsoleController(disk_num = disk_input)
            cc.play_game()
        elif version == 'g':
            mode = input("Choose the mode to play: Enter 'p' for user play mode, enter 's' for the solution mode.")
            while mode != 'p' and mode != 's':
                print("Your input mode is invalid, please try again!")
                mode = input("Choose the mode to play: Enter 'p' for user play mode, enter 's' for the solution mode.")
            else:
                if mode == 'p':
                    gui = GUIController(disk_input, 3, 1024, 320, 20)
                elif mode == 's':
                    print("Please run the main function in 'gui_solution_controller.py' file.")
