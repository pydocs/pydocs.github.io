������������bsdxy"""
=====================
Simple Axes Divider 3
=====================

See also :doc:`/tutorials/toolkits/axes_grid`.
"""���`a
���`a
���bknfimport���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���bnna.���bnniaxes_size���`a ���akbas���`a ���bnndSize���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���`a ���bknfimport���`a ���`gDivider���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmfc5.5���`a,���`a ���bmia4���`a)���`a)���`a
���`a
���bc1x?# the rect parameter will be ignore as we will set axes_locator���`a
���`drect���`a ���aoa=���`a ���`a(���bmfc0.1���`a,���`a ���bmfc0.1���`a,���`a ���bmfc0.8���`a,���`a ���bmfc0.8���`a)���`a
���`bax���`a ���aoa=���`a ���`a[���`cfig���aoa.���`hadd_axes���`a(���`drect���`a,���`a ���`elabel���aoa=���bs2a"���bsib%d���bs2a"���`a ���aoa%���`a ���`ai���`a)���`a ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmia4���`a)���`a]���`a
���`a
���`a
���`ehoriz���`a ���aoa=���`a ���`a[���`dSize���aoa.���`eAxesX���`a(���`bax���`a[���bmia0���`a]���`a)���`a,���`a ���`dSize���aoa.���`eFixed���`a(���bmfb.5���`a)���`a,���`a ���`dSize���aoa.���`eAxesX���`a(���`bax���`a[���bmia1���`a]���`a)���`a]���`a
���`dvert���`a ���aoa=���`a ���`a[���`dSize���aoa.���`eAxesY���`a(���`bax���`a[���bmia0���`a]���`a)���`a,���`a ���`dSize���aoa.���`eFixed���`a(���bmfb.5���`a)���`a,���`a ���`dSize���aoa.���`eAxesY���`a(���`bax���`a[���bmia2���`a]���`a)���`a]���`a
���`a
���bc1xM# divide the axes rectangle into grid whose size is specified by horiz * vert���`a
���`gdivider���`a ���aoa=���`a ���`gDivider���`a(���`cfig���`a,���`a ���`drect���`a,���`a ���`ehoriz���`a,���`a ���`dvert���`a,���`a ���`faspect���aoa=���bkceFalse���`a)���`a
���`a
���`a
���`bax���`a[���bmia0���`a]���aoa.���`pset_axes_locator���`a(���`gdivider���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia0���`a,���`a ���`bny���aoa=���bmia0���`a)���`a)���`a
���`bax���`a[���bmia1���`a]���aoa.���`pset_axes_locator���`a(���`gdivider���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia2���`a,���`a ���`bny���aoa=���bmia0���`a)���`a)���`a
���`bax���`a[���bmia2���`a]���aoa.���`pset_axes_locator���`a(���`gdivider���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia0���`a,���`a ���`bny���aoa=���bmia2���`a)���`a)���`a
���`bax���`a[���bmia3���`a]���aoa.���`pset_axes_locator���`a(���`gdivider���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia2���`a,���`a ���`bny���aoa=���bmia2���`a)���`a)���`a
���`a
���`bax���`a[���bmia0���`a]���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia2���`a)���`a
���`bax���`a[���bmia1���`a]���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`a
���`bax���`a[���bmia0���`a]���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`bax���`a[���bmia2���`a]���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia2���`a)���`a
���`a
���`gdivider���aoa.���`jset_aspect���`a(���bmfb1.���`a)���`a
���`a
���akcfor���`a ���`cax1���`a ���bowbin���`a ���`bax���`a:���`a
���`d    ���`cax1���aoa.���`ktick_params���`a(���`klabelbottom���aoa=���bkceFalse���`a,���`a ���`ilabelleft���aoa=���bkceFalse���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�