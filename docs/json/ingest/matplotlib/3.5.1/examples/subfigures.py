Ù¯‚Ù´ƒ™7Ù±‚bsdy°"""
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

"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnflexample_plotÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib12Ù±‚`a,Ù±‚`a Ù±‚`khide_labelsÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bpcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`jpcolormeshÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚bmib30Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dvminÙ±‚aoa=Ù±‚aoa-Ù±‚bmfc2.5Ù±‚`a,Ù±‚`a Ù±‚`dvmaxÙ±‚aoa=Ù±‚bmfc2.5Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚`khide_labelsÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gx-labelÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚`hfontsizeÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gy-labelÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚`hfontsizeÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1eTitleÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚`hfontsizeÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`bpcÙ±‚`a
Ù±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680808Ù±‚`a)Ù±‚`a
Ù±‚bc1x# gridspec inside gridspecÙ±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`jsubfiguresÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fwspaceÙ±‚aoa=Ù±‚bmfd0.07Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`gaxsLeftÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fshareyÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1d0.75Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`gaxsLeftÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bpcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lexample_plotÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jLeft plotsÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gx-largeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bpcÙ±‚`a,Ù±‚`a Ù±‚`fshrinkÙ±‚aoa=Ù±‚bmfc0.6Ù±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`gaxsLeftÙ±‚`a,Ù±‚`a Ù±‚`hlocationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`haxsRightÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`fsharexÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`bnnÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbienumerateÙ±‚`a(Ù±‚`haxsRightÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bpcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lexample_plotÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`khide_labelsÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`bnnÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia2Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fxlabelÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`bnnÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fylabelÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1d0.85Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bpcÙ±‚`a,Ù±‚`a Ù±‚`fshrinkÙ±‚aoa=Ù±‚bmfc0.6Ù±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`haxsRightÙ±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1kRight plotsÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gx-largeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1oFigure suptitleÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hxx-largeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xN##############################################################################Ù±‚`a
Ù±‚bc1x5# It is possible to mix subplots and subfigures usingÙ±‚`a
Ù±‚bc1xB# `matplotlib.figure.Figure.add_subfigure`.  This requires gettingÙ±‚`a
Ù±‚bc1x1# the gridspec that the subplots are laid out on.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`hgridspecÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`oget_subplotspecÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`lget_gridspecÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x*# clear the left column for the subfigure:Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aaÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`aaÙ±‚aoa.Ù±‚`fremoveÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# plot data in remaining axes:Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aaÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`caxsÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a]Ù±‚aoa.Ù±‚`dflatÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`aaÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmib10Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x1# make the subfigure in the empty gridspec slots:Ù±‚`a
Ù±‚`fsubfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`madd_subfigureÙ±‚`a(Ù±‚`hgridspecÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`gaxsLeftÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fsubfigÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fshareyÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`fsubfigÙ±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1d0.75Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`gaxsLeftÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bpcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lexample_plotÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a
Ù±‚`fsubfigÙ±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jLeft plotsÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gx-largeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`fsubfigÙ±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bpcÙ±‚`a,Ù±‚`a Ù±‚`fshrinkÙ±‚aoa=Ù±‚bmfc0.6Ù±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`gaxsLeftÙ±‚`a,Ù±‚`a Ù±‚`hlocationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1oFigure suptitleÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hxx-largeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xN##############################################################################Ù±‚`a
Ù±‚bc1xH# Subfigures can have different widths and heights.  This is exactly theÙ±‚`a
Ù±‚bc1xI# same example as the first example, but *width_ratios* has been changed:Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`jsubfiguresÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fwspaceÙ±‚aoa=Ù±‚bmfd0.07Ù±‚`a,Ù±‚`a Ù±‚`lwidth_ratiosÙ±‚aoa=Ù±‚`a[Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`gaxsLeftÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fshareyÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1d0.75Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`gaxsLeftÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bpcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lexample_plotÙ±‚`a(Ù±‚`baxÙ±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jLeft plotsÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gx-largeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bpcÙ±‚`a,Ù±‚`a Ù±‚`fshrinkÙ±‚aoa=Ù±‚bmfc0.6Ù±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`gaxsLeftÙ±‚`a,Ù±‚`a Ù±‚`hlocationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`haxsRightÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`fsharexÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`bnnÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbienumerateÙ±‚`a(Ù±‚`haxsRightÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bpcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lexample_plotÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`khide_labelsÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`bnnÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia2Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fxlabelÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`bnnÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fylabelÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1d0.85Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bpcÙ±‚`a,Ù±‚`a Ù±‚`fshrinkÙ±‚aoa=Ù±‚bmfc0.6Ù±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`haxsRightÙ±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1kRight plotsÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gx-largeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1oFigure suptitleÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hxx-largeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xN##############################################################################Ù±‚`a
Ù±‚bc1x## Subfigures can be also be nested:Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmia8Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1cfigÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`jsubfiguresÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fwspaceÙ±‚aoa=Ù±‚bmfd0.07Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ecoralÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jsubfigs[0]Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ecoralÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jsubfigs[1]Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ksubfigsnestÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`jsubfiguresÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`mheight_ratiosÙ±‚aoa=Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmfc1.4Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`ksubfigsnestÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1nsubfigsnest[0]Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`ksubfigsnestÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`haxsnest0Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ksubfigsnestÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`fshareyÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`bnnÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbienumerateÙ±‚`a(Ù±‚`haxsnest0Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`bpcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lexample_plotÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`khide_labelsÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`ksubfigsnestÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚aoa.Ù±‚`hcolorbarÙ±‚`a(Ù±‚`bpcÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚aoa=Ù±‚`haxsnest0Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ksubfigsnestÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1nsubfigsnest[1]Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`ksubfigsnestÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1agÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`haxsnest1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ksubfigsnestÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`fsharexÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`haxsRightÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gsubfigsÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö