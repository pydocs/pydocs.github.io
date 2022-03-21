������������bsdy�"""
==========
Color Demo
==========

Matplotlib recognizes the following formats to specify a color:

1) an RGB or RGBA tuple of float values in ``[0, 1]`` (e.g. ``(0.1, 0.2, 0.5)``
   or ``(0.1, 0.2, 0.5, 0.3)``).  RGBA is short for Red, Green, Blue, Alpha;
2) a hex RGB or RGBA string (e.g., ``'#0F0F0F'`` or ``'#0F0F0F0F'``);
3) a shorthand hex RGB or RGBA string, equivalent to the hex RGB or RGBA
   string obtained by duplicating each character, (e.g., ``'#abc'``, equivalent
   to ``'#aabbcc'``, or ``'#abcd'``, equivalent to ``'#aabbccdd'``);
4) a string representation of a float value in ``[0, 1]`` inclusive for gray
   level (e.g., ``'0.5'``);
5) a single letter string, i.e. one of
   ``{'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}``, which are short-hand notations
   for shades of blue, green, red, cyan, magenta, yellow, black, and white;
6) a X11/CSS4 ("html") color name, e.g. ``"blue"``;
7) a name from the `xkcd color survey <https://xkcd.com/color/rgb/>`__,
   prefixed with ``'xkcd:'`` (e.g., ``'xkcd:sky blue'``);
8) a "Cn" color spec, i.e. ``'C'`` followed by a number, which is an index into
   the default property cycle (:rc:`axes.prop_cycle`); the indexing is intended
   to occur at rendering time, and defaults to black if the cycle does not
   include color.
9) one of ``{'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
   'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'}`` which are
   the Tableau Colors from the 'tab10' categorical palette (which is the
   default color cycle);

For more information on colors in matplotlib see

* the :doc:`/tutorials/colors/colors` tutorial;
* the `matplotlib.colors` API;
* the :doc:`/gallery/color/named_colors` example.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfc0.0���`a,���`a ���bmfc2.0���`a,���`a ���bmic201���`a)���`a
���`as���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`at���`a)���`a
���`a
���bc1o# 1) RGB tuple:���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`ifacecolor���aoa=���`a(���bmfc.18���`a,���`a ���bmfc.31���`a,���`a ���bmfc.31���`a)���`a)���`a
���bc1p# 2) hex string:���`a
���`bax���aoa.���`mset_facecolor���`a(���bs1a'���bs1g#eafff5���bs1a'���`a)���`a
���bc1w# 3) gray level string:���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1vVoltage vs. time chart���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1c0.7���bs1a'���`a)���`a
���bc1x# 4) single letter color string���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1htime (s)���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ac���bs1a'���`a)���`a
���bc1s# 5) a named color:���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1lvoltage (mV)���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ipeachpuff���bs1a'���`a)���`a
���bc1x# 6) a named xkcd color:���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`as���`a,���`a ���bs1a'���bs1lxkcd:crimson���bs1a'���`a)���`a
���bc1q# 7) Cn notation:���`a
���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���bmfb.7���aoa*���`as���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC4���bs1a'���`a,���`a ���`ilinestyle���aoa=���bs1a'���bs1b--���bs1a'���`a)���`a
���bc1r# 8) tab notation:���`a
���`bax���aoa.���`ktick_params���`a(���`jlabelcolor���aoa=���bs1a'���bs1jtab:orange���bs1a'���`a)���`a
���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.colors`���`a
���bc1x"#    - `matplotlib.axes.Axes.plot`���`a
���bc1x+#    - `matplotlib.axes.Axes.set_facecolor`���`a
���bc1x'#    - `matplotlib.axes.Axes.set_title`���`a
���bc1x(#    - `matplotlib.axes.Axes.set_xlabel`���`a
���bc1x(#    - `matplotlib.axes.Axes.set_ylabel`���`a
���bc1x)#    - `matplotlib.axes.Axes.tick_params`���`a
`dNone�