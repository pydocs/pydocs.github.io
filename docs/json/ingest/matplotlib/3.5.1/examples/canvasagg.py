������������bsdy�"""
==============
CanvasAgg demo
==============

This example shows how to use the agg backend directly to create images, which
may be of use to web application developers who want full control over their
code without using the pyplot interface to manage figures, figure closing etc.

.. note::

    It is not necessary to avoid using the pyplot interface in order to
    create figures without a graphical front-end - simply setting
    the backend to "Agg" would be sufficient.

In this example, we show how to save the contents of the agg canvas to a file,
and how to extract them to a numpy array, which can in turn be passed off
to Pillow_.  The latter functionality allows e.g. to use Matplotlib inside a
cgi-script *without* needing to write a figure to disk, and to write images in
any format supported by Pillow.

.. _Pillow: https://pillow.readthedocs.io/
.. redirect-from:: /gallery/misc/agg_buffer
.. redirect-from:: /gallery/misc/agg_buffer_to_array
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnhbackends���bnna.���bnnkbackend_agg���`a ���bknfimport���`a ���`oFigureCanvasAgg���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnffigure���`a ���bknfimport���`a ���`fFigure���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnncPIL���`a ���bknfimport���`a ���`eImage���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`fFigure���`a(���`gfigsize���aoa=���`a(���bmia5���`a,���`a ���bmia4���`a)���`a,���`a ���`cdpi���aoa=���bmic100���`a)���`a
���bc1xN# A canvas must be manually attached to the figure (pyplot would automatically���`a
���bc1xF# do it).  This is done by instantiating the canvas with the figure as���`a
���bc1k# argument.���`a
���`fcanvas���`a ���aoa=���`a ���`oFigureCanvasAgg���`a(���`cfig���`a)���`a
���`a
���bc1s# Do some plotting.���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`a)���`a
���`bax���aoa.���`dplot���`a(���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a]���`a)���`a
���`a
���bc1xO# Option 1: Save the figure to a file; can also be a file-like object (BytesIO,���`a
���bc1h# etc.).���`a
���`cfig���aoa.���`gsavefig���`a(���bs2a"���bs2htest.png���bs2a"���`a)���`a
���`a
���bc1xM# Option 2: Retrieve a memoryview on the renderer buffer, and convert it to a���`a
���bc1n# numpy array.���`a
���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`drgba���`a ���aoa=���`a ���`bnp���aoa.���`gasarray���`a(���`fcanvas���aoa.���`kbuffer_rgba���`a(���`a)���`a)���`a
���bc1x# ... and pass it to PIL.���`a
���`bim���`a ���aoa=���`a ���`eImage���aoa.���`ifromarray���`a(���`drgba���`a)���`a
���bc1xG# This image can then be saved to any format supported by Pillow, e.g.:���`a
���`bim���aoa.���`dsave���`a(���bs2a"���bs2htest.bmp���bs2a"���`a)���`a
���`a
���bc1xN# Uncomment this line to display the image using ImageMagick's `display` tool.���`a
���bc1k# im.show()���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x8#    - `matplotlib.backends.backend_agg.FigureCanvasAgg`���`a
���bc1x!#    - `matplotlib.figure.Figure`���`a
���bc1x-#    - `matplotlib.figure.Figure.add_subplot`���`a
���bc1xG#    - `matplotlib.figure.Figure.savefig` / `matplotlib.pyplot.savefig`���`a
���bc1x=#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`���`a
`dNone�