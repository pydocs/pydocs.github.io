������������bsdy�"""
======================
Plotting with keywords
======================

There are some instances where you have data in a format that lets you
access particular variables with strings: for example, with
`numpy.recarray` or `pandas.DataFrame`.

Matplotlib allows you provide such an object with the ``data`` keyword
argument. If provided, then you may generate plots with the strings
corresponding to these variables.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`ddata���`a ���aoa=���`a ���`a{���bs1a'���bs1aa���bs1a'���`a:���`a ���`bnp���aoa.���`farange���`a(���bmib50���`a)���`a,���`a
���`h        ���bs1a'���bs1ac���bs1a'���`a:���`a ���`bnp���aoa.���`frandom���aoa.���`grandint���`a(���bmia0���`a,���`a ���bmib50���`a,���`a ���bmib50���`a)���`a,���`a
���`h        ���bs1a'���bs1ad���bs1a'���`a:���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmib50���`a)���`a}���`a
���`ddata���`a[���bs1a'���bs1ab���bs1a'���`a]���`a ���aoa=���`a ���`ddata���`a[���bs1a'���bs1aa���bs1a'���`a]���`a ���aoa+���`a ���bmib10���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmib50���`a)���`a
���`ddata���`a[���bs1a'���bs1ad���bs1a'���`a]���`a ���aoa=���`a ���`bnp���aoa.���`cabs���`a(���`ddata���`a[���bs1a'���bs1ad���bs1a'���`a]���`a)���`a ���aoa*���`a ���bmic100���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`gscatter���`a(���bs1a'���bs1aa���bs1a'���`a,���`a ���bs1a'���bs1ab���bs1a'���`a,���`a ���`ac���aoa=���bs1a'���bs1ac���bs1a'���`a,���`a ���`as���aoa=���bs1a'���bs1ad���bs1a'���`a,���`a ���`ddata���aoa=���`ddata���`a)���`a
���`bax���aoa.���`cset���`a(���`fxlabel���aoa=���bs1a'���bs1gentry a���bs1a'���`a,���`a ���`fylabel���aoa=���bs1a'���bs1gentry b���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�