��������b���bsdxc"""
============
Layer Images
============

Layer images above one another using alpha blending
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfefunc3���`a(���`ax���`a,���`a ���`ay���`a)���`a:���`a
���`d    ���akfreturn���`a ���`a(���bmia1���`a ���aoa-���`a ���`ax���`a ���aoa/���`a ���bmia2���`a ���aoa+���`a ���`ax���aoa*���aoa*���bmia5���`a ���aoa+���`a ���`ay���aoa*���aoa*���bmia3���`a)���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`ax���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`ay���aoa*���aoa*���bmia2���`a)���`a)���`a
���`a
���`a
���bc1x/# make these smaller to increase the resolution���`a
���`bdx���`a,���`a ���`bdy���`a ���aoa=���`a ���bmfd0.05���`a,���`a ���bmfd0.05���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc3.0���`a,���`a ���bmfc3.0���`a,���`a ���`bdx���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc3.0���`a,���`a ���bmfc3.0���`a,���`a ���`bdy���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���bc1xA# when layering multiple images, the images need to have the same���`a
���bc1xC# extent.  This does not mean they need to have the same shape, but���`a
���bc1xF# they both need to render to the same coordinate system determined by���`a
���bc1xC# xmin, xmax, ymin, ymax.  Note if you use different interpolations���`a
���bc1x@# for the images their apparent extent could be different due to���`a
���bc1x# interpolation edge effects���`a
���`a
���`fextent���`a ���aoa=���`a ���`bnp���aoa.���`cmin���`a(���`ax���`a)���`a,���`a ���`bnp���aoa.���`cmax���`a(���`ax���`a)���`a,���`a ���`bnp���aoa.���`cmin���`a(���`ay���`a)���`a,���`a ���`bnp���aoa.���`cmax���`a(���`ay���`a)���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gframeon���aoa=���bkceFalse���`a)���`a
���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cadd���aoa.���`eouter���`a(���bnberange���`a(���bmia8���`a)���`a,���`a ���bnberange���`a(���bmia8���`a)���`a)���`a ���aoa%���`a ���bmia2���`b  ���bc1l# chessboard���`a
���`cim1���`a ���aoa=���`a ���`cplt���aoa.���`fimshow���`a(���`bZ1���`a,���`a ���`dcmap���aoa=���`cplt���aoa.���`bcm���aoa.���`dgray���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1gnearest���bs1a'���`a,���`a
���`q                 ���`fextent���aoa=���`fextent���`a)���`a
���`a
���`bZ2���`a ���aoa=���`a ���`efunc3���`a(���`aX���`a,���`a ���`aY���`a)���`a
���`a
���`cim2���`a ���aoa=���`a ���`cplt���aoa.���`fimshow���`a(���`bZ2���`a,���`a ���`dcmap���aoa=���`cplt���aoa.���`bcm���aoa.���`gviridis���`a,���`a ���`ealpha���aoa=���bmfb.9���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1hbilinear���bs1a'���`a,���`a
���`q                 ���`fextent���aoa=���`fextent���`a)���`a
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
���bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`���`a
`dNone�