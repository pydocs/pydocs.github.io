ŸØÇÅŸ¥ÉôSŸ±ÇbsdyS"""
==============================
Figure size in different units
==============================

The native figure size unit in Matplotlib is inches, deriving from print
industry standards. However, users may need to specify their figures in other
units like centimeters or pixels. This example illustrates how to do this
efficiently.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x%# sphinx_gallery_thumbnail_number = 2Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`ktext_kwargsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±ÇbnbddictŸ±Ç`a(Ÿ±Ç`bhaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bvaŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fcenterŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib28Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1bC1Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xN##############################################################################Ÿ±Ç`a
Ÿ±Çbc1x!# Figure size in inches (default)Ÿ±Ç`a
Ÿ±Çbc1x!# -------------------------------Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1s6 inches x 2 inchesŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`ktext_kwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1x# Figure size in centimeterŸ±Ç`a
Ÿ±Çbc1x# -------------------------Ÿ±Ç`a
Ÿ±Çbc1xJ# Multiplying centimeter-based numbers with a conversion factor from cm toŸ±Ç`a
Ÿ±Çbc1xL# inches, gives the right numbers. Naming the conversion factor ``cm`` makesŸ±Ç`a
Ÿ±Çbc1xJ# the conversion almost look like appending a unit to the number, which isŸ±Ç`a
Ÿ±Çbc1r# nicely readable.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Ç`bcmŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Çaoa/Ÿ±Çbmfd2.54Ÿ±Ç`b  Ÿ±Çbc1w# centimeters in inchesŸ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmib15Ÿ±Çaoa*Ÿ±Ç`bcmŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Çaoa*Ÿ±Ç`bcmŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1j15cm x 5cmŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`ktext_kwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1v# Figure size in pixelŸ±Ç`a
Ÿ±Çbc1v# --------------------Ÿ±Ç`a
Ÿ±Çbc1x2# Similarly, one can use a conversion from pixels.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xE# Note that you could break this if you use `~.pyplot.savefig` with aŸ±Ç`a
Ÿ±Çbc1x# different explicit dpi value.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Ç`bpxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Çaoa/Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hrcParamsŸ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1jfigure.dpiŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`b  Ÿ±Çbc1q# pixel in inchesŸ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmic600Ÿ±Çaoa*Ÿ±Ç`bpxŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic200Ÿ±Çaoa*Ÿ±Ç`bpxŸ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1m600px x 200pxŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`ktext_kwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1xK# Quick interactive work is usually rendered to the screen, making pixels aŸ±Ç`a
Ÿ±Çbc1xI# good size of unit. But defining the conversion factor may feel a littleŸ±Ç`a
Ÿ±Çbc1x# tedious for quick iterations.Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xK# Because of the default ``rcParams['figure.dpi'] = 100``, one can mentallyŸ±Ç`a
Ÿ±Çbc1x,# divide the needed pixel value by 100 [#]_:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1m600px x 200pxŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`ktext_kwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1xM# .. [#] Unfortunately, this does not work well for the ``matplotlib inline``Ÿ±Ç`a
Ÿ±Çbc1xL#        backend in Jupyter because that backend uses a different default ofŸ±Ç`a
Ÿ±Çbc1xK#        ``rcParams['figure.dpi'] = 72``. Additionally, it saves the figureŸ±Ç`a
Ÿ±Çbc1xK#        with ``bbox_inches='tight'``, which crops the figure and makes theŸ±Ç`a
Ÿ±Çbc1x##        actual size unpredictable.Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x!#    - `matplotlib.pyplot.figure`Ÿ±Ç`a
Ÿ±Çbc1x##    - `matplotlib.pyplot.subplots`Ÿ±Ç`a
Ÿ±Çbc1x)#    - `matplotlib.pyplot.subplot_mosaic`Ÿ±Ç`a
`dNoneˆ