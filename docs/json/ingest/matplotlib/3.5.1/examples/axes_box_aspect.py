��������R���bsdy """
===============
Axes box aspect
===============

This demo shows how to set the aspect of an axes box directly via
`~.Axes.set_box_aspect`. The box aspect is the ratio between axes height
and axes width in physical units, independent of the data limits.
This is useful to e.g. produce a square plot, independent of the data it
contains, or to have a usual plot with the same axes dimensions next to
an image plot with fixed (data-)aspect.

The following lists a few use cases for `~.Axes.set_box_aspect`.
"""���`a
���`a
���bc1xL############################################################################���`a
���bc1x$# A square axes, independent of data���`a
���bc1x$# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~���`a
���bc1a#���`a
���bc1x<# Produce a square axes, no matter what the data limits are.���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`dfig1���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`bax���aoa.���`hset_xlim���`a(���bmic300���`a,���`a ���bmic400���`a)���`a
���`bax���aoa.���`nset_box_aspect���`a(���bmia1���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xL############################################################################���`a
���bc1t# Shared square axes���`a
���bc1t# ~~~~~~~~~~~~~~~~~~���`a
���bc1a#���`a
���bc1x3# Produce shared subplots that are squared in size.���`a
���bc1a#���`a
���`dfig2���`a,���`a ���`a(���`bax���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia2���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`a
���`bax���aoa.���`dplot���`a(���`a[���bmia1���`a,���`a ���bmia5���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmib10���`a]���`a)���`a
���`cax2���aoa.���`dplot���`a(���`a[���bmic100���`a,���`a ���bmic500���`a]���`a,���`a ���`a[���bmib10���`a,���`a ���bmib15���`a]���`a)���`a
���`a
���`bax���aoa.���`nset_box_aspect���`a(���bmia1���`a)���`a
���`cax2���aoa.���`nset_box_aspect���`a(���bmia1���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xL############################################################################���`a
���bc1r# Square twin axes���`a
���bc1r# ~~~~~~~~~~~~~~~~���`a
���bc1a#���`a
���bc1xJ# Produce a square axes, with a twin axes. The twinned axes takes over the���`a
���bc1x# box aspect of the parent.���`a
���bc1a#���`a
���`a
���`dfig3���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`cax2���`a ���aoa=���`a ���`bax���aoa.���`etwinx���`a(���`a)���`a
���`a
���`bax���aoa.���`dplot���`a(���`a[���bmia0���`a,���`a ���bmib10���`a]���`a)���`a
���`cax2���aoa.���`dplot���`a(���`a[���bmib12���`a,���`a ���bmib10���`a]���`a)���`a
���`a
���`bax���aoa.���`nset_box_aspect���`a(���bmia1���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xL############################################################################���`a
���bc1x# Normal plot next to image���`a
���bc1x# ~~~~~~~~~~~~~~~~~~~~~~~~~���`a
���bc1a#���`a
���bc1xD# When creating an image plot with fixed data aspect and the default���`a
���bc1xJ# ``adjustable="box"`` next to a normal plot, the axes would be unequal in���`a
���bc1xO# height. `~.Axes.set_box_aspect` provides an easy solution to that by allowing���`a
���bc1xI# to have the normal plot's axes use the images dimensions as box aspect.���`a
���bc1a#���`a
���bc1xL# This example also shows that ``constrained_layout`` interplays nicely with���`a
���bc1u# a fixed box aspect.���`a
���`a
���`dfig4���`a,���`a ���`a(���`bax���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia2���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`b  ���bc1x)# Fixing random state for reproducibility���`a
���`bim���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib16���`a,���`a ���bmib27���`a)���`a
���`bax���aoa.���`fimshow���`a(���`bim���`a)���`a
���`a
���`cax2���aoa.���`dplot���`a(���`a[���bmib23���`a,���`a ���bmib45���`a]���`a)���`a
���`cax2���aoa.���`nset_box_aspect���`a(���`bim���aoa.���`eshape���`a[���bmia0���`a]���aoa/���`bim���aoa.���`eshape���`a[���bmia1���`a]���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xL############################################################################���`a
���bc1x# Square joint/marginal plot���`a
���bc1x# ~~~~~~~~~~~~~~~~~~~~~~~~~~���`a
���bc1a#���`a
���bc1xL# It may be desirable to show marginal distributions next to a plot of joint���`a
���bc1xF# data. The following creates a square plot with the box aspect of the���`a
���bc1xL# marginal axes being equal to the width- and height-ratios of the gridspec.���`a
���bc1xL# This ensures that all axes align perfectly, independent on the size of the���`a
���bc1i# figure.���`a
���`a
���`dfig5���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`fsharex���aoa=���bs2a"���bs2ccol���bs2a"���`a,���`a ���`fsharey���aoa=���bs2a"���bs2crow���bs2a"���`a,���`a
���`x                         ���`kgridspec_kw���aoa=���bnbddict���`a(���`mheight_ratios���aoa=���`a[���bmia1���`a,���`a ���bmia3���`a]���`a,���`a
���`x*                                          ���`lwidth_ratios���aoa=���`a[���bmia3���`a,���`a ���bmia1���`a]���`a)���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`nset_box_aspect���`a(���bmia1���aoa/���bmia3���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`nset_box_aspect���`a(���bmia1���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`nset_box_aspect���`a(���bmia3���aoa/���bmia1���`a)���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`b  ���bc1x)# Fixing random state for reproducibility���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmia2���`a,���`a ���bmic400���`a)���`a ���aoa*���`a ���`a[���`a[���bmfb.5���`a]���`a,���`a ���`a[���bmic180���`a]���`a]���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`dhist���`a(���`ax���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`dhist���`a(���`ay���`a,���`a ���`korientation���aoa=���bs2a"���bs2jhorizontal���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xL############################################################################���`a
���bc1x# Square joint/marginal plot���`a
���bc1x# ~~~~~~~~~~~~~~~~~~~~~~~~~~���`a
���bc1a#���`a
���bc1xI# When setting the box aspect, one may still set the data aspect as well.���`a
���bc1xL# Here we create an axes with a box twice as long as tall and use an "equal"���`a
���bc1xH# data aspect for its contents, i.e. the circle actually stays circular.���`a
���`a
���`dfig6���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`bax���aoa.���`iadd_patch���`a(���`cplt���aoa.���`fCircle���`a(���`a(���bmia5���`a,���`a ���bmia3���`a)���`a,���`a ���bmia1���`a)���`a)���`a
���`bax���aoa.���`jset_aspect���`a(���bs2a"���bs2eequal���bs2a"���`a,���`a ���`jadjustable���aoa=���bs2a"���bs2gdatalim���bs2a"���`a)���`a
���`bax���aoa.���`nset_box_aspect���`a(���bmfc0.5���`a)���`a
���`bax���aoa.���`iautoscale���`a(���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xL############################################################################���`a
���bc1x# Box aspect for many subplots���`a
���bc1x# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~���`a
���bc1a#���`a
���bc1xI# It is possible to pass the box aspect to an axes at initialization. The���`a
���bc1x?# following creates a 2 by 3 subplot grid with all square axes.���`a
���`a
���`dfig7���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia3���`a,���`a ���`jsubplot_kw���aoa=���bnbddict���`a(���`jbox_aspect���aoa=���bmia1���`a)���`a,���`a
���`x                         ���`fsharex���aoa=���bkcdTrue���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`a
���akcfor���`a ���`ai���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`caxs���aoa.���`dflat���`a)���`a:���`a
���`d    ���`bax���aoa.���`gscatter���`a(���`ai���`a ���aoa%���`a ���bmia3���`a,���`a ���aoa-���`a(���`a(���`ai���`a ���aoa/���aoa/���`a ���bmia3���`a)���`a ���aoa-���`a ���bmfc0.5���`a)���aoa*���bmic200���`a,���`a ���`ac���aoa=���`a[���`cplt���aoa.���`bcm���aoa.���`chsv���`a(���`ai���`a ���aoa/���`a ���bmia6���`a)���`a]���`a,���`a ���`as���aoa=���bmic300���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x,#    - `matplotlib.axes.Axes.set_box_aspect`���`a
`dNone�