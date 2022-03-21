Ù¯‚Ù´ƒ™Ù±‚bsdyú"""
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
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnjtransformsÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnkmtransformsÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚bnberangeÙ±‚`a(Ù±‚bmib10Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia7Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`flabelsÙ±‚aoa=Ù±‚`a[Ù±‚bs1a'Ù±‚bs1vreally, really, reallyÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1dlongÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1flabelsÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfgon_drawÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`fbboxesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`elabelÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`oget_yticklabelsÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1x# Bounding box in pixelsÙ±‚`a
Ù±‚`h        Ù±‚`gbbox_pxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`elabelÙ±‚aoa.Ù±‚`qget_window_extentÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bc1xB# Transform to relative figure coordinates. This is the inverse ofÙ±‚`a
Ù±‚`h        Ù±‚bc1n# transFigure.Ù±‚`a
Ù±‚`h        Ù±‚`hbbox_figÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gbbox_pxÙ±‚aoa.Ù±‚`ktransformedÙ±‚`a(Ù±‚`cfigÙ±‚aoa.Ù±‚`ktransFigureÙ±‚aoa.Ù±‚`hinvertedÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`fbboxesÙ±‚aoa.Ù±‚`fappendÙ±‚`a(Ù±‚`hbbox_figÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1xF# the bbox that bounds all the bboxes, again in relative figure coordsÙ±‚`a
Ù±‚`d    Ù±‚`dbboxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`kmtransformsÙ±‚aoa.Ù±‚`dBboxÙ±‚aoa.Ù±‚`eunionÙ±‚`a(Ù±‚`fbboxesÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`ksubplotparsÙ±‚aoa.Ù±‚`dleftÙ±‚`a Ù±‚aoa<Ù±‚`a Ù±‚`dbboxÙ±‚aoa.Ù±‚`ewidthÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1x.# Move the subplot left edge more to the rightÙ±‚`a
Ù±‚`h        Ù±‚`cfigÙ±‚aoa.Ù±‚`osubplots_adjustÙ±‚`a(Ù±‚`dleftÙ±‚aoa=Ù±‚bmfc1.1Ù±‚aoa*Ù±‚`dbboxÙ±‚aoa.Ù±‚`ewidthÙ±‚`a)Ù±‚`b  Ù±‚bc1n# pad a littleÙ±‚`a
Ù±‚`h        Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jdraw_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gon_drawÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x3#    - `matplotlib.artist.Artist.get_window_extent`Ù±‚`a
Ù±‚bc1x##    - `matplotlib.transforms.Bbox`Ù±‚`a
Ù±‚bc1x3#    - `matplotlib.transforms.BboxBase.transformed`Ù±‚`a
Ù±‚bc1x-#    - `matplotlib.transforms.BboxBase.union`Ù±‚`a
Ù±‚bc1x1#    - `matplotlib.transforms.Transform.inverted`Ù±‚`a
Ù±‚bc1x1#    - `matplotlib.figure.Figure.subplots_adjust`Ù±‚`a
Ù±‚bc1x(#    - `matplotlib.figure.SubplotParams`Ù±‚`a
Ù±‚bc1x>#    - `matplotlib.backend_bases.FigureCanvasBase.mpl_connect`Ù±‚`a
`dNoneö