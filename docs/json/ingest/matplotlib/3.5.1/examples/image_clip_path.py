������������bsdx�"""
============================
Clipping images with patches
============================

Demo of image that's been clipped by a circular patch.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���akbas���`a ���bnngpatches���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnecbook���`a ���akbas���`a ���bnnecbook���`a
���`a
���`a
���akdwith���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1pgrace_hopper.jpg���bs1a'���`a)���`a ���akbas���`a ���`jimage_file���`a:���`a
���`d    ���`eimage���`a ���aoa=���`a ���`cplt���aoa.���`fimread���`a(���`jimage_file���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`eimage���`a)���`a
���`epatch���`a ���aoa=���`a ���`gpatches���aoa.���`fCircle���`a(���`a(���bmic260���`a,���`a ���bmic200���`a)���`a,���`a ���`fradius���aoa=���bmic200���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransData���`a)���`a
���`bim���aoa.���`mset_clip_path���`a(���`epatch���`a)���`a
���`a
���`bax���aoa.���`daxis���`a(���bs1a'���bs1coff���bs1a'���`a)���`a
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
���bc1x/#    - `matplotlib.artist.Artist.set_clip_path`���`a
`dNone�