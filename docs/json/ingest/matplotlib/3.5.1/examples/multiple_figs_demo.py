������������bsdy�"""
===================================
Managing multiple figures in pyplot
===================================

`matplotlib.pyplot` uses the concept of a *current figure* and *current axes*.
Figures are identified via a figure number that is passed to `~.pyplot.figure`.
The figure with the given number is set as *current figure*. Additionally, if
no figure with the number exists, a new one is created.

.. note::

    We discourage working with multiple figures in pyplot because managing
    the *current figure* is cumbersome and error-prone. Instead, we recommend
    to use the object-oriented approach and call methods on Figure and Axes
    instances.

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfc0.0���`a,���`a ���bmfc2.0���`a,���`a ���bmfd0.01���`a)���`a
���`bs1���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`bs2���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia4���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1q# Create figure 1���`a
���`a
���`cplt���aoa.���`ffigure���`a(���bmia1���`a)���`a
���`cplt���aoa.���`gsubplot���`a(���bmic211���`a)���`a
���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���`bs1���`a)���`a
���`cplt���aoa.���`gsubplot���`a(���bmic212���`a)���`a
���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���bmia2���aoa*���`bs1���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1q# Create figure 2���`a
���`a
���`cplt���aoa.���`ffigure���`a(���bmia2���`a)���`a
���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���`bs2���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x3# Now switch back to figure 1 and make some changes���`a
���`a
���`cplt���aoa.���`ffigure���`a(���bmia1���`a)���`a
���`cplt���aoa.���`gsubplot���`a(���bmic211���`a)���`a
���`cplt���aoa.���`dplot���`a(���`at���`a,���`a ���`bs2���`a,���`a ���bs1a'���bs1as���bs1a'���`a)���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`cgca���`a(���`a)���`a
���`bax���aoa.���`oset_xticklabels���`a(���`a[���`a]���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�