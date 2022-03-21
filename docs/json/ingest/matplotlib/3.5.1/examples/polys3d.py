��������F���bsdy?"""
=============================================
Generate polygons to fill under 3D line graph
=============================================

Demonstrate how to create polygons which fill the space under a line
graph. In this example polygons are semi-transparent, creating a sort
of 'jagged stained glass' effect.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkcollections���`a ���bknfimport���`a ���`nPolyCollection���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���escipy���escipye1.8.0fmoduleescipyfmodule����bnna.���bnnestats���`a ���bknfimport���`a ���`gpoisson���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���akcdef���`a ���bnfspolygon_under_graph���`a(���`ax���`a,���`a ���`ay���`a)���`a:���`a
���`d    ���bsdx�"""
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph. This assumes x is in ascending order.
    """���`a
���`d    ���akfreturn���`a ���`a[���`a(���`ax���`a[���bmia0���`a]���`a,���`a ���bmfb0.���`a)���`a,���`a ���aoa*���bnbczip���`a(���`ax���`a,���`a ���`ay���`a)���`a,���`a ���`a(���`ax���`a[���aoa-���bmia1���`a]���`a,���`a ���bmfb0.���`a)���`a]���`a
���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfb0.���`a,���`a ���bmfc10.���`a,���`a ���bmib31���`a)���`a
���`glambdas���`a ���aoa=���`a ���bnberange���`a(���bmia1���`a,���`a ���bmia9���`a)���`a
���`a
���bc1x8# verts[i] is a list of (x, y) pairs defining polygon i.���`a
���`everts���`a ���aoa=���`a ���`a[���`spolygon_under_graph���`a(���`ax���`a,���`a ���`gpoisson���aoa.���`cpmf���`a(���`al���`a,���`a ���`ax���`a)���`a)���`a ���akcfor���`a ���`al���`a ���bowbin���`a ���`glambdas���`a]���`a
���`jfacecolors���`a ���aoa=���`a ���`cplt���aoa.���`icolormaps���`a[���bs1a'���bs1iviridis_r���bs1a'���`a]���`a(���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bnbclen���`a(���`everts���`a)���`a)���`a)���`a
���`a
���`dpoly���`a ���aoa=���`a ���`nPolyCollection���`a(���`everts���`a,���`a ���`jfacecolors���aoa=���`jfacecolors���`a,���`a ���`ealpha���aoa=���bmfb.7���`a)���`a
���`bax���aoa.���`padd_collection3d���`a(���`dpoly���`a,���`a ���`bzs���aoa=���`glambdas���`a,���`a ���`dzdir���aoa=���bs1a'���bs1ay���bs1a'���`a)���`a
���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmib10���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia1���`a,���`a ���bmia9���`a)���`a,���`a ���`dzlim���aoa=���`a(���bmia0���`a,���`a ���bmfd0.35���`a)���`a,���`a
���`g       ���`fxlabel���aoa=���bs1a'���bs1ax���bs1a'���`a,���`a ���`fylabel���aoa=���bsaar���bs1a'���bs1a$���bs1a\���bs1glambda$���bs1a'���`a,���`a ���`fzlabel���aoa=���bs1a'���bs1kprobability���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�