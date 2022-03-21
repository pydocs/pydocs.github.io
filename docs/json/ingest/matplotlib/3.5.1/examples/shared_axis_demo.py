ŸØÇÅŸ¥ÉòﬂŸ±Çbsdy
"""
===========
Shared Axis
===========

You can share the x or y axis limits for one axis with another by
passing an axes instance as a *sharex* or *sharey* keyword argument.

Changing the axis limits on one axes will be reflected automatically
in the other, and vice-versa, so when you navigate with the toolbar
the axes will follow each other on their shared axes.  Ditto for
changes in the axis scaling (e.g., log vs. linear).  However, it is
possible to have differences in tick labeling, e.g., you can selectively
turn off the tick labels on one axes.

The example below shows how to customize the tick labels on the
various axes.  Shared axes share the tick locator, tick formatter,
view limits, and transformation (e.g., log, linear).  But the ticklabels
themselves do not share properties.  This is a feature and not a bug,
because you may want to make the tick labels smaller on the upper
axes, e.g., in the example below.

If you want to turn off the ticklabels for a given axes (e.g., on
subplot(211) or subplot(212), you cannot do the standard trick::

   setp(ax2, xticklabels=[])

because this changes the tick Formatter, which is shared among all
axes.  But you can alter the visibility of the labels, which is a
property::

  setp(ax2.get_xticklabels(), visible=False)

"""Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`farangeŸ±Ç`a(Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc5.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfd0.01Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bs1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bs2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`cexpŸ±Ç`a(Ÿ±Çaoa-Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`bs3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Çbmia4Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cax1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`gsubplotŸ±Ç`a(Ÿ±Çbmic311Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bs1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilabelsizeŸ±Çaoa=Ÿ±Çbmia6Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1n# share x onlyŸ±Ç`a
Ÿ±Ç`cax2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`gsubplotŸ±Ç`a(Ÿ±Çbmic312Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fsharexŸ±Çaoa=Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bs2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x"# make these tick labels invisibleŸ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1axŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`klabelbottomŸ±Çaoa=Ÿ±ÇbkceFalseŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1o# share x and yŸ±Ç`a
Ÿ±Ç`cax3Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`gsubplotŸ±Ç`a(Ÿ±Çbmic313Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fsharexŸ±Çaoa=Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`fshareyŸ±Çaoa=Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`bs3Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dxlimŸ±Ç`a(Ÿ±Çbmfd0.01Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc5.0Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ