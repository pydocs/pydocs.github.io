�����������bsdxI"""
============
Oscilloscope
============

Emulates an oscilloscope.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnelines���`a ���bknfimport���`a ���`fLine2D���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnianimation���`a ���akbas���`a ���bnnianimation���`a
���`a
���`a
���akeclass���`a ���bnceScope���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`bax���`a,���`a ���`dmaxt���aoa=���bmia2���`a,���`a ���`bdt���aoa=���bmfd0.02���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`bax���`a ���aoa=���`a ���`bax���`a
���`h        ���bbpdself���aoa.���`bdt���`a ���aoa=���`a ���`bdt���`a
���`h        ���bbpdself���aoa.���`dmaxt���`a ���aoa=���`a ���`dmaxt���`a
���`h        ���bbpdself���aoa.���`etdata���`a ���aoa=���`a ���`a[���bmia0���`a]���`a
���`h        ���bbpdself���aoa.���`eydata���`a ���aoa=���`a ���`a[���bmia0���`a]���`a
���`h        ���bbpdself���aoa.���`dline���`a ���aoa=���`a ���`fLine2D���`a(���bbpdself���aoa.���`etdata���`a,���`a ���bbpdself���aoa.���`eydata���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`hadd_line���`a(���bbpdself���aoa.���`dline���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`hset_ylim���`a(���aoa-���bmfb.1���`a,���`a ���bmfc1.1���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bbpdself���aoa.���`dmaxt���`a)���`a
���`a
���`d    ���akcdef���`a ���bnffupdate���`a(���bbpdself���`a,���`a ���`ay���`a)���`a:���`a
���`h        ���`elastt���`a ���aoa=���`a ���bbpdself���aoa.���`etdata���`a[���aoa-���bmia1���`a]���`a
���`h        ���akbif���`a ���`elastt���`a ���aoa>���`a ���bbpdself���aoa.���`etdata���`a[���bmia0���`a]���`a ���aoa+���`a ���bbpdself���aoa.���`dmaxt���`a:���`b  ���bc1r# reset the arrays���`a
���`l            ���bbpdself���aoa.���`etdata���`a ���aoa=���`a ���`a[���bbpdself���aoa.���`etdata���`a[���aoa-���bmia1���`a]���`a]���`a
���`l            ���bbpdself���aoa.���`eydata���`a ���aoa=���`a ���`a[���bbpdself���aoa.���`eydata���`a[���aoa-���bmia1���`a]���`a]���`a
���`l            ���bbpdself���aoa.���`bax���aoa.���`hset_xlim���`a(���bbpdself���aoa.���`etdata���`a[���bmia0���`a]���`a,���`a ���bbpdself���aoa.���`etdata���`a[���bmia0���`a]���`a ���aoa+���`a ���bbpdself���aoa.���`dmaxt���`a)���`a
���`l            ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`h        ���`at���`a ���aoa=���`a ���bbpdself���aoa.���`etdata���`a[���aoa-���bmia1���`a]���`a ���aoa+���`a ���bbpdself���aoa.���`bdt���`a
���`h        ���bbpdself���aoa.���`etdata���aoa.���`fappend���`a(���`at���`a)���`a
���`h        ���bbpdself���aoa.���`eydata���aoa.���`fappend���`a(���`ay���`a)���`a
���`h        ���bbpdself���aoa.���`dline���aoa.���`hset_data���`a(���bbpdself���aoa.���`etdata���`a,���`a ���bbpdself���aoa.���`eydata���`a)���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`dline���`a,���`a
���`a
���`a
���akcdef���`a ���bnfgemitter���`a(���`ap���aoa=���bmfc0.1���`a)���`a:���`a
���`d    ���bsdxA"""Return a random value in [0, 1) with probability p, else 0."""���`a
���`d    ���akewhile���`a ���bkcdTrue���`a:���`a
���`h        ���`av���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia1���`a)���`a
���`h        ���akbif���`a ���`av���`a ���aoa>���`a ���`ap���`a:���`a
���`l            ���akeyield���`a ���bmfb0.���`a
���`h        ���akdelse���`a:���`a
���`l            ���akeyield���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia1���`a)���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a ���aoa/���aoa/���`a ���bmib10���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`escope���`a ���aoa=���`a ���`eScope���`a(���`bax���`a)���`a
���`a
���bc1xC# pass a generator in "emitter" to produce data for the update func���`a
���`cani���`a ���aoa=���`a ���`ianimation���aoa.���`mFuncAnimation���`a(���`cfig���`a,���`a ���`escope���aoa.���`fupdate���`a,���`a ���`gemitter���`a,���`a ���`hinterval���aoa=���bmib50���`a,���`a
���`x                              ���`dblit���aoa=���bkcdTrue���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�