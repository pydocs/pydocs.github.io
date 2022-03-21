Ù¯‚Ù´ƒ˜îÙ±‚bsdyş"""
=======
Textbox
=======

The Textbox widget lets users interactively provide text input, including
formulas. In this example, the plot is updated using the `.on_submit` method.
This method triggers the execution of the *submit* function when the
user presses enter in the textbox or leaves the textbox.

Note:  The `matplotlib.widgets.TextBox` widget is different from the following
static elements: :doc:`/tutorials/text/annotations` and
:doc:`/gallery/text_labels_and_annotations/placing_text_boxes`.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngwidgetsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`gTextBoxÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`osubplots_adjustÙ±‚`a(Ù±‚`fbottomÙ±‚aoa=Ù±‚bmfc0.2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚aoa-Ù±‚bmfc2.0Ù±‚`a,Ù±‚`a Ù±‚bmfc2.0Ù±‚`a,Ù±‚`a Ù±‚bmfe0.001Ù±‚`a)Ù±‚`a
Ù±‚`alÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`atÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`jzeros_likeÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnffsubmitÙ±‚`a(Ù±‚`jexpressionÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx¡"""
    Update the plotted function to the new math *expression*.

    *expression* is a string using "t" as its independent variable, e.g.
    "t ** 3".
    """Ù±‚`a
Ù±‚`d    Ù±‚`eydataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbdevalÙ±‚`a(Ù±‚`jexpressionÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`alÙ±‚aoa.Ù±‚`iset_ydataÙ±‚`a(Ù±‚`eydataÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`erelimÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`nautoscale_viewÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`eaxboxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`hadd_axesÙ±‚`a(Ù±‚`a[Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚bmfd0.05Ù±‚`a,Ù±‚`a Ù±‚bmfc0.8Ù±‚`a,Ù±‚`a Ù±‚bmfe0.075Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`htext_boxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gTextBoxÙ±‚`a(Ù±‚`eaxboxÙ±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2hEvaluateÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`mtextalignmentÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fcenterÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`htext_boxÙ±‚aoa.Ù±‚`ion_submitÙ±‚`a(Ù±‚`fsubmitÙ±‚`a)Ù±‚`a
Ù±‚`htext_boxÙ±‚aoa.Ù±‚`gset_valÙ±‚`a(Ù±‚bs2a"Ù±‚bs2ft ** 2Ù±‚bs2a"Ù±‚`a)Ù±‚`b  Ù±‚bc1x+# Trigger `submit` with the initial string.Ù±‚`a
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
Ù±‚bc1x##    - `matplotlib.widgets.TextBox`Ù±‚`a
`dNoneö