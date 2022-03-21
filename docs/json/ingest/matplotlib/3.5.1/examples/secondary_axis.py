Ù¯‚Ù´ƒ™æÙ±‚bsdy×"""
==============
Secondary Axis
==============

Sometimes we want a secondary axis on a plot, for instance to convert
radians to degrees on the same plot.  We can do this by making a child
axes with only one axis visible via `.axes.Axes.secondary_xaxis` and
`.axes.Axes.secondary_yaxis`.  This secondary axis can have a different scale
than the main axis by providing both a forward and an inverse conversion
function in a tuple to the *functions* keyword argument:
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnhdatetimeÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnedatesÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnfmdatesÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnftickerÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`pAutoMinorLocatorÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmic360Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmic180Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1oangle [degrees]Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fsignalÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1iSine waveÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfgdeg2radÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmic180Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfgrad2degÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmic180Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`esecaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`osecondary_xaxisÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ifunctionsÙ±‚aoa=Ù±‚`a(Ù±‚`gdeg2radÙ±‚`a,Ù±‚`a Ù±‚`grad2degÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`esecaxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1kangle [rad]Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xK###########################################################################Ù±‚`a
Ù±‚bc1xC# Here is the case of converting from wavenumber to wavelength in aÙ±‚`a
Ù±‚bc1p# log-log scale.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1k# .. note::Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xJ#   In this case, the xscale of the parent is logarithmic, so the child isÙ±‚`a
Ù±‚bc1x#   made logarithmic as well.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmfd0.02Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmfd0.02Ù±‚`a)Ù±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚aoa*Ù±‚`a Ù±‚bmia2Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`floglogÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ff [Hz]Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1cPSDÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1oRandom spectrumÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfhone_overÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx,"""Vectorized 1/x, treating x==0 manually"""Ù±‚`a
Ù±‚`d    Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`earrayÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚aoa.Ù±‚`fastypeÙ±‚`a(Ù±‚bnbefloatÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`inear_zeroÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`giscloseÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`axÙ±‚`a[Ù±‚`inear_zeroÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cinfÙ±‚`a
Ù±‚`d    Ù±‚`axÙ±‚`a[Ù±‚aoa~Ù±‚`inear_zeroÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmia1Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`axÙ±‚`a[Ù±‚aoa~Ù±‚`inear_zeroÙ±‚`a]Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`axÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x'# the function "1/x" is its own inverseÙ±‚`a
Ù±‚`ginverseÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hone_overÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`esecaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`osecondary_xaxisÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ifunctionsÙ±‚aoa=Ù±‚`a(Ù±‚`hone_overÙ±‚`a,Ù±‚`a Ù±‚`ginverseÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`esecaxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jperiod [s]Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xK###########################################################################Ù±‚`a
Ù±‚bc1xH# Sometime we want to relate the axes in a transform that is ad-hoc fromÙ±‚`a
Ù±‚bc1xD# the data, and is derived empirically.  In that case we can set theÙ±‚`a
Ù±‚bc1xO# forward and inverse transforms functions to be linear interpolations from theÙ±‚`a
Ù±‚bc1x# one data set to the other.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1k# .. note::Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xG#   In order to properly handle the data margins, the mapping functionsÙ±‚`a
Ù±‚bc1xO#   (``forward`` and ``inverse`` in this example) need to be defined beyond theÙ±‚`a
Ù±‚bc1x#   nominal plot limits.Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xK#   In the specific case of the numpy linear interpolation, `numpy.interp`,Ù±‚`a
Ù±‚bc1xL#   this condition can be arbitrarily enforced by providing optional keywordÙ±‚`a
Ù±‚bc1xI#   arguments *left*, *right* such that values outside the data range areÙ±‚`a
Ù±‚bc1x(#   mapped well outside the plot limits.Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`exdataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmib11Ù±‚`a,Ù±‚`a Ù±‚bmfc0.4Ù±‚`a)Ù±‚`a
Ù±‚`eydataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`exdataÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eydataÙ±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1lPlotted dataÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`dxoldÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib11Ù±‚`a,Ù±‚`a Ù±‚bmfc0.2Ù±‚`a)Ù±‚`a
Ù±‚bc1xI# fake data set relating x coordinate to another data-derived coordinate.Ù±‚`a
Ù±‚bc1x'# xnew must be monotonic, so we sort...Ù±‚`a
Ù±‚`dxnewÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsortÙ±‚`a(Ù±‚bmib10Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`cexpÙ±‚`a(Ù±‚aoa-Ù±‚`dxoldÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`dxoldÙ±‚`a)Ù±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmia3Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`dxoldÙ±‚`a[Ù±‚bmia3Ù±‚`a:Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`dxnewÙ±‚`a[Ù±‚bmia3Ù±‚`a:Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1nTransform dataÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1eX [m]Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`flegendÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfgforwardÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`finterpÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`dxoldÙ±‚`a,Ù±‚`a Ù±‚`dxnewÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfginverseÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`finterpÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`dxnewÙ±‚`a,Ù±‚`a Ù±‚`dxoldÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`esecaxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`osecondary_xaxisÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ifunctionsÙ±‚aoa=Ù±‚`a(Ù±‚`gforwardÙ±‚`a,Ù±‚`a Ù±‚`ginverseÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`esecaxÙ±‚aoa.Ù±‚`exaxisÙ±‚aoa.Ù±‚`qset_minor_locatorÙ±‚`a(Ù±‚`pAutoMinorLocatorÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`esecaxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1c$X_Ù±‚bsig{other}Ù±‚bs1a$Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xK###########################################################################Ù±‚`a
Ù±‚bc1xG# A final example translates np.datetime64 to yearday on the x axis andÙ±‚`a
Ù±‚bc1xC# from Celsius to Fahrenheit on the y axis.  Note the addition of aÙ±‚`a
Ù±‚bc1x?# third y axis, and that it can be placed using a float for theÙ±‚`a
Ù±‚bc1s# location argumentÙ±‚`a
Ù±‚`a
Ù±‚`edatesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`hdatetimeÙ±‚`a(Ù±‚bmid2018Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`itimedeltaÙ±‚`a(Ù±‚`ehoursÙ±‚aoa=Ù±‚`akÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia6Ù±‚`a)Ù±‚`a
Ù±‚`i         Ù±‚akcforÙ±‚`a Ù±‚`akÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmic240Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`ktemperatureÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`erandnÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`edatesÙ±‚`a)Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmia4Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc6.7Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`rconstrained_layoutÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`edatesÙ±‚`a,Ù±‚`a Ù±‚`ktemperatureÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bsaarÙ±‚bs1a'Ù±‚bs1b$TÙ±‚bs1a\Ù±‚bs1g [^oC]$Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`fxticksÙ±‚`a(Ù±‚`hrotationÙ±‚aoa=Ù±‚bmib70Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfidate2ydayÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx:"""Convert matplotlib datenum to days since 2018-01-01."""Ù±‚`a
Ù±‚`d    Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`fmdatesÙ±‚aoa.Ù±‚`hdate2numÙ±‚`a(Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`hdatetimeÙ±‚`a(Ù±‚bmid2018Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`ayÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfiyday2dateÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdx@"""Return a matplotlib datenum for *x* days after 2018-01-01."""Ù±‚`a
Ù±‚`d    Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`fmdatesÙ±‚aoa.Ù±‚`hdate2numÙ±‚`a(Ù±‚`hdatetimeÙ±‚aoa.Ù±‚`hdatetimeÙ±‚`a(Ù±‚bmid2018Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`ayÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`gsecax_xÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`osecondary_xaxisÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ifunctionsÙ±‚aoa=Ù±‚`a(Ù±‚`idate2ydayÙ±‚`a,Ù±‚`a Ù±‚`iyday2dateÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`gsecax_xÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1kyday [2018]Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfucelsius_to_fahrenheitÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚bmfc1.8Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmib32Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfufahrenheit_to_celsiusÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmib32Ù±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfc1.8Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`gsecax_yÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`osecondary_yaxisÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚bs1a'Ù±‚bs1erightÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`ifunctionsÙ±‚aoa=Ù±‚`a(Ù±‚`ucelsius_to_fahrenheitÙ±‚`a,Ù±‚`a Ù±‚`ufahrenheit_to_celsiusÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`gsecax_yÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bsaarÙ±‚bs1a'Ù±‚bs1b$TÙ±‚bs1a\Ù±‚bs1g [^oF]$Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfrcelsius_to_anomalyÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`ktemperatureÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfranomaly_to_celsiusÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dmeanÙ±‚`a(Ù±‚`ktemperatureÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x"# use of a float for the position:Ù±‚`a
Ù±‚`hsecax_y2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`osecondary_yaxisÙ±‚`a(Ù±‚`a
Ù±‚`d    Ù±‚bmfc1.2Ù±‚`a,Ù±‚`a Ù±‚`ifunctionsÙ±‚aoa=Ù±‚`a(Ù±‚`rcelsius_to_anomalyÙ±‚`a,Ù±‚`a Ù±‚`ranomaly_to_celsiusÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`hsecax_y2Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bsaarÙ±‚bs1a'Ù±‚bs1e$T - Ù±‚bs1a\Ù±‚bs1hoverlineÙ±‚bsic{T}Ù±‚bs1a\Ù±‚bs1g [^oC]$Ù±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xM#############################################################################Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x# .. admonition:: ReferencesÙ±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1xN#    The use of the following functions, methods, classes and modules is shownÙ±‚`a
Ù±‚bc1u#    in this example:Ù±‚`a
Ù±‚bc1a#Ù±‚`a
Ù±‚bc1x-#    - `matplotlib.axes.Axes.secondary_xaxis`Ù±‚`a
Ù±‚bc1x-#    - `matplotlib.axes.Axes.secondary_yaxis`Ù±‚`a
`dNoneö