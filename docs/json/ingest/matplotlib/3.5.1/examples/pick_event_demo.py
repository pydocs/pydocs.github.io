������������bsdy	h"""
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
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnelines���`a ���bknfimport���`a ���`fLine2D���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`iRectangle���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndtext���`a ���bknfimport���`a ���`dText���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnneimage���`a ���bknfimport���`a ���`iAxesImage���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����bnna.���bnnfrandom���`a ���bknfimport���`a ���`drand���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���akcdef���`a ���bnfkpick_simple���`a(���`a)���`a:���`a
���`d    ���bc1x,# simple picking, lines, rectangles and text���`a
���`d    ���`cfig���`a,���`a ���`a(���`cax1���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`d    ���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1x#click on points, rectangles or text���bs1a'���`a,���`a ���`fpicker���aoa=���bkcdTrue���`a)���`a
���`d    ���`cax1���aoa.���`jset_ylabel���`a(���bs1a'���bs1fylabel���bs1a'���`a,���`a ���`fpicker���aoa=���bkcdTrue���`a,���`a ���`dbbox���aoa=���bnbddict���`a(���`ifacecolor���aoa=���bs1a'���bs1cred���bs1a'���`a)���`a)���`a
���`d    ���`dline���`a,���`a ���aoa=���`a ���`cax1���aoa.���`dplot���`a(���`drand���`a(���bmic100���`a)���`a,���`a ���bs1a'���bs1ao���bs1a'���`a,���`a ���`fpicker���aoa=���bkcdTrue���`a,���`a ���`jpickradius���aoa=���bmia5���`a)���`a
���`a
���`d    ���bc1t# pick the rectangle���`a
���`d    ���`cax2���aoa.���`cbar���`a(���bnberange���`a(���bmib10���`a)���`a,���`a ���`drand���`a(���bmib10���`a)���`a,���`a ���`fpicker���aoa=���bkcdTrue���`a)���`a
���`d    ���akcfor���`a ���`elabel���`a ���bowbin���`a ���`cax2���aoa.���`oget_xticklabels���`a(���`a)���`a:���`b  ���bc1x # make the xtick labels pickable���`a
���`h        ���`elabel���aoa.���`jset_picker���`a(���bkcdTrue���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfgonpick1���`a(���`eevent���`a)���`a:���`a
���`h        ���akbif���`a ���bnbjisinstance���`a(���`eevent���aoa.���`fartist���`a,���`a ���`fLine2D���`a)���`a:���`a
���`l            ���`hthisline���`a ���aoa=���`a ���`eevent���aoa.���`fartist���`a
���`l            ���`exdata���`a ���aoa=���`a ���`hthisline���aoa.���`iget_xdata���`a(���`a)���`a
���`l            ���`eydata���`a ���aoa=���`a ���`hthisline���aoa.���`iget_ydata���`a(���`a)���`a
���`l            ���`cind���`a ���aoa=���`a ���`eevent���aoa.���`cind���`a
���`l            ���bnbeprint���`a(���bs1a'���bs1monpick1 line:���bs1a'���`a,���`a ���`bnp���aoa.���`lcolumn_stack���`a(���`a[���`exdata���`a[���`cind���`a]���`a,���`a ���`eydata���`a[���`cind���`a]���`a]���`a)���`a)���`a
���`h        ���akdelif���`a ���bnbjisinstance���`a(���`eevent���aoa.���`fartist���`a,���`a ���`iRectangle���`a)���`a:���`a
���`l            ���`epatch���`a ���aoa=���`a ���`eevent���aoa.���`fartist���`a
���`l            ���bnbeprint���`a(���bs1a'���bs1nonpick1 patch:���bs1a'���`a,���`a ���`epatch���aoa.���`hget_path���`a(���`a)���`a)���`a
���`h        ���akdelif���`a ���bnbjisinstance���`a(���`eevent���aoa.���`fartist���`a,���`a ���`dText���`a)���`a:���`a
���`l            ���`dtext���`a ���aoa=���`a ���`eevent���aoa.���`fartist���`a
���`l            ���bnbeprint���`a(���bs1a'���bs1monpick1 text:���bs1a'���`a,���`a ���`dtext���aoa.���`hget_text���`a(���`a)���`a)���`a
���`a
���`d    ���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1jpick_event���bs1a'���`a,���`a ���`gonpick1���`a)���`a
���`a
���`a
���akcdef���`a ���bnfopick_custom_hit���`a(���`a)���`a:���`a
���`d    ���bc1x)# picking with a custom hit test function���`a
���`d    ���bc1x?# you can define custom pickers by setting picker to a callable���`a
���`d    ���bc1x+# function.  The function has the signature���`a
���`d    ���bc1a#���`a
���`d    ���bc1x(#  hit, props = func(artist, mouseevent)���`a
���`d    ���bc1a#���`a
���`d    ���bc1xD# to determine the hit test.  if the mouse event is over the artist,���`a
���`d    ���bc1x.# return hit=True and props is a dictionary of���`a
���`d    ���bc1x7# properties you want added to the PickEvent attributes���`a
���`a
���`d    ���akcdef���`a ���bnfkline_picker���`a(���`dline���`a,���`a ���`jmouseevent���`a)���`a:���`a
���`h        ���bsdx�"""
        Find the points within a certain distance from the mouseclick in
        data coords and attach some extra attributes, pickx and picky
        which are the data points that were picked.
        """���`a
���`h        ���akbif���`a ���`jmouseevent���aoa.���`exdata���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���akfreturn���`a ���bkceFalse���`a,���`a ���bnbddict���`a(���`a)���`a
���`h        ���`exdata���`a ���aoa=���`a ���`dline���aoa.���`iget_xdata���`a(���`a)���`a
���`h        ���`eydata���`a ���aoa=���`a ���`dline���aoa.���`iget_ydata���`a(���`a)���`a
���`h        ���`dmaxd���`a ���aoa=���`a ���bmfd0.05���`a
���`h        ���`ad���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`a
���`l            ���`a(���`exdata���`a ���aoa-���`a ���`jmouseevent���aoa.���`exdata���`a)���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`a(���`eydata���`a ���aoa-���`a ���`jmouseevent���aoa.���`eydata���`a)���aoa*���aoa*���bmia2���`a)���`a
���`a
���`h        ���`cind���`a,���`a ���aoa=���`a ���`bnp���aoa.���`gnonzero���`a(���`ad���`a ���aoa<���aoa=���`a ���`dmaxd���`a)���`a
���`h        ���akbif���`a ���bnbclen���`a(���`cind���`a)���`a:���`a
���`l            ���`epickx���`a ���aoa=���`a ���`exdata���`a[���`cind���`a]���`a
���`l            ���`epicky���`a ���aoa=���`a ���`eydata���`a[���`cind���`a]���`a
���`l            ���`eprops���`a ���aoa=���`a ���bnbddict���`a(���`cind���aoa=���`cind���`a,���`a ���`epickx���aoa=���`epickx���`a,���`a ���`epicky���aoa=���`epicky���`a)���`a
���`l            ���akfreturn���`a ���bkcdTrue���`a,���`a ���`eprops���`a
���`h        ���akdelse���`a:���`a
���`l            ���akfreturn���`a ���bkceFalse���`a,���`a ���bnbddict���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfgonpick2���`a(���`eevent���`a)���`a:���`a
���`h        ���bnbeprint���`a(���bs1a'���bs1monpick2 line:���bs1a'���`a,���`a ���`eevent���aoa.���`epickx���`a,���`a ���`eevent���aoa.���`epicky���`a)���`a
���`a
���`d    ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1xcustom picker for line data���bs1a'���`a)���`a
���`d    ���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`drand���`a(���bmic100���`a)���`a,���`a ���`drand���`a(���bmic100���`a)���`a,���`a ���bs1a'���bs1ao���bs1a'���`a,���`a ���`fpicker���aoa=���`kline_picker���`a)���`a
���`d    ���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1jpick_event���bs1a'���`a,���`a ���`gonpick2���`a)���`a
���`a
���`a
���akcdef���`a ���bnfqpick_scatter_plot���`a(���`a)���`a:���`a
���`d    ���bc1xJ# picking on a scatter plot (matplotlib.collections.RegularPolyCollection)���`a
���`a
���`d    ���`ax���`a,���`a ���`ay���`a,���`a ���`ac���`a,���`a ���`as���`a ���aoa=���`a ���`drand���`a(���bmia4���`a,���`a ���bmic100���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfgonpick3���`a(���`eevent���`a)���`a:���`a
���`h        ���`cind���`a ���aoa=���`a ���`eevent���aoa.���`cind���`a
���`h        ���bnbeprint���`a(���bs1a'���bs1ponpick3 scatter:���bs1a'���`a,���`a ���`cind���`a,���`a ���`ax���`a[���`cind���`a]���`a,���`a ���`ay���`a[���`cind���`a]���`a)���`a
���`a
���`d    ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`d    ���`bax���aoa.���`gscatter���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bmic100���aoa*���`as���`a,���`a ���`ac���`a,���`a ���`fpicker���aoa=���bkcdTrue���`a)���`a
���`d    ���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1jpick_event���bs1a'���`a,���`a ���`gonpick3���`a)���`a
���`a
���`a
���akcdef���`a ���bnfjpick_image���`a(���`a)���`a:���`a
���`d    ���bc1x-# picking images (matplotlib.image.AxesImage)���`a
���`d    ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`drand���`a(���bmib10���`a,���`a ���bmia5���`a)���`a,���`a ���`fextent���aoa=���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia1���`a,���`a ���bmia2���`a)���`a,���`a ���`fpicker���aoa=���bkcdTrue���`a)���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`drand���`a(���bmia5���`a,���`a ���bmib10���`a)���`a,���`a ���`fextent���aoa=���`a(���bmia3���`a,���`a ���bmia4���`a,���`a ���bmia1���`a,���`a ���bmia2���`a)���`a,���`a ���`fpicker���aoa=���bkcdTrue���`a)���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`drand���`a(���bmib20���`a,���`a ���bmib25���`a)���`a,���`a ���`fextent���aoa=���`a(���bmia1���`a,���`a ���bmia2���`a,���`a ���bmia3���`a,���`a ���bmia4���`a)���`a,���`a ���`fpicker���aoa=���bkcdTrue���`a)���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`drand���`a(���bmib30���`a,���`a ���bmib12���`a)���`a,���`a ���`fextent���aoa=���`a(���bmia3���`a,���`a ���bmia4���`a,���`a ���bmia3���`a,���`a ���bmia4���`a)���`a,���`a ���`fpicker���aoa=���bkcdTrue���`a)���`a
���`d    ���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmia5���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia0���`a,���`a ���bmia5���`a)���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfgonpick4���`a(���`eevent���`a)���`a:���`a
���`h        ���`fartist���`a ���aoa=���`a ���`eevent���aoa.���`fartist���`a
���`h        ���akbif���`a ���bnbjisinstance���`a(���`fartist���`a,���`a ���`iAxesImage���`a)���`a:���`a
���`l            ���`bim���`a ���aoa=���`a ���`fartist���`a
���`l            ���`aA���`a ���aoa=���`a ���`bim���aoa.���`iget_array���`a(���`a)���`a
���`l            ���bnbeprint���`a(���bs1a'���bs1monpick4 image���bs1a'���`a,���`a ���`aA���aoa.���`eshape���`a)���`a
���`a
���`d    ���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1jpick_event���bs1a'���`a,���`a ���`gonpick4���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs1a'���bs1h__main__���bs1a'���`a:���`a
���`d    ���`kpick_simple���`a(���`a)���`a
���`d    ���`opick_custom_hit���`a(���`a)���`a
���`d    ���`qpick_scatter_plot���`a(���`a)���`a
���`d    ���`jpick_image���`a(���`a)���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�