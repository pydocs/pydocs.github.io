�����������bsdx8"""
===============
Simple Colorbar
===============

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���`a ���bknfimport���`a ���`smake_axes_locatable���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`gsubplot���`a(���`a)���`a
���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`bnp���aoa.���`farange���`a(���bmic100���`a)���aoa.���`greshape���`a(���`a(���bmib10���`a,���`a ���bmib10���`a)���`a)���`a)���`a
���`a
���bc1xE# create an axes on the right side of ax. The width of cax will be 5%���`a
���bc1xF# of ax and the padding between cax and ax will be fixed at 0.05 inch.���`a
���`gdivider���`a ���aoa=���`a ���`smake_axes_locatable���`a(���`bax���`a)���`a
���`ccax���`a ���aoa=���`a ���`gdivider���aoa.���`kappend_axes���`a(���bs2a"���bs2eright���bs2a"���`a,���`a ���`dsize���aoa=���bs2a"���bs2a5���bs2a%���bs2a"���`a,���`a ���`cpad���aoa=���bmfd0.05���`a)���`a
���`a
���`cplt���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`ccax���aoa=���`ccax���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�