Ù¯‚Ù´ƒ™	Ù±‚bsdxÓ"""
======
Spines
======

This demo compares:

- normal axes, with spines on all four sides;
- an axes with spines only on the left and bottom;
- an axes using custom bounds to limit the extent of the spine.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xB# Constrained layout makes sure the labels don't overlap the axes.Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax0Ù±‚`a,Ù±‚`a Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`enrowsÙ±‚aoa=Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`cax0Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1mnormal spinesÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1rbottom-left spinesÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x# Hide the right and top spinesÙ±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`erightÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`ctopÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚bc1x/# Only show ticks on the left and bottom spinesÙ±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x%# Only draw spine between the y-ticksÙ±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`dleftÙ±‚aoa.Ù±‚`jset_boundsÙ±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚bc1x# Hide the right and top spinesÙ±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`erightÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`ctopÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚bc1x/# Only show ticks on the left and bottom spinesÙ±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`eyaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`rset_ticks_positionÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö