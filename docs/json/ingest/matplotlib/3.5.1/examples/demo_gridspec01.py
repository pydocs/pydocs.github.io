������������bsdx�"""
=================
subplot2grid demo
=================

This example demonstrates the use of `.pyplot.subplot2grid` to generate
subplots.  Using `.GridSpec`, as demonstrated in
:doc:`/gallery/userdemo/demo_gridspec03` is generally preferred.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfmannotate_axes���`a(���`cfig���`a)���`a:���`a
���`d    ���akcfor���`a ���`ai���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`cfig���aoa.���`daxes���`a)���`a:���`a
���`h        ���`bax���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs2a"���bs2bax���bsib%d���bs2a"���`a ���aoa%���`a ���`a(���`ai���aoa+���bmia1���`a)���`a,���`a ���`bva���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`bha���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`h        ���`bax���aoa.���`ktick_params���`a(���`klabelbottom���aoa=���bkceFalse���`a,���`a ���`ilabelleft���aoa=���bkceFalse���`a)���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`lsubplot2grid���`a(���`a(���bmia3���`a,���`a ���bmia3���`a)���`a,���`a ���`a(���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���`gcolspan���aoa=���bmia3���`a)���`a
���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`lsubplot2grid���`a(���`a(���bmia3���`a,���`a ���bmia3���`a)���`a,���`a ���`a(���bmia1���`a,���`a ���bmia0���`a)���`a,���`a ���`gcolspan���aoa=���bmia2���`a)���`a
���`cax3���`a ���aoa=���`a ���`cplt���aoa.���`lsubplot2grid���`a(���`a(���bmia3���`a,���`a ���bmia3���`a)���`a,���`a ���`a(���bmia1���`a,���`a ���bmia2���`a)���`a,���`a ���`growspan���aoa=���bmia2���`a)���`a
���`cax4���`a ���aoa=���`a ���`cplt���aoa.���`lsubplot2grid���`a(���`a(���bmia3���`a,���`a ���bmia3���`a)���`a,���`a ���`a(���bmia2���`a,���`a ���bmia0���`a)���`a)���`a
���`cax5���`a ���aoa=���`a ���`cplt���aoa.���`lsubplot2grid���`a(���`a(���bmia3���`a,���`a ���bmia3���`a)���`a,���`a ���`a(���bmia2���`a,���`a ���bmia1���`a)���`a)���`a
���`a
���`mannotate_axes���`a(���`cfig���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�