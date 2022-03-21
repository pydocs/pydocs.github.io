������������bsdy�"""
====================
List of named colors
====================

This plots a list of the named colors supported in matplotlib. Note that
:ref:`xkcd colors <xkcd-colors>` are supported as well, but are not listed here
for brevity.

For more information on colors in matplotlib see

* the :doc:`/tutorials/colors/colors` tutorial;
* the `matplotlib.colors` API;
* the :doc:`/gallery/color/color_demo`.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`iRectangle���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���akbas���`a ���bnngmcolors���`a
���`a
���`a
���akcdef���`a ���bnfoplot_colortable���`a(���`fcolors���`a,���`a ���`etitle���`a,���`a ���`ksort_colors���aoa=���bkcdTrue���`a,���`a ���`iemptycols���aoa=���bmia0���`a)���`a:���`a
���`a
���`d    ���`jcell_width���`a ���aoa=���`a ���bmic212���`a
���`d    ���`kcell_height���`a ���aoa=���`a ���bmib22���`a
���`d    ���`lswatch_width���`a ���aoa=���`a ���bmib48���`a
���`d    ���`fmargin���`a ���aoa=���`a ���bmib12���`a
���`d    ���`itopmargin���`a ���aoa=���`a ���bmib40���`a
���`a
���`d    ���bc1x1# Sort colors by hue, saturation, value and name.���`a
���`d    ���akbif���`a ���`ksort_colors���`a ���bowbis���`a ���bkcdTrue���`a:���`a
���`h        ���`fby_hsv���`a ���aoa=���`a ���bnbfsorted���`a(���`a(���bnbetuple���`a(���`gmcolors���aoa.���`jrgb_to_hsv���`a(���`gmcolors���aoa.���`fto_rgb���`a(���`ecolor���`a)���`a)���`a)���`a,���`a
���`x                         ���`dname���`a)���`a
���`x                        ���akcfor���`a ���`dname���`a,���`a ���`ecolor���`a ���bowbin���`a ���`fcolors���aoa.���`eitems���`a(���`a)���`a)���`a
���`h        ���`enames���`a ���aoa=���`a ���`a[���`dname���`a ���akcfor���`a ���`chsv���`a,���`a ���`dname���`a ���bowbin���`a ���`fby_hsv���`a]���`a
���`d    ���akdelse���`a:���`a
���`h        ���`enames���`a ���aoa=���`a ���bnbdlist���`a(���`fcolors���`a)���`a
���`a
���`d    ���`an���`a ���aoa=���`a ���bnbclen���`a(���`enames���`a)���`a
���`d    ���`encols���`a ���aoa=���`a ���bmia4���`a ���aoa-���`a ���`iemptycols���`a
���`d    ���`enrows���`a ���aoa=���`a ���`an���`a ���aoa/���aoa/���`a ���`encols���`a ���aoa+���`a ���bnbcint���`a(���`an���`a ���aoa%���`a ���`encols���`a ���aoa>���`a ���bmia0���`a)���`a
���`a
���`d    ���`ewidth���`a ���aoa=���`a ���`jcell_width���`a ���aoa*���`a ���bmia4���`a ���aoa+���`a ���bmia2���`a ���aoa*���`a ���`fmargin���`a
���`d    ���`fheight���`a ���aoa=���`a ���`kcell_height���`a ���aoa*���`a ���`enrows���`a ���aoa+���`a ���`fmargin���`a ���aoa+���`a ���`itopmargin���`a
���`d    ���`cdpi���`a ���aoa=���`a ���bmib72���`a
���`a
���`d    ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���`ewidth���`a ���aoa/���`a ���`cdpi���`a,���`a ���`fheight���`a ���aoa/���`a ���`cdpi���`a)���`a,���`a ���`cdpi���aoa=���`cdpi���`a)���`a
���`d    ���`cfig���aoa.���`osubplots_adjust���`a(���`fmargin���aoa/���`ewidth���`a,���`a ���`fmargin���aoa/���`fheight���`a,���`a
���`x                        ���`a(���`ewidth���aoa-���`fmargin���`a)���aoa/���`ewidth���`a,���`a ���`a(���`fheight���aoa-���`itopmargin���`a)���aoa/���`fheight���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���`jcell_width���`a ���aoa*���`a ���bmia4���`a)���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���`kcell_height���`a ���aoa*���`a ���`a(���`enrows���aoa-���bmfc0.5���`a)���`a,���`a ���aoa-���`kcell_height���aoa/���bmfb2.���`a)���`a
���`d    ���`bax���aoa.���`eyaxis���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`d    ���`bax���aoa.���`exaxis���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`d    ���`bax���aoa.���`lset_axis_off���`a(���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���`etitle���`a,���`a ���`hfontsize���aoa=���bmib24���`a,���`a ���`cloc���aoa=���bs2a"���bs2dleft���bs2a"���`a,���`a ���`cpad���aoa=���bmib10���`a)���`a
���`a
���`d    ���akcfor���`a ���`ai���`a,���`a ���`dname���`a ���bowbin���`a ���bnbienumerate���`a(���`enames���`a)���`a:���`a
���`h        ���`crow���`a ���aoa=���`a ���`ai���`a ���aoa%���`a ���`enrows���`a
���`h        ���`ccol���`a ���aoa=���`a ���`ai���`a ���aoa/���aoa/���`a ���`enrows���`a
���`h        ���`ay���`a ���aoa=���`a ���`crow���`a ���aoa*���`a ���`kcell_height���`a
���`a
���`h        ���`nswatch_start_x���`a ���aoa=���`a ���`jcell_width���`a ���aoa*���`a ���`ccol���`a
���`h        ���`jtext_pos_x���`a ���aoa=���`a ���`jcell_width���`a ���aoa*���`a ���`ccol���`a ���aoa+���`a ���`lswatch_width���`a ���aoa+���`a ���bmia7���`a
���`a
���`h        ���`bax���aoa.���`dtext���`a(���`jtext_pos_x���`a,���`a ���`ay���`a,���`a ���`dname���`a,���`a ���`hfontsize���aoa=���bmib14���`a,���`a
���`p                ���`shorizontalalignment���aoa=���bs1a'���bs1dleft���bs1a'���`a,���`a
���`p                ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`a
���`h        ���`bax���aoa.���`iadd_patch���`a(���`a
���`l            ���`iRectangle���`a(���`bxy���aoa=���`a(���`nswatch_start_x���`a,���`a ���`ay���aoa-���bmia9���`a)���`a,���`a ���`ewidth���aoa=���`lswatch_width���`a,���`a
���`v                      ���`fheight���aoa=���bmib18���`a,���`a ���`ifacecolor���aoa=���`fcolors���`a[���`dname���`a]���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1c0.7���bs1a'���`a)���`a
���`h        ���`a)���`a
���`a
���`d    ���akfreturn���`a ���`cfig���`a
���`a
���`oplot_colortable���`a(���`gmcolors���aoa.���`kBASE_COLORS���`a,���`a ���bs2a"���bs2kBase Colors���bs2a"���`a,���`a
���`p                ���`ksort_colors���aoa=���bkceFalse���`a,���`a ���`iemptycols���aoa=���bmia1���`a)���`a
���`oplot_colortable���`a(���`gmcolors���aoa.���`nTABLEAU_COLORS���`a,���`a ���bs2a"���bs2oTableau Palette���bs2a"���`a,���`a
���`p                ���`ksort_colors���aoa=���bkceFalse���`a,���`a ���`iemptycols���aoa=���bmia2���`a)���`a
���`a
���bc1x%# sphinx_gallery_thumbnail_number = 3���`a
���`oplot_colortable���`a(���`gmcolors���aoa.���`kCSS4_COLORS���`a,���`a ���bs2a"���bs2jCSS Colors���bs2a"���`a)���`a
���`a
���bc1xF# Optionally plot the XKCD colors (Caution: will produce large figure)���`a
���bc1x@# xkcd_fig = plot_colortable(mcolors.XKCD_COLORS, "XKCD Colors")���`a
���bc1x%# xkcd_fig.savefig("XKCD_Colors.png")���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x#    - `matplotlib.colors`���`a
���bc1x%#    - `matplotlib.colors.rgb_to_hsv`���`a
���bc1x"#    - `matplotlib.colors.to_rgba`���`a
���bc1x1#    - `matplotlib.figure.Figure.get_size_inches`���`a
���bc1x1#    - `matplotlib.figure.Figure.subplots_adjust`���`a
���bc1x"#    - `matplotlib.axes.Axes.text`���`a
���bc1x%#    - `matplotlib.patches.Rectangle`���`a
`dNone�