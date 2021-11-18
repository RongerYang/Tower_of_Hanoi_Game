"""
Model of Tower of Hanoi Game.

Rods holding stacks of disks, enforcing the constraint
that a larger disk may not be placed on a smaller one.

=== Attributes ===
    @param dict rods:
       dictionary with keys being indexed rods and values being list of Disk
       objects with different radius_sizes under corresponding indexed rods.
    @param MoveSequence move_seq:
       a sequence of moves of disks
"""
from Models.disk_model import Disk
from Models.move_sequence_model import MoveSequence

class ToHG:

    """
    Initialize a ToHG object with number of rods being rod_num and number of
    disks being disk_num.

    @param ToHG self: this ToHG self
    @param int rod_num: number of rods if applicable, or 3 rods as default
    @param int disk_num: number of disks at the first rod if applicable,
        or 3 disks as default
    @rtype: None
    """
    def __init__(self, rod_num = 3, disk_num = 3):
        self.rods = {}
        self._move_seq = MoveSequence()
        for i in range(rod_num):
            self.rods[i] = []
            if i == 0:
                for j in range(disk_num):
                    self.rods[i].insert(0, Disk(j+1))

    """
    Return the move sequence of this ToHG object.

    @param ToHG self: this ToHG self
    @rtype: MoveSequence
    """
    def get_move_seq(self):
        return self._move_seq

    """
    Return number of disks of ToHG self

    @param ToHG self: this ToHG self
    @rtype: int
    """
    def get_number_of_disks(self):
        return sum([len(self.rods[i]) for i in range(len(self.rods))])

    """
    Return the Disk object at disk_at position of rod_index rod counting from the bottom.

    @param ToHG self: this ToHG self
    @param int rod_index: index of rod 
    @param int disk_at: index of the disk to get counting from the bottom 
    @rtype: Disk|None
    """
    def _get_rod_at(self, rod_index, disk_at):
        if 0 <= rod_index < len(self.rods) and 0 <= disk_at < len(self.rods[rod_index]):
            return self.rods[rod_index][disk_at]
        return None

    """
    Return number of moves of this ToHG self
    
    @param ToHG self: this ToHG self
    @rtype: int
    """
    def number_of_moves(self):
        return len(self._move_seq.moves)

    """
    Add move to ToHG self

    @param ToHG self: this ToHG self
    @param int origin: rod number (index from 0) of disk to move
    @param int dest: rod number you want to move disk to
    @rtype: None
    """
    def move(self, origin, dest):
        if dest not in self.rods.keys() \
                or origin not in self.rods.keys():
            if dest not in self.rods.keys():
                raise IllegalMoveError("Destination rod is out of range.")
            if origin not in self.rods.keys():
                raise IllegalMoveError("Source rod is out of range.")
        elif self.rods[origin] == []:
            raise IllegalMoveError("Source rod is empty.")
        elif origin == dest:
            raise IllegalMoveError("Invalid move.")
        elif self.rods[dest] == [] or \
                        self.get_top_disk(origin).size \
                        < self.get_top_disk(dest).size:
            self._move_seq.moves.append((origin, dest))
            target_disk = self.rods[origin].pop(-1)
            self.rods[dest].append(target_disk)
        else:
            raise IllegalMoveError("Cannot stack larger disk on smaller.")

    """
    Return the index of the rod which contains Disk disk

    @param ToHG self: this ToHG self
    @param Disk disk: the Disk that need to be located
    @rtype: int
    """
    def get_disk_location(self, disk):
        for rod_index in self.rods:
            for disk_index in self.rods[rod_index]:
                if disk_index.__eq__(disk):
                    return rod_index


    """
    Return the top Disk of the indexed rods[rod_index]

    @param ToHG self: this ToHG self
    @param int rod_index: the index of the rod
    @rtype: Disk
    """
    def get_top_disk(self, rod_index):
        if not self.rods[rod_index] == []:
            return self.rods[rod_index][-1]

    """
    Return whether the ToHG self is successful (i.e. all rods except for the
    last rod is empty)
    
    @param ToHG self: this ToHG self
    @rtype: bool
    """
    def check_success(self):
        for i in range(len(self.rods) - 1):
            if len(self.rods[i]) > 0:
                return False
        return True


    """
    Return whether ToHG self is equivalent to other in terms of object type, rods,
    and move_seq.
    
    @param ToHG self: this ToHG self
    @param ToHG|Any other: other object to be checked whether it is equivalent to self
    @rtype: bool
    """
    def __eq__(self, other):
        return type(self) == type(other) and self.rods == other.rods \
               and self.move_seq == other.move_seq

    """
    
    """
    def __str__(self):
        all_disks = []
        for height in range(self.get_number_of_disks()):
            for rod in range(len(self.rods)):
                if self._get_rod_at(rod, height) is not None:
                    all_disks.append(self._get_rod_at(rod, height))
        max_disk_size = max([c.size for c in all_disks]) \
            if len(all_disks) > 0 else 0
        rod_str = "=" * (2 * max_disk_size + 1)
        rod_spacing = "  "
        rods_str = (rod_str + rod_spacing) * len(self.rods)

        def _disk_str(size):
            # helper for string representation of disk
            if size == 0:
                return " " * len(rod_str)
            disk_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(rod_str) - len(disk_part)) / 2)
            return space_filler + disk_part + space_filler

        lines = ""
        for height in range(self.get_number_of_disks() - 1, -1, -1):
            line = ""
            for rod in range(len(self.rods)):
                r = self._get_rod_at(rod, height)
                if isinstance(r, Disk):
                    s = _disk_str(int(r.size))
                else:
                    s = _disk_str(0)
                line += s + rod_spacing
            lines += line + "\n"
        lines += rods_str

        return lines



class IllegalMoveError(Exception):
    """ Exception indicating move that violate ToHG"""
    pass