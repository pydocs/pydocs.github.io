�����������bsdy�"""
===============================================
Programmatically controlling subplot adjustment
===============================================

.. note::

    This example is primarily intended to show some advanced concepts in
    Matplotlib.

    If you are only looking for having enough space for your labels, it is
    almost always simpler and good enough to either set the subplot parameters
    manually using `.Figure.subplots_adjust`, or use one of the automatic
    layout mechanisms
    (:doc:`/tutorials/intermediate/constrainedlayout_guide` or
    :doc:`/tutorials/intermediate/tight_layout_guide`).

This example describes a user-defined way to read out Artist sizes and
set the subplot parameters accordingly. Its main purpose is to illustrate
some advanced concepts like reading out text positions, working with
bounding boxes and transforms and using
:ref:`events <event-handling-tutorial>`. But it can also serve as a starting
point if you want to automate the layouting and need more flexibility than
tight layout and constrained layout.

Below, we collect the bounding boxes of all y-labels and move the left border
of the subplot to the right so that it leaves enough room for the union of all
the bounding boxes.

There's one catch with calculating text bounding boxes:
Querying the text bounding boxes (`.Text.get_window_extent`) needs a
renderer (`.RendererBase` instance), to calculate the text size. This renderer
is only available after the figure has been drawn (`.Figure.draw`).

A solution to this is putting the adjustment logic in a draw callback.
This function is executed after the figure has been drawn. It can now check
if the subplot leaves enough room for the text. If not, the subplot parameters
are updated and second draw is triggered.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���akbas���`a ���bnnkmtransforms���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���bnberange���`a(���bmib10���`a)���`a)���`a
���`bax���aoa.���`jset_yticks���`a(���`a[���bmia2���`a,���`a ���bmia5���`a,���`a ���bmia7���`a]���`a,���`a ���`flabels���aoa=���`a[���bs1a'���bs1vreally, really, really���bs1a'���`a,���`a ���bs1a'���bs1dlong���bs1a'���`a,���`a ���bs1a'���bs1flabels���bs1a'���`a]���`a)���`a
���`a
���`a
���akcdef���`a ���bnfgon_draw���`a(���`eevent���`a)���`a:���`a
���`d    ���`fbboxes���`a ���aoa=���`a ���`a[���`a]���`a
���`d    ���akcfor���`a ���`elabel���`a ���bowbin���`a ���`bax���aoa.���`oget_yticklabels���`a(���`a)���`a:���`a
���`h        ���bc1x# Bounding box in pixels���`a
���`h        ���`gbbox_px���`a ���aoa=���`a ���`elabel���aoa.���`qget_window_extent���`a(���`a)���`a
���`h        ���bc1xB# Transform to relative figure coordinates. This is the inverse of���`a
���`h        ���bc1n# transFigure.���`a
���`h        ���`hbbox_fig���`a ���aoa=���`a ���`gbbox_px���aoa.���`ktransformed���`a(���`cfig���aoa.���`ktransFigure���aoa.���`hinverted���`a(���`a)���`a)���`a
���`h        ���`fbboxes���aoa.���`fappend���`a(���`hbbox_fig���`a)���`a
���`d    ���bc1xF# the bbox that bounds all the bboxes, again in relative figure coords���`a
���`d    ���`dbbox���`a ���aoa=���`a ���`kmtransforms���aoa.���`dBbox���aoa.���`eunion���`a(���`fbboxes���`a)���`a
���`d    ���akbif���`a ���`cfig���aoa.���`ksubplotpars���aoa.���`dleft���`a ���aoa<���`a ���`dbbox���aoa.���`ewidth���`a:���`a
���`h        ���bc1x.# Move the subplot left edge more to the right���`a
���`h        ���`cfig���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfc1.1���aoa*���`dbbox���aoa.���`ewidth���`a)���`b  ���bc1n# pad a little���`a
���`h        ���`cfig���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1jdraw_event���bs1a'���`a,���`a ���`gon_draw���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x3#    - `matplotlib.artist.Artist.get_window_extent`���`a
���bc1x##    - `matplotlib.transforms.Bbox`���`a
���bc1x3#    - `matplotlib.transforms.BboxBase.transformed`���`a
���bc1x-#    - `matplotlib.transforms.BboxBase.union`���`a
���bc1x1#    - `matplotlib.transforms.Transform.inverted`���`a
���bc1x1#    - `matplotlib.figure.Figure.subplots_adjust`���`a
���bc1x(#    - `matplotlib.figure.SubplotParams`���`a
���bc1x>#    - `matplotlib.backend_bases.FigureCanvasBase.mpl_connect`���`a
`dNone�