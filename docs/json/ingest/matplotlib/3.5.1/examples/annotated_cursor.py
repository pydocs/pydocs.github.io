��������s���bsdy�"""
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

"""���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngwidgets���`a ���bknfimport���`a ���`fCursor���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akeclass���`a ���bncoAnnotatedCursor���`a(���`fCursor���`a)���`a:���`a
���`d    ���bsdy�"""
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

    """���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`dline���`a,���`a ���`lnumberformat���aoa=���bs2a"���bsig{0:.4g}���bs2a;���bsig{1:.4g}���bs2a"���`a,���`a ���`foffset���aoa=���`a(���bmia5���`a,���`a ���bmia5���`a)���`a,���`a
���`q                 ���`hdataaxis���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`itextprops���aoa=���`a{���`a}���`a,���`a ���aoa*���aoa*���`jcursorargs���`a)���`a:���`a
���`h        ���bc1x:# The line object, for which the coordinates are displayed���`a
���`h        ���bbpdself���aoa.���`dline���`a ���aoa=���`a ���`dline���`a
���`h        ���bc1xG# The format string, on which .format() is called for creating the text���`a
���`h        ���bbpdself���aoa.���`lnumberformat���`a ���aoa=���`a ���`lnumberformat���`a
���`h        ���bc1v# Text position offset���`a
���`h        ���bbpdself���aoa.���`foffset���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`foffset���`a)���`a
���`h        ���bc1x4# The axis in which the cursor position is looked up���`a
���`h        ���bbpdself���aoa.���`hdataaxis���`a ���aoa=���`a ���`hdataaxis���`a
���`a
���`h        ���bc1x## First call baseclass constructor.���`a
���`h        ���bc1x5# Draws cursor and remembers background for blitting.���`a
���`h        ���bc1x# Saves ax as class attribute.���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���aoa*���aoa*���`jcursorargs���`a)���`a
���`a
���`h        ���bc1x%# Default value for position of text.���`a
���`h        ���bbpdself���aoa.���`lset_position���`a(���bbpdself���aoa.���`dline���aoa.���`iget_xdata���`a(���`a)���`a[���bmia0���`a]���`a,���`a ���bbpdself���aoa.���`dline���aoa.���`iget_ydata���`a(���`a)���`a[���bmia0���`a]���`a)���`a
���`h        ���bc1x # Create invisible animated text���`a
���`h        ���bbpdself���aoa.���`dtext���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`dtext���`a(���`a
���`l            ���bbpdself���aoa.���`bax���aoa.���`jget_xbound���`a(���`a)���`a[���bmia0���`a]���`a,���`a
���`l            ���bbpdself���aoa.���`bax���aoa.���`jget_ybound���`a(���`a)���`a[���bmia0���`a]���`a,���`a
���`l            ���bs2a"���bs2d0, 0���bs2a"���`a,���`a
���`l            ���`hanimated���aoa=���bnbdbool���`a(���bbpdself���aoa.���`guseblit���`a)���`a,���`a
���`l            ���`gvisible���aoa=���bkceFalse���`a,���`a ���aoa*���aoa*���`itextprops���`a)���`a
���`h        ���bc1x1# The position at which the cursor was last drawn���`a
���`h        ���bbpdself���aoa.���`rlastdrawnplotpoint���`a ���aoa=���`a ���bkcdNone���`a
���`a
���`d    ���akcdef���`a ���bnffonmove���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bsdxZ"""
        Overridden draw callback for cursor. Called when moving the mouse.
        """���`a
���`a
���`h        ���bc1x@# Leave method under the same conditions as in overridden method���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`fignore���`a(���`eevent���`a)���`a:���`a
���`l            ���bbpdself���aoa.���`rlastdrawnplotpoint���`a ���aoa=���`a ���bkcdNone���`a
���`l            ���akfreturn���`a
���`h        ���akbif���`a ���bowcnot���`a ���bbpdself���aoa.���`fcanvas���aoa.���`jwidgetlock���aoa.���`iavailable���`a(���bbpdself���`a)���`a:���`a
���`l            ���bbpdself���aoa.���`rlastdrawnplotpoint���`a ���aoa=���`a ���bkcdNone���`a
���`l            ���akfreturn���`a
���`a
���`h        ���bc1xB# If the mouse left drawable area, we now make the text invisible.���`a
���`h        ���bc1xD# Baseclass will redraw complete canvas after, which makes both text���`a
���`h        ���bc1w# and cursor disappear.���`a
���`h        ���akbif���`a ���`eevent���aoa.���`finaxes���`a ���aob!=���`a ���bbpdself���aoa.���`bax���`a:���`a
���`l            ���bbpdself���aoa.���`rlastdrawnplotpoint���`a ���aoa=���`a ���bkcdNone���`a
���`l            ���bbpdself���aoa.���`dtext���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`l            ���bnbesuper���`a(���`a)���aoa.���`fonmove���`a(���`eevent���`a)���`a
���`l            ���akfreturn���`a
���`a
���`h        ���bc1x9# Get the coordinates, which should be displayed as text,���`a
���`h        ���bc1x%# if the event coordinates are valid.���`a
���`h        ���`iplotpoint���`a ���aoa=���`a ���bkcdNone���`a
���`h        ���akbif���`a ���`eevent���aoa.���`exdata���`a ���bowbis���`a ���bowcnot���`a ���bkcdNone���`a ���bowcand���`a ���`eevent���aoa.���`eydata���`a ���bowbis���`a ���bowcnot���`a ���bkcdNone���`a:���`a
���`l            ���bc1x/# Get plot point related to current x position.���`a
���`l            ���bc1x*# These coordinates are displayed in text.���`a
���`l            ���`iplotpoint���`a ���aoa=���`a ���bbpdself���aoa.���`lset_position���`a(���`eevent���aoa.���`exdata���`a,���`a ���`eevent���aoa.���`eydata���`a)���`a
���`l            ���bc1x8# Modify event, such that the cursor is displayed on the���`a
���`l            ���bc1x)# plotted line, not at the mouse pointer,���`a
���`l            ���bc1x%# if the returned plot point is valid���`a
���`l            ���akbif���`a ���`iplotpoint���`a ���bowbis���`a ���bowcnot���`a ���bkcdNone���`a:���`a
���`p                ���`eevent���aoa.���`exdata���`a ���aoa=���`a ���`iplotpoint���`a[���bmia0���`a]���`a
���`p                ���`eevent���aoa.���`eydata���`a ���aoa=���`a ���`iplotpoint���`a[���bmia1���`a]���`a
���`a
���`h        ���bc1x@# If the plotpoint is given, compare to last drawn plotpoint and���`a
���`h        ���bc1x# return if they are the same.���`a
���`h        ���bc1xF# Skip even the call of the base class, because this would restore the���`a
���`h        ���bc1xA# background, draw the cursor lines and would leave us the job to���`a
���`h        ���bc1s# re-draw the text.���`a
���`h        ���akbif���`a ���`iplotpoint���`a ���bowbis���`a ���bowcnot���`a ���bkcdNone���`a ���bowcand���`a ���`iplotpoint���`a ���aob==���`a ���bbpdself���aoa.���`rlastdrawnplotpoint���`a:���`a
���`l            ���akfreturn���`a
���`a
���`h        ���bc1x7# Baseclass redraws canvas and cursor. Due to blitting,���`a
���`h        ���bc1x5# the added text is removed in this call, because the���`a
���`h        ���bc1x# background is redrawn.���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���`fonmove���`a(���`eevent���`a)���`a
���`a
���`h        ���bc1x2# Check if the display of text is still necessary.���`a
���`h        ���bc1v# If not, just return.���`a
���`h        ���bc1x4# This behaviour is also cloned from the base class.���`a
���`h        ���akbif���`a ���bowcnot���`a ���bbpdself���aoa.���`jget_active���`a(���`a)���`a ���bowbor���`a ���bowcnot���`a ���bbpdself���aoa.���`gvisible���`a:���`a
���`l            ���akfreturn���`a
���`a
���`h        ���bc1x2# Draw the widget, if event coordinates are valid.���`a
���`h        ���akbif���`a ���`iplotpoint���`a ���bowbis���`a ���bowcnot���`a ���bkcdNone���`a:���`a
���`l            ���bc1x%# Update position and displayed text.���`a
���`l            ���bc1x%# Position: Where the event occurred.���`a
���`l            ���bc1x3# Text: Determined by set_position() method earlier���`a
���`l            ���bc1x/# Position is transformed to pixel coordinates,���`a
���`l            ���bc1x8# an offset is added there and this is transformed back.���`a
���`l            ���`dtemp���`a ���aoa=���`a ���`a[���`eevent���aoa.���`exdata���`a,���`a ���`eevent���aoa.���`eydata���`a]���`a
���`l            ���`dtemp���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`itransData���aoa.���`itransform���`a(���`dtemp���`a)���`a
���`l            ���`dtemp���`a ���aoa=���`a ���`dtemp���`a ���aoa+���`a ���bbpdself���aoa.���`foffset���`a
���`l            ���`dtemp���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`itransData���aoa.���`hinverted���`a(���`a)���aoa.���`itransform���`a(���`dtemp���`a)���`a
���`l            ���bbpdself���aoa.���`dtext���aoa.���`lset_position���`a(���`dtemp���`a)���`a
���`l            ���bbpdself���aoa.���`dtext���aoa.���`hset_text���`a(���bbpdself���aoa.���`lnumberformat���aoa.���`fformat���`a(���aoa*���`iplotpoint���`a)���`a)���`a
���`l            ���bbpdself���aoa.���`dtext���aoa.���`kset_visible���`a(���bbpdself���aoa.���`gvisible���`a)���`a
���`a
���`l            ���bc1x0# Tell base class, that we have drawn something.���`a
���`l            ���bc1x;# Baseclass needs to know, that it needs to restore a clean���`a
���`l            ���bc1x6# background, if the cursor leaves our figure context.���`a
���`l            ���bbpdself���aoa.���`ineedclear���`a ���aoa=���`a ���bkcdTrue���`a
���`a
���`l            ���bc1x@# Remember the recently drawn cursor position, so events for the���`a
���`l            ���bc1x># same position (mouse moves slightly between two plot points)���`a
���`l            ���bc1p# can be skipped���`a
���`l            ���bbpdself���aoa.���`rlastdrawnplotpoint���`a ���aoa=���`a ���`iplotpoint���`a
���`h        ���bc1x # otherwise, make text invisible���`a
���`h        ���akdelse���`a:���`a
���`l            ���bbpdself���aoa.���`dtext���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`a
���`h        ���bc1x7# Draw changes. Cannot use _update method of baseclass,���`a
���`h        ���bc1x6# because it would first restore the background, which���`a
���`h        ���bc1x'# is done already and is not necessary.���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`guseblit���`a:���`a
���`l            ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���bbpdself���aoa.���`dtext���`a)���`a
���`l            ���bbpdself���aoa.���`fcanvas���aoa.���`dblit���`a(���bbpdself���aoa.���`bax���aoa.���`dbbox���`a)���`a
���`h        ���akdelse���`a:���`a
���`l            ���bc1x># If blitting is deactivated, the overridden _update call made���`a
���`l            ���bc1x)# by the base class immediately returned.���`a
���`l            ���bc1x$# We still have to draw the changes.���`a
���`l            ���bbpdself���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnflset_position���`a(���bbpdself���`a,���`a ���`dxpos���`a,���`a ���`dypos���`a)���`a:���`a
���`h        ���bsdy�"""
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
        """���`a
���`a
���`h        ���bc1t# Get plot line data���`a
���`h        ���`exdata���`a ���aoa=���`a ���bbpdself���aoa.���`dline���aoa.���`iget_xdata���`a(���`a)���`a
���`h        ���`eydata���`a ���aoa=���`a ���bbpdself���aoa.���`dline���aoa.���`iget_ydata���`a(���`a)���`a
���`a
���`h        ���bc1xG# The dataaxis attribute decides, in which axis we look up which cursor���`a
���`h        ���bc1m# coordinate.���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`hdataaxis���`a ���aob==���`a ���bs1a'���bs1ax���bs1a'���`a:���`a
���`l            ���`cpos���`a ���aoa=���`a ���`dxpos���`a
���`l            ���`ddata���`a ���aoa=���`a ���`exdata���`a
���`l            ���`clim���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`hget_xlim���`a(���`a)���`a
���`h        ���akdelif���`a ���bbpdself���aoa.���`hdataaxis���`a ���aob==���`a ���bs1a'���bs1ay���bs1a'���`a:���`a
���`l            ���`cpos���`a ���aoa=���`a ���`dypos���`a
���`l            ���`ddata���`a ���aoa=���`a ���`eydata���`a
���`l            ���`clim���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`hget_ylim���`a(���`a)���`a
���`h        ���akdelse���`a:���`a
���`l            ���akeraise���`a ���bnejValueError���`a(���bsaaf���bs2a"���bs2xThe data axis specifier ���bsia{���bbpdself���aoa.���`hdataaxis���bsia}���bs2h should ���bs2a"���`a
���`x                             ���bsaaf���bs2a"���bs2cbe ���bs2a'���bs2ax���bs2a'���bs2d or ���bs2a'���bs2ay���bs2a'���bs2a"���`a)���`a
���`a
���`h        ���bc1x4# If position is valid and in valid plot data range.���`a
���`h        ���akbif���`a ���`cpos���`a ���bowbis���`a ���bowcnot���`a ���bkcdNone���`a ���bowcand���`a ���`clim���`a[���bmia0���`a]���`a ���aoa<���aoa=���`a ���`cpos���`a ���aoa<���aoa=���`a ���`clim���`a[���aoa-���bmia1���`a]���`a:���`a
���`l            ���bc1x*# Find closest x value in sorted x vector.���`a
���`l            ���bc1x.# This requires the plotted data to be sorted.���`a
���`l            ���`eindex���`a ���aoa=���`a ���`bnp���aoa.���`lsearchsorted���`a(���`ddata���`a,���`a ���`cpos���`a)���`a
���`l            ���bc1x-# Return none, if this index is out of range.���`a
���`l            ���akbif���`a ���`eindex���`a ���aoa<���`a ���bmia0���`a ���bowbor���`a ���`eindex���`a ���aoa>���aoa=���`a ���bnbclen���`a(���`ddata���`a)���`a:���`a
���`p                ���akfreturn���`a ���bkcdNone���`a
���`l            ���bc1x# Return plot point as tuple.���`a
���`l            ���akfreturn���`a ���`a(���`exdata���`a[���`eindex���`a]���`a,���`a ���`eydata���`a[���`eindex���`a]���`a)���`a
���`a
���`h        ���bc1xD# Return none if there is no good related point for this x position.���`a
���`h        ���akfreturn���`a ���bkcdNone���`a
���`a
���`d    ���akcdef���`a ���bnfeclear���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bsdx_"""
        Overridden clear callback for cursor, called before drawing the figure.
        """���`a
���`a
���`h        ���bc1x9# The base class saves the clean background for blitting.���`a
���`h        ���bc1x # Text and cursor are invisible,���`a
���`h        ���bc1x*# until the first mouse move event occurs.���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���`eclear���`a(���`eevent���`a)���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`fignore���`a(���`eevent���`a)���`a:���`a
���`l            ���akfreturn���`a
���`h        ���bbpdself���aoa.���`dtext���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfg_update���`a(���bbpdself���`a)���`a:���`a
���`h        ���bsdy�"""
        Overridden method for either blitting or drawing the widget canvas.

        Passes call to base class if blitting is activated, only.
        In other cases, one draw_idle call is enough, which is placed
        explicitly in this class (see *onmove()*).
        In that case, `~matplotlib.widgets.Cursor` is not supposed to draw
        something using this method.
        """���`a
���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`guseblit���`a:���`a
���`l            ���bnbesuper���`a(���`a)���aoa.���`g_update���`a(���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia6���`a)���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2xCursor Tracking x Position���bs2a"���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a,���`a ���bmid1000���`a)���`a
���`ay���`a ���aoa=���`a ���`ax���aoa*���aoa*���bmia2���`a
���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmib25���`a)���`a
���`a
���bc1p# A minimum call���`a
���bc1x<# Set useblit=True on most backends for enhanced performance���`a
���bc1x5# and pass the ax parameter to the Cursor base class.���`a
���bc1x<# cursor = AnnotatedCursor(line=lin[0], ax=ax, useblit=True)���`a
���`a
���bc1xA# A more advanced call. Properties for text and lines are passed.���`a
���bc1xH# Watch the passed color names and the color of cursor line and text, to���`a
���bc1x2# relate the passed options to graphical elements.���`a
���bc1x.# The dataaxis parameter is still the default.���`a
���`fcursor���`a ���aoa=���`a ���`oAnnotatedCursor���`a(���`a
���`d    ���`dline���aoa=���`dline���`a,���`a
���`d    ���`lnumberformat���aoa=���bs2a"���bsig{0:.2f}���bseb\n���bsig{1:.2f}���bs2a"���`a,���`a
���`d    ���`hdataaxis���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`foffset���aoa=���`a[���bmib10���`a,���`a ���bmib10���`a]���`a,���`a
���`d    ���`itextprops���aoa=���`a{���bs1a'���bs1ecolor���bs1a'���`a:���`a ���bs1a'���bs1dblue���bs1a'���`a,���`a ���bs1a'���bs1jfontweight���bs1a'���`a:���`a ���bs1a'���bs1dbold���bs1a'���`a}���`a,���`a
���`d    ���`bax���aoa=���`bax���`a,���`a
���`d    ���`guseblit���aoa=���bkcdTrue���`a,���`a
���`d    ���`ecolor���aoa=���bs1a'���bs1cred���bs1a'���`a,���`a
���`d    ���`ilinewidth���aoa=���bmia2���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x%# Trouble with non-biunique functions���`a
���bc1x%# -----------------------------------���`a
���bc1x@# A call demonstrating problems with the *dataaxis=y* parameter.���`a
���bc1xN# The text now looks up the matching x value for the current cursor y position���`a
���bc1xI# instead of vice versa. Hover your cursor to y=4. There are two x values���`a
���bc1x@# producing this y value: -2 and 2. The function is only unique,���`a
���bc1x8# but not biunique. Only one value is shown in the text.���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia6���`a)���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2xCursor Tracking y Position���bs2a"���`a)���`a
���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���aoa-���bmia5���`a,���`a ���bmia5���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmib25���`a)���`a
���`a
���`fcursor���`a ���aoa=���`a ���`oAnnotatedCursor���`a(���`a
���`d    ���`dline���aoa=���`dline���`a,���`a
���`d    ���`lnumberformat���aoa=���bs2a"���bsig{0:.2f}���bseb\n���bsig{1:.2f}���bs2a"���`a,���`a
���`d    ���`hdataaxis���aoa=���bs1a'���bs1ay���bs1a'���`a,���`a ���`foffset���aoa=���`a[���bmib10���`a,���`a ���bmib10���`a]���`a,���`a
���`d    ���`itextprops���aoa=���`a{���bs1a'���bs1ecolor���bs1a'���`a:���`a ���bs1a'���bs1dblue���bs1a'���`a,���`a ���bs1a'���bs1jfontweight���bs1a'���`a:���`a ���bs1a'���bs1dbold���bs1a'���`a}���`a,���`a
���`d    ���`bax���aoa=���`bax���`a,���`a
���`d    ���`guseblit���aoa=���bkcdTrue���`a,���`a
���`d    ���`ecolor���aoa=���bs1a'���bs1cred���bs1a'���`a,���`a ���`ilinewidth���aoa=���bmia2���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�