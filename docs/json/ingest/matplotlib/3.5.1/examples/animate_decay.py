��������k���bsdx�"""
=====
Decay
=====

This example showcases:

- using a generator to drive an animation,
- changing axes limits during an animation.
"""���`a
���`a
���bknfimport���`a ���bnniitertools���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnianimation���`a ���akbas���`a ���bnnianimation���`a
���`a
���`a
���akcdef���`a ���bnfhdata_gen���`a(���`a)���`a:���`a
���`d    ���akcfor���`a ���`ccnt���`a ���bowbin���`a ���`iitertools���aoa.���`ecount���`a(���`a)���`a:���`a
���`h        ���`at���`a ���aoa=���`a ���`ccnt���`a ���aoa/���`a ���bmib10���`a
���`h        ���akeyield���`a ���`at���`a,���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`at���aoa/���bmfc10.���`a)���`a
���`a
���`a
���akcdef���`a ���bnfdinit���`a(���`a)���`a:���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���aoa-���bmfc1.1���`a,���`a ���bmfc1.1���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmib10���`a)���`a
���`d    ���akcdel���`a ���`exdata���`a[���`a:���`a]���`a
���`d    ���akcdel���`a ���`eydata���`a[���`a:���`a]���`a
���`d    ���`dline���aoa.���`hset_data���`a(���`exdata���`a,���`a ���`eydata���`a)���`a
���`d    ���akfreturn���`a ���`dline���`a,���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`a[���`a]���`a,���`a ���`a[���`a]���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`bax���aoa.���`dgrid���`a(���`a)���`a
���`exdata���`a,���`a ���`eydata���`a ���aoa=���`a ���`a[���`a]���`a,���`a ���`a[���`a]���`a
���`a
���`a
���akcdef���`a ���bnfcrun���`a(���`ddata���`a)���`a:���`a
���`d    ���bc1q# update the data���`a
���`d    ���`at���`a,���`a ���`ay���`a ���aoa=���`a ���`ddata���`a
���`d    ���`exdata���aoa.���`fappend���`a(���`at���`a)���`a
���`d    ���`eydata���aoa.���`fappend���`a(���`ay���`a)���`a
���`d    ���`dxmin���`a,���`a ���`dxmax���`a ���aoa=���`a ���`bax���aoa.���`hget_xlim���`a(���`a)���`a
���`a
���`d    ���akbif���`a ���`at���`a ���aoa>���aoa=���`a ���`dxmax���`a:���`a
���`h        ���`bax���aoa.���`hset_xlim���`a(���`dxmin���`a,���`a ���bmia2���aoa*���`dxmax���`a)���`a
���`h        ���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`d    ���`dline���aoa.���`hset_data���`a(���`exdata���`a,���`a ���`eydata���`a)���`a
���`a
���`d    ���akfreturn���`a ���`dline���`a,���`a
���`a
���`cani���`a ���aoa=���`a ���`ianimation���aoa.���`mFuncAnimation���`a(���`cfig���`a,���`a ���`crun���`a,���`a ���`hdata_gen���`a,���`a ���`hinterval���aoa=���bmib10���`a,���`a ���`iinit_func���aoa=���`dinit���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�