������������bsdy�"""
===============================
Rectangle and ellipse selectors
===============================

Click somewhere, move the mouse, and release the mouse button.
`.RectangleSelector` and `.EllipseSelector` draw a rectangle or an ellipse
from the initial click position to the current mouse position (within the same
axes) until the button is released.  A connected callback receives the click-
and release-events.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngwidgets���`a ���bknfimport���`a ���`oEllipseSelector���`a,���`a ���`qRectangleSelector���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfoselect_callback���`a(���`feclick���`a,���`a ���`herelease���`a)���`a:���`a
���`d    ���bsdxk"""
    Callback for line selection.

    *eclick* and *erelease* are the press and release events.
    """���`a
���`d    ���`bx1���`a,���`a ���`by1���`a ���aoa=���`a ���`feclick���aoa.���`exdata���`a,���`a ���`feclick���aoa.���`eydata���`a
���`d    ���`bx2���`a,���`a ���`by2���`a ���aoa=���`a ���`herelease���aoa.���`exdata���`a,���`a ���`herelease���aoa.���`eydata���`a
���`d    ���bnbeprint���`a(���bsaaf���bs2a"���bs2a(���bsia{���`bx1���bsia:���bs2d3.2f���bsia}���bs2b, ���bsia{���`by1���bsia:���bs2d3.2f���bsia}���bs2g) --> (���bsia{���`bx2���bsia:���bs2d3.2f���bsia}���bs2b, ���bsia{���`by2���bsia:���bs2d3.2f���bsia}���bs2a)���bs2a"���`a)���`a
���`d    ���bnbeprint���`a(���bsaaf���bs2a"���bs2xThe buttons you used were: ���bsia{���`feclick���aoa.���`fbutton���bsia}���bs2a ���bsia{���`herelease���aoa.���`fbutton���bsia}���bs2a"���`a)���`a
���`a
���`a
���akcdef���`a ���bnfotoggle_selector���`a(���`eevent���`a)���`a:���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1lKey pressed.���bs1a'���`a)���`a
���`d    ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1at���bs1a'���`a:���`a
���`h        ���akcfor���`a ���`hselector���`a ���bowbin���`a ���`iselectors���`a:���`a
���`l            ���`dname���`a ���aoa=���`a ���bnbdtype���`a(���`hselector���`a)���aoa.���bvmh__name__���`a
���`l            ���akbif���`a ���`hselector���aoa.���`factive���`a:���`a
���`p                ���bnbeprint���`a(���bsaaf���bs1a'���bsia{���`dname���bsia}���bs1m deactivated.���bs1a'���`a)���`a
���`p                ���`hselector���aoa.���`jset_active���`a(���bkceFalse���`a)���`a
���`l            ���akdelse���`a:���`a
���`p                ���bnbeprint���`a(���bsaaf���bs1a'���bsia{���`dname���bsia}���bs1k activated.���bs1a'���`a)���`a
���`p                ���`hselector���aoa.���`jset_active���`a(���bkcdTrue���`a)���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`caxs���`a ���aoa=���`a ���`cfig���aoa.���`hsubplots���`a(���bmia2���`a)���`a
���`a
���`aN���`a ���aoa=���`a ���bmif100000���`b  ���bc1x:# If N is large one can see improvement by using blitting.���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmib10���`a,���`a ���`aN���`a)���`a
���`a
���`iselectors���`a ���aoa=���`a ���`a[���`a]���`a
���akcfor���`a ���`bax���`a,���`a ���`nselector_class���`a ���bowbin���`a ���bnbczip���`a(���`caxs���`a,���`a ���`a[���`qRectangleSelector���`a,���`a ���`oEllipseSelector���`a]���`a)���`a:���`a
���`d    ���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`ax���`a)���`a)���`b  ���bc1p# plot something���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bsaaf���bs2a"���bs2xClick and drag to draw a ���bsia{���`nselector_class���aoa.���bvmh__name__���bsia}���bs2a.���bs2a"���`a)���`a
���`d    ���`iselectors���aoa.���`fappend���`a(���`nselector_class���`a(���`a
���`h        ���`bax���`a,���`a ���`oselect_callback���`a,���`a
���`h        ���`guseblit���aoa=���bkcdTrue���`a,���`a
���`h        ���`fbutton���aoa=���`a[���bmia1���`a,���`a ���bmia3���`a]���`a,���`b  ���bc1w# disable middle button���`a
���`h        ���`hminspanx���aoa=���bmia5���`a,���`a ���`hminspany���aoa=���bmia5���`a,���`a
���`h        ���`jspancoords���aoa=���bs1a'���bs1fpixels���bs1a'���`a,���`a
���`h        ���`kinteractive���aoa=���bkcdTrue���`a)���`a)���`a
���`d    ���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1okey_press_event���bs1a'���`a,���`a ���`otoggle_selector���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs2a"���bs2fPress ���bs2a'���bs2at���bs2a'���bs2x$ to toggle the selectors on and off.���bseb\n���bs2a"���`a
���`q                 ���aoa+���`a ���`caxs���`a[���bmia0���`a]���aoa.���`iget_title���`a(���`a)���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x-#    - `matplotlib.widgets.RectangleSelector`���`a
���bc1x+#    - `matplotlib.widgets.EllipseSelector`���`a
`dNone�