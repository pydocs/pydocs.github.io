������������bsdy�"""
==============================================
Contouring the solution space of optimizations
==============================================

Contour plotting is particularly handy when illustrating the solution
space of optimization problems.  Not only can `.axes.Axes.contour` be
used to represent the topography of the objective function, it can be
used to generate boundary curves of the constraint functions.  The
constraint lines can be drawn with
`~matplotlib.patheffects.TickedStroke` to distinguish the valid and
invalid sides of the constraint boundaries.

`.axes.Axes.contour` generates curves with larger values to the left
of the contour.  The angle parameter is measured zero ahead with
increasing values to the left.  Consequently, when using
`~matplotlib.patheffects.TickedStroke` to illustrate a constraint in
a typical optimization problem, the angle should be set between
zero and 180 degrees.

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`kpatheffects���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`a
���`bnx���`a ���aoa=���`a ���bmic101���`a
���`bny���`a ���aoa=���`a ���bmic105���`a
���`a
���bc1w# Set up survey vectors���`a
���`dxvec���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfe0.001���`a,���`a ���bmfc4.0���`a,���`a ���`bnx���`a)���`a
���`dyvec���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfe0.001���`a,���`a ���bmfc4.0���`a,���`a ���`bny���`a)���`a
���`a
���bc1x># Set up survey matrices.  Design disk loading and gear ratio.���`a
���`bx1���`a,���`a ���`bx2���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`dxvec���`a,���`a ���`dyvec���`a)���`a
���`a
���bc1x# Evaluate some stuff to plot���`a
���`cobj���`a ���aoa=���`a ���`bx1���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`bx2���aoa*���aoa*���bmia2���`a ���aoa-���`a ���bmia2���aoa*���`bx1���`a ���aoa-���`a ���bmia2���aoa*���`bx2���`a ���aoa+���`a ���bmia2���`a
���`bg1���`a ���aoa=���`a ���aoa-���`a(���bmia3���aoa*���`bx1���`a ���aoa+���`a ���`bx2���`a ���aoa-���`a ���bmfc5.5���`a)���`a
���`bg2���`a ���aoa=���`a ���aoa-���`a(���`bx1���`a ���aoa+���`a ���bmia2���aoa*���`bx2���`a ���aoa-���`a ���bmfc4.5���`a)���`a
���`bg3���`a ���aoa=���`a ���bmfc0.8���`a ���aoa+���`a ���`bx1���aoa*���aoa*���aoa-���bmia3���`a ���aoa-���`a ���`bx2���`a
���`a
���`dcntr���`a ���aoa=���`a ���`bax���aoa.���`gcontour���`a(���`bx1���`a,���`a ���`bx2���`a,���`a ���`cobj���`a,���`a ���`a[���bmfd0.01���`a,���`a ���bmfc0.1���`a,���`a ���bmfc0.5���`a,���`a ���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia4���`a,���`a ���bmia8���`a,���`a ���bmib16���`a]���`a,���`a
���`r                  ���`fcolors���aoa=���bs1a'���bs1eblack���bs1a'���`a)���`a
���`bax���aoa.���`fclabel���`a(���`dcntr���`a,���`a ���`cfmt���aoa=���bs2a"���bsie%2.1f���bs2a"���`a,���`a ���`nuse_clabeltext���aoa=���bkcdTrue���`a)���`a
���`a
���`ccg1���`a ���aoa=���`a ���`bax���aoa.���`gcontour���`a(���`bx1���`a,���`a ���`bx2���`a,���`a ���`bg1���`a,���`a ���`a[���bmia0���`a]���`a,���`a ���`fcolors���aoa=���bs1a'���bs1jsandybrown���bs1a'���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`ccg1���aoa.���`kcollections���`a,���`a
���`i         ���`lpath_effects���aoa=���`a[���`kpatheffects���aoa.���`pwithTickedStroke���`a(���`eangle���aoa=���bmic135���`a)���`a]���`a)���`a
���`a
���`ccg2���`a ���aoa=���`a ���`bax���aoa.���`gcontour���`a(���`bx1���`a,���`a ���`bx2���`a,���`a ���`bg2���`a,���`a ���`a[���bmia0���`a]���`a,���`a ���`fcolors���aoa=���bs1a'���bs1iorangered���bs1a'���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`ccg2���aoa.���`kcollections���`a,���`a
���`i         ���`lpath_effects���aoa=���`a[���`kpatheffects���aoa.���`pwithTickedStroke���`a(���`eangle���aoa=���bmib60���`a,���`a ���`flength���aoa=���bmia2���`a)���`a]���`a)���`a
���`a
���`ccg3���`a ���aoa=���`a ���`bax���aoa.���`gcontour���`a(���`bx1���`a,���`a ���`bx2���`a,���`a ���`bg3���`a,���`a ���`a[���bmia0���`a]���`a,���`a ���`fcolors���aoa=���bs1a'���bs1jmediumblue���bs1a'���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`ccg3���aoa.���`kcollections���`a,���`a
���`i         ���`lpath_effects���aoa=���`a[���`kpatheffects���aoa.���`pwithTickedStroke���`a(���`gspacing���aoa=���bmia7���`a)���`a]���`a)���`a
���`a
���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia4���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia4���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�