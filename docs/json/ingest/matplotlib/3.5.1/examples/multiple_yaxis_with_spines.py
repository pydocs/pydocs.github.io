ŸØÇÅŸ¥Éô’Ÿ±ÇbsaarŸ±Çbsdy)"""
==========================
Multiple Yaxis With Spines
==========================

Create multiple y axes with a shared x axis. This is done by creating
a `~.axes.Axes.twinx` axes, turning all spines but the right one invisible
and offset its position using `~.spines.Spine.set_position`.

Note that this approach uses `matplotlib.axes.Axes` and their
`~matplotlib.spines.Spine`\s. An alternative approach for parasite
axes is shown in the :doc:`/gallery/axisartist/demo_parasite_axes` and
:doc:`/gallery/axisartist/demo_parasite_axes2` examples.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`osubplots_adjustŸ±Ç`a(Ÿ±Ç`erightŸ±Çaoa=Ÿ±Çbmfd0.75Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`etwin1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`etwinxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`etwin2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`etwinxŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xI# Offset the right spine of twin2.  The ticks and label have already beenŸ±Ç`a
Ÿ±Çbc1x%# placed on the right by twinx above.Ÿ±Ç`a
Ÿ±Ç`etwin2Ÿ±Çaoa.Ÿ±Ç`fspinesŸ±Çaoa.Ÿ±Ç`erightŸ±Çaoa.Ÿ±Ç`lset_positionŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2daxesŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc1.2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`bp1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2bb-Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2gDensityŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bp2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`etwin1Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2br-Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2kTemperatureŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bp3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`etwin2Ÿ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmib50Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib30Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib15Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2bg-Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`elabelŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2hVelocityŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`etwin1Ÿ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`etwin2Ÿ±Çaoa.Ÿ±Ç`hset_ylimŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib65Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2hDistanceŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2gDensityŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`etwin1Ÿ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2kTemperatureŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`etwin2Ÿ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2hVelocityŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`elabelŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Ç`bp1Ÿ±Çaoa.Ÿ±Ç`iget_colorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`etwin1Ÿ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`elabelŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Ç`bp2Ÿ±Çaoa.Ÿ±Ç`iget_colorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`etwin2Ÿ±Çaoa.Ÿ±Ç`eyaxisŸ±Çaoa.Ÿ±Ç`elabelŸ±Çaoa.Ÿ±Ç`iset_colorŸ±Ç`a(Ÿ±Ç`bp3Ÿ±Çaoa.Ÿ±Ç`iget_colorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ctkwŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmia4Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewidthŸ±Çaoa=Ÿ±Çbmfc1.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ayŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Ç`bp1Ÿ±Çaoa.Ÿ±Ç`iget_colorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`ctkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`etwin1Ÿ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ayŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Ç`bp2Ÿ±Çaoa.Ÿ±Ç`iget_colorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`ctkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`etwin2Ÿ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ayŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Çaoa=Ÿ±Ç`bp3Ÿ±Çaoa.Ÿ±Ç`iget_colorŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`ctkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`daxisŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`ctkwŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`flegendŸ±Ç`a(Ÿ±Ç`ghandlesŸ±Çaoa=Ÿ±Ç`a[Ÿ±Ç`bp1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bp3Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ