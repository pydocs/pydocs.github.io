Ù¯‚Ù´ƒ˜üÙ±‚bsdyM"""
=======================================================
Using Gridspec to make multi-column/row subplot layouts
=======================================================

`.GridSpec` is a flexible way to layout
subplot grids.  Here is an example with a 3x3 grid, and
axes spanning all three columns, two columns, and two rows.

"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnhgridspecÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`hGridSpecÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfkformat_axesÙ±‚`a(Ù±‚`cfigÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnbienumerateÙ±‚`a(Ù±‚`cfigÙ±‚aoa.Ù±‚`daxesÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2baxÙ±‚bsib%dÙ±‚bs2a"Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`a(Ù±‚`aiÙ±‚aoa+Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`bvaÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fcenterÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`bhaÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2fcenterÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`ktick_paramsÙ±‚`a(Ù±‚`klabelbottomÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a,Ù±‚`a Ù±‚`ilabelleftÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`bgsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hGridSpecÙ±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚`ffigureÙ±‚aoa=Ù±‚`cfigÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`bgsÙ±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚bc1xG# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))Ù±‚`a
Ù±‚`cax2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`bgsÙ±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`cax3Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`bgsÙ±‚`a[Ù±‚bmia1Ù±‚`a:Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`cax4Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`bgsÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`cax5Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cfigÙ±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`bgsÙ±‚`a[Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚bmia2Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2hGridSpecÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`kformat_axesÙ±‚`a(Ù±‚`cfigÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö