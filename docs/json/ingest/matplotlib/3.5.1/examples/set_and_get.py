�����������bsdy�"""
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
"""���`a
���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmfc1.0���`a,���`a ���bmfd0.01���`a)���`a
���`by1���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`ax���`a)���`a
���`by2���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia4���aoa*���`bnp���aoa.���`bpi���aoa*���`ax���`a)���`a
���`elines���`a ���aoa=���`a ���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`by1���`a,���`a ���`ax���`a,���`a ���`by2���`a)���`a
���`bl1���`a,���`a ���`bl2���`a ���aoa=���`a ���`elines���`a
���`cplt���aoa.���`dsetp���`a(���`elines���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1b--���bs1a'���`a)���`g       ���bc1t# set both to dashed���`a
���`cplt���aoa.���`dsetp���`a(���`bl1���`a,���`a ���`ilinewidth���aoa=���bmia2���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ar���bs1a'���`a)���`b  ���bc1x# line1 is thick and red���`a
���`cplt���aoa.���`dsetp���`a(���`bl2���`a,���`a ���`ilinewidth���aoa=���bmia1���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ag���bs1a'���`a)���`b  ���bc1x# line2 is thinner and green���`a
���`a
���`a
���bnbeprint���`a(���bs1a'���bs1lLine setters���bs1a'���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`bl1���`a)���`a
���bnbeprint���`a(���bs1a'���bs1lLine getters���bs1a'���`a)���`a
���`cplt���aoa.���`dgetp���`a(���`bl1���`a)���`a
���`a
���bnbeprint���`a(���bs1a'���bs1qRectangle setters���bs1a'���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`cplt���aoa.���`cgca���`a(���`a)���aoa.���`epatch���`a)���`a
���bnbeprint���`a(���bs1a'���bs1qRectangle getters���bs1a'���`a)���`a
���`cplt���aoa.���`dgetp���`a(���`cplt���aoa.���`cgca���`a(���`a)���aoa.���`epatch���`a)���`a
���`a
���`at���`a ���aoa=���`a ���`cplt���aoa.���`etitle���`a(���bs1a'���bs1fHi mom���bs1a'���`a)���`a
���bnbeprint���`a(���bs1a'���bs1lText setters���bs1a'���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`at���`a)���`a
���bnbeprint���`a(���bs1a'���bs1lText getters���bs1a'���`a)���`a
���`cplt���aoa.���`dgetp���`a(���`at���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�