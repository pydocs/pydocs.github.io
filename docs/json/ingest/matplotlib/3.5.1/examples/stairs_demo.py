��������P���bsdx�"""
===========
Stairs Demo
===========

This example demonstrates the use of `~.matplotlib.pyplot.stairs` for stepwise
constant functions. A common use case is histogram and histogram-like data
visualization.

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`iStepPatch���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmia0���`a)���`a
���`ah���`a,���`a ���`eedges���`a ���aoa=���`a ���`bnp���aoa.���`ihistogram���`a(���`bnp���aoa.���`frandom���aoa.���`fnormal���`a(���bmia5���`a,���`a ���bmia3���`a,���`a ���bmid5000���`a)���`a,���`a
���`x                        ���`dbins���aoa=���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmib10���`a,���`a ���bmib20���`a)���`a)���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`gfigsize���aoa=���`a(���bmia7���`a,���`a ���bmib15���`a)���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`fstairs���`a(���`ah���`a,���`a ���`eedges���`a,���`a ���`elabel���aoa=���bs1a'���bs1pSimple histogram���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`fstairs���`a(���`ah���`a,���`a ���`eedges���`a ���aoa+���`a ���bmia5���`a,���`a ���`hbaseline���aoa=���bmib50���`a,���`a ���`elabel���aoa=���bs1a'���bs1qModified baseline���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`fstairs���`a(���`ah���`a,���`a ���`eedges���`a ���aoa+���`a ���bmib10���`a,���`a ���`hbaseline���aoa=���bkcdNone���`a,���`a ���`elabel���aoa=���bs1a'���bs1hNo edges���bs1a'���`a)���`a
���`caxs���`a[���bmia0���`a]���aoa.���`iset_title���`a(���bs2a"���bs2oStep Histograms���bs2a"���`a)���`a
���`a
���`caxs���`a[���bmia1���`a]���aoa.���`fstairs���`a(���`bnp���aoa.���`farange���`a(���bmia1���`a,���`a ���bmia6���`a,���`a ���bmia1���`a)���`a,���`a ���`dfill���aoa=���bkcdTrue���`a,���`a
���`n              ���`elabel���aoa=���bs1a'���bs1pFilled histogram���bseb\n���bs1rw/ automatic edges���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`fstairs���`a(���`bnp���aoa.���`farange���`a(���bmia1���`a,���`a ���bmia6���`a,���`a ���bmia1���`a)���aoa*���bmfc0.3���`a,���`a ���`bnp���aoa.���`farange���`a(���bmia2���`a,���`a ���bmia8���`a,���`a ���bmia1���`a)���`a,���`a
���`n              ���`korientation���aoa=���bs1a'���bs1jhorizontal���bs1a'���`a,���`a ���`ehatch���aoa=���bs1a'���bs1b//���bs1a'���`a,���`a
���`n              ���`elabel���aoa=���bs1a'���bs1qHatched histogram���bseb\n���bs1xw/ horizontal orientation���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a]���aoa.���`iset_title���`a(���bs2a"���bs2pFilled histogram���bs2a"���`a)���`a
���`a
���`epatch���`a ���aoa=���`a ���`iStepPatch���`a(���`fvalues���aoa=���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a,���`a ���bmia2���`a,���`a ���bmia1���`a]���`a,���`a
���`r                  ���`eedges���aoa=���bnberange���`a(���bmia1���`a,���`a ���bmia7���`a)���`a,���`a
���`r                  ���`elabel���aoa=���`a(���bs1a'���bs1xPatch derived underlying object���bseb\n���bs1a'���`a
���`x                         ���bs1a'���bs1x%with default edge/facecolor behaviour���bs1a'���`a)���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`iadd_patch���`a(���`epatch���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia7���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`hset_ylim���`a(���aoa-���bmia1���`a,���`a ���bmia5���`a)���`a
���`caxs���`a[���bmia2���`a]���aoa.���`iset_title���`a(���bs2a"���bs2pStepPatch artist���bs2a"���`a)���`a
���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���`a:���`a
���`d    ���`bax���aoa.���`flegend���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1xC# *baseline* can take an array to allow for stacked histogram plots���`a
���`aA���`a ���aoa=���`a ���`a[���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a]���`a,���`a
���`e     ���`a[���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a]���`a,���`a
���`e     ���`a[���bmia2���`a,���`a ���bmia4���`a,���`a ���bmia6���`a]���`a,���`a
���`e     ���`a[���bmia3���`a,���`a ���bmia6���`a,���`a ���bmia9���`a]���`a]���`a
���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`aA���`a)���`a ���aoa-���`a ���bmia1���`a)���`a:���`a
���`d    ���`cplt���aoa.���`fstairs���`a(���`aA���`a[���`ai���aoa+���bmia1���`a]���`a,���`a ���`hbaseline���aoa=���`aA���`a[���`ai���`a]���`a,���`a ���`dfill���aoa=���bkcdTrue���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1x3# Comparison of `.pyplot.step` and `.pyplot.stairs`���`a
���bc1x3# -------------------------------------------------���`a
���bc1a#���`a
���bc1xO# `.pyplot.step` defines the positions of the steps as single values. The steps���`a
���bc1xJ# extend left/right/both ways from these reference values depending on the���`a
���bc1xB# parameter *where*. The number of *x* and *y* values is the same.���`a
���bc1a#���`a
���bc1xL# In contrast, `.pyplot.stairs` defines the positions of the steps via their���`a
���bc1xC# bounds *edges*, which is one element longer than the step values.���`a
���`a
���`dbins���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmib14���`a)���`a
���`gcenters���`a ���aoa=���`a ���`dbins���`a[���`a:���aoa-���bmia1���`a]���`a ���aoa+���`a ���`bnp���aoa.���`ddiff���`a(���`dbins���`a)���`a ���aoa/���`a ���bmia2���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���`gcenters���`a ���aoa/���`a ���bmia2���`a)���`a
���`a
���`cplt���aoa.���`dstep���`a(���`dbins���`a[���`a:���aoa-���bmia1���`a]���`a,���`a ���`ay���`a,���`a ���`ewhere���aoa=���bs1a'���bs1dpost���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1kstep(where=���bs1a"���bs1dpost���bs1a"���bs1a)���bs1a'���`a)���`a
���`cplt���aoa.���`dplot���`a(���`dbins���`a[���`a:���aoa-���bmia1���`a]���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1co--���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`a
���`cplt���aoa.���`fstairs���`a(���`ay���`a ���aoa-���`a ���bmia1���`a,���`a ���`dbins���`a,���`a ���`hbaseline���aoa=���bkcdNone���`a,���`a ���`elabel���aoa=���bs1a'���bs1hstairs()���bs1a'���`a)���`a
���`cplt���aoa.���`dplot���`a(���`gcenters���`a,���`a ���`ay���`a ���aoa-���`a ���bmia1���`a,���`a ���bs1a'���bs1co--���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1dgrey���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a
���`cplt���aoa.���`dplot���`a(���`bnp���aoa.���`frepeat���`a(���`dbins���`a,���`a ���bmia2���`a)���`a,���`a ���`bnp���aoa.���`fhstack���`a(���`a[���`ay���`a[���bmia0���`a]���`a,���`a ���`bnp���aoa.���`frepeat���`a(���`ay���`a,���`a ���bmia2���`a)���`a,���`a ���`ay���`a[���aoa-���bmia1���`a]���`a]���`a)���`a ���aoa-���`a ���bmia1���`a,���`a
���`i         ���bs1a'���bs1ao���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1cred���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.2���`a)���`a
���`a
���`cplt���aoa.���`flegend���`a(���`a)���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1sstep() vs. stairs()���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xA#    - `matplotlib.axes.Axes.stairs` / `matplotlib.pyplot.stairs`���`a
���bc1x%#    - `matplotlib.patches.StepPatch`���`a
`dNone�