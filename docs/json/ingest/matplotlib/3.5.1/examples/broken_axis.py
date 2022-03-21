Ù¯‚Ù´ƒ™nÙ±‚bsdxo"""
===========
Broken Axis
===========

Broken axis example, where the y-axis will have a portion cut out.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cptsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmib30Ù±‚`a)Ù±‚aoa*Ù±‚bmfb.2Ù±‚`a
Ù±‚bc1xG# Now let's make two outlier points which are far away from everything.Ù±‚`a
Ù±‚`cptsÙ±‚`a[Ù±‚`a[Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmib14Ù±‚`a]Ù±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚aoa=Ù±‚`a Ù±‚bmfb.8Ù±‚`a
Ù±‚`a
Ù±‚bc1xB# If we were to simply plot pts, we'd lose most of the interestingÙ±‚`a
Ù±‚bc1xG# details due to the outliers. So let's 'break' or 'cut-out' the y-axisÙ±‚`a
Ù±‚bc1xH# into two portions - use the top (ax1) for the outliers, and the bottomÙ±‚`a
Ù±‚bc1x3# (ax2) for the details of the majority of our dataÙ±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`fsharexÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`osubplots_adjustÙ±‚`a(Ù±‚`fhspaceÙ±‚aoa=Ù±‚bmfd0.05Ù±‚`a)Ù±‚`b  Ù±‚bc1x# adjust space between axesÙ±‚`a
Ù±‚`a
Ù±‚bc1x!# plot the same data on both axesÙ±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`cptsÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`cptsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x<# zoom-in / limit the view to different portions of the dataÙ±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmfc.78Ù±‚`a,Ù±‚`a Ù±‚bmfb1.Ù±‚`a)Ù±‚`b  Ù±‚bc1o# outliers onlyÙ±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfc.22Ù±‚`a)Ù±‚`b  Ù±‚bc1r# most of the dataÙ±‚`a
Ù±‚`a
Ù±‚bc1x$# hide the spines between ax and ax2Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`fbottomÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`fspinesÙ±‚aoa.Ù±‚`ctopÙ±‚aoa.Ù±‚`kset_visibleÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`htick_topÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`ktick_paramsÙ±‚`a(Ù±‚`hlabeltopÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`b  Ù±‚bc1x"# don't put tick labels at the topÙ±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`ktick_bottomÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x4# Now, let's turn towards the cut-out slanted lines.Ù±‚`a
Ù±‚bc1xD# We create line objects in axes coordinates, in which (0,0), (0,1),Ù±‚`a
Ù±‚bc1x4# (1,0), and (1,1) are the four corners of the axes.Ù±‚`a
Ù±‚bc1xL# The slanted lines themselves are markers at those locations, such that theÙ±‚`a
Ù±‚bc1xL# lines keep their angle and position, independent of the axes size or scaleÙ±‚`a
Ù±‚bc1x'# Finally, we need to disable clipping.Ù±‚`a
Ù±‚`a
Ù±‚`adÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfb.5Ù±‚`b  Ù±‚bc1xA# proportion of vertical to horizontal extent of the slanted lineÙ±‚`a
Ù±‚`fkwargsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbddictÙ±‚`a(Ù±‚`fmarkerÙ±‚aoa=Ù±‚`a[Ù±‚`a(Ù±‚aoa-Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚aoa-Ù±‚`adÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`adÙ±‚`a)Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`jmarkersizeÙ±‚aoa=Ù±‚bmib12Ù±‚`a,Ù±‚`a
Ù±‚`n              Ù±‚`ilinestyleÙ±‚aoa=Ù±‚bs2a"Ù±‚bs2dnoneÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`cmecÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1akÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`cmewÙ±‚aoa=Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`gclip_onÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚aoa=Ù±‚`cax1Ù±‚aoa.Ù±‚`itransAxesÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`itransformÙ±‚aoa=Ù±‚`cax2Ù±‚aoa.Ù±‚`itransAxesÙ±‚`a,Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`fkwargsÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö