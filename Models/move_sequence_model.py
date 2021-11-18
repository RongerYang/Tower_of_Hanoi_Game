"""
Sequences of moves in the Tower of Hanoi Game.

=== Attributes ===
    @param list[tuple[int]] moves:
        A sequence of moves in the Tower of Hanoi Game, where the moves is a list of
        integer pairs tuple (a,b) with a being the index number of the source
        rod and b being the index number of the destination rod
"""
class MoveSequence(object):

    """
    Initialize a MoveSequence object with moves if applicable, or an empty list
    as the default moves

    @param MoveSequence self: this MoveSequence self
    @param list[tuple[int]] moves: sequences of moves in the Tower of Hanoi Game
    @rtype: None
    """
    def __init__(self, moves = []):
        self.moves = moves

    """
    Return the move at position i in this MoveSequence object starting from index 0

    @param MoveSequence self: this MoveSequence self
    @param int i: move in the MoveSequence at i-th position
    @rtype: tuple[int]
    """
    def get_move(self, i):
        try:
            return self.moves[i]
        except:
            print(f"Index {i} is out of range.")

    """
    Add move by moving disk from the rod indexed source to the rod indexed destination to
    the MoveSequence self
    
    @param MoveSequence self: this MoveSequence self
    @param int source: rod with index number being source 
    @param int destination: rod with index number being destination 
    @rtype: None
    """
    def move_disk(self, source, destination):
        self.moves.append((source, destination))
        

    """
    Return whether self is equivalent to other in terms of object type and its moves.

    @param MoveSequence self: this MoveSequence self
    @param MoveSequence|Any other: other object to be checked whether it is equivalent to self
    @return: bool
    """
    def __eq__(self, other):
        return type(self) == type(other) and self.moves == other.moves


    """
    Display the moves of this MoveSequence self
    
    @param MoveSequence self: this MoveSequence self
    @return: str
    """
    def __str__(self):
        return self.moves

