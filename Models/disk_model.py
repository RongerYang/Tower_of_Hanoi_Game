"""
A disk for stacking in the Tower of Hanoi Game

=== Attributes ===
    @param int size: radius of a disk

Assume that no more than one Disk object with the same size will
be added to a ToHG object.
"""
class Disk:

    """
    Initialize a Disk object with radius_size.

    @param Disk self: this Disk self
    @param int size: initial size of this Disk self
    @rtype: None
    """
    def __init__(self, size):
        self.size = size

    """
    Return whether the Disk self is equivalent to other in terms of object
    type and size.
    
    @param Disk self: this Disk self
    @param Disk|Any other: other item to be checked whether it is equivalent to self
    @rtype: bool
    """
    def __eq__(self, other):
        return type(self) == type(other) and self.size == other.size

    """
    Displaying the self Disk object graphically.
    
    @param Disk self: this Disk self
    @rtype: str
    """
    def __str__(self):
        return "--" * self.size