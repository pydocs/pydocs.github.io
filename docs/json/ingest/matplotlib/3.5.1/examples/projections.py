ŸØÇÅŸ¥ÉòÏŸ±Çbsdy`"""
========================
3D plot projection types
========================

Demonstrates the different camera projections for 3D plots, and the effects of
changing the focal length for a perspective projection. Note that Matplotlib
corrects for the 'zoom' effect of changing the focal length.

The default focal length of 1 corresponds to a Field of View (FOV) of 90 deg.
An increased focal length between 1 and infinity "flattens" the image, while a
decreased focal length between 1 and 0 exaggerates the perspective and gives
the image more apparent depth. In the limiting case, a focal length of
infinity corresponds to an orthographic projection after correction of the
zoom effect.

You can calculate focal length from a FOV via the equation:

.. mathmpl::

    1 / \tan (FOV / 2)

Or vice versa:

.. mathmpl::

    FOV = 2 * \atan (1 / focal length)

"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnngmplot3dŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`faxes3dŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`caxsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`jsubplot_kwŸ±Çaoa=Ÿ±Ç`a{Ÿ±Çbs1a'Ÿ±Çbs1jprojectionŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1b3dŸ±Çbs1a'Ÿ±Ç`a}Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1s# Get the test dataŸ±Ç`a
Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`faxes3dŸ±Çaoa.Ÿ±Ç`mget_test_dataŸ±Ç`a(Ÿ±Çbmfd0.05Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1o# Plot the dataŸ±Ç`a
Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`caxsŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`nplot_wireframeŸ±Ç`a(Ÿ±Ç`aXŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aYŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`aZŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`grstrideŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gcstrideŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x"# Set the orthographic projection.Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`mset_proj_typeŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1eorthoŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1m# FOV = 0 degŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia0Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2a'Ÿ±Çbs2eorthoŸ±Çbs2a'Ÿ±Çbseb\nŸ±Çbs2rfocal_length = ‚àûŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x!# Set the perspective projectionsŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`mset_proj_typeŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1eperspŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1n# FOV = 90 degŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2a'Ÿ±Çbs2eperspŸ±Çbs2a'Ÿ±Çbseb\nŸ±Çbs2xfocal_length = 1 (default)Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`mset_proj_typeŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1eperspŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`lfocal_lengthŸ±Çaoa=Ÿ±Çbmfc0.2Ÿ±Ç`a)Ÿ±Ç`b  Ÿ±Çbc1q# FOV = 157.4 degŸ±Ç`a
Ÿ±Ç`caxsŸ±Ç`a[Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2a'Ÿ±Çbs2eperspŸ±Çbs2a'Ÿ±Çbseb\nŸ±Çbs2rfocal_length = 0.2Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ