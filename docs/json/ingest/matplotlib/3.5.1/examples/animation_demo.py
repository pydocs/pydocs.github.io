�����������bsdy�"""
================
pyplot animation
================

Generating an animation by calling `~.pyplot.pause` between plotting commands.

The method shown here is only suitable for simple, low-performance use.  For
more demanding applications, look at the :mod:`.animation` module and the
examples that use it.

Note that calling `time.sleep` instead of `~.pyplot.pause` would *not* work.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���`a(���bmib50���`a,���`a ���bmib50���`a,���`a ���bmib50���`a)���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`ddata���`a)���`a)���`a:���`a
���`d    ���`bax���aoa.���`ccla���`a(���`a)���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`ddata���`a[���`ai���`a]���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs2a"���bs2fframe ���bsib{}���bs2a"���aoa.���`fformat���`a(���`ai���`a)���`a)���`a
���`d    ���bc1x2# Note that using time.sleep does *not* work here!���`a
���`d    ���`cplt���aoa.���`epause���`a(���bmfc0.1���`a)���`a
`dNone�