������������bsdxA"""
==================
Animated line plot
==================

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnianimation���`a ���akbas���`a ���bnnianimation���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a,���`a ���bmfd0.01���`a)���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a)���`a
���`a
���`a
���akcdef���`a ���bnfganimate���`a(���`ai���`a)���`a:���`a
���`d    ���`dline���aoa.���`iset_ydata���`a(���`bnp���aoa.���`csin���`a(���`ax���`a ���aoa+���`a ���`ai���`a ���aoa/���`a ���bmib50���`a)���`a)���`b  ���bc1r# update the data.���`a
���`d    ���akfreturn���`a ���`dline���`a,���`a
���`a
���`a
���`cani���`a ���aoa=���`a ���`ianimation���aoa.���`mFuncAnimation���`a(���`a
���`d    ���`cfig���`a,���`a ���`ganimate���`a,���`a ���`hinterval���aoa=���bmib20���`a,���`a ���`dblit���aoa=���bkcdTrue���`a,���`a ���`jsave_count���aoa=���bmib50���`a)���`a
���`a
���bc1x!# To save the animation, use e.g.���`a
���bc1a#���`a
���bc1w# ani.save("movie.mp4")���`a
���bc1a#���`a
���bc1d# or���`a
���bc1a#���`a
���bc1x"# writer = animation.FFMpegWriter(���`a
���bc1x7#     fps=15, metadata=dict(artist='Me'), bitrate=1800)���`a
���bc1x&# ani.save("movie.mp4", writer=writer)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�