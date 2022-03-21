Ù¯‚Ù´ƒ™¶Ù±‚bsdxÿ"""
===============
Spine Placement
===============

Adjusting the location and appearance of axis spines.

Note: If you want to obtain arrow heads at the ends of the axes, also check
out the :doc:`/gallery/spines/centered_spines_with_arrows` example.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚aoa-Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ocentered spinesÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`dleftÙ±‚aoa.Ù±‚`lset_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`erightÙ±‚aoa.Ù±‚`iset_colorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`fbottomÙ±‚aoa.Ù±‚`lset_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`ctopÙ±‚aoa.Ù±‚`iset_colorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1mzeroed spinesÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`dleftÙ±‚aoa.Ù±‚`lset_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dzeroÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`erightÙ±‚aoa.Ù±‚`iset_colorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`fbottomÙ±‚aoa.Ù±‚`lset_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dzeroÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`ctopÙ±‚aoa.Ù±‚`iset_colorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1xspines at axes (0.6, 0.1)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`dleftÙ±‚aoa.Ù±‚`lset_positionÙ±‚`a(Ù±‚`a(Ù±‚bs1a'Ù±‚bs1daxesÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bmfc0.6Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`erightÙ±‚aoa.Ù±‚`iset_colorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`fbottomÙ±‚aoa.Ù±‚`lset_positionÙ±‚`a(Ù±‚`a(Ù±‚bs1a'Ù±‚bs1daxesÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`ctopÙ±‚aoa.Ù±‚`iset_colorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1uspines at data (1, 2)Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`dleftÙ±‚aoa.Ù±‚`lset_positionÙ±‚`a(Ù±‚`a(Ù±‚bs1a'Ù±‚bs1ddataÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`erightÙ±‚aoa.Ù±‚`iset_colorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`fbottomÙ±‚aoa.Ù±‚`lset_positionÙ±‚`a(Ù±‚`a(Ù±‚bs1a'Ù±‚bs1ddataÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`ctopÙ±‚aoa.Ù±‚`iset_colorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x># Define a method that adjusts the location of the axis spinesÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfmadjust_spinesÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`fspinesÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`clocÙ±‚`a,Ù±‚`a Ù±‚`espineÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`eitemsÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`clocÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`fspinesÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`espineÙ±‚aoa.Ù±‚`lset_positionÙ±‚`a(Ù±‚`a(Ù±‚bs1a'Ù±‚bs1goutwardÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a)Ù±‚`b  Ù±‚bc1v# outward by 10 pointsÙ±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`espineÙ±‚aoa.Ù±‚`iset_colorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dnoneÙ±‚bs1a'Ù±‚`a)Ù±‚`b  Ù±‚bc1r# don't draw spineÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x(# turn off ticks where there is no spineÙ±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`fspinesÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1p# no yaxis ticksÙ±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`iset_ticksÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`fspinesÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bc1p# no xaxis ticksÙ±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`iset_ticksÙ±‚`a(Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1xO###############################################################################Ù±‚`a
Ù±‚bc1x># Create another figure using our new ``adjust_spines`` methodÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`gclip_onÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`madjust_spinesÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`gclip_onÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`madjust_spinesÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`gclip_onÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`madjust_spinesÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`gclip_onÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`madjust_spinesÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö