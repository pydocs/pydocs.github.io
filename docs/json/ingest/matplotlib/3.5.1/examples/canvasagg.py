ŸØÇÅŸ¥Éò…Ÿ±Çbsdy«"""
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
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnhbackendsŸ±Çbnna.Ÿ±Çbnnkbackend_aggŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`oFigureCanvasAggŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnffigureŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`fFigureŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnncPILŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`eImageŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fFigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cdpiŸ±Çaoa=Ÿ±Çbmic100Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1xN# A canvas must be manually attached to the figure (pyplot would automaticallyŸ±Ç`a
Ÿ±Çbc1xF# do it).  This is done by instantiating the canvas with the figure asŸ±Ç`a
Ÿ±Çbc1k# argument.Ÿ±Ç`a
Ÿ±Ç`fcanvasŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`oFigureCanvasAggŸ±Ç`a(Ÿ±Ç`cfigŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1s# Do some plotting.Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xO# Option 1: Save the figure to a file; can also be a file-like object (BytesIO,Ÿ±Ç`a
Ÿ±Çbc1h# etc.).Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`gsavefigŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2htest.pngŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM# Option 2: Retrieve a memoryview on the renderer buffer, and convert it to aŸ±Ç`a
Ÿ±Çbc1n# numpy array.Ÿ±Ç`a
Ÿ±Ç`fcanvasŸ±Çaoa.Ÿ±Ç`ddrawŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`drgbaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gasarrayŸ±Ç`a(Ÿ±Ç`fcanvasŸ±Çaoa.Ÿ±Ç`kbuffer_rgbaŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x# ... and pass it to PIL.Ÿ±Ç`a
Ÿ±Ç`bimŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`eImageŸ±Çaoa.Ÿ±Ç`ifromarrayŸ±Ç`a(Ÿ±Ç`drgbaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1xG# This image can then be saved to any format supported by Pillow, e.g.:Ÿ±Ç`a
Ÿ±Ç`bimŸ±Çaoa.Ÿ±Ç`dsaveŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2htest.bmpŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xN# Uncomment this line to display the image using ImageMagick's `display` tool.Ÿ±Ç`a
Ÿ±Çbc1k# im.show()Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x8#    - `matplotlib.backends.backend_agg.FigureCanvasAgg`Ÿ±Ç`a
Ÿ±Çbc1x!#    - `matplotlib.figure.Figure`Ÿ±Ç`a
Ÿ±Çbc1x-#    - `matplotlib.figure.Figure.add_subplot`Ÿ±Ç`a
Ÿ±Çbc1xG#    - `matplotlib.figure.Figure.savefig` / `matplotlib.pyplot.savefig`Ÿ±Ç`a
Ÿ±Çbc1x=#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`Ÿ±Ç`a
`dNoneˆ