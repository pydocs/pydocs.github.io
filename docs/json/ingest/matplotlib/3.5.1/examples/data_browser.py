Ù¯‚Ù´ƒ™$Ù±‚bsdy"""
============
Data Browser
============

Connecting data between multiple canvases.

This example covers how to interact data with multiple canvases. This
let's you select and highlight a point on one axis, and generating the
data of that point on the other axis.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnclPointBrowserÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxÒ"""
    Click on a point to select and highlight it -- the data that
    generated the point will be shown in the lower axes.  Use the 'n'
    and 'p' keys to browse through the next and previous points
    """Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`glastindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia0Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfd0.05Ù±‚`a,Ù±‚`a Ù±‚bmfd0.95Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1nselected: noneÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x                            Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a,Ù±‚`a Ù±‚`bvaÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hselectedÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚`bxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚`bysÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`bmsÙ±‚aoa=Ù±‚bmib12Ù±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.4Ù±‚`a,Ù±‚`a
Ù±‚`x!                                 Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fyellowÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gvisibleÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfhon_pressÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`glastindÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`a(Ù±‚bs1a'Ù±‚bs1anÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1apÙ±‚bs1a'Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`ckeyÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1anÙ±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`cincÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`cincÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚aoa-Ù±‚bmia1Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`glastindÙ±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚`cincÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`glastindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dclipÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`glastindÙ±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`bxsÙ±‚`a)Ù±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fupdateÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgon_pickÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fartistÙ±‚`a Ù±‚aob!=Ù±‚`a Ù±‚`dlineÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`aNÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`eeventÙ±‚aoa.Ù±‚`cindÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bowcnotÙ±‚`a Ù±‚`aNÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚bkcdTrueÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bc1u# the click locationsÙ±‚`a
Ù±‚`h        Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`jmouseeventÙ±‚aoa.Ù±‚`exdataÙ±‚`a
Ù±‚`h        Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`jmouseeventÙ±‚aoa.Ù±‚`eydataÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`idistancesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ehypotÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bxsÙ±‚`a[Ù±‚`eeventÙ±‚aoa.Ù±‚`cindÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bysÙ±‚`a[Ù±‚`eeventÙ±‚aoa.Ù±‚`cindÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`findminÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`idistancesÙ±‚aoa.Ù±‚`fargminÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`gdataindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`cindÙ±‚`a[Ù±‚`findminÙ±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`glastindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gdataindÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fupdateÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnffupdateÙ±‚`a(Ù±‚bbpdselfÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`glastindÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`gdataindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`glastindÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`cax2Ù±‚aoa.Ù±‚`cclaÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cax2Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`aXÙ±‚`a[Ù±‚`gdataindÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`cax2Ù±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfd0.05Ù±‚`a,Ù±‚`a Ù±‚bmfc0.9Ù±‚`a,Ù±‚`a Ù±‚bsaafÙ±‚bs1a'Ù±‚bs1cmu=Ù±‚bsia{Ù±‚`bxsÙ±‚`a[Ù±‚`gdataindÙ±‚`a]Ù±‚bsia:Ù±‚bs1d1.3fÙ±‚bsia}Ù±‚bseb\nÙ±‚bs1fsigma=Ù±‚bsia{Ù±‚`bysÙ±‚`a[Ù±‚`gdataindÙ±‚`a]Ù±‚bsia:Ù±‚bs1d1.3fÙ±‚bsia}Ù±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`q                 Ù±‚`itransformÙ±‚aoa=Ù±‚`cax2Ù±‚aoa.Ù±‚`itransAxesÙ±‚`a,Ù±‚`a Ù±‚`bvaÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cax2Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚aoa-Ù±‚bmfc0.5Ù±‚`a,Ù±‚`a Ù±‚bmfc1.5Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hselectedÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hselectedÙ±‚aoa.Ù±‚`hset_dataÙ±‚`a(Ù±‚`bxsÙ±‚`a[Ù±‚`gdataindÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`bysÙ±‚`a[Ù±‚`gdataindÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dtextÙ±‚aoa.Ù±‚`hset_textÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jselected: Ù±‚bsib%dÙ±‚bs1a'Ù±‚`a Ù±‚aoa%Ù±‚`a Ù±‚`gdataindÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bvmh__name__Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1h__main__Ù±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`d    Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`d    Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`aXÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic200Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bysÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cstdÙ±‚`a(Ù±‚`aXÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x"click on point to plot time seriesÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bxsÙ±‚`a,Ù±‚`a Ù±‚`bysÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fpickerÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`jpickradiusÙ±‚aoa=Ù±‚bmia5Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`gbrowserÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lPointBrowserÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jpick_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gbrowserÙ±‚aoa.Ù±‚`gon_pickÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1okey_press_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gbrowserÙ±‚aoa.Ù±‚`hon_pressÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö