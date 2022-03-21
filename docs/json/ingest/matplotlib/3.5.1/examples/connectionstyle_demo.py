��������N���bsdy9"""
=================================
Connection styles for annotations
=================================

When creating an annotation using `~.Axes.annotate`, the arrow shape can be
controlled via the *connectionstyle* parameter of *arrowprops*. For further
details see the description of `.FancyArrowPatch`.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfndemo_con_style���`a(���`bax���`a,���`a ���`oconnectionstyle���`a)���`a:���`a
���`d    ���`bx1���`a,���`a ���`by1���`a ���aoa=���`a ���bmfc0.3���`a,���`a ���bmfc0.2���`a
���`d    ���`bx2���`a,���`a ���`by2���`a ���aoa=���`a ���bmfc0.8���`a,���`a ���bmfc0.6���`a
���`a
���`d    ���`bax���aoa.���`dplot���`a(���`a[���`bx1���`a,���`a ���`bx2���`a]���`a,���`a ���`a[���`by1���`a,���`a ���`by2���`a]���`a,���`a ���bs2a"���bs2a.���bs2a"���`a)���`a
���`d    ���`bax���aoa.���`hannotate���`a(���bs2a"���bs2a"���`a,���`a
���`p                ���`bxy���aoa=���`a(���`bx1���`a,���`a ���`by1���`a)���`a,���`a ���`hxycoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`p                ���`fxytext���aoa=���`a(���`bx2���`a,���`a ���`by2���`a)���`a,���`a ���`jtextcoords���aoa=���bs1a'���bs1ddata���bs1a'���`a,���`a
���`p                ���`jarrowprops���aoa=���bnbddict���`a(���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a ���`ecolor���aoa=���bs2a"���bs2c0.5���bs2a"���`a,���`a
���`x                                 ���`gshrinkA���aoa=���bmia5���`a,���`a ���`gshrinkB���aoa=���bmia5���`a,���`a
���`x                                 ���`fpatchA���aoa=���bkcdNone���`a,���`a ���`fpatchB���aoa=���bkcdNone���`a,���`a
���`x                                 ���`oconnectionstyle���aoa=���`oconnectionstyle���`a,���`a
���`x                                 ���`a)���`a,���`a
���`p                ���`a)���`a
���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfc.05���`a,���`a ���bmfc.95���`a,���`a ���`oconnectionstyle���aoa.���`greplace���`a(���bs2a"���bs2a,���bs2a"���`a,���`a ���bs2a"���bs2a,���bseb\n���bs2a"���`a)���`a,���`a
���`l            ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a ���`bha���aoa=���bs2a"���bs2dleft���bs2a"���`a,���`a ���`bva���aoa=���bs2a"���bs2ctop���bs2a"���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia5���`a,���`a ���`gfigsize���aoa=���`a(���bmia7���`a,���`a ���bmfc6.3���`a)���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���bs2a"���bs2xangle3,angleA=90,angleB=0���bs2a"���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���`a,���`a ���bs2a"���bs2xangle3,angleA=0,angleB=90���bs2a"���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���`a,���`a ���bs2a"���bs2karc3,rad=0.���bs2a"���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���bs2a"���bs2larc3,rad=0.3���bs2a"���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia2���`a,���`a ���bmia1���`a]���`a,���`a ���bs2a"���bs2marc3,rad=-0.3���bs2a"���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia0���`a,���`a ���bmia2���`a]���`a,���`a ���bs2a"���bs2x!angle,angleA=-90,angleB=180,rad=0���bs2a"���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���bs2a"���bs2x!angle,angleA=-90,angleB=180,rad=5���bs2a"���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia2���`a,���`a ���bmia2���`a]���`a,���`a ���bs2a"���bs2x angle,angleA=-90,angleB=10,rad=5���bs2a"���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia0���`a,���`a ���bmia3���`a]���`a,���`a ���bs2a"���bs2x-arc,angleA=-90,angleB=0,armA=30,armB=30,rad=0���bs2a"���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia1���`a,���`a ���bmia3���`a]���`a,���`a ���bs2a"���bs2x-arc,angleA=-90,angleB=0,armA=30,armB=30,rad=5���bs2a"���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia2���`a,���`a ���bmia3���`a]���`a,���`a ���bs2a"���bs2x,arc,angleA=-90,angleB=0,armA=0,armB=40,rad=0���bs2a"���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia0���`a,���`a ���bmia4���`a]���`a,���`a ���bs2a"���bs2pbar,fraction=0.3���bs2a"���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia1���`a,���`a ���bmia4���`a]���`a,���`a ���bs2a"���bs2qbar,fraction=-0.3���bs2a"���`a)���`a
���`ndemo_con_style���`a(���`caxs���`a[���bmia2���`a,���`a ���bmia4���`a]���`a,���`a ���bs2a"���bs2xbar,angle=180,fraction=-0.2���bs2a"���`a)���`a
���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`d    ���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia0���`a,���`a ���bmfd1.25���`a)���`a,���`a ���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a,���`a ���`faspect���aoa=���bmfd1.25���`a)���`a
���`cfig���aoa.���`xset_constrained_layout_pads���`a(���`fwspace���aoa=���bmia0���`a,���`a ���`fhspace���aoa=���bmia0���`a,���`a ���`ew_pad���aoa=���bmia0���`a,���`a ���`eh_pad���aoa=���bmia0���`a)���`a
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
���bc1x&#    - `matplotlib.axes.Axes.annotate`���`a
���bc1x+#    - `matplotlib.patches.FancyArrowPatch`���`a
`dNone�