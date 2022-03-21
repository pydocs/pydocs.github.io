Ù¯‚Ù´ƒ™Ù±‚bsdyÀ"""
======================
Set and get properties
======================

The pyplot interface allows you to use ``setp`` and ``getp`` to
set and get object properties respectively, as well as to do
introspection on the object.

Setting with ``setp``
=====================

To set the linestyle of a line to be dashed, you use ``setp``::

  >>> line, = plt.plot([1, 2, 3])
  >>> plt.setp(line, linestyle='--')

If you want to know the valid types of arguments, you can provide the
name of the property you want to set without a value::

  >>> plt.setp(line, 'linestyle')
      linestyle: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}

If you want to see all the properties that can be set, and their
possible values, you can do::

    >>> plt.setp(line)

``setp`` operates on a single instance or a list of instances.  If you
are in query mode introspecting the possible values, only the first
instance in the sequence is used.  When actually setting values, all
the instances will be set.  For example, suppose you have a list of
two lines, the following will make both lines thicker and red::

    >>> x = np.arange(0, 1, 0.01)
    >>> y1 = np.sin(2*np.pi*x)
    >>> y2 = np.sin(4*np.pi*x)
    >>> lines = plt.plot(x, y1, x, y2)
    >>> plt.setp(lines, linewidth=2, color='r')


Getting with ``getp``
=====================

``getp`` returns the value of a given attribute.  You can use it to query
the value of a single attribute::

    >>> plt.getp(line, 'linewidth')
        0.5

or all the attribute/value pairs::

    >>> plt.getp(line)
        aa = True
        alpha = 1.0
        antialiased = True
        c = b
        clip_on = True
        color = b
        ... long listing skipped ...

Aliases
=======

To reduce keystrokes in interactive mode, a number of properties
have short aliases, e.g., 'lw' for 'linewidth' and 'mec' for
'markeredgecolor'.  When calling set or get in introspection mode,
these properties will be listed as 'fullname' or 'aliasname'.
"""Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`farangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmfc1.0Ù±‚`a,Ù±‚`a Ù±‚bmfd0.01Ù±‚`a)Ù±‚`a
Ù±‚`by1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia2Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`by2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`csinÙ±‚`a(Ù±‚bmia4Ù±‚aoa*Ù±‚`bnpÙ±‚aoa.Ù±‚`bpiÙ±‚aoa*Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`elinesÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`by1Ù±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`by2Ù±‚`a)Ù±‚`a
Ù±‚`bl1Ù±‚`a,Ù±‚`a Ù±‚`bl2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`elinesÙ±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dsetpÙ±‚`a(Ù±‚`elinesÙ±‚`a,Ù±‚`a Ù±‚`ilinestyleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b--Ù±‚bs1a'Ù±‚`a)Ù±‚`g       Ù±‚bc1t# set both to dashedÙ±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dsetpÙ±‚`a(Ù±‚`bl1Ù±‚`a,Ù±‚`a Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1arÙ±‚bs1a'Ù±‚`a)Ù±‚`b  Ù±‚bc1x# line1 is thick and redÙ±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dsetpÙ±‚`a(Ù±‚`bl2Ù±‚`a,Ù±‚`a Ù±‚`ilinewidthÙ±‚aoa=Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`ecolorÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1agÙ±‚bs1a'Ù±‚`a)Ù±‚`b  Ù±‚bc1x# line2 is thinner and greenÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lLine settersÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dsetpÙ±‚`a(Ù±‚`bl1Ù±‚`a)Ù±‚`a
Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lLine gettersÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dgetpÙ±‚`a(Ù±‚`bl1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1qRectangle settersÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dsetpÙ±‚`a(Ù±‚`cpltÙ±‚aoa.Ù±‚`cgcaÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`epatchÙ±‚`a)Ù±‚`a
Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1qRectangle gettersÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dgetpÙ±‚`a(Ù±‚`cpltÙ±‚aoa.Ù±‚`cgcaÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`epatchÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`atÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`etitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fHi momÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lText settersÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dsetpÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lText gettersÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dgetpÙ±‚`a(Ù±‚`atÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö