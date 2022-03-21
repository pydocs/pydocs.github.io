������������bsdx�"""
============
Ellipse Demo
============

Draw many ellipses. Here individual ellipses are drawn. Compare this
to the :doc:`Ellipse collection example
</gallery/shapes_and_collections/ellipse_collection>`.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`gEllipse���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cNUM���`a ���aoa=���`a ���bmic250���`a
���`a
���`dells���`a ���aoa=���`a ���`a[���`gEllipse���`a(���`bxy���aoa=���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia2���`a)���`a ���aoa*���`a ���bmib10���`a,���`a
���`p                ���`ewidth���aoa=���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`a)���`a,���`a ���`fheight���aoa=���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`a)���`a,���`a
���`p                ���`eangle���aoa=���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`a)���`a ���aoa*���`a ���bmic360���`a)���`a
���`h        ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���`cNUM���`a)���`a]���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���`a{���bs1a'���bs1faspect���bs1a'���`a:���`a ���bs1a'���bs1eequal���bs1a'���`a}���`a)���`a
���akcfor���`a ���`ae���`a ���bowbin���`a ���`dells���`a:���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`ae���`a)���`a
���`d    ���`ae���aoa.���`lset_clip_box���`a(���`bax���aoa.���`dbbox���`a)���`a
���`d    ���`ae���aoa.���`iset_alpha���`a(���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`a)���`a)���`a
���`d    ���`ae���aoa.���`mset_facecolor���`a(���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia3���`a)���`a)���`a
���`a
���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmib10���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmib10���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1q# ===============���`a
���bc1q# Ellipse Rotated���`a
���bc1q# ===============���`a
���bc1a#���`a
���bc1x+# Draw many ellipses with different angles.���`a
���bc1a#���`a
���`a
���`jangle_step���`a ���aoa=���`a ���bmib45���`b  ���bc1i# degrees���`a
���`fangles���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmic180���`a,���`a ���`jangle_step���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`jsubplot_kw���aoa=���`a{���bs1a'���bs1faspect���bs1a'���`a:���`a ���bs1a'���bs1eequal���bs1a'���`a}���`a)���`a
���`a
���akcfor���`a ���`eangle���`a ���bowbin���`a ���`fangles���`a:���`a
���`d    ���`gellipse���`a ���aoa=���`a ���`gEllipse���`a(���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���bmia4���`a,���`a ���bmia2���`a,���`a ���`eangle���aoa=���`eangle���`a,���`a ���`ealpha���aoa=���bmfc0.1���`a)���`a
���`d    ���`bax���aoa.���`jadd_artist���`a(���`gellipse���`a)���`a
���`a
���`bax���aoa.���`hset_xlim���`a(���aoa-���bmfc2.2���`a,���`a ���bmfc2.2���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���aoa-���bmfc2.2���`a,���`a ���bmfc2.2���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.patches`���`a
���bc1x##    - `matplotlib.patches.Ellipse`���`a
���bc1x(#    - `matplotlib.axes.Axes.add_artist`���`a
���bc1x.#    - `matplotlib.artist.Artist.set_clip_box`���`a
���bc1x+#    - `matplotlib.artist.Artist.set_alpha`���`a
���bc1x/#    - `matplotlib.patches.Patch.set_facecolor`���`a
`dNone�