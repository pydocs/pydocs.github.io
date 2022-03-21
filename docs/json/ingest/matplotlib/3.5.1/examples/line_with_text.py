��������	���bsdx�"""
=======================
Artist within an artist
=======================

Override basic methods so an artist can contain another
artist.  In this case, the line contains a Text instance to label it.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnelines���`a ���akbas���`a ���bnnelines���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���akbas���`a ���bnnkmtransforms���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndtext���`a ���akbas���`a ���bnnemtext���`a
���`a
���`a
���akeclass���`a ���bncfMyLine���`a(���`elines���aoa.���`fLine2D���`a)���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`h        ���bc1x5# we'll update the position when the line data is set���`a
���`h        ���bbpdself���aoa.���`dtext���`a ���aoa=���`a ���`emtext���aoa.���`dText���`a(���bmia0���`a,���`a ���bmia0���`a,���`a ���bs1a'���bs1a'���`a)���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`a
���`h        ���bc1x:# we can't access the label attr until *after* the line is���`a
���`h        ���bc1k# initiated���`a
���`h        ���bbpdself���aoa.���`dtext���aoa.���`hset_text���`a(���bbpdself���aoa.���`iget_label���`a(���`a)���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfjset_figure���`a(���bbpdself���`a,���`a ���`ffigure���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`dtext���aoa.���`jset_figure���`a(���`ffigure���`a)���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���`jset_figure���`a(���`ffigure���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfhset_axes���`a(���bbpdself���`a,���`a ���`daxes���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`dtext���aoa.���`hset_axes���`a(���`daxes���`a)���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���`hset_axes���`a(���`daxes���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfmset_transform���`a(���bbpdself���`a,���`a ���`itransform���`a)���`a:���`a
���`h        ���bc1p# 2 pixel offset���`a
���`h        ���`itexttrans���`a ���aoa=���`a ���`itransform���`a ���aoa+���`a ���`kmtransforms���aoa.���`hAffine2D���`a(���`a)���aoa.���`itranslate���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`h        ���bbpdself���aoa.���`dtext���aoa.���`mset_transform���`a(���`itexttrans���`a)���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���`mset_transform���`a(���`itransform���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfhset_data���`a(���bbpdself���`a,���`a ���`ax���`a,���`a ���`ay���`a)���`a:���`a
���`h        ���akbif���`a ���bnbclen���`a(���`ax���`a)���`a:���`a
���`l            ���bbpdself���aoa.���`dtext���aoa.���`lset_position���`a(���`a(���`ax���`a[���aoa-���bmia1���`a]���`a,���`a ���`ay���`a[���aoa-���bmia1���`a]���`a)���`a)���`a
���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���`hset_data���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfddraw���`a(���bbpdself���`a,���`a ���`hrenderer���`a)���`a:���`a
���`h        ���bc1x:# draw my label at the end of the line with 2 pixel offset���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���`ddraw���`a(���`hrenderer���`a)���`a
���`h        ���bbpdself���aoa.���`dtext���aoa.���`ddraw���`a(���`hrenderer���`a)���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia2���`a,���`a ���bmib20���`a)���`a
���`dline���`a ���aoa=���`a ���`fMyLine���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`cmfc���aoa=���bs1a'���bs1cred���bs1a'���`a,���`a ���`bms���aoa=���bmib12���`a,���`a ���`elabel���aoa=���bs1a'���bs1jline label���bs1a'���`a)���`a
���`dline���aoa.���`dtext���aoa.���`iset_color���`a(���bs1a'���bs1cred���bs1a'���`a)���`a
���`dline���aoa.���`dtext���aoa.���`lset_fontsize���`a(���bmib16���`a)���`a
���`a
���`bax���aoa.���`hadd_line���`a(���`dline���`a)���`a
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
���bc1x#    - `matplotlib.lines`���`a
���bc1x #    - `matplotlib.lines.Line2D`���`a
���bc1x)#    - `matplotlib.lines.Line2D.set_data`���`a
���bc1x#    - `matplotlib.artist`���`a
���bc1x!#    - `matplotlib.artist.Artist`���`a
���bc1x&#    - `matplotlib.artist.Artist.draw`���`a
���bc1x/#    - `matplotlib.artist.Artist.set_transform`���`a
���bc1x#    - `matplotlib.text`���`a
���bc1x#    - `matplotlib.text.Text`���`a
���bc1x'#    - `matplotlib.text.Text.set_color`���`a
���bc1x*#    - `matplotlib.text.Text.set_fontsize`���`a
���bc1x*#    - `matplotlib.text.Text.set_position`���`a
���bc1x&#    - `matplotlib.axes.Axes.add_line`���`a
���bc1x#    - `matplotlib.transforms`���`a
���bc1x'#    - `matplotlib.transforms.Affine2D`���`a
`dNone�