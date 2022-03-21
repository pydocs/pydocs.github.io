��������+���bsdy�"""
========================
Custom Figure subclasses
========================

You can pass a `.Figure` subclass to `.pyplot.figure` if you want to change
the default behavior of the figure.

This example defines a `.Figure` subclass ``WatermarkFigure`` that accepts an
additional parameter ``watermark`` to display a custom watermark text. The
figure is created using the ``FigureClass`` parameter of `.pyplot.figure`.
The additional ``watermark`` parameter is passed on to the subclass
constructor.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnffigure���`a ���bknfimport���`a ���`fFigure���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akeclass���`a ���bncoWatermarkFigure���`a(���`fFigure���`a)���`a:���`a
���`d    ���bsdx%"""A figure with a text watermark."""���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���aoa*���`dargs���`a,���`a ���`iwatermark���aoa=���bkcdNone���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`a
���`h        ���akbif���`a ���`iwatermark���`a ���bowbis���`a ���bowcnot���`a ���bkcdNone���`a:���`a
���`l            ���`dbbox���`a ���aoa=���`a ���bnbddict���`a(���`hboxstyle���aoa=���bs1a'���bs1fsquare���bs1a'���`a,���`a ���`blw���aoa=���bmia3���`a,���`a ���`bec���aoa=���bs1a'���bs1dgray���bs1a'���`a,���`a
���`x                        ���`bfc���aoa=���`a(���bmfc0.9���`a,���`a ���bmfc0.9���`a,���`a ���bmfb.9���`a,���`a ���bmfb.5���`a)���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`l            ���bbpdself���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���`iwatermark���`a,���`a
���`v                      ���`bha���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`bva���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`hrotation���aoa=���bmib30���`a,���`a
���`v                      ���`hfontsize���aoa=���bmib40���`a,���`a ���`ecolor���aoa=���bs1a'���bs1dgray���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a,���`a ���`dbbox���aoa=���`dbbox���`a)���`a
���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmia3���`a,���`a ���bmia3���`a,���`a ���bmic201���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`dtanh���`a(���`ax���`a)���`a ���aoa+���`a ���bmfc0.1���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���bmia5���`a ���aoa*���`a ���`ax���`a)���`a
���`a
���`cplt���aoa.���`ffigure���`a(���`kFigureClass���aoa=���`oWatermarkFigure���`a,���`a ���`iwatermark���aoa=���bs1a'���bs1edraft���bs1a'���`a)���`a
���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x!#    - `matplotlib.pyplot.figure`���`a
���bc1x!#    - `matplotlib.figure.Figure`���`a
���bc1x&#    - `matplotlib.figure.Figure.text`���`a
`dNone�