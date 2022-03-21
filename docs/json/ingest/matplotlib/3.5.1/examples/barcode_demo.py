������������bsdy�"""
=======
Barcode
=======
This demo shows how to produce a bar code.

The figure size is calculated so that the width in pixels is a multiple of the
number of data points to prevent interpolation artifacts. Additionally, the
``Axes`` is defined to span the whole figure and all ``Axis`` are turned off.

The data itself is rendered with `~.Axes.imshow` using

- ``code.reshape(1, -1)`` to turn the data into a 2D array with one row.
- ``imshow(..., aspect='auto')`` to allow for non-square pixels.
- ``imshow(..., interpolation='nearest')`` to prevent blurred edges. This
  should not happen anyway because we fine-tuned the figure width in pixels,
  but just to be safe.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`dcode���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���`a
���`d    ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a
���`d    ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a
���`d    ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a
���`d    ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a]���`a)���`a
���`a
���`mpixel_per_bar���`a ���aoa=���`a ���bmia4���`a
���`cdpi���`a ���aoa=���`a ���bmic100���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bnbclen���`a(���`dcode���`a)���`a ���aoa*���`a ���`mpixel_per_bar���`a ���aoa/���`a ���`cdpi���`a,���`a ���bmia2���`a)���`a,���`a ���`cdpi���aoa=���`cdpi���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a]���`a)���`b  ���bc1w# span the whole figure���`a
���`bax���aoa.���`lset_axis_off���`a(���`a)���`a
���`bax���aoa.���`fimshow���`a(���`dcode���aoa.���`greshape���`a(���bmia1���`a,���`a ���aoa-���bmia1���`a)���`a,���`a ���`dcmap���aoa=���bs1a'���bs1fbinary���bs1a'���`a,���`a ���`faspect���aoa=���bs1a'���bs1dauto���bs1a'���`a,���`a
���`j          ���`minterpolation���aoa=���bs1a'���bs1gnearest���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`���`a
���bc1x*#    - `matplotlib.figure.Figure.add_axes`���`a
`dNone�