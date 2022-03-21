��������n���bsdx�"""
=================
Errorbar function
=================

This exhibits the most basic use of the error bar method.
In this case, constant values are provided for the error
in both the x- and y-directions.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1n# example data���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.1���`a,���`a ���bmia4���`a,���`a ���bmfc0.5���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`ax���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`dxerr���aoa=���bmfc0.2���`a,���`a ���`dyerr���aoa=���bmfc0.4���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xE#    - `matplotlib.axes.Axes.errorbar` / `matplotlib.pyplot.errorbar`���`a
`dNone�