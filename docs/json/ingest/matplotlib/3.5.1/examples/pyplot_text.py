������������bsdx,"""
===========
Pyplot Text
===========

"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`bmu���`a,���`a ���`esigma���`a ���aoa=���`a ���bmic100���`a,���`a ���bmib15���`a
���`ax���`a ���aoa=���`a ���`bmu���`a ���aoa+���`a ���`esigma���`a ���aoa*���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmie10000���`a)���`a
���`a
���bc1x# the histogram of the data���`a
���`an���`a,���`a ���`dbins���`a,���`a ���`gpatches���`a ���aoa=���`a ���`cplt���aoa.���`dhist���`a(���`ax���`a,���`a ���bmib50���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ag���bs1a'���`a,���`a ���`ealpha���aoa=���bmfd0.75���`a)���`a
���`a
���`a
���`cplt���aoa.���`fxlabel���`a(���bs1a'���bs1fSmarts���bs1a'���`a)���`a
���`cplt���aoa.���`fylabel���`a(���bs1a'���bs1kProbability���bs1a'���`a)���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1oHistogram of IQ���bs1a'���`a)���`a
���`cplt���aoa.���`dtext���`a(���bmib60���`a,���`a ���bmfd.025���`a,���`a ���bsaar���bs1a'���bs1a$���bs1a\���bs1gmu=100,���bs1a\���bs1a ���bs1a\���bs1isigma=15$���bs1a'���`a)���`a
���`cplt���aoa.���`dxlim���`a(���bmib40���`a,���`a ���bmic160���`a)���`a
���`cplt���aoa.���`dylim���`a(���bmia0���`a,���`a ���bmfd0.03���`a)���`a
���`cplt���aoa.���`dgrid���`a(���bkcdTrue���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.pyplot.hist`���`a
���bc1x!#    - `matplotlib.pyplot.xlabel`���`a
���bc1x!#    - `matplotlib.pyplot.ylabel`���`a
���bc1x#    - `matplotlib.pyplot.text`���`a
���bc1x#    - `matplotlib.pyplot.grid`���`a
���bc1x#    - `matplotlib.pyplot.show`���`a
`dNone�