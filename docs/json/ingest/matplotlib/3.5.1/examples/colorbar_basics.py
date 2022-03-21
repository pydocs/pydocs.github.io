ŸØÇÅŸ¥ÉôhŸ±Çbsdx◊"""
========
Colorbar
========

Use `~.figure.Figure.colorbar` by specifying the mappable object (here
the `~.matplotlib.image.AxesImage` returned by `~.axes.Axes.imshow`)
and the axes to attach the colorbar to.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# setup some generic dataŸ±Ç`a
Ÿ±Ç`aNŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib37Ÿ±Ç`a
Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`emgridŸ±Ç`a[Ÿ±Ç`a:Ÿ±Ç`aNŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a:Ÿ±Ç`aNŸ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`ccosŸ±Ç`a(Ÿ±Ç`axŸ±Çaoa*Ÿ±Çbmfc0.2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Ç`ayŸ±Çaoa*Ÿ±Çbmfc0.3Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x9# mask out the negative and positive values, respectivelyŸ±Ç`a
Ÿ±Ç`dZposŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bmaŸ±Çaoa.Ÿ±Ç`kmasked_lessŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dZnegŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bmaŸ±Çaoa.Ÿ±Ç`nmasked_greaterŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax3Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmib13Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`encolsŸ±Çaoa=Ÿ±Çbmia3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x*# plot just the positive data and save theŸ±Ç`a
Ÿ±Çbc1x0# color "mappable" object returned by ax1.imshowŸ±Ç`a
Ÿ±Ç`cposŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`dZposŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1eBluesŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`minterpolationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dnoneŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x-# add the colorbar using the figure's method,Ÿ±Ç`a
Ÿ±Çbc1x0# telling which mappable we're talking about andŸ±Ç`a
Ÿ±Çbc1x%# which axes object it should be nearŸ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cposŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x/# repeat everything above for the negative dataŸ±Ç`a
Ÿ±Çbc1x:# you can specify location, anchor and shrink the colorbarŸ±Ç`a
Ÿ±Ç`cnegŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`dZnegŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fReds_rŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`minterpolationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dnoneŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cnegŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`cax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hlocationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1erightŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fanchorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.3Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshrinkŸ±Çaoa=Ÿ±Çbmfc0.7Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x8# Plot both positive and negative values between +/- 1.2Ÿ±Ç`a
Ÿ±Ç`opos_neg_clippedŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax3Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dcmapŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dRdBuŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvminŸ±Çaoa=Ÿ±Çaoa-Ÿ±Çbmfc1.2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dvmaxŸ±Çaoa=Ÿ±Çbmfc1.2Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`x                             Ÿ±Ç`minterpolationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dnoneŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x<# Add minorticks on the colorbar to make it easy to read theŸ±Ç`a
Ÿ±Çbc1x# values off the colorbar.Ÿ±Ç`a
Ÿ±Ç`dcbarŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`opos_neg_clippedŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa=Ÿ±Ç`cax3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fextendŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1dbothŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`dcbarŸ±Çaoa.Ÿ±Ç`mminorticks_onŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`Ÿ±Ç`a
Ÿ±Çbc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`Ÿ±Ç`a
Ÿ±Çbc1x3#    - `matplotlib.colorbar.Colorbar.minorticks_on`Ÿ±Ç`a
Ÿ±Çbc1x4#    - `matplotlib.colorbar.Colorbar.minorticks_off`Ÿ±Ç`a
`dNoneˆ