������������bsdx~"""
===================
Pyplot Two Subplots
===================

Create a figure with two subplots with `.pyplot.subplot`.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfaf���`a(���`at���`a)���`a:���`a
���`d    ���akfreturn���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a)���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`a
���`a
���`bt1���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc5.0���`a,���`a ���bmfc0.1���`a)���`a
���`bt2���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc5.0���`a,���`a ���bmfd0.02���`a)���`a
���`a
���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`cplt���aoa.���`gsubplot���`a(���bmic211���`a)���`a
���`cplt���aoa.���`dplot���`a(���`bt1���`a,���`a ���`af���`a(���`bt1���`a)���`a,���`a ���`ecolor���aoa=���bs1a'���bs1htab:blue���bs1a'���`a,���`a ���`fmarker���aoa=���bs1a'���bs1ao���bs1a'���`a)���`a
���`cplt���aoa.���`dplot���`a(���`bt2���`a,���`a ���`af���`a(���`bt2���`a)���`a,���`a ���`ecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`gsubplot���`a(���bmic212���`a)���`a
���`cplt���aoa.���`dplot���`a(���`bt2���`a,���`a ���`bnp���aoa.���`ccos���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`bt2���`a)���`a,���`a ���`ecolor���aoa=���bs1a'���bs1jtab:orange���bs1a'���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1b--���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x!#    - `matplotlib.pyplot.figure`���`a
���bc1x"#    - `matplotlib.pyplot.subplot`���`a
`dNone�