ŸØÇÅŸ¥ÉôŸ±Çbsdy∞"""
===================
Packed-bubble chart
===================

Create a packed-bubble chart to represent scalar data.
The presented algorithm tries to move all bubbles as close to the center of
mass as possible while avoiding some collisions by moving around colliding
objects. In this example we plot the market share of different desktop
browsers.
(source: https://gs.statcounter.com/browser-market-share/desktop/worldwidev)
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`tbrowser_market_shareŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a{Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1hbrowsersŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1gfirefoxŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1fchromeŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1fsafariŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dedgeŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1bieŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1eoperaŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1lmarket_shareŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfd8.61Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe69.55Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd8.36Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd4.12Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd2.76Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd2.43Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1g#5A69AFŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1g#579E65Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1g#F9C784Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1g#FC944AŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1g#F24C00Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1g#00B825Ÿ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a}Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakeclassŸ±Ç`a Ÿ±ÇbnckBubbleChartŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbfmh__init__Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dareaŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`nbubble_spacingŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbsdyU"""
        Setup for bubble collapse.

        Parameters
        ----------
        area : array-like
            Area of the bubbles.
        bubble_spacing : float, default: 0
            Minimal spacing between bubbles after collapsing.

        Notes
        -----
        If "area" is sorted, the results might look weird.
        """Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`dareaŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gasarrayŸ±Ç`a(Ÿ±Ç`dareaŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`arŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`dareaŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`nbubble_spacingŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`nbubble_spacingŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`donesŸ±Ç`a(Ÿ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`dareaŸ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`arŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dareaŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gmaxstepŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`cmaxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`nbubble_spacingŸ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`istep_distŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gmaxstepŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x+# calculate initial grid layout for bubblesŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`flengthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dceilŸ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`dgridŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Ç`flengthŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gmaxstepŸ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`bgxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bgyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hmeshgridŸ±Ç`a(Ÿ±Ç`dgridŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dgridŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bgxŸ±Çaoa.Ÿ±Ç`gflattenŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bgyŸ±Çaoa.Ÿ±Ç`gflattenŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a[Ÿ±Ç`a:Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a)Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ccomŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ncenter_of_massŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfncenter_of_massŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gaverageŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gweightsŸ±Çaoa=Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfocenter_distanceŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbubbleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gbubblesŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ehypotŸ±Ç`a(Ÿ±Ç`fbubbleŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`fbubbleŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfpoutline_distanceŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbubbleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gbubblesŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`ocenter_distanceŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ocenter_distanceŸ±Ç`a(Ÿ±Ç`fbubbleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gbubblesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`ocenter_distanceŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`fbubbleŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`b\
Ÿ±Ç`l            Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`nbubble_spacingŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfpcheck_collisionsŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbubbleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gbubblesŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`hdistanceŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`poutline_distanceŸ±Ç`a(Ÿ±Ç`fbubbleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gbubblesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±Ç`hdistanceŸ±Ç`a[Ÿ±Ç`hdistanceŸ±Ç`a Ÿ±Çaoa<Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnfmcollides_withŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fbubbleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gbubblesŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`hdistanceŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`poutline_distanceŸ±Ç`a(Ÿ±Ç`fbubbleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gbubblesŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`gidx_minŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`fargminŸ±Ç`a(Ÿ±Ç`hdistanceŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakfreturnŸ±Ç`a Ÿ±Ç`gidx_minŸ±Ç`a Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbnbdtypeŸ±Ç`a(Ÿ±Ç`gidx_minŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`gndarrayŸ±Ç`a Ÿ±ÇakdelseŸ±Ç`a Ÿ±Ç`a[Ÿ±Ç`gidx_minŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfhcollapseŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ln_iterationsŸ±Çaoa=Ÿ±Çbmib50Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbsdx≤"""
        Move bubbles to the center of mass.

        Parameters
        ----------
        n_iterations : int, default: 50
            Number of moves to perform.
        """Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`b_iŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Ç`ln_iterationsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`emovesŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`hrest_bubŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`fdeleteŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çbc1x1# try to move directly towards the center of massŸ±Ç`a
Ÿ±Ç`p                Ÿ±Çbc1x4# direction vector from bubble to the center of massŸ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`gdir_vecŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ccomŸ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çbc1x.# shorten direction vector to have length of 1Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`gdir_vecŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gdir_vecŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`gdir_vecŸ±Çaoa.Ÿ±Ç`cdotŸ±Ç`a(Ÿ±Ç`gdir_vecŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çbc1x# calculate new bubble positionŸ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`inew_pointŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`gdir_vecŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`istep_distŸ±Ç`a
Ÿ±Ç`p                Ÿ±Ç`jnew_bubbleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`inew_pointŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a:Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±Çbc1x6# check whether new bubble collides with other bubblesŸ±Ç`a
Ÿ±Ç`p                Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbowcnotŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`pcheck_collisionsŸ±Ç`a(Ÿ±Ç`jnew_bubbleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hrest_bubŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jnew_bubbleŸ±Ç`a
Ÿ±Ç`t                    Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ccomŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ncenter_of_massŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`emovesŸ±Ç`a Ÿ±Çaoa+Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Çbc1x3# try to move around a bubble that you collide withŸ±Ç`a
Ÿ±Ç`t                    Ÿ±Çbc1w# find colliding bubbleŸ±Ç`a
Ÿ±Ç`t                    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`icollidingŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`mcollides_withŸ±Ç`a(Ÿ±Ç`jnew_bubbleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hrest_bubŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Çbc1x# calculate direction vectorŸ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`gdir_vecŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`hrest_bubŸ±Ç`a[Ÿ±Ç`icollidingŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`gdir_vecŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`gdir_vecŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`dsqrtŸ±Ç`a(Ÿ±Ç`gdir_vecŸ±Çaoa.Ÿ±Ç`cdotŸ±Ç`a(Ÿ±Ç`gdir_vecŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Çbc1x# calculate orthogonal vectorŸ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`dorthŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`gdir_vecŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`gdir_vecŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Çbc1x# test which direction to goŸ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`jnew_point1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`dorthŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a
Ÿ±Ç`x&                                      Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`istep_distŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`jnew_point2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`a Ÿ±Ç`dorthŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a
Ÿ±Ç`x&                                      Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`istep_distŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`edist1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ocenter_distanceŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ccomŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`jnew_point1Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`edist2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ocenter_distanceŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ccomŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`jnew_point2Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`inew_pointŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jnew_point1Ÿ±Ç`a Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`edist1Ÿ±Ç`a Ÿ±Çaoa<Ÿ±Ç`a Ÿ±Ç`edist2Ÿ±Ç`a Ÿ±ÇakdelseŸ±Ç`a Ÿ±Ç`jnew_point2Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±Ç`jnew_bubbleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`fappendŸ±Ç`a(Ÿ±Ç`inew_pointŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a:Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`x                        Ÿ±ÇakbifŸ±Ç`a Ÿ±ÇbowcnotŸ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`pcheck_collisionsŸ±Ç`a(Ÿ±Ç`jnew_bubbleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hrest_bubŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`x                            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`a]Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`jnew_bubbleŸ±Ç`a
Ÿ±Ç`x                            Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ccomŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`ncenter_of_massŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`emovesŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa<Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`istep_distŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`istep_distŸ±Ç`a Ÿ±Çaoa/Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcdefŸ±Ç`a Ÿ±ÇbnfdplotŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇbsdxË"""
        Draw the bubble plot.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
        labels : list
            Labels of the bubbles.
        colors : list
            Colors of the bubbles.
        """Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`aiŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±ÇbnbclenŸ±Ç`a(Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`dcircŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`fCircleŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`p                Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`fcolorsŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iadd_patchŸ±Ç`a(Ÿ±Ç`dcircŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çaoa*Ÿ±ÇbbpdselfŸ±Çaoa.Ÿ±Ç`gbubblesŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`flabelsŸ±Ç`a[Ÿ±Ç`aiŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`t                    Ÿ±Ç`shorizontalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`lbubble_chartŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kBubbleChartŸ±Ç`a(Ÿ±Ç`dareaŸ±Çaoa=Ÿ±Ç`tbrowser_market_shareŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1lmarket_shareŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                           Ÿ±Ç`nbubble_spacingŸ±Çaoa=Ÿ±Çbmfc0.1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`lbubble_chartŸ±Çaoa.Ÿ±Ç`hcollapseŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`jsubplot_kwŸ±Çaoa=Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`faspectŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2eequalŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lbubble_chartŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`tbrowser_market_shareŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1hbrowsersŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`tbrowser_market_shareŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1ecolorŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`daxisŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2coffŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`erelimŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`nautoscale_viewŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1tBrowser market shareŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ