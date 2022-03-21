Ù¯‚Ù´ƒ™ÄÙ±‚bsdyC"""
==========
Lasso Demo
==========

Show how to use a lasso to select a set of points and get the indices
of the selected points.  A callback is used to change the color of the
selected points

This is currently a proof-of-concept implementation (though it is
usable as is).  There will be some refinement of the API.
"""Ù±‚`a
Ù±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fcolorsÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚`gmcolorsÙ±‚`a,Ù±‚`a Ù±‚`dpathÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnkcollectionsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`uRegularPolyCollectionÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngwidgetsÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`eLassoÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnceDatumÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`gcolorinÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gmcolorsÙ±‚aoa.Ù±‚`gto_rgbaÙ±‚`a(Ù±‚bs2a"Ù±‚bs2credÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`hcoloroutÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`gmcolorsÙ±‚aoa.Ù±‚`gto_rgbaÙ±‚`a(Ù±‚bs2a"Ù±‚bs2dblueÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`gincludeÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ayÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`gincludeÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ecolorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`gcolorinÙ±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ecolorÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hcoloroutÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnclLassoManagerÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`ddataÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`daxesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`ddataÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cNxyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`ddataÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`jfacecolorsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`adÙ±‚aoa.Ù±‚`ecolorÙ±‚`a Ù±‚akcforÙ±‚`a Ù±‚`adÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`ddataÙ±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cxysÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`a(Ù±‚`adÙ±‚aoa.Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`adÙ±‚aoa.Ù±‚`ayÙ±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`adÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`ddataÙ±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jcollectionÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`uRegularPolyCollectionÙ±‚`a(Ù±‚`a
Ù±‚`l            Ù±‚bmia6Ù±‚`a,Ù±‚`a Ù±‚`esizesÙ±‚aoa=Ù±‚`a(Ù±‚bmic100Ù±‚`a,Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`jfacecolorsÙ±‚aoa=Ù±‚`jfacecolorsÙ±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`goffsetsÙ±‚aoa=Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cxysÙ±‚`a,Ù±‚`a
Ù±‚`l            Ù±‚`ktransOffsetÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransDataÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`baxÙ±‚aoa.Ù±‚`nadd_collectionÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jcollectionÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`ccidÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1rbutton_press_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hon_pressÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfhcallbackÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`evertsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`jfacecolorsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`jcollectionÙ±‚aoa.Ù±‚`nget_facecolorsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`apÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dpathÙ±‚aoa.Ù±‚`dPathÙ±‚`a(Ù±‚`evertsÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`apÙ±‚aoa.Ù±‚`ocontains_pointsÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cxysÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`cxysÙ±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akbifÙ±‚`a Ù±‚`cindÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚`jfacecolorsÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eDatumÙ±‚aoa.Ù±‚`gcolorinÙ±‚`a
Ù±‚`l            Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚`jfacecolorsÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eDatumÙ±‚aoa.Ù±‚`hcoloroutÙ±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`idraw_idleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`jwidgetlockÙ±‚aoa.Ù±‚`greleaseÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`elassoÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akcdelÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`elassoÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfhon_pressÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`jwidgetlockÙ±‚aoa.Ù±‚`flockedÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`elassoÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eLassoÙ±‚`a(Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a,Ù±‚`a
Ù±‚`x                           Ù±‚`a(Ù±‚`eeventÙ±‚aoa.Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`eydataÙ±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`x                           Ù±‚bbpdselfÙ±‚aoa.Ù±‚`hcallbackÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚bc1x&# acquire a lock on the widget drawingÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`jwidgetlockÙ±‚`a(Ù±‚bbpdselfÙ±‚aoa.Ù±‚`elassoÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bvmh__name__Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1h__main__Ù±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`eDatumÙ±‚`a(Ù±‚aoa*Ù±‚`bxyÙ±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`bxyÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`daxesÙ±‚`a(Ù±‚`dxlimÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dylimÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`lautoscale_onÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x$Lasso points using left mouse buttonÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`dlmanÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lLassoManagerÙ±‚`a(Ù±‚`baxÙ±‚`a,Ù±‚`a Ù±‚`ddataÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö