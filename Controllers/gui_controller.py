import time
import tkinter as tk
from tkinter import messagebox
from gui_viewables import DiskView, RodView
from Models.tohg_model import ToHG, IllegalMoveError

""" Graphical User Interface (GUI) controller

=== Attributes ===
    @param float disk_scale: height in pixels to scale
        disk height
    @param root tk.Tk: tkinter root window
"""
class GUIController:

    """
    Initialize a new GUIController.

    @param GUIController self:
    @param int number_of_disks: number of disks for first rod
    @param int number_of_rods: number of rods
    @param float content_width: width, in pixels, of working area
    @param float content_height: height, in pixels, of working area
    @param float disk_scale: height in pixels for showing disk thicknesses, and to
                scale disk diameters
    @rtype: None
    """
    def __init__(self, number_of_disks, number_of_rods, content_width,
                 content_height, disk_scale):
        self._model = ToHG(number_of_rods, 0)
        self._rods = []
        self._disk_to_move = None
        self._blinking = False
        self._number_of_rods = number_of_rods
        self.disk_scale = disk_scale
        self.root = tk.Tk()
        canvas = tk.Canvas(self.root,
                           background="blue",
                           width=content_width, height=content_height)
        canvas.pack(expand=True, fill=tk.BOTH)
        self.moves_label = tk.Label(self.root)
        self.show_number_of_moves()
        self.moves_label.pack()
        # the dimensions of a rod are the same as a disk that's
        # one size bigger than the biggest of the number_of_disks disks.
        for rod_ind in range(number_of_rods):
            width = self.disk_scale * (number_of_disks + 1)
            x_cent = content_width * (rod_ind + 1) / (number_of_rods + 1.0)
            y_cent = content_height - disk_scale / 2
            rod = RodView(width,
                              lambda s: self.rod_clicked(s),
                              canvas,
                              self.disk_scale,
                              x_cent,
                              y_cent)
            self._rods.append(rod)
        total_size = self.disk_scale
        for sizeparam in range(1, number_of_disks + 1):
            size = (number_of_disks + 1 - sizeparam)
            width = self.disk_scale * size
            x_cent = content_width / (number_of_rods + 1.0)
            y_cent = content_height - disk_scale / 2 - total_size
            disk = DiskView(size, width, lambda c: self.disk_clicked(c),
                            canvas, self.disk_scale, x_cent, y_cent)
            self._model.rods[0].append(disk)
            total_size += self.disk_scale
        tk.mainloop()

    """ 
    React to disk being clicked: if not in the middle of blinking
    then select disk for moving, or for moving onto.

    @param GUIController self:
    @param DiskView disk: clicked disk
    @rtype: None
    """
    def disk_clicked(self, disk):
        if not self._blinking:
            self.select_disk(disk)

    """ 
    React to rod being clicked: if not in the middle of blinking
    then select disk for moving, or for moving onto.

    @param GUIController self:
    @param RodView rod: clicked rod
    @rtype: None
    """
    def rod_clicked(self, rod):
        if not self._blinking:
            self.select_rod(rod)

    """
    Select top disk.

    If no disk is selected to move, then select the disk at
    top of clicked_disk's rod (which may be clicked_disk
    itself) and highlight it.
    If selected_disk is already highlighted, then unhighlight it.
    Otherwise try to move self._disk_to_move onto the rod that
    clicked_disk is on.

    @param GUIController self:
    @param DiskView disk: clicked disk
    @rtype: None
    """
    def select_disk(self, disk):
        rod = self._rods[self._model.get_disk_location(disk)]
        rod_index = self.rod_index(rod)
        disk = self._model.get_top_disk(rod_index)
        if self._disk_to_move is None:
            self._disk_to_move = disk
            self._disk_to_move.highlight(True)
            self.root.update()
        elif self._disk_to_move is disk:
            self._disk_to_move.highlight(False)
            self._disk_to_move = None
            self.root.update()
        else:
            self.select_platform_for_move(disk, rod_index)

    """ 
    Initiate a move.

    If there is already some disk highlighted (i.e.
    self._disk_to_move is not None), unless
    self._disk_to_move is on dest_rod, in which case do nothing.

    @param GUIController self:
    @type dest_rod: RodView
    @rtype: None
    """
    def select_rod(self, dest_rod):
        if self._disk_to_move is not None:
            origin_rod = self._rods[
                self._model.get_disk_location(self._disk_to_move)]
            dest_rod_index = self.rod_index(dest_rod)
            origin_rod_index = self.rod_index(origin_rod)
            if origin_rod_index != dest_rod_index:
                top_disk = self._model.get_top_disk(dest_rod_index)
                if top_disk is None:
                    self.select_platform_for_move(dest_rod, dest_rod_index)
                else:
                    self.select_platform_for_move(top_disk, dest_rod_index)

    """ 
    Show the disk move on screen, and update the model.

    Change self._disk_to_move's coordinates so that it's on top of platform.

    @param GUIController self:
    @param PlatformView platform:
    @param int rod_index:
    @rtype: None
    """
    def select_platform_for_move(self, platform, rod_index):
        if self._disk_to_move is not None:
            try:
                from_rod = self._model.get_disk_location(
                    self._disk_to_move)
                self._model.move(from_rod, rod_index)
                self._disk_to_move.place(platform.x_center, platform.y_center
                                         - self.disk_scale)
                self.show_number_of_moves()
            except IllegalMoveError as e:
                print(e)
                self._blinking = True
                for i in range(10):
                    self._disk_to_move.highlight(i % 2 != 0)
                    self.root.update()
                    time.sleep(0.1)
                self._blinking = False
            self._disk_to_move.highlight(False)
            self._disk_to_move = None
            self.root.update()
            if self._model.check_success():
                messagebox.showinfo("Solved", "Solved! Congratulations!\n"
                                              "Minimal Number of Moves: {}\n"
                                              "Your Number of Moves: {}"
                                    .format(2 ** self._model.get_number_of_disks() - 1,
                                            self._model.number_of_moves()))

    """ 
    Return the index of rod.

    @param GUIController self:
    @param RodView rod:
    @rtype: int
    """
    def rod_index(self, rod):
        return self._rods.index(rod)

    """
    Show the number of moves so far and the minimal number of moves on tk.

    @param GUIController self:
    @rtype: None
    """
    def show_number_of_moves(self):
        self.moves_label.config(text="Number of Moves: " +
                                     str(self._model.number_of_moves()) +
                                     "\tMinimal Number of Moves: " +
                                    str(2 ** self._model.get_number_of_disks() - 1))

    """ 
    Return ith rod.

    @param GUIController self:
    @param int i:
    @rtype: RodView
    """
    def get_rod(self, i):
        return self._rods[i]

    """ 
    Return the top disk from ith rod.

    @param GUIController self:
    @param int i:
    @rtype: DiskView
    """
    def get_top_disk(self, i):
        return self._model.get_top_disk(i)


#
# if __name__ == "__main__":
#     gui = GUIController(3, 3, 1024, 320, 20)
#     tk.mainloop()