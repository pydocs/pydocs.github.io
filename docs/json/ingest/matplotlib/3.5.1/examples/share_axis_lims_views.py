��������u���bsdy�"""
Sharing axis limits and views
=============================

It's common to make two or more plots which share an axis, e.g., two subplots
with time as a common axis.  When you pan and zoom around on one, you want the
other to move around with you.  To facilitate this, matplotlib Axes support a
``sharex`` and ``sharey`` attribute.  When you create a `~.pyplot.subplot` or
`~.pyplot.axes`, you can pass in a keyword indicating what axes you want to
share with.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmib10���`a,���`a ���bmfd0.01���`a)���`a
���`a
���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���bmic211���`a)���`a
���`cax1���aoa.���`dplot���`a(���`at���`a,���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a)���`a
���`a
���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���bmic212���`a,���`a ���`fsharex���aoa=���`cax1���`a)���`a
���`cax2���aoa.���`dplot���`a(���`at���`a,���`a ���`bnp���aoa.���`csin���`a(���bmia4���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�