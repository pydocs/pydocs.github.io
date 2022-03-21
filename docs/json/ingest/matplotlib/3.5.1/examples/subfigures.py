��������7���bsdy�"""
=================
Figure subfigures
=================

Sometimes it is desirable to have a figure with two different layouts in it.
This can be achieved with
:doc:`nested gridspecs</gallery/subplots_axes_and_figures/gridspec_nested>`,
but having a virtual figure with its own artists is helpful, so
Matplotlib also has "subfigures", accessed by calling
`matplotlib.figure.Figure.add_subfigure` in a way that is analogous to
`matplotlib.figure.Figure.add_subplot`, or
`matplotlib.figure.Figure.subfigures` to make an array of subfigures.  Note
that subfigures can also have their own child subfigures.

.. note::
    ``subfigure`` is new in v3.4, and the API is still provisional.

"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnflexample_plot���`a(���`bax���`a,���`a ���`hfontsize���aoa=���bmib12���`a,���`a ���`khide_labels���aoa=���bkceFalse���`a)���`a:���`a
���`d    ���`bpc���`a ���aoa=���`a ���`bax���aoa.���`jpcolormesh���`a(���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmib30���`a,���`a ���bmib30���`a)���`a,���`a ���`dvmin���aoa=���aoa-���bmfc2.5���`a,���`a ���`dvmax���aoa=���bmfc2.5���`a)���`a
���`d    ���akbif���`a ���bowcnot���`a ���`khide_labels���`a:���`a
���`h        ���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1gx-label���bs1a'���`a,���`a ���`hfontsize���aoa=���`hfontsize���`a)���`a
���`h        ���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1gy-label���bs1a'���`a,���`a ���`hfontsize���aoa=���`hfontsize���`a)���`a
���`h        ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1eTitle���bs1a'���`a,���`a ���`hfontsize���aoa=���`hfontsize���`a)���`a
���`d    ���akfreturn���`a ���`bpc���`a
���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680808���`a)���`a
���bc1x# gridspec inside gridspec���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmib10���`a,���`a ���bmia4���`a)���`a)���`a
���`gsubfigs���`a ���aoa=���`a ���`cfig���aoa.���`jsubfigures���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`fwspace���aoa=���bmfd0.07���`a)���`a
���`a
���`gaxsLeft���`a ���aoa=���`a ���`gsubfigs���`a[���bmia0���`a]���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`gsubfigs���`a[���bmia0���`a]���aoa.���`mset_facecolor���`a(���bs1a'���bs1d0.75���bs1a'���`a)���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`gaxsLeft���`a:���`a
���`d    ���`bpc���`a ���aoa=���`a ���`lexample_plot���`a(���`bax���`a)���`a
���`gsubfigs���`a[���bmia0���`a]���aoa.���`hsuptitle���`a(���bs1a'���bs1jLeft plots���bs1a'���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1gx-large���bs1a'���`a)���`a
���`gsubfigs���`a[���bmia0���`a]���aoa.���`hcolorbar���`a(���`bpc���`a,���`a ���`fshrink���aoa=���bmfc0.6���`a,���`a ���`bax���aoa=���`gaxsLeft���`a,���`a ���`hlocation���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���`haxsRight���`a ���aoa=���`a ���`gsubfigs���`a[���bmia1���`a]���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a)���`a
���akcfor���`a ���`bnn���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`haxsRight���`a)���`a:���`a
���`d    ���`bpc���`a ���aoa=���`a ���`lexample_plot���`a(���`bax���`a,���`a ���`khide_labels���aoa=���bkcdTrue���`a)���`a
���`d    ���akbif���`a ���`bnn���`a ���aob==���`a ���bmia2���`a:���`a
���`h        ���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1fxlabel���bs1a'���`a)���`a
���`d    ���akbif���`a ���`bnn���`a ���aob==���`a ���bmia1���`a:���`a
���`h        ���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1fylabel���bs1a'���`a)���`a
���`a
���`gsubfigs���`a[���bmia1���`a]���aoa.���`mset_facecolor���`a(���bs1a'���bs1d0.85���bs1a'���`a)���`a
���`gsubfigs���`a[���bmia1���`a]���aoa.���`hcolorbar���`a(���`bpc���`a,���`a ���`fshrink���aoa=���bmfc0.6���`a,���`a ���`bax���aoa=���`haxsRight���`a)���`a
���`gsubfigs���`a[���bmia1���`a]���aoa.���`hsuptitle���`a(���bs1a'���bs1kRight plots���bs1a'���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1gx-large���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1oFigure suptitle���bs1a'���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1hxx-large���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xN##############################################################################���`a
���bc1x5# It is possible to mix subplots and subfigures using���`a
���bc1xB# `matplotlib.figure.Figure.add_subfigure`.  This requires getting���`a
���bc1x1# the gridspec that the subplots are laid out on.���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia3���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmib10���`a,���`a ���bmia4���`a)���`a)���`a
���`hgridspec���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`oget_subplotspec���`a(���`a)���aoa.���`lget_gridspec���`a(���`a)���`a
���`a
���bc1x*# clear the left column for the subfigure:���`a
���akcfor���`a ���`aa���`a ���bowbin���`a ���`caxs���`a[���`a:���`a,���`a ���bmia0���`a]���`a:���`a
���`d    ���`aa���aoa.���`fremove���`a(���`a)���`a
���`a
���bc1x# plot data in remaining axes:���`a
���akcfor���`a ���`aa���`a ���bowbin���`a ���`caxs���`a[���`a:���`a,���`a ���bmia1���`a:���`a]���aoa.���`dflat���`a:���`a
���`d    ���`aa���aoa.���`dplot���`a(���`bnp���aoa.���`farange���`a(���bmib10���`a)���`a)���`a
���`a
���bc1x1# make the subfigure in the empty gridspec slots:���`a
���`fsubfig���`a ���aoa=���`a ���`cfig���aoa.���`madd_subfigure���`a(���`hgridspec���`a[���`a:���`a,���`a ���bmia0���`a]���`a)���`a
���`a
���`gaxsLeft���`a ���aoa=���`a ���`fsubfig���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`fsubfig���aoa.���`mset_facecolor���`a(���bs1a'���bs1d0.75���bs1a'���`a)���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`gaxsLeft���`a:���`a
���`d    ���`bpc���`a ���aoa=���`a ���`lexample_plot���`a(���`bax���`a)���`a
���`fsubfig���aoa.���`hsuptitle���`a(���bs1a'���bs1jLeft plots���bs1a'���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1gx-large���bs1a'���`a)���`a
���`fsubfig���aoa.���`hcolorbar���`a(���`bpc���`a,���`a ���`fshrink���aoa=���bmfc0.6���`a,���`a ���`bax���aoa=���`gaxsLeft���`a,���`a ���`hlocation���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1oFigure suptitle���bs1a'���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1hxx-large���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xN##############################################################################���`a
���bc1xH# Subfigures can have different widths and heights.  This is exactly the���`a
���bc1xI# same example as the first example, but *width_ratios* has been changed:���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmib10���`a,���`a ���bmia4���`a)���`a)���`a
���`gsubfigs���`a ���aoa=���`a ���`cfig���aoa.���`jsubfigures���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`fwspace���aoa=���bmfd0.07���`a,���`a ���`lwidth_ratios���aoa=���`a[���bmia2���`a,���`a ���bmia1���`a]���`a)���`a
���`a
���`gaxsLeft���`a ���aoa=���`a ���`gsubfigs���`a[���bmia0���`a]���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���`gsubfigs���`a[���bmia0���`a]���aoa.���`mset_facecolor���`a(���bs1a'���bs1d0.75���bs1a'���`a)���`a
���akcfor���`a ���`bax���`a ���bowbin���`a ���`gaxsLeft���`a:���`a
���`d    ���`bpc���`a ���aoa=���`a ���`lexample_plot���`a(���`bax���`a)���`a
���`gsubfigs���`a[���bmia0���`a]���aoa.���`hsuptitle���`a(���bs1a'���bs1jLeft plots���bs1a'���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1gx-large���bs1a'���`a)���`a
���`gsubfigs���`a[���bmia0���`a]���aoa.���`hcolorbar���`a(���`bpc���`a,���`a ���`fshrink���aoa=���bmfc0.6���`a,���`a ���`bax���aoa=���`gaxsLeft���`a,���`a ���`hlocation���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���`haxsRight���`a ���aoa=���`a ���`gsubfigs���`a[���bmia1���`a]���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a)���`a
���akcfor���`a ���`bnn���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`haxsRight���`a)���`a:���`a
���`d    ���`bpc���`a ���aoa=���`a ���`lexample_plot���`a(���`bax���`a,���`a ���`khide_labels���aoa=���bkcdTrue���`a)���`a
���`d    ���akbif���`a ���`bnn���`a ���aob==���`a ���bmia2���`a:���`a
���`h        ���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1fxlabel���bs1a'���`a)���`a
���`d    ���akbif���`a ���`bnn���`a ���aob==���`a ���bmia1���`a:���`a
���`h        ���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1fylabel���bs1a'���`a)���`a
���`a
���`gsubfigs���`a[���bmia1���`a]���aoa.���`mset_facecolor���`a(���bs1a'���bs1d0.85���bs1a'���`a)���`a
���`gsubfigs���`a[���bmia1���`a]���aoa.���`hcolorbar���`a(���`bpc���`a,���`a ���`fshrink���aoa=���bmfc0.6���`a,���`a ���`bax���aoa=���`haxsRight���`a)���`a
���`gsubfigs���`a[���bmia1���`a]���aoa.���`hsuptitle���`a(���bs1a'���bs1kRight plots���bs1a'���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1gx-large���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1oFigure suptitle���bs1a'���`a,���`a ���`hfontsize���aoa=���bs1a'���bs1hxx-large���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xN##############################################################################���`a
���bc1x## Subfigures can be also be nested:���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`rconstrained_layout���aoa=���bkcdTrue���`a,���`a ���`gfigsize���aoa=���`a(���bmib10���`a,���`a ���bmia8���`a)���`a)���`a
���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1cfig���bs1a'���`a)���`a
���`a
���`gsubfigs���`a ���aoa=���`a ���`cfig���aoa.���`jsubfigures���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`fwspace���aoa=���bmfd0.07���`a)���`a
���`a
���`gsubfigs���`a[���bmia0���`a]���aoa.���`mset_facecolor���`a(���bs1a'���bs1ecoral���bs1a'���`a)���`a
���`gsubfigs���`a[���bmia0���`a]���aoa.���`hsuptitle���`a(���bs1a'���bs1jsubfigs[0]���bs1a'���`a)���`a
���`a
���`gsubfigs���`a[���bmia1���`a]���aoa.���`mset_facecolor���`a(���bs1a'���bs1ecoral���bs1a'���`a)���`a
���`gsubfigs���`a[���bmia1���`a]���aoa.���`hsuptitle���`a(���bs1a'���bs1jsubfigs[1]���bs1a'���`a)���`a
���`a
���`ksubfigsnest���`a ���aoa=���`a ���`gsubfigs���`a[���bmia0���`a]���aoa.���`jsubfigures���`a(���bmia2���`a,���`a ���bmia1���`a,���`a ���`mheight_ratios���aoa=���`a[���bmia1���`a,���`a ���bmfc1.4���`a]���`a)���`a
���`ksubfigsnest���`a[���bmia0���`a]���aoa.���`hsuptitle���`a(���bs1a'���bs1nsubfigsnest[0]���bs1a'���`a)���`a
���`ksubfigsnest���`a[���bmia0���`a]���aoa.���`mset_facecolor���`a(���bs1a'���bs1ar���bs1a'���`a)���`a
���`haxsnest0���`a ���aoa=���`a ���`ksubfigsnest���`a[���bmia0���`a]���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���`fsharey���aoa=���bkcdTrue���`a)���`a
���akcfor���`a ���`bnn���`a,���`a ���`bax���`a ���bowbin���`a ���bnbienumerate���`a(���`haxsnest0���`a)���`a:���`a
���`d    ���`bpc���`a ���aoa=���`a ���`lexample_plot���`a(���`bax���`a,���`a ���`khide_labels���aoa=���bkcdTrue���`a)���`a
���`ksubfigsnest���`a[���bmia0���`a]���aoa.���`hcolorbar���`a(���`bpc���`a,���`a ���`bax���aoa=���`haxsnest0���`a)���`a
���`a
���`ksubfigsnest���`a[���bmia1���`a]���aoa.���`hsuptitle���`a(���bs1a'���bs1nsubfigsnest[1]���bs1a'���`a)���`a
���`ksubfigsnest���`a[���bmia1���`a]���aoa.���`mset_facecolor���`a(���bs1a'���bs1ag���bs1a'���`a)���`a
���`haxsnest1���`a ���aoa=���`a ���`ksubfigsnest���`a[���bmia1���`a]���aoa.���`hsubplots���`a(���bmia3���`a,���`a ���bmia1���`a,���`a ���`fsharex���aoa=���bkcdTrue���`a)���`a
���`a
���`haxsRight���`a ���aoa=���`a ���`gsubfigs���`a[���bmia1���`a]���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�