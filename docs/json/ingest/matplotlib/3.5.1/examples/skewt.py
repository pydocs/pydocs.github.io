Ù¯‚Ù´ƒ™ÜÙ±‚bsdy """
===========================================================
SkewT-logP diagram: using transforms and custom projections
===========================================================

This serves as an intensive exercise of Matplotlib's transforms and custom
projection API. This example produces a so-called SkewT-logP diagram, which is
a common plot in meteorology for displaying vertical profiles of temperature.
As far as Matplotlib is concerned, the complexity comes from having X and Y
axes that are not orthogonal. This is handled by including a skew component to
the basic Axes transforms. Additional complexity comes in handling the fact
that the upper and lower X-axes have different data ranges, which necessitates
a bunch of custom classes for ticks, spines, and axis to handle this.
"""Ù±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnjcontextlibÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`iExitStackÙ±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnndaxesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`dAxesÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnjtransformsÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnjtransformsÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnndaxisÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnemaxisÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfspinesÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnngmspinesÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnkprojectionsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`sregister_projectionÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xI# The sole purpose of this class is to look at the upper, lower, or totalÙ±‚`a
Ù±‚bc1xI# interval as appropriate and see what parts of the tick to draw, if any.Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnciSkewXTickÙ±‚`a(Ù±‚`emaxisÙ±‚aoa.Ù±‚`eXTickÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfddrawÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`hrendererÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1xG# When adding the callbacks with `stack.callback`, we fetch the currentÙ±‚`a
Ù±‚`h        Ù±‚bc1xG# visibility state of the artist with `get_visible`; the ExitStack willÙ±‚`a
Ù±‚`h        Ù±‚bc1xE# restore these states (`set_visible`) at the end of the block (afterÙ±‚`a
Ù±‚`h        Ù±‚bc1l# the draw).Ù±‚`a
Ù±‚`h        Ù±‚akdwithÙ±‚`a Ù±‚`iExitStackÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚akbasÙ±‚`a Ù±‚`estackÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akcforÙ±‚`a Ù±‚`fartistÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`a[Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hgridlineÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itick1lineÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itick2lineÙ±‚`a,Ù±‚`a
Ù±‚`x                           Ù±‚bbpdselfÙ±‚aoa.Ù±‚`flabel1Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`flabel2Ù±‚`a]Ù±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚`estackÙ±‚aoa.Ù±‚`hcallbackÙ±‚`a(Ù±‚`fartistÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a,Ù±‚`a Ù±‚`fartistÙ±‚aoa.Ù±‚`kget_visibleÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`kneeds_lowerÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jtransformsÙ±‚aoa.Ù±‚`qinterval_containsÙ±‚`a(Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`daxesÙ±‚aoa.Ù±‚`jlower_xlimÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gget_locÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`kneeds_upperÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jtransformsÙ±‚aoa.Ù±‚`qinterval_containsÙ±‚`a(Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`daxesÙ±‚aoa.Ù±‚`jupper_xlimÙ±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gget_locÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itick1lineÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itick1lineÙ±‚aoa.Ù±‚`kget_visibleÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚bowcandÙ±‚`a Ù±‚`kneeds_lowerÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`flabel1Ù±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`flabel1Ù±‚aoa.Ù±‚`kget_visibleÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚bowcandÙ±‚`a Ù±‚`kneeds_lowerÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itick2lineÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itick2lineÙ±‚aoa.Ù±‚`kget_visibleÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚bowcandÙ±‚`a Ù±‚`kneeds_upperÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`flabel2Ù±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`flabel2Ù±‚aoa.Ù±‚`kget_visibleÙ±‚`a(Ù±‚`a)Ù±‚`a Ù±‚bowcandÙ±‚`a Ù±‚`kneeds_upperÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`hrendererÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfqget_view_intervalÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`daxesÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qget_view_intervalÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xJ# This class exists to provide two separate sets of intervals to the tick,Ù±‚`a
Ù±‚bc1x0# as well as create instances of the custom tickÙ±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnciSkewXAxisÙ±‚`a(Ù±‚`emaxisÙ±‚aoa.Ù±‚`eXAxisÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfi_get_tickÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`emajorÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`iSkewXTickÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`daxesÙ±‚`a,Ù±‚`a Ù±‚bkcdNoneÙ±‚`a,Ù±‚`a Ù±‚`emajorÙ±‚aoa=Ù±‚`emajorÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfqget_view_intervalÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`daxesÙ±‚aoa.Ù±‚`jupper_xlimÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`daxesÙ±‚aoa.Ù±‚`jlower_xlimÙ±‚`a[Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x?# This class exists to calculate the separate data range of theÙ±‚`a
Ù±‚bc1xD# upper X-axis and draw the spine there. It also provides this rangeÙ±‚`a
Ù±‚bc1x0# to the X-axis artist for ticking and gridlinesÙ±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnciSkewSpineÙ±‚`a(Ù±‚`gmspinesÙ±‚aoa.Ù±‚`eSpineÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfp_adjust_locationÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`cptsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`e_pathÙ±‚aoa.Ù±‚`hverticesÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jspine_typeÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`cptsÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`daxesÙ±‚aoa.Ù±‚`jupper_xlimÙ±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`cptsÙ±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`daxesÙ±‚aoa.Ù±‚`jlower_xlimÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xK# This class handles registration of the skew-xaxes as a projection as wellÙ±‚`a
Ù±‚bc1xK# as setting up the appropriate transformations. It also overrides standardÙ±‚`a
Ù±‚bc1x+# spines and axes instances as appropriate.Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnciSkewXAxesÙ±‚`a(Ù±‚`dAxesÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x?# The projection must specify a name.  This will be used be theÙ±‚`a
Ù±‚`d    Ù±‚bc1xF# user to select the projection, i.e. ``subplot(projection='skewx')``.Ù±‚`a
Ù±‚`d    Ù±‚`dnameÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1a'Ù±‚bs1eskewxÙ±‚bs1a'Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfj_init_axisÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1x9# Taken from Axes and modified to use our modified X-axisÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`exaxisÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`iSkewXAxisÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`ctopÙ±‚aoa.Ù±‚`mregister_axisÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`exaxisÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`fbottomÙ±‚aoa.Ù±‚`mregister_axisÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`exaxisÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eyaxisÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`emaxisÙ±‚aoa.Ù±‚`eYAxisÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`dleftÙ±‚aoa.Ù±‚`mregister_axisÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eyaxisÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`erightÙ±‚aoa.Ù±‚`mregister_axisÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`eyaxisÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfp_gen_axes_spinesÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`fspinesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a{Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`iSkewSpineÙ±‚aoa.Ù±‚`llinear_spineÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`gmspinesÙ±‚aoa.Ù±‚`eSpineÙ±‚aoa.Ù±‚`llinear_spineÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`gmspinesÙ±‚aoa.Ù±‚`eSpineÙ±‚aoa.Ù±‚`llinear_spineÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚bs1a'Ù±‚bs1erightÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`gmspinesÙ±‚aoa.Ù±‚`eSpineÙ±‚aoa.Ù±‚`llinear_spineÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1erightÙ±‚bs1a'Ù±‚`a)Ù±‚`a}Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚`fspinesÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfw_set_lim_and_transformsÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx‡"""
        This is called once when the plot is created to set up all the
        transforms for the data, text and grids.
        """Ù±‚`a
Ù±‚`h        Ù±‚`crotÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmib30Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1x;# Get the standard transform setup from the Axes base classÙ±‚`a
Ù±‚`h        Ù±‚bnbesuperÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`w_set_lim_and_transformsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1xA# Need to put the skew in the middle, after the scale and limits,Ù±‚`a
Ù±‚`h        Ù±‚bc1x># but before the transAxes. This way, the skew is done in AxesÙ±‚`a
Ù±‚`h        Ù±‚bc1xD# coordinates thus performing the transform around the proper originÙ±‚`a
Ù±‚`h        Ù±‚bc1xF# We keep the pre-transAxes transform around for other users, like theÙ±‚`a
Ù±‚`h        Ù±‚bc1x# spines for finding boundsÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`otransDataToAxesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jtransScaleÙ±‚`a
Ù±‚`l            Ù±‚aoa+Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ktransLimitsÙ±‚`a
Ù±‚`l            Ù±‚aoa+Ù±‚`a Ù±‚`jtransformsÙ±‚aoa.Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`hskew_degÙ±‚`a(Ù±‚`crotÙ±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bc1x/# Create the full transform from Data to PixelsÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itransDataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`otransDataToAxesÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1xE# Blended transforms like this need to have the skewing applied usingÙ±‚`a
Ù±‚`h        Ù±‚bc1x(# both axes, in axes coords like before.Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`p_xaxis_transformÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`a
Ù±‚`l            Ù±‚`jtransformsÙ±‚aoa.Ù±‚`xblended_transform_factoryÙ±‚`a(Ù±‚`a
Ù±‚`p                Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jtransScaleÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ktransLimitsÙ±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`jtransformsÙ±‚aoa.Ù±‚`qIdentityTransformÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚aoa+Ù±‚`a Ù±‚`jtransformsÙ±‚aoa.Ù±‚`hAffine2DÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`hskew_degÙ±‚`a(Ù±‚`crotÙ±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚aoa+Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a
Ù±‚`h        Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bndi@propertyÙ±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfjlower_xlimÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`daxesÙ±‚aoa.Ù±‚`gviewLimÙ±‚aoa.Ù±‚`iintervalxÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bndi@propertyÙ±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfjupper_xlimÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`cptsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a[Ù±‚bmfb0.Ù±‚`a,Ù±‚`a Ù±‚bmfb1.Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmfb1.Ù±‚`a,Ù±‚`a Ù±‚bmfb1.Ù±‚`a]Ù±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`otransDataToAxesÙ±‚aoa.Ù±‚`hinvertedÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`itransformÙ±‚`a(Ù±‚`cptsÙ±‚`a)Ù±‚`a[Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xH# Now register the projection with matplotlib so the user can select it.Ù±‚`a
Ù±‚`sregister_projectionÙ±‚`a(Ù±‚`iSkewXAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bvmh__name__Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1h__main__Ù±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x8# Now make a simple example using the custom projection.Ù±‚`a
Ù±‚`d    Ù±‚bkndfromÙ±‚`a Ù±‚bnnbioÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`hStringIOÙ±‚`a
Ù±‚`d    Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnftickerÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`a(Ù±‚`oMultipleLocatorÙ±‚`a,Ù±‚`a Ù±‚`mNullFormatterÙ±‚`a,Ù±‚`a
Ù±‚`x#                                   Ù±‚`oScalarFormatterÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`d    Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1t# Some example data.Ù±‚`a
Ù±‚`d    Ù±‚`hdata_txtÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bs1c'''Ù±‚bs1a
Ù±‚bs1x"        978.0    345    7.8    0.8Ù±‚bs1a
Ù±‚bs1x"        971.0    404    7.2    0.2Ù±‚bs1a
Ù±‚bs1x"        946.7    610    5.2   -1.8Ù±‚bs1a
Ù±‚bs1x"        944.0    634    5.0   -2.0Ù±‚bs1a
Ù±‚bs1x"        925.0    798    3.4   -2.6Ù±‚bs1a
Ù±‚bs1x"        911.8    914    2.4   -2.7Ù±‚bs1a
Ù±‚bs1x"        906.0    966    2.0   -2.7Ù±‚bs1a
Ù±‚bs1x"        877.9   1219    0.4   -3.2Ù±‚bs1a
Ù±‚bs1x"        850.0   1478   -1.3   -3.7Ù±‚bs1a
Ù±‚bs1x"        841.0   1563   -1.9   -3.8Ù±‚bs1a
Ù±‚bs1x"        823.0   1736    1.4   -0.7Ù±‚bs1a
Ù±‚bs1x"        813.6   1829    4.5    1.2Ù±‚bs1a
Ù±‚bs1x"        809.0   1875    6.0    2.2Ù±‚bs1a
Ù±‚bs1x"        798.0   1988    7.4   -0.6Ù±‚bs1a
Ù±‚bs1x"        791.0   2061    7.6   -1.4Ù±‚bs1a
Ù±‚bs1x"        783.9   2134    7.0   -1.7Ù±‚bs1a
Ù±‚bs1x"        755.1   2438    4.8   -3.1Ù±‚bs1a
Ù±‚bs1x"        727.3   2743    2.5   -4.4Ù±‚bs1a
Ù±‚bs1x"        700.5   3048    0.2   -5.8Ù±‚bs1a
Ù±‚bs1x"        700.0   3054    0.2   -5.8Ù±‚bs1a
Ù±‚bs1x"        698.0   3077    0.0   -6.0Ù±‚bs1a
Ù±‚bs1x"        687.0   3204   -0.1   -7.1Ù±‚bs1a
Ù±‚bs1x"        648.9   3658   -3.2  -10.9Ù±‚bs1a
Ù±‚bs1x"        631.0   3881   -4.7  -12.7Ù±‚bs1a
Ù±‚bs1x"        600.7   4267   -6.4  -16.7Ù±‚bs1a
Ù±‚bs1x"        592.0   4381   -6.9  -17.9Ù±‚bs1a
Ù±‚bs1x"        577.6   4572   -8.1  -19.6Ù±‚bs1a
Ù±‚bs1x"        555.3   4877  -10.0  -22.3Ù±‚bs1a
Ù±‚bs1x"        536.0   5151  -11.7  -24.7Ù±‚bs1a
Ù±‚bs1x"        533.8   5182  -11.9  -25.0Ù±‚bs1a
Ù±‚bs1x"        500.0   5680  -15.9  -29.9Ù±‚bs1a
Ù±‚bs1x"        472.3   6096  -19.7  -33.4Ù±‚bs1a
Ù±‚bs1x"        453.0   6401  -22.4  -36.0Ù±‚bs1a
Ù±‚bs1x"        400.0   7310  -30.7  -43.7Ù±‚bs1a
Ù±‚bs1x"        399.7   7315  -30.8  -43.8Ù±‚bs1a
Ù±‚bs1x"        387.0   7543  -33.1  -46.1Ù±‚bs1a
Ù±‚bs1x"        382.7   7620  -33.8  -46.8Ù±‚bs1a
Ù±‚bs1x"        342.0   8398  -40.5  -53.5Ù±‚bs1a
Ù±‚bs1x"        320.4   8839  -43.7  -56.7Ù±‚bs1a
Ù±‚bs1x"        318.0   8890  -44.1  -57.1Ù±‚bs1a
Ù±‚bs1x"        310.0   9060  -44.7  -58.7Ù±‚bs1a
Ù±‚bs1x"        306.1   9144  -43.9  -57.9Ù±‚bs1a
Ù±‚bs1x"        305.0   9169  -43.7  -57.7Ù±‚bs1a
Ù±‚bs1x"        300.0   9280  -43.5  -57.5Ù±‚bs1a
Ù±‚bs1x"        292.0   9462  -43.7  -58.7Ù±‚bs1a
Ù±‚bs1x"        276.0   9838  -47.1  -62.1Ù±‚bs1a
Ù±‚bs1x"        264.0  10132  -47.5  -62.5Ù±‚bs1a
Ù±‚bs1x"        251.0  10464  -49.7  -64.7Ù±‚bs1a
Ù±‚bs1x"        250.0  10490  -49.7  -64.7Ù±‚bs1a
Ù±‚bs1x"        247.0  10569  -48.7  -63.7Ù±‚bs1a
Ù±‚bs1x"        244.0  10649  -48.9  -63.9Ù±‚bs1a
Ù±‚bs1x"        243.3  10668  -48.9  -63.9Ù±‚bs1a
Ù±‚bs1x"        220.0  11327  -50.3  -65.3Ù±‚bs1a
Ù±‚bs1x"        212.0  11569  -50.5  -65.5Ù±‚bs1a
Ù±‚bs1x"        210.0  11631  -49.7  -64.7Ù±‚bs1a
Ù±‚bs1x"        200.0  11950  -49.9  -64.9Ù±‚bs1a
Ù±‚bs1x"        194.0  12149  -49.9  -64.9Ù±‚bs1a
Ù±‚bs1x"        183.0  12529  -51.3  -66.3Ù±‚bs1a
Ù±‚bs1x"        164.0  13233  -55.3  -68.3Ù±‚bs1a
Ù±‚bs1x"        152.0  13716  -56.5  -69.5Ù±‚bs1a
Ù±‚bs1x"        150.0  13800  -57.1  -70.1Ù±‚bs1a
Ù±‚bs1x"        136.0  14414  -60.5  -72.5Ù±‚bs1a
Ù±‚bs1x"        132.0  14600  -60.1  -72.1Ù±‚bs1a
Ù±‚bs1x"        131.4  14630  -60.2  -72.2Ù±‚bs1a
Ù±‚bs1x"        128.0  14792  -60.9  -72.9Ù±‚bs1a
Ù±‚bs1x"        125.0  14939  -60.1  -72.1Ù±‚bs1a
Ù±‚bs1x"        119.0  15240  -62.2  -73.8Ù±‚bs1a
Ù±‚bs1x"        112.0  15616  -64.9  -75.9Ù±‚bs1a
Ù±‚bs1x"        108.0  15838  -64.1  -75.1Ù±‚bs1a
Ù±‚bs1x"        107.8  15850  -64.1  -75.1Ù±‚bs1a
Ù±‚bs1x"        105.0  16010  -64.7  -75.7Ù±‚bs1a
Ù±‚bs1x"        103.0  16128  -62.9  -73.9Ù±‚bs1a
Ù±‚bs1x"        100.0  16310  -62.5  -73.5Ù±‚bs1a
Ù±‚bs1d    Ù±‚bs1c'''Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1p# Parse the dataÙ±‚`a
Ù±‚`d    Ù±‚`jsound_dataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hStringIOÙ±‚`a(Ù±‚`hdata_txtÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`apÙ±‚`a,Ù±‚`a Ù±‚`ahÙ±‚`a,Ù±‚`a Ù±‚`aTÙ±‚`a,Ù±‚`a Ù±‚`bTdÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gloadtxtÙ±‚`a(Ù±‚`jsound_dataÙ±‚`a,Ù±‚`a Ù±‚`funpackÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1xC# Create a new figure. The dimensions here give a good aspect ratioÙ±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`gfigsizeÙ±‚aoa=Ù±‚`a(Ù±‚bmff6.5875Ù±‚`a,Ù±‚`a Ù±‚bmff6.2125Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eskewxÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1xC# Plot the data using normal plotting functions, in this case usingÙ±‚`a
Ù±‚`d    Ù±‚bc1xB# log scaling in Y, as dictated by the typical meteorological plotÙ±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hsemilogyÙ±‚`a(Ù±‚`aTÙ±‚`a,Ù±‚`a Ù±‚`apÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC3Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hsemilogyÙ±‚`a(Ù±‚`bTdÙ±‚`a,Ù±‚`a Ù±‚`apÙ±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC2Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x,# An example of a slanted line at constant XÙ±‚`a
Ù±‚`d    Ù±‚`alÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`gaxvlineÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1bC0Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x6# Disables the log-formatting that comes with semilogyÙ±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`sset_major_formatterÙ±‚`a(Ù±‚`oScalarFormatterÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`sset_minor_formatterÙ±‚`a(Ù±‚`mNullFormatterÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`jset_yticksÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmid1000Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmid1050Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qset_major_locatorÙ±‚`a(Ù±‚`oMultipleLocatorÙ±‚`a(Ù±‚bmib10Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚aoa-Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x#    - `matplotlib.transforms`Ù±‚`a
Ù±‚bc1x#    - `matplotlib.spines`Ù±‚`a
Ù±‚bc1x #    - `matplotlib.spines.Spine`Ù±‚`a
Ù±‚bc1x.#    - `matplotlib.spines.Spine.register_axis`Ù±‚`a
Ù±‚bc1x#    - `matplotlib.projections`Ù±‚`a
Ù±‚bc1x3#    - `matplotlib.projections.register_projection`Ù±‚`a
`dNoneö