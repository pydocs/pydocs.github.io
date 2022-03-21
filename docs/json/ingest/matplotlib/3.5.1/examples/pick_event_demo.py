Ù¯‚Ù´ƒ™°Ù±‚bsdy	h"""
===============
Pick Event Demo
===============


You can enable picking by setting the "picker" property of an artist
(for example, a matplotlib Line2D, Text, Patch, Polygon, AxesImage,
etc...)

There are a variety of meanings of the picker property:

* *None* - picking is disabled for this artist (default)

* bool - if *True* then picking will be enabled and the artist will fire a pick
  event if the mouse event is over the artist.

  Setting ``pickradius`` will add an epsilon tolerance in points and the artist
  will fire off an event if its data is within epsilon of the mouse event.  For
  some artists like lines and patch collections, the artist may provide
  additional data to the pick event that is generated, for example, the indices
  of the data within epsilon of the pick event

* function - if picker is callable, it is a user supplied function which
  determines whether the artist is hit by the mouse event.

     hit, props = picker(artist, mouseevent)

  to determine the hit test.  If the mouse event is over the artist, return
  hit=True and props is a dictionary of properties you want added to the
  PickEvent attributes.

After you have enabled an artist for picking by setting the "picker"
property, you need to connect to the figure canvas pick_event to get
pick callbacks on mouse press events.  For example,

  def pick_handler(event):
      mouseevent = event.mouseevent
      artist = event.artist
      # now do something with this...


The pick event (matplotlib.backend_bases.PickEvent) which is passed to
your callback is always fired with two attributes:

  mouseevent - the mouse event that generate the pick event.  The
    mouse event in turn has attributes like x and y (the coordinates in
    display space, such as pixels from left, bottom) and xdata, ydata (the
    coords in data space).  Additionally, you can get information about
    which buttons were pressed, which keys were pressed, which Axes
    the mouse is over, etc.  See matplotlib.backend_bases.MouseEvent
    for details.

  artist - the matplotlib.artist that generated the pick event.

Additionally, certain artists like Line2D and PatchCollection may
attach additional meta data like the indices into the data that meet
the picker criteria (for example, all the points in the line that are within
the specified epsilon tolerance)

The examples below illustrate each of these methods.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnelinesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`fLine2DÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnngpatchesÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`iRectangleÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnndtextÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`dTextÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnneimageÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`iAxesImageÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bkndfromÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚bnna.Ù±‚bnnfrandomÙ±‚`a Ù±‚bknfimportÙ±‚`a Ù±‚`drandÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfkpick_simpleÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x,# simple picking, lines, rectangles and textÙ±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x#click on points, rectangles or textÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fpickerÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cax1Ù±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fylabelÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fpickerÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`dbboxÙ±‚aoa=Ù±‚bnbddictÙ±‚`a(Ù±‚`ifacecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1credÙ±‚bs1a'Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cax1Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`drandÙ±‚`a(Ù±‚bmic100Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fpickerÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`jpickradiusÙ±‚aoa=Ù±‚bmia5Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1t# pick the rectangleÙ±‚`a
Ù±‚`d    Ù±‚`cax2Ù±‚aoa.Ù±‚`cbarÙ±‚`a(Ù±‚bnberangeÙ±‚`a(Ù±‚bmib10Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`drandÙ±‚`a(Ù±‚bmib10Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fpickerÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚akcforÙ±‚`a Ù±‚`elabelÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`cax2Ù±‚aoa.Ù±‚`oget_xticklabelsÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`b  Ù±‚bc1x # make the xtick labels pickableÙ±‚`a
Ù±‚`h        Ù±‚`elabelÙ±‚aoa.Ù±‚`jset_pickerÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgonpick1Ù±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bnbjisinstanceÙ±‚`a(Ù±‚`eeventÙ±‚aoa.Ù±‚`fartistÙ±‚`a,Ù±‚`a Ù±‚`fLine2DÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`hthislineÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fartistÙ±‚`a
Ù±‚`l            Ù±‚`exdataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hthislineÙ±‚aoa.Ù±‚`iget_xdataÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`eydataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`hthislineÙ±‚aoa.Ù±‚`iget_ydataÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`cindÙ±‚`a
Ù±‚`l            Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1monpick1 line:Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`lcolumn_stackÙ±‚`a(Ù±‚`a[Ù±‚`exdataÙ±‚`a[Ù±‚`cindÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`eydataÙ±‚`a[Ù±‚`cindÙ±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akdelifÙ±‚`a Ù±‚bnbjisinstanceÙ±‚`a(Ù±‚`eeventÙ±‚aoa.Ù±‚`fartistÙ±‚`a,Ù±‚`a Ù±‚`iRectangleÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`epatchÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fartistÙ±‚`a
Ù±‚`l            Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1nonpick1 patch:Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`epatchÙ±‚aoa.Ù±‚`hget_pathÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akdelifÙ±‚`a Ù±‚bnbjisinstanceÙ±‚`a(Ù±‚`eeventÙ±‚aoa.Ù±‚`fartistÙ±‚`a,Ù±‚`a Ù±‚`dTextÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`dtextÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fartistÙ±‚`a
Ù±‚`l            Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1monpick1 text:Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`dtextÙ±‚aoa.Ù±‚`hget_textÙ±‚`a(Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jpick_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gonpick1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfopick_custom_hitÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x)# picking with a custom hit test functionÙ±‚`a
Ù±‚`d    Ù±‚bc1x?# you can define custom pickers by setting picker to a callableÙ±‚`a
Ù±‚`d    Ù±‚bc1x+# function.  The function has the signatureÙ±‚`a
Ù±‚`d    Ù±‚bc1a#Ù±‚`a
Ù±‚`d    Ù±‚bc1x(#  hit, props = func(artist, mouseevent)Ù±‚`a
Ù±‚`d    Ù±‚bc1a#Ù±‚`a
Ù±‚`d    Ù±‚bc1xD# to determine the hit test.  if the mouse event is over the artist,Ù±‚`a
Ù±‚`d    Ù±‚bc1x.# return hit=True and props is a dictionary ofÙ±‚`a
Ù±‚`d    Ù±‚bc1x7# properties you want added to the PickEvent attributesÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfkline_pickerÙ±‚`a(Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚`jmouseeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdxÒ"""
        Find the points within a certain distance from the mouseclick in
        data coords and attach some extra attributes, pickx and picky
        which are the data points that were picked.
        """Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`jmouseeventÙ±‚aoa.Ù±‚`exdataÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚bkceFalseÙ±‚`a,Ù±‚`a Ù±‚bnbddictÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`exdataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dlineÙ±‚aoa.Ù±‚`iget_xdataÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`eydataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dlineÙ±‚aoa.Ù±‚`iget_ydataÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`dmaxdÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.05Ù±‚`a
Ù±‚`h        Ù±‚`adÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`dsqrtÙ±‚`a(Ù±‚`a
Ù±‚`l            Ù±‚`a(Ù±‚`exdataÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`jmouseeventÙ±‚aoa.Ù±‚`exdataÙ±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`a(Ù±‚`eydataÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`jmouseeventÙ±‚aoa.Ù±‚`eydataÙ±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚`cindÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`gnonzeroÙ±‚`a(Ù±‚`adÙ±‚`a Ù±‚aoa<Ù±‚aoa=Ù±‚`a Ù±‚`dmaxdÙ±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bnbclenÙ±‚`a(Ù±‚`cindÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`epickxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`exdataÙ±‚`a[Ù±‚`cindÙ±‚`a]Ù±‚`a
Ù±‚`l            Ù±‚`epickyÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eydataÙ±‚`a[Ù±‚`cindÙ±‚`a]Ù±‚`a
Ù±‚`l            Ù±‚`epropsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bnbddictÙ±‚`a(Ù±‚`cindÙ±‚aoa=Ù±‚`cindÙ±‚`a,Ù±‚`a Ù±‚`epickxÙ±‚aoa=Ù±‚`epickxÙ±‚`a,Ù±‚`a Ù±‚`epickyÙ±‚aoa=Ù±‚`epickyÙ±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚bkcdTrueÙ±‚`a,Ù±‚`a Ù±‚`epropsÙ±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚bkceFalseÙ±‚`a,Ù±‚`a Ù±‚bnbddictÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgonpick2Ù±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1monpick2 line:Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`epickxÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`epickyÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1xcustom picker for line dataÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dlineÙ±‚`a,Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`drandÙ±‚`a(Ù±‚bmic100Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`drandÙ±‚`a(Ù±‚bmic100Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fpickerÙ±‚aoa=Ù±‚`kline_pickerÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jpick_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gonpick2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfqpick_scatter_plotÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1xJ# picking on a scatter plot (matplotlib.collections.RegularPolyCollection)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`acÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`drandÙ±‚`a(Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgonpick3Ù±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`cindÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`cindÙ±‚`a
Ù±‚`h        Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ponpick3 scatter:Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`cindÙ±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a[Ù±‚`cindÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a[Ù±‚`cindÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`gscatterÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚aoa*Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚`acÙ±‚`a,Ù±‚`a Ù±‚`fpickerÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jpick_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gonpick3Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfjpick_imageÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bc1x-# picking images (matplotlib.image.AxesImage)Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`drandÙ±‚`a(Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fextentÙ±‚aoa=Ù±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fpickerÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`drandÙ±‚`a(Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmib10Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fextentÙ±‚aoa=Ù±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fpickerÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`drandÙ±‚`a(Ù±‚bmib20Ù±‚`a,Ù±‚`a Ù±‚bmib25Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fextentÙ±‚aoa=Ù±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fpickerÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`drandÙ±‚`a(Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚bmib12Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fextentÙ±‚aoa=Ù±‚`a(Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`fpickerÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`dxlimÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dylimÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgonpick4Ù±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚`fartistÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fartistÙ±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚bnbjisinstanceÙ±‚`a(Ù±‚`fartistÙ±‚`a,Ù±‚`a Ù±‚`iAxesImageÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`bimÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fartistÙ±‚`a
Ù±‚`l            Ù±‚`aAÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bimÙ±‚aoa.Ù±‚`iget_arrayÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`l            Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1monpick4 imageÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`aAÙ±‚aoa.Ù±‚`eshapeÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jpick_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gonpick4Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akbifÙ±‚`a Ù±‚bvmh__name__Ù±‚`a Ù±‚aob==Ù±‚`a Ù±‚bs1a'Ù±‚bs1h__main__Ù±‚bs1a'Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`kpick_simpleÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`opick_custom_hitÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`qpick_scatter_plotÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`jpick_imageÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö