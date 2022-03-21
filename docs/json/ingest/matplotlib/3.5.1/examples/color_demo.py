ŸØÇÅŸ¥Éò˜Ÿ±Çbsdy∫"""
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
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑenumpyŸ†Ñenumpyf1.22.3fmoduleenumpyfmoduleıŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnnbnpŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`atŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`hlinspaceŸ±Ç`a(Ÿ±Çbmfc0.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc2.0Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmic201Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`asŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`csinŸ±Ç`a(Ÿ±Çbmia2Ÿ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`bnpŸ±Çaoa.Ÿ±Ç`bpiŸ±Ç`a Ÿ±Çaoa*Ÿ±Ç`a Ÿ±Ç`atŸ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1o# 1) RGB tuple:Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`baxŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Ç`ifacecolorŸ±Çaoa=Ÿ±Ç`a(Ÿ±Çbmfc.18Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc.31Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfc.31Ÿ±Ç`a)Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1p# 2) hex string:Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`mset_facecolorŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1g#eafff5Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1w# 3) gray level string:Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`iset_titleŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1vVoltage vs. time chartŸ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1c0.7Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x# 4) single letter color stringŸ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_xlabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1htime (s)Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1acŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1s# 5) a named color:Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`jset_ylabelŸ±Ç`a(Ÿ±Çbs1a'Ÿ±Çbs1lvoltage (mV)Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1ipeachpuffŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x# 6) a named xkcd color:Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`asŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbs1a'Ÿ±Çbs1lxkcd:crimsonŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1q# 7) Cn notation:Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`dplotŸ±Ç`a(Ÿ±Ç`atŸ±Ç`a,Ÿ±Ç`a Ÿ±Çbmfb.7Ÿ±Çaoa*Ÿ±Ç`asŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ecolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1bC4Ÿ±Çbs1a'Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ilinestyleŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1b--Ÿ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1r# 8) tab notation:Ÿ±Ç`a
Ÿ±Ç`baxŸ±Çaoa.Ÿ±Ç`ktick_paramsŸ±Ç`a(Ÿ±Ç`jlabelcolorŸ±Çaoa=Ÿ±Çbs1a'Ÿ±Çbs1jtab:orangeŸ±Çbs1a'Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Çbc1xM#############################################################################Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x# .. admonition:: ReferencesŸ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1xN#    The use of the following functions, methods, classes and modules is shownŸ±Ç`a
Ÿ±Çbc1u#    in this example:Ÿ±Ç`a
Ÿ±Çbc1a#Ÿ±Ç`a
Ÿ±Çbc1x#    - `matplotlib.colors`Ÿ±Ç`a
Ÿ±Çbc1x"#    - `matplotlib.axes.Axes.plot`Ÿ±Ç`a
Ÿ±Çbc1x+#    - `matplotlib.axes.Axes.set_facecolor`Ÿ±Ç`a
Ÿ±Çbc1x'#    - `matplotlib.axes.Axes.set_title`Ÿ±Ç`a
Ÿ±Çbc1x(#    - `matplotlib.axes.Axes.set_xlabel`Ÿ±Ç`a
Ÿ±Çbc1x(#    - `matplotlib.axes.Axes.set_ylabel`Ÿ±Ç`a
Ÿ±Çbc1x)#    - `matplotlib.axes.Axes.tick_params`Ÿ±Ç`a
`dNoneˆ