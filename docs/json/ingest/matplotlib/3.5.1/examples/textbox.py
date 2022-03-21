������������bsdy�"""
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
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngwidgets���`a ���bknfimport���`a ���`gTextBox���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`fbottom���aoa=���bmfc0.2���`a)���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc2.0���`a,���`a ���bmfc2.0���`a,���`a ���bmfe0.001���`a)���`a
���`al���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`bnp���aoa.���`jzeros_like���`a(���`at���`a)���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`a
���`a
���akcdef���`a ���bnffsubmit���`a(���`jexpression���`a)���`a:���`a
���`d    ���bsdx�"""
    Update the plotted function to the new math *expression*.

    *expression* is a string using "t" as its independent variable, e.g.
    "t ** 3".
    """���`a
���`d    ���`eydata���`a ���aoa=���`a ���bnbdeval���`a(���`jexpression���`a)���`a
���`d    ���`al���aoa.���`iset_ydata���`a(���`eydata���`a)���`a
���`d    ���`bax���aoa.���`erelim���`a(���`a)���`a
���`d    ���`bax���aoa.���`nautoscale_view���`a(���`a)���`a
���`d    ���`cplt���aoa.���`ddraw���`a(���`a)���`a
���`a
���`a
���`eaxbox���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmfc0.1���`a,���`a ���bmfd0.05���`a,���`a ���bmfc0.8���`a,���`a ���bmfe0.075���`a]���`a)���`a
���`htext_box���`a ���aoa=���`a ���`gTextBox���`a(���`eaxbox���`a,���`a ���bs2a"���bs2hEvaluate���bs2a"���`a,���`a ���`mtextalignment���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`htext_box���aoa.���`ion_submit���`a(���`fsubmit���`a)���`a
���`htext_box���aoa.���`gset_val���`a(���bs2a"���bs2ft ** 2���bs2a"���`a)���`b  ���bc1x+# Trigger `submit` with the initial string.���`a
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
���bc1x##    - `matplotlib.widgets.TextBox`���`a
`dNone�