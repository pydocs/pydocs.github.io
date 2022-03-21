������������bsdx�"""
=========================
Fig Axes Customize Simple
=========================

Customize the background, labels and ticks of a simple plot.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1xO###############################################################################���`a
���bc1xA# `.pyplot.figure` creates a `matplotlib.figure.Figure` instance.���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`drect���`a ���aoa=���`a ���`cfig���aoa.���`epatch���`b  ���bc1v# a rectangle instance���`a
���`drect���aoa.���`mset_facecolor���`a(���bs1a'���bs1tlightgoldenrodyellow���bs1a'���`a)���`a
���`a
���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmfc0.1���`a,���`a ���bmfc0.3���`a,���`a ���bmfc0.4���`a,���`a ���bmfc0.4���`a]���`a)���`a
���`drect���`a ���aoa=���`a ���`cax1���aoa.���`epatch���`a
���`drect���aoa.���`mset_facecolor���`a(���bs1a'���bs1nlightslategray���bs1a'���`a)���`a
���`a
���`a
���akcfor���`a ���`elabel���`a ���bowbin���`a ���`cax1���aoa.���`exaxis���aoa.���`nget_ticklabels���`a(���`a)���`a:���`a
���`d    ���bc1x# label is a Text instance���`a
���`d    ���`elabel���aoa.���`iset_color���`a(���bs1a'���bs1gtab:red���bs1a'���`a)���`a
���`d    ���`elabel���aoa.���`lset_rotation���`a(���bmib45���`a)���`a
���`d    ���`elabel���aoa.���`lset_fontsize���`a(���bmib16���`a)���`a
���`a
���akcfor���`a ���`dline���`a ���bowbin���`a ���`cax1���aoa.���`eyaxis���aoa.���`mget_ticklines���`a(���`a)���`a:���`a
���`d    ���bc1x# line is a Line2D instance���`a
���`d    ���`dline���aoa.���`iset_color���`a(���bs1a'���bs1itab:green���bs1a'���`a)���`a
���`d    ���`dline���aoa.���`nset_markersize���`a(���bmib25���`a)���`a
���`d    ���`dline���aoa.���`sset_markeredgewidth���`a(���bmia3���`a)���`a
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
���bc1x,#    - `matplotlib.axis.Axis.get_ticklabels`���`a
���bc1x+#    - `matplotlib.axis.Axis.get_ticklines`���`a
���bc1x*#    - `matplotlib.text.Text.set_rotation`���`a
���bc1x*#    - `matplotlib.text.Text.set_fontsize`���`a
���bc1x'#    - `matplotlib.text.Text.set_color`���`a
���bc1x #    - `matplotlib.lines.Line2D`���`a
���bc1x*#    - `matplotlib.lines.Line2D.set_color`���`a
���bc1x/#    - `matplotlib.lines.Line2D.set_markersize`���`a
���bc1x4#    - `matplotlib.lines.Line2D.set_markeredgewidth`���`a
���bc1x/#    - `matplotlib.patches.Patch.set_facecolor`���`a
`dNone�