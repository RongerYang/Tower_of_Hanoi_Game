"""
PlatformView: A visible Disk or rod, which a disk can sit on top of.
DiskView: A visible Disk object represented as a PlatformView.
RodView: A visible rod.

Each PlatformView instance receives a Canvas instance. The Canvas class is a
class in the tkinter framework. The class is used for a place in a window
to draw shapes.

PlatformView objects draw themselves as rectangles on the canvas, to represent
side views of rods or rounds of disks with particular sizes.

DiskView objects can be moved and highlighted.
Note that DiskView inherits from both Disk and PlatformView

PlatformView objects receive a function to call in order to report to some
UI object (e.g. GUIController) that their rectangle was clicked on.

Visible slab, could be a Disk or rod

    === Attributes ===
    @param Canvas canvas: tkinter class for drawing
    @param float thickness: vertical extent of platform
"""
from tkinter import Canvas
from Models.disk_model import Disk


class PlatformView:

    """
    Create a new PlatformView

    @param PlatformView self:
    @param float width: width in pixels of view
    @param function click_handler: function to react to mouse clicks
    @param Canvas canvas: space to draw on
    @param float thickness: vertical extent of platform
    @param float x_center: horizontal center of this platform
    @param float y_center: vertical center of platform
    """
    def __init__(self, width, click_handler, canvas,
                 thickness, x_center, y_center):
        self.canvas = canvas
        self._width = width
        self.x_center = x_center
        self.y_center = y_center
        self.thickness = thickness

        # Create a rectangle on the canvas, and record the index that tkinter
        # uses to refer to it.
        self.index = canvas.create_rectangle(0, 0, 0, 0)
        self.canvas.itemconfigure(self.index)

        # Initial placement.
        self.place(x_center, y_center)

        # Tell the canvas to report when the rectangle is clicked.
        # The report is a call to click_handler, passing it this CheeseView
        # instance so the controller knows which one was clicked.
        self.canvas.tag_bind(self.index,
                             '<ButtonRelease>',
                             lambda _: click_handler(self))

    """ 
    Place rectangular image of this disk/rod at (x_center, y_center)

    @param PlatformView self:
    @param float x_center: horizontal center of platform
    @param float y_center: vertical center of platform
    @rtype: None
    """
    def place(self, x_center, y_center):
        # corners are half of size or thickness away
        self.canvas.coords(self.index,
                           round(x_center - self._width/2),
                           round(y_center - self.thickness/2),
                           round(x_center + self._width/2),
                           round(y_center + self.thickness/2))
        # record new center
        self.x_center = x_center
        self.y_center = y_center


"""
A visible Disk
"""
class DiskView(Disk, PlatformView):

    """ 
    Initialize a new DiskView.

    @param DiskView self: this DiskView self
    @param int size: relative size of disk, with 1 smallest
    @param float width: horizontal extent of disk, in pixels
    @param function click_handler: function to react to mouse clicks
    @param Canvas canvas: space to draw disk on
    @param float thickness: vertical extent of disk
    @param float x_center:
                horizontal center of disk
    @param float y_center: vertical center or disk
    """
    def __init__(self, size, width, click_handler, canvas, thickness,
                 x_center, y_center):
        PlatformView.__init__(self, width, click_handler, canvas, thickness,
                              x_center, y_center)
        Disk.__init__(self, size)

        # Initially unhighlighted.
        self.highlight(False)

    """
    Set this DiskView's colour to highlighted or not.

    @param DiskView self: this DiskView self
    @param bool highlighting: whether to highlight
    """
    def highlight(self: 'DiskView', highlighting: bool):
        self.canvas.itemconfigure(self.index,
                                  fill=('red' if highlighting else 'orange'))

""" 
A visible Rod
"""
class RodView(PlatformView):


    """
    Create a new RodView

    @type self: RodView
    @type width: float
    @type click_handler: function
    @type canvas: Canvas
    @type thickness: float
    @type x_center: float
    @type y_center: float
    """
    def __init__(self, width, click_handler, canvas, thickness,
                 x_center, y_center):
        PlatformView.__init__(self, width, click_handler, canvas, thickness,
                              x_center, y_center)
        self.canvas.itemconfigure(self.index, fill='black')
