������������bsdxY"""
===============
Watermark image
===============

Using a PNG file as a watermark.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnecbook���`a ���akbas���`a ���bnnecbook���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnneimage���`a ���akbas���`a ���bnneimage���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akdwith���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1ilogo2.png���bs1a'���`a)���`a ���akbas���`a ���`dfile���`a:���`a
���`d    ���`bim���`a ���aoa=���`a ���`eimage���aoa.���`fimread���`a(���`dfile���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`bax���aoa.���`dplot���`a(���`bnp���aoa.���`csin���`a(���bmib10���`a ���aoa*���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia1���`a)���`a)���`a,���`a ���bs1a'���bs1b-o���bs1a'���`a,���`a ���`bms���aoa=���bmib20���`a,���`a ���`ealpha���aoa=���bmfc0.7���`a,���`a ���`cmfc���aoa=���bs1a'���bs1forange���bs1a'���`a)���`a
���`bax���aoa.���`dgrid���`a(���`a)���`a
���`cfig���aoa.���`hfigimage���`a(���`bim���`a,���`a ���bmib10���`a,���`a ���bmib10���`a,���`a ���`fzorder���aoa=���bmia3���`a,���`a ���`ealpha���aoa=���bmfb.5���`a)���`a
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
���bc1x#    - `matplotlib.image`���`a
���bc1x=#    - `matplotlib.image.imread` / `matplotlib.pyplot.imread`���`a
���bc1x*#    - `matplotlib.figure.Figure.figimage`���`a
`dNone�