ŸØÇÅŸ¥Éô≠Ÿ±Çbsdy"""
============
Rainbow text
============

The example shows how to string together several text objects.

History
-------
On the matplotlib-users list back in February 2012, G√∂khan Sever asked the
following question:

  | Is there a way in matplotlib to partially specify the color of a string?
  |
  | Example:
  |
  | plt.ylabel("Today is cloudy.")
  |
  | How can I show "today" as red, "is" as green and "cloudy." as blue?
  |
  | Thanks.

The solution below is modified from Paul Ivanov's original answer.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnjtransformsŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`hAffine2DŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇakcdefŸ±Ç`a Ÿ±Çbnflrainbow_textŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`gstringsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`korientationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jhorizontalŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`q                 Ÿ±Ç`baxŸ±Çaoa=Ÿ±ÇbkcdNoneŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Çbsdy]"""
    Take a list of *strings* and *colors* and place them next to each
    other, with text strings[i] being shown in colors[i].

    Parameters
    ----------
    x, y : float
        Text position in data coordinates.
    strings : list of str
        The strings to draw.
    colors : list of color
        The colors to use.
    orientation : {'horizontal', 'vertical'}
    ax : Axes, optional
        The Axes to draw into. If None, the current axes will be used.
    **kwargs
        All other keyword arguments are passed to plt.text(), so you can
        set the font size, family, etc.
    """Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±ÇbowbisŸ±Ç`a Ÿ±ÇbkcdNoneŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`cgcaŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`itransDataŸ±Ç`a
Ÿ±Ç`d    Ÿ±Ç`fcanvasŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ffigureŸ±Çaoa.Ÿ±Ç`fcanvasŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakfassertŸ±Ç`a Ÿ±Ç`korientationŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1jhorizontalŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1hverticalŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`korientationŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1hverticalŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`fkwargsŸ±Çaoa.Ÿ±Ç`fupdateŸ±Ç`a(Ÿ±Ç`hrotationŸ±Çaoa=Ÿ±Çbmib90Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`qverticalalignmentŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1fbottomŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`d    Ÿ±ÇakcforŸ±Ç`a Ÿ±Ç`asŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`acŸ±Ç`a Ÿ±ÇbowbinŸ±Ç`a Ÿ±ÇbnbczipŸ±Ç`a(Ÿ±Ç`gstringsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Ç`a)Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`dtextŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dtextŸ±Ç`a(Ÿ±Ç`axŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ayŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2a Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Ç`acŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`itransformŸ±Çaoa=Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Çaoa*Ÿ±Ç`fkwargsŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Çbc1x+# Need to draw to update the text position.Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`ddrawŸ±Ç`a(Ÿ±Ç`fcanvasŸ±Çaoa.Ÿ±Ç`lget_rendererŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±Ç`bexŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`qget_window_extentŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakbifŸ±Ç`a Ÿ±Ç`korientationŸ±Ç`a Ÿ±Çaob==Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1jhorizontalŸ±Çbs1a'Ÿ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`mget_transformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`hAffine2DŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`itranslateŸ±Ç`a(Ÿ±Ç`bexŸ±Çaoa.Ÿ±Ç`ewidthŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`h        Ÿ±ÇakdelseŸ±Ç`a:Ÿ±Ç`a
Ÿ±Ç`l            Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`dtextŸ±Çaoa.Ÿ±Ç`mget_transformŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa+Ÿ±Ç`a Ÿ±Ç`hAffine2DŸ±Ç`a(Ÿ±Ç`a)Ÿ±Çaoa.Ÿ±Ç`itranslateŸ±Ç`a(Ÿ±Çbmia0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bexŸ±Çaoa.Ÿ±Ç`fheightŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`ewordsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Çbs2a"Ÿ±Çbs2x all unicorns poop rainbows ! ! !Ÿ±Çbs2a"Ÿ±Çaoa.Ÿ±Ç`esplitŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`fcolorsŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbs1a'Ÿ±Çbs1credŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1forangeŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1dgoldŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1ilawngreenŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1mlightseagreenŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1iroyalblueŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a
Ÿ±Ç`j          Ÿ±Çbs1a'Ÿ±Çbs1jbluevioletŸ±Çbs1a'Ÿ±Ç`a]Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ffigureŸ±Ç`a(Ÿ±Ç`gfigsizeŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmia6Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lrainbow_textŸ±Ç`a(Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewordsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib18Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`lrainbow_textŸ±Ç`a(Ÿ±Çbmfd0.05Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc0.1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ewordsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fcolorsŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`korientationŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1hverticalŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbmib18Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ