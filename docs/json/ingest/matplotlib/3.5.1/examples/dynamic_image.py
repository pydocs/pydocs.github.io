��������/���bsdx�"""
=================================================
Animated image using a precomputed list of images
=================================================

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnianimation���`a ���akbas���`a ���bnnianimation���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`a
���akcdef���`a ���bnfaf���`a(���`ax���`a,���`a ���`ay���`a)���`a:���`a
���`d    ���akfreturn���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a ���aoa+���`a ���`bnp���aoa.���`ccos���`a(���`ay���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmic120���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmic100���`a)���aoa.���`greshape���`a(���aoa-���bmia1���`a,���`a ���bmia1���`a)���`a
���`a
���bc1xF# ims is a list of lists, each row is a list of artists to draw in the���`a
���bc1xE# current frame; here we are just animating one artist, the image, in���`a
���bc1l# each frame���`a
���`cims���`a ���aoa=���`a ���`a[���`a]���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmib60���`a)���`a:���`a
���`d    ���`ax���`a ���aoa+���aoa=���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmfc15.���`a
���`d    ���`ay���`a ���aoa+���aoa=���`a ���`bnp���aoa.���`bpi���`a ���aoa/���`a ���bmfc20.���`a
���`d    ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`af���`a(���`ax���`a,���`a ���`ay���`a)���`a,���`a ���`hanimated���aoa=���bkcdTrue���`a)���`a
���`d    ���akbif���`a ���`ai���`a ���aob==���`a ���bmia0���`a:���`a
���`h        ���`bax���aoa.���`fimshow���`a(���`af���`a(���`ax���`a,���`a ���`ay���`a)���`a)���`b  ���bc1x# show an initial one first���`a
���`d    ���`cims���aoa.���`fappend���`a(���`a[���`bim���`a]���`a)���`a
���`a
���`cani���`a ���aoa=���`a ���`ianimation���aoa.���`oArtistAnimation���`a(���`cfig���`a,���`a ���`cims���`a,���`a ���`hinterval���aoa=���bmib50���`a,���`a ���`dblit���aoa=���bkcdTrue���`a,���`a
���`x                                 ���`lrepeat_delay���aoa=���bmid1000���`a)���`a
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