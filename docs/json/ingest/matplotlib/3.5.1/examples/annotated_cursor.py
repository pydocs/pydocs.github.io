ŸØÇÅŸ¥ÉôsŸ±Çbsdy÷"""
================
Annotated Cursor
================

Display a data cursor including a text box, which shows the plot point close
to the mouse pointer.

The new cursor inherits from `~matplotlib.widgets.Cursor` and demonstrates the
creation of new widgets and their event callbacks.

See also the :doc:`cross hair cursor
</gallery/misc/cursor_demo>`, which implements a cursor tracking the plotted
data, but without using inheritance and without displaying the currently
tracked coordinates.

.. note::
    The figure related to this example does not show the cursor, because that
    figure is automatically created in a build queue, where the first mouse
    movement, which triggers the cursor creation, is missing.

"""Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnngwidgetsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`fCursorŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakeclassŸ±Ç`a Ÿ±ÇbncoAnnotatedCursorŸ±Ç`a(Ÿ±Ç`fCursorŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdy◊"""
    A crosshair cursor like `~matplotlib.widgets.Cursor` with a text showing \
    the current coordinates.

    For the cursor to remain responsive you must keep a reference to it.
    The data of the axis specified as *dataaxis* must be in ascending
    order. Otherwise, the `numpy.searchsorted` call might fail and the text
    disappears. You can satisfy the requirement by sorting the data you plot.
    Usually the data is already sorted (if it was created e.g. using
    `numpy.linspace`), but e.g. scatter plots might cause this problem.
    The cursor sticks to the plotted line.

    Parameters
    ----------
    line : `matplotlib.lines.Line2D`
        The plot line from which the data coordinates are displayed.

    numberformat : `python format string <https://docs.python.org/3/\
    library/string.html#formatstrings>`_, optional, default: "{0:.4g};{1:.4g}"
        The displayed text is created by calling *format()* on this string
        with the two coordinates.

    offset : (float, float) default: (5, 5)
        The offset in display (pixel) coordinates of the text position
        relative to the cross hair.

    dataaxis : {"x", "y"}, optional, default: "x"
        If "x" is specified, the vertical cursor line sticks to the mouse
        pointer. The horizontal cursor line sticks to *line*
        at that x value. The text shows the data coordinates of *line*
        at the pointed x value. If you specify "y", it works in the opposite
        manner. But: For the "y" value, where the mouse points to, there might
        be multiple matching x values, if the plotted function is not biunique.
        Cursor and text coordinate will always refer to only one x value.
        So if you use the parameter value "y", ensure that your function is
        biunique.

    Other Parameters
    ----------------
    textprops : `matplotlib.text` properties as dictionary
        Specifies the appearance of the rendered text object.

    **cursorargs : `matplotlib.widgets.Cursor` properties
        Arguments passed to the internal `~matplotlib.widgets.Cursor` instance.
        The `matplotlib.axes.Axes` argument is mandatory! The parameter
        *useblit* can be set to *True* in order to achieve faster rendering.

    """Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbfmh__init__Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dlineŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lnumberformatŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbsig{0:.4g}Ÿ±Çbs2a;Ÿ±Çbsig{1:.4g}Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foffsetŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`hdataaxisŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`itextpropsŸ±Çaoa=Ÿ±Ç`a{Ÿ±Ç`a}Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`jcursorargsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x:# The line object, for which the coordinates are displayedŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dlineŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dlineŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1xG# The format string, on which .format() is called for creating the textŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`lnumberformatŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`lnumberformatŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1v# Text position offsetŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`foffsetŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`foffsetŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x4# The axis in which the cursor position is looked upŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`hdataaxisŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hdataaxisŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x## First call baseclass constructor.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x5# Draws cursor and remembers background for blitting.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x# Saves ax as class attribute.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Çbfmh__init__Ÿ±Ç`a(Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`jcursorargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x%# Default value for position of text.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`lset_positionŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dlineŸ±Çaoa.Ÿ±Ç`iget_xdataŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dlineŸ±Çaoa.Ÿ±Ç`iget_ydataŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x # Create invisible animated textŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jget_xboundŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jget_yboundŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbs2a"Ÿ±Çbs2d0, 0Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`hanimatedŸ±Çaoa=Ÿ±ÇbnbdboolŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`guseblitŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`gvisibleŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`itextpropsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x1# The position at which the cursor was last drawnŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`rlastdrawnplotpointŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnffonmoveŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eeventŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbsdxZ"""
        Overridden draw callback for cursor. Called when moving the mouse.
        """Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x@# Leave method under the same conditions as in overridden methodŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`fignoreŸ±Ç`a(Ÿ±Ç`eeventŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`rlastdrawnplotpointŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakfreturnŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbowcnotŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`fcanvasŸ±Çaoa.Ÿ±Ç`jwidgetlockŸ±Çaoa.Ÿ±Ç`iavailableŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`rlastdrawnplotpointŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakfreturnŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1xB# If the mouse left drawable area, we now make the text invisible.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1xD# Baseclass will redraw complete canvas after, which makes both textŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1w# and cursor disappear.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`eeventŸ±Çaoa.Ÿ±Ç`finaxesŸ±Ç`a Ÿ±Çaob!=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`rlastdrawnplotpointŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`kset_visibleŸ±Ç`a(Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`fonmoveŸ±Ç`a(Ÿ±Ç`eeventŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakfreturnŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x9# Get the coordinates, which should be displayed as text,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x%# if the event coordinates are valid.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`iplotpointŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`eeventŸ±Çaoa.Ÿ±Ç`exdataŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbowcnotŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a Ÿ±ÇbowcandŸ±Ç`a Ÿ±Ç`eeventŸ±Çaoa.Ÿ±Ç`eydataŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbowcnotŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x/# Get plot point related to current x position.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x*# These coordinates are displayed in text.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`iplotpointŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`lset_positionŸ±Ç`a(Ÿ±Ç`eeventŸ±Çaoa.Ÿ±Ç`exdataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eeventŸ±Çaoa.Ÿ±Ç`eydataŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x8# Modify event, such that the cursor is displayed on theŸ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x)# plotted line, not at the mouse pointer,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x%# if the returned plot point is validŸ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`iplotpointŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbowcnotŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`eeventŸ±Çaoa.Ÿ±Ç`exdataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iplotpointŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`eeventŸ±Çaoa.Ÿ±Ç`eydataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iplotpointŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x@# If the plotpoint is given, compare to last drawn plotpoint andŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x# return if they are the same.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1xF# Skip even the call of the base class, because this would restore theŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1xA# background, draw the cursor lines and would leave us the job toŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1s# re-draw the text.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`iplotpointŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbowcnotŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a Ÿ±ÇbowcandŸ±Ç`a Ÿ±Ç`iplotpointŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`rlastdrawnplotpointŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakfreturnŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x7# Baseclass redraws canvas and cursor. Due to blitting,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x5# the added text is removed in this call, because theŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x# background is redrawn.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`fonmoveŸ±Ç`a(Ÿ±Ç`eeventŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x2# Check if the display of text is still necessary.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1v# If not, just return.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x4# This behaviour is also cloned from the base class.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbowcnotŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`jget_activeŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±ÇbowborŸ±Ç`a Ÿ±ÇbowcnotŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gvisibleŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakfreturnŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x2# Draw the widget, if event coordinates are valid.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`iplotpointŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbowcnotŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x%# Update position and displayed text.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x%# Position: Where the event occurred.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x3# Text: Determined by set_position() method earlierŸ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x/# Position is transformed to pixel coordinates,Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x8# an offset is added there and this is transformed back.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dtempŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Ç`eeventŸ±Çaoa.Ÿ±Ç`exdataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eeventŸ±Çaoa.Ÿ±Ç`eydataŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dtempŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransDataŸ±Çaoa.Ÿ±Ç`itransformŸ±Ç`a(Ÿ±Ç`dtempŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dtempŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dtempŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`foffsetŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dtempŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransDataŸ±Çaoa.Ÿ±Ç`hinvertedŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`itransformŸ±Ç`a(Ÿ±Ç`dtempŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`lset_positionŸ±Ç`a(Ÿ±Ç`dtempŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`hset_textŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`lnumberformatŸ±Çaoa.Ÿ±Ç`fformatŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`iplotpointŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`kset_visibleŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gvisibleŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x0# Tell base class, that we have drawn something.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x;# Baseclass needs to know, that it needs to restore a cleanŸ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x6# background, if the cursor leaves our figure context.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ineedclearŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbkcdTrueŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x@# Remember the recently drawn cursor position, so events for theŸ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x># same position (mouse moves slightly between two plot points)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1p# can be skippedŸ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`rlastdrawnplotpointŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`iplotpointŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x # otherwise, make text invisibleŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`kset_visibleŸ±Ç`a(Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x7# Draw changes. Cannot use _update method of baseclass,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x6# because it would first restore the background, whichŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x'# is done already and is not necessary.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`guseblitŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`kdraw_artistŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`fcanvasŸ±Çaoa.Ÿ±Ç`dblitŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dbboxŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x># If blitting is deactivated, the overridden _update call madeŸ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x)# by the base class immediately returned.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x$# We still have to draw the changes.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`fcanvasŸ±Çaoa.Ÿ±Ç`idraw_idleŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnflset_positionŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dxposŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dyposŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbsdy»"""
        Finds the coordinates, which have to be shown in text.

        The behaviour depends on the *dataaxis* attribute. Function looks
        up the matching plot coordinate for the given mouse position.

        Parameters
        ----------
        xpos : float
            The current x position of the cursor in data coordinates.
            Important if *dataaxis* is set to 'x'.
        ypos : float
            The current y position of the cursor in data coordinates.
            Important if *dataaxis* is set to 'y'.

        Returns
        -------
        ret : {2D array-like, None}
            The coordinates which should be displayed.
            *None* is the fallback value.
        """Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1t# Get plot line dataŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`exdataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dlineŸ±Çaoa.Ÿ±Ç`iget_xdataŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`eydataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dlineŸ±Çaoa.Ÿ±Ç`iget_ydataŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1xG# The dataaxis attribute decides, in which axis we look up which cursorŸ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1m# coordinate.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`hdataaxisŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`cposŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dxposŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`exdataŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`climŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hget_xlimŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakdelifŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`hdataaxisŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1ayŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`cposŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dyposŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`ddataŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`eydataŸ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`climŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hget_ylimŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakeraiseŸ±Ç`a Ÿ±ÇbnejValueErrorŸ±Ç`a(Ÿ±ÇbsaafŸ±Çbs2a"Ÿ±Çbs2xThe data axis specifier Ÿ±Çbsia{Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`hdataaxisŸ±Çbsia}Ÿ±Çbs2h should Ÿ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`x                             Ÿ±ÇbsaafŸ±Çbs2a"Ÿ±Çbs2cbe Ÿ±Çbs2a'Ÿ±Çbs2axŸ±Çbs2a'Ÿ±Çbs2d or Ÿ±Çbs2a'Ÿ±Çbs2ayŸ±Çbs2a'Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x4# If position is valid and in valid plot data range.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`cposŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbowcnotŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a Ÿ±ÇbowcandŸ±Ç`a Ÿ±Ç`climŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa<Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cposŸ±Ç`a Ÿ±Çaoa<Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`climŸ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x*# Find closest x value in sorted x vector.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x.# This requires the plotted data to be sorted.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`eindexŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`lsearchsortedŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cposŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x-# Return none, if this index is out of range.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`eindexŸ±Ç`a Ÿ±Çaoa<Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a Ÿ±ÇbowborŸ±Ç`a Ÿ±Ç`eindexŸ±Ç`a Ÿ±Çaoa>Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`ddataŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇakfreturnŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a
Ÿ±Ç`l            Ÿ±Çbc1x# Return plot point as tuple.Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`a(Ÿ±Ç`exdataŸ±Ç`a[Ÿ±Ç`eindexŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eydataŸ±Ç`a[Ÿ±Ç`eindexŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1xD# Return none if there is no good related point for this x position.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfeclearŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`eeventŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbsdx_"""
        Overridden clear callback for cursor, called before drawing the figure.
        """Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x9# The base class saves the clean background for blitting.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x # Text and cursor are invisible,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x*# until the first mouse move event occurs.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`eclearŸ±Ç`a(Ÿ±Ç`eeventŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`fignoreŸ±Ç`a(Ÿ±Ç`eeventŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakfreturnŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`kset_visibleŸ±Ç`a(Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfg_updateŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbsdyá"""
        Overridden method for either blitting or drawing the widget canvas.

        Passes call to base class if blitting is activated, only.
        In other cases, one draw_idle call is enough, which is placed
        explicitly in this class (see *onmove()*).
        In that case, `~matplotlib.widgets.Cursor` is not supposed to draw
        something using this method.
        """Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`guseblitŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbnbesuperŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`g_updateŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xCursor Tracking x PositionŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmid1000Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`axŸ±Çaoa*Ÿ±Çaoa*Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dlineŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib25Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1p# A minimum callŸ±Ç`a
Ÿ±Çbc1x<# Set useblit=True on most backends for enhanced performanceŸ±Ç`a
Ÿ±Çbc1x5# and pass the ax parameter to the Cursor base class.Ÿ±Ç`a
Ÿ±Çbc1x<# cursor = AnnotatedCursor(line=lin[0], ax=ax, useblit=True)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xA# A more advanced call. Properties for text and lines are passed.Ÿ±Ç`a
Ÿ±Çbc1xH# Watch the passed color names and the color of cursor line and text, toŸ±Ç`a
Ÿ±Çbc1x2# relate the passed options to graphical elements.Ÿ±Ç`a
Ÿ±Çbc1x.# The dataaxis parameter is still the default.Ÿ±Ç`a
Ÿ±Ç`fcursorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oAnnotatedCursorŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dlineŸ±Çaoa=Ÿ±Ç`dlineŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`lnumberformatŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbsig{0:.2f}Ÿ±Çbseb\nŸ±Çbsig{1:.2f}Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hdataaxisŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foffsetŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`itextpropsŸ±Çaoa=Ÿ±Ç`a{Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dblueŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1jfontweightŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dboldŸ±Çbs1a'Ÿ±Ç`a}Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`guseblitŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1credŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ilinewidthŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO###############################################################################Ÿ±Ç`a
Ÿ±Çbc1x%# Trouble with non-biunique functionsŸ±Ç`a
Ÿ±Çbc1x%# -----------------------------------Ÿ±Ç`a
Ÿ±Çbc1x@# A call demonstrating problems with the *dataaxis=y* parameter.Ÿ±Ç`a
Ÿ±Çbc1xN# The text now looks up the matching x value for the current cursor y positionŸ±Ç`a
Ÿ±Çbc1xI# instead of vice versa. Hover your cursor to y=4. There are two x valuesŸ±Ç`a
Ÿ±Çbc1x@# producing this y value: -2 and 2. The function is only unique,Ÿ±Ç`a
Ÿ±Çbc1x8# but not biunique. Only one value is shown in the text.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2xCursor Tracking y PositionŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`dlineŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çaoa-Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib25Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`fcursorŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oAnnotatedCursorŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`dlineŸ±Çaoa=Ÿ±Ç`dlineŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`lnumberformatŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbsig{0:.2f}Ÿ±Çbseb\nŸ±Çbsig{1:.2f}Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`hdataaxisŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ayŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`foffsetŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`itextpropsŸ±Çaoa=Ÿ±Ç`a{Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dblueŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1jfontweightŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dboldŸ±Çbs1a'Ÿ±Ç`a}Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`guseblitŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1credŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinewidthŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ