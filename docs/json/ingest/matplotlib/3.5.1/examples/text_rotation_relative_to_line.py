ŸØÇÅŸ¥Éò“Ÿ±Çbsdy¿"""
==============================
Text Rotation Relative To Line
==============================

Text objects in matplotlib are normally rotated with respect to the
screen coordinate system (i.e., 45 degrees rotation plots text along a
line that is in between horizontal and vertical no matter how the axes
are changed).  However, at times one wants to rotate text with respect
to something on the plot.  In this case, the correct angle won't be
the angle of that object in the plot coordinate system, but the angle
that that object APPEARS in the screen coordinate system.  This angle
can be determined automatically by setting the parameter
*transform_rotates_text*, as shown in the example below.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x!# Plot diagonal line (45 degrees)Ÿ±Ç`a
Ÿ±Ç`ahŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a,Ÿ±Ç`a Ÿ±ÇbnberangeŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib10Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xB# set limits so that it no longer looks on screen to be 45 degreesŸ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`hset_xlimŸ±Ç`a(Ÿ±Ç`a[Ÿ±Çaoa-Ÿ±Çbmib10Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmib20Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1x# Locations to plot textŸ±Ç`a
Ÿ±Ç`bl1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia1Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bl2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`earrayŸ±Ç`a(Ÿ±Ç`a(Ÿ±Çbmia5Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia5Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1n# Rotate angleŸ±Ç`a
Ÿ±Ç`eangleŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbmib45Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1k# Plot textŸ±Ç`a
Ÿ±Ç`cth1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`bl1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1xtext not rotated correctlyŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib16Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Ç`eangleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`mrotation_modeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fanchorŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cth2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Çaoa*Ÿ±Ç`bl2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1vtext rotated correctlyŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`hfontsizeŸ±Çaoa=Ÿ±Çbmib16Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Ç`eangleŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`mrotation_modeŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fanchorŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`n              Ÿ±Ç`vtransform_rotates_textŸ±Çaoa=Ÿ±ÇbkcdTrueŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ