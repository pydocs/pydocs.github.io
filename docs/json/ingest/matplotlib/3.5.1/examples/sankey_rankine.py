ŸØÇÅŸ¥ÉôíŸ±Çbsdxî"""
===================
Rankine power cycle
===================

Demonstrate the Sankey class with a practical example of a Rankine power cycle.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfsankeyŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`fSankeyŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia9Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`kadd_subplotŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fxticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fyticksŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±Ç`etitleŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2x0Rankine Power Cycle: Example 8.6 from Moran and Ÿ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±Çbs2a"Ÿ±Çbs2gShapiroŸ±Çbseb\nŸ±Çbsed\x22Ÿ±Çbs2x+Fundamentals of Engineering Thermodynamics Ÿ±Çbs2a"Ÿ±Ç`a
Ÿ±Ç`u                     Ÿ±Çbs2a"Ÿ±Çbsed\x22Ÿ±Çbs2o, 6th ed., 2008Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dHdotŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmfg260.431Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmff35.078Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfg180.794Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfg221.115Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmff22.700Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbmfg142.361Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmff10.193Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmff10.210Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmff43.670Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmff44.312Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbmff68.631Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmff10.758Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmff10.758Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.017Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.642Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbmfg232.121Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmff44.559Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfg100.613Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfg132.168Ÿ±Ç`a]Ÿ±Ç`b  Ÿ±Çbc1d# MWŸ±Ç`a
Ÿ±Ç`fsankeyŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fSankeyŸ±Ç`a(Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`baxŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnbfformatŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbsid%.3GŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dunitŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1c MWŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cgapŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`escaleŸ±Çaoa=Ÿ±Çbmfc1.0Ÿ±Çaoa/Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbseb\nŸ±Çbseb\nŸ±Çbs1fPump 1Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Çbmib90Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1g#37c959Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmib13Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia6Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia7Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1kShaft powerŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`kpathlengthsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfc0.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.883Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbseb\nŸ±Çbseb\nŸ±Çbs1dOpenŸ±Çbseb\nŸ±Çbs1fheaterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1g#37c959Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmib11Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia7Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia8Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`kpathlengthsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd1.93Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`epriorŸ±Çaoa=Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gconnectŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbseb\nŸ±Çbseb\nŸ±Çbs1fPump 2Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1g#37c959Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmib14Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia8Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia9Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1kShaft powerŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`kpathlengthsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfc0.4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`epriorŸ±Çaoa=Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gconnectŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fClosedŸ±Çbseb\nŸ±Çbs1fheaterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ktrunklengthŸ±Çaoa=Ÿ±Çbmfe2.914Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bfcŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1g#37c959Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia9Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmib11Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmib10Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`kpathlengthsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe1.543Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`epriorŸ±Çaoa=Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gconnectŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dTrapŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1g#37c959Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ktrunklengthŸ±Çaoa=Ÿ±Çbmfe5.102Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmib11Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmib12Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbseb\nŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`kpathlengthsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfc1.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd1.01Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`epriorŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gconnectŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eSteamŸ±Çbseb\nŸ±Çbs1igeneratorŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1g#ff5555Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmib15Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmib10Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1iHeat rateŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`kpathlengthsŸ±Çaoa=Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`epriorŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gconnectŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbseb\nŸ±Çbseb\nŸ±Çbseb\nŸ±Çbs1iTurbine 1Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1g#37c959Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmib16Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`kpathlengthsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.153Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe1.543Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`epriorŸ±Çaoa=Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gconnectŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbseb\nŸ±Çbseb\nŸ±Çbseb\nŸ±Çbs1fReheatŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1g#37c959Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`kpathlengthsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfe0.725Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`epriorŸ±Çaoa=Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gconnectŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1iTurbine 2Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ktrunklengthŸ±Çaoa=Ÿ±Çbmfe3.212Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1g#37c959Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmib16Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia5Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmib17Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1kShaft powerŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1kShaft powerŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`kpathlengthsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfe0.751Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.15Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd1.93Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`epriorŸ±Çaoa=Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gconnectŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`caddŸ±Ç`a(Ÿ±Ç`jpatchlabelŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1iCondenserŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1g#58b1faŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ktrunklengthŸ±Çaoa=Ÿ±Çbmfe1.764Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`eflowsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia5Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmib18Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa-Ÿ±Ç`dHdotŸ±Ç`a[Ÿ±Çbmia6Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`flabelsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1iHeat rateŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`kpathlengthsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çbmfd0.45Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.25Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfe0.883Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`k           Ÿ±Ç`lorientationsŸ±Çaoa=Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`epriorŸ±Çaoa=Ÿ±Çbmia8Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gconnectŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`hdiagramsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`fsankeyŸ±Çaoa.Ÿ±Ç`ffinishŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`gdiagramŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`hdiagramsŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gdiagramŸ±Çaoa.Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`nset_fontweightŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1dboldŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`gdiagramŸ±Çaoa.Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`lset_fontsizeŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1b10Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`dtextŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`gdiagramŸ±Çaoa.Ÿ±Ç`etextsŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`lset_fontsizeŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1b10Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1xI# Notice that the explicit connections are handled automatically, but theŸ±Ç`a
Ÿ±Çbc1xK# implicit ones currently are not.  The lengths of the paths and the trunksŸ±Ç`a
Ÿ±Çbc1x6# must be adjusted manually, and that is a bit tricky.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.sankey`Ÿ±Ç`a
Ÿ±Çbc1x!#    - `matplotlib.sankey.Sankey`Ÿ±Ç`a
Ÿ±Çbc1x%#    - `matplotlib.sankey.Sankey.add`Ÿ±Ç`a
Ÿ±Çbc1x(#    - `matplotlib.sankey.Sankey.finish`Ÿ±Ç`a
`dNoneˆ