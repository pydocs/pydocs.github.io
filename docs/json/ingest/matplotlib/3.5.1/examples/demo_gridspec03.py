������������bsdy\"""
=============
GridSpec demo
=============

This example demonstrates the use of `.GridSpec` to generate subplots,
the control of the relative sizes of subplots with *width_ratios* and
*height_ratios*, and the control of the spacing around and between subplots
using subplot params (*left*, *right*, *bottom*, *top*, *wspace*, and
*hspace*).
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnhgridspec���`a ���bknfimport���`a ���`hGridSpec���`a
���`a
���`a
���akcdef���`a ���bnfmannotate_axes���`a(���`cfig���`a)���`a:���`a
���`d    ���akcfor���`a ���`ai���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`cfig���aoa.���`daxes���`a)���`a:���`a
���`h        ���`bax���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs2a"���bs2bax���bsib%d���bs2a"���`a ���aoa%���`a ���`a(���`ai���aoa+���bmia1���`a)���`a,���`a ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`h        ���`bax���aoa.���`ktick_params���`a(���`klabelbottom���aoa=���bkceFalse���`a,���`a ���`ilabelleft���aoa=���bkceFalse���`a)���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs2a"���bs2x=Controlling subplot sizes with width_ratios and height_ratios���bs2a"���`a)���`a
���`a
���`bgs���`a ���aoa=���`a ���`hGridSpec���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`lwidth_ratios���aoa=���`a[���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`mheight_ratios���aoa=���`a[���bmia4���`a,���`a ���bmia1���`a]���`a)���`a
���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia0���`a]���`a)���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia1���`a]���`a)���`a
���`cax3���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia2���`a]���`a)���`a
���`cax4���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia3���`a]���`a)���`a
���`a
���`mannotate_axes���`a(���`cfig���`a)���`a
���`a
���bc1xM#############################################################################���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs2a"���bs2x/Controlling spacing around and between subplots���bs2a"���`a)���`a
���`a
���`cgs1���`a ���aoa=���`a ���`hGridSpec���`a(���bmia3���`a,���`a ���bmia3���`a,���`a ���`dleft���aoa=���bmfd0.05���`a,���`a ���`eright���aoa=���bmfd0.48���`a,���`a ���`fwspace���aoa=���bmfd0.05���`a)���`a
���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`cgs1���`a[���`a:���aoa-���bmia1���`a,���`a ���`a:���`a]���`a)���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`cgs1���`a[���aoa-���bmia1���`a,���`a ���`a:���aoa-���bmia1���`a]���`a)���`a
���`cax3���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`cgs1���`a[���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a)���`a
���`a
���`cgs2���`a ���aoa=���`a ���`hGridSpec���`a(���bmia3���`a,���`a ���bmia3���`a,���`a ���`dleft���aoa=���bmfd0.55���`a,���`a ���`eright���aoa=���bmfd0.98���`a,���`a ���`fhspace���aoa=���bmfd0.05���`a)���`a
���`cax4���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`cgs2���`a[���`a:���`a,���`a ���`a:���aoa-���bmia1���`a]���`a)���`a
���`cax5���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`cgs2���`a[���`a:���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a)���`a
���`cax6���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`cgs2���`a[���aoa-���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a)���`a
���`a
���`mannotate_axes���`a(���`cfig���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�