������������bsdy"""
============
Rainbow text
============

The example shows how to string together several text objects.

History
-------
On the matplotlib-users list back in February 2012, Gökhan Sever asked the
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
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���bknfimport���`a ���`hAffine2D���`a
���`a
���`a
���akcdef���`a ���bnflrainbow_text���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`gstrings���`a,���`a ���`fcolors���`a,���`a ���`korientation���aoa=���bs1a'���bs1jhorizontal���bs1a'���`a,���`a
���`q                 ���`bax���aoa=���bkcdNone���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`d    ���bsdy]"""
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
    """���`a
���`d    ���akbif���`a ���`bax���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`h        ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`cgca���`a(���`a)���`a
���`d    ���`at���`a ���aoa=���`a ���`bax���aoa.���`itransData���`a
���`d    ���`fcanvas���`a ���aoa=���`a ���`bax���aoa.���`ffigure���aoa.���`fcanvas���`a
���`a
���`d    ���akfassert���`a ���`korientation���`a ���bowbin���`a ���`a[���bs1a'���bs1jhorizontal���bs1a'���`a,���`a ���bs1a'���bs1hvertical���bs1a'���`a]���`a
���`d    ���akbif���`a ���`korientation���`a ���aob==���`a ���bs1a'���bs1hvertical���bs1a'���`a:���`a
���`h        ���`fkwargs���aoa.���`fupdate���`a(���`hrotation���aoa=���bmib90���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`a
���`d    ���akcfor���`a ���`as���`a,���`a ���`ac���`a ���bowbin���`a ���bnbczip���`a(���`gstrings���`a,���`a ���`fcolors���`a)���`a:���`a
���`h        ���`dtext���`a ���aoa=���`a ���`bax���aoa.���`dtext���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`as���`a ���aoa+���`a ���bs2a"���bs2a ���bs2a"���`a,���`a ���`ecolor���aoa=���`ac���`a,���`a ���`itransform���aoa=���`at���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`a
���`h        ���bc1x+# Need to draw to update the text position.���`a
���`h        ���`dtext���aoa.���`ddraw���`a(���`fcanvas���aoa.���`lget_renderer���`a(���`a)���`a)���`a
���`h        ���`bex���`a ���aoa=���`a ���`dtext���aoa.���`qget_window_extent���`a(���`a)���`a
���`h        ���akbif���`a ���`korientation���`a ���aob==���`a ���bs1a'���bs1jhorizontal���bs1a'���`a:���`a
���`l            ���`at���`a ���aoa=���`a ���`dtext���aoa.���`mget_transform���`a(���`a)���`a ���aoa+���`a ���`hAffine2D���`a(���`a)���aoa.���`itranslate���`a(���`bex���aoa.���`ewidth���`a,���`a ���bmia0���`a)���`a
���`h        ���akdelse���`a:���`a
���`l            ���`at���`a ���aoa=���`a ���`dtext���aoa.���`mget_transform���`a(���`a)���`a ���aoa+���`a ���`hAffine2D���`a(���`a)���aoa.���`itranslate���`a(���bmia0���`a,���`a ���`bex���aoa.���`fheight���`a)���`a
���`a
���`a
���`ewords���`a ���aoa=���`a ���bs2a"���bs2x all unicorns poop rainbows ! ! !���bs2a"���aoa.���`esplit���`a(���`a)���`a
���`fcolors���`a ���aoa=���`a ���`a[���bs1a'���bs1cred���bs1a'���`a,���`a ���bs1a'���bs1forange���bs1a'���`a,���`a ���bs1a'���bs1dgold���bs1a'���`a,���`a ���bs1a'���bs1ilawngreen���bs1a'���`a,���`a ���bs1a'���bs1mlightseagreen���bs1a'���`a,���`a ���bs1a'���bs1iroyalblue���bs1a'���`a,���`a
���`j          ���bs1a'���bs1jblueviolet���bs1a'���`a]���`a
���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`lrainbow_text���`a(���bmfc0.1���`a,���`a ���bmfd0.05���`a,���`a ���`ewords���`a,���`a ���`fcolors���`a,���`a ���`dsize���aoa=���bmib18���`a)���`a
���`lrainbow_text���`a(���bmfd0.05���`a,���`a ���bmfc0.1���`a,���`a ���`ewords���`a,���`a ���`fcolors���`a,���`a ���`korientation���aoa=���bs1a'���bs1hvertical���bs1a'���`a,���`a ���`dsize���aoa=���bmib18���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�