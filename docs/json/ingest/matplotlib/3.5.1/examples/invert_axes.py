������������bsdxx"""
===========
Invert Axes
===========

You can use decreasing axes by flipping the normal order of the axis
limits
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmfd0.01���`a,���`a ���bmfc5.0���`a,���`a ���bmfd0.01���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���bmia5���`a,���`a ���bmia0���`a)���`b  ���bc1q# decreasing time���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1sdecreasing time (s)���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1lvoltage (mV)���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1tShould be growing...���bs1a'���`a)���`a
���`bax���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�