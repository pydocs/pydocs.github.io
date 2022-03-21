��������/���bsdx�"""
======================
Style sheets reference
======================

This script demonstrates the different available style sheets on a
common set of example plots: scatter plot, image, bar graph, patches,
line plot and histogram,

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���akcdef���`a ���bnflplot_scatter���`a(���`bax���`a,���`a ���`dprng���`a,���`a ���`jnb_samples���aoa=���bmic100���`a)���`a:���`a
���`d    ���bsds"""Scatter plot."""���`a
���`d    ���akcfor���`a ���`bmu���`a,���`a ���`esigma���`a,���`a ���`fmarker���`a ���bowbin���`a ���`a[���`a(���aoa-���bmfb.5���`a,���`a ���bmfd0.75���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a,���`a ���`a(���bmfd0.75���`a,���`a ���bmfb1.���`a,���`a ���bs1a'���bs1as���bs1a'���`a)���`a]���`a:���`a
���`h        ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`dprng���aoa.���`fnormal���`a(���`cloc���aoa=���`bmu���`a,���`a ���`escale���aoa=���`esigma���`a,���`a ���`dsize���aoa=���`a(���bmia2���`a,���`a ���`jnb_samples���`a)���`a)���`a
���`h        ���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`bls���aoa=���bs1a'���bs1dnone���bs1a'���`a,���`a ���`fmarker���aoa=���`fmarker���`a)���`a
���`d    ���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1gX-label���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1jAxes title���bs1a'���`a)���`a
���`d    ���akfreturn���`a ���`bax���`a
���`a
���`a
���akcdef���`a ���bnfxplot_colored_sinusoidal_lines���`a(���`bax���`a)���`a:���`a
���`d    ���bsdxH"""Plot sinusoidal lines with colors following the style color cycle."""���`a
���`d    ���`aL���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a
���`d    ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���`aL���`a)���`a
���`d    ���`inb_colors���`a ���aoa=���`a ���bnbclen���`a(���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1oaxes.prop_cycle���bs1a'���`a]���`a)���`a
���`d    ���`eshift���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���`aL���`a,���`a ���`inb_colors���`a,���`a ���`hendpoint���aoa=���bkceFalse���`a)���`a
���`d    ���akcfor���`a ���`as���`a ���bowbin���`a ���`eshift���`a:���`a
���`h        ���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a ���aoa+���`a ���`as���`a)���`a,���`a ���bs1a'���bs1a-���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���`a[���`ax���`a[���bmia0���`a]���`a,���`a ���`ax���`a[���aoa-���bmia1���`a]���`a]���`a)���`a
���`d    ���akfreturn���`a ���`bax���`a
���`a
���`a
���akcdef���`a ���bnfoplot_bar_graphs���`a(���`bax���`a,���`a ���`dprng���`a,���`a ���`imin_value���aoa=���bmia5���`a,���`a ���`imax_value���aoa=���bmib25���`a,���`a ���`jnb_samples���aoa=���bmia5���`a)���`a:���`a
���`d    ���bsdxF"""Plot two bar graphs side by side, with letters as x-tick labels."""���`a
���`d    ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���`jnb_samples���`a)���`a
���`d    ���`bya���`a,���`a ���`byb���`a ���aoa=���`a ���`dprng���aoa.���`grandint���`a(���`imin_value���`a,���`a ���`imax_value���`a,���`a ���`dsize���aoa=���`a(���bmia2���`a,���`a ���`jnb_samples���`a)���`a)���`a
���`d    ���`ewidth���`a ���aoa=���`a ���bmfd0.25���`a
���`d    ���`bax���aoa.���`cbar���`a(���`ax���`a,���`a ���`bya���`a,���`a ���`ewidth���`a)���`a
���`d    ���`bax���aoa.���`cbar���`a(���`ax���`a ���aoa+���`a ���`ewidth���`a,���`a ���`byb���`a,���`a ���`ewidth���`a,���`a ���`ecolor���aoa=���bs1a'���bs1bC2���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`jset_xticks���`a(���`ax���`a ���aoa+���`a ���`ewidth���`a,���`a ���`flabels���aoa=���`a[���bs1a'���bs1aa���bs1a'���`a,���`a ���bs1a'���bs1ab���bs1a'���`a,���`a ���bs1a'���bs1ac���bs1a'���`a,���`a ���bs1a'���bs1ad���bs1a'���`a,���`a ���bs1a'���bs1ae���bs1a'���`a]���`a)���`a
���`d    ���akfreturn���`a ���`bax���`a
���`a
���`a
���akcdef���`a ���bnftplot_colored_circles���`a(���`bax���`a,���`a ���`dprng���`a,���`a ���`jnb_samples���aoa=���bmib15���`a)���`a:���`a
���`d    ���bsdx�"""
    Plot circle patches.

    NB: draws a fixed amount of samples, rather than using the length of
    the color cycle, because different styles may have different numbers
    of colors.
    """���`a
���`d    ���akcfor���`a ���`hsty_dict���`a,���`a ���`aj���`a ���bowbin���`a ���bnbczip���`a(���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1oaxes.prop_cycle���bs1a'���`a]���`a,���`a ���bnberange���`a(���`jnb_samples���`a)���`a)���`a:���`a
���`h        ���`bax���aoa.���`iadd_patch���`a(���`cplt���aoa.���`fCircle���`a(���`dprng���aoa.���`fnormal���`a(���`escale���aoa=���bmia3���`a,���`a ���`dsize���aoa=���bmia2���`a)���`a,���`a
���`x                                 ���`fradius���aoa=���bmfc1.0���`a,���`a ���`ecolor���aoa=���`hsty_dict���`a[���bs1a'���bs1ecolor���bs1a'���`a]���`a)���`a)���`a
���`d    ���bc1xF# Force the limits to be the same across the styles (because different���`a
���`d    ���bc1x9# styles may have different numbers of available colors).���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���`a[���aoa-���bmia4���`a,���`a ���bmia8���`a]���`a)���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���`a[���aoa-���bmia5���`a,���`a ���bmia6���`a]���`a)���`a
���`d    ���`bax���aoa.���`jset_aspect���`a(���bs1a'���bs1eequal���bs1a'���`a,���`a ���`jadjustable���aoa=���bs1a'���bs1cbox���bs1a'���`a)���`b  ���bc1x# to plot circles as circles���`a
���`d    ���akfreturn���`a ���`bax���`a
���`a
���`a
���akcdef���`a ���bnftplot_image_and_patch���`a(���`bax���`a,���`a ���`dprng���`a,���`a ���`dsize���aoa=���`a(���bmib20���`a,���`a ���bmib20���`a)���`a)���`a:���`a
���`d    ���bsdxH"""Plot an image with random values and superimpose a circular patch."""���`a
���`d    ���`fvalues���`a ���aoa=���`a ���`dprng���aoa.���`mrandom_sample���`a(���`dsize���aoa=���`dsize���`a)���`a
���`d    ���`bax���aoa.���`fimshow���`a(���`fvalues���`a,���`a ���`minterpolation���aoa=���bs1a'���bs1dnone���bs1a'���`a)���`a
���`d    ���`ac���`a ���aoa=���`a ���`cplt���aoa.���`fCircle���`a(���`a(���bmia5���`a,���`a ���bmia5���`a)���`a,���`a ���`fradius���aoa=���bmia5���`a,���`a ���`elabel���aoa=���bs1a'���bs1epatch���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`iadd_patch���`a(���`ac���`a)���`a
���`d    ���bc1n# Remove ticks���`a
���`d    ���`bax���aoa.���`jset_xticks���`a(���`a[���`a]���`a)���`a
���`d    ���`bax���aoa.���`jset_yticks���`a(���`a[���`a]���`a)���`a
���`a
���`a
���akcdef���`a ���bnfoplot_histograms���`a(���`bax���`a,���`a ���`dprng���`a,���`a ���`jnb_samples���aoa=���bmie10000���`a)���`a:���`a
���`d    ���bsdx."""Plot 4 histograms and a text annotation."""���`a
���`d    ���`fparams���`a ���aoa=���`a ���`a(���`a(���bmib10���`a,���`a ���bmib10���`a)���`a,���`a ���`a(���bmia4���`a,���`a ���bmib12���`a)���`a,���`a ���`a(���bmib50���`a,���`a ���bmib12���`a)���`a,���`a ���`a(���bmia6���`a,���`a ���bmib55���`a)���`a)���`a
���`d    ���akcfor���`a ���`aa���`a,���`a ���`ab���`a ���bowbin���`a ���`fparams���`a:���`a
���`h        ���`fvalues���`a ���aoa=���`a ���`dprng���aoa.���`dbeta���`a(���`aa���`a,���`a ���`ab���`a,���`a ���`dsize���aoa=���`jnb_samples���`a)���`a
���`h        ���`bax���aoa.���`dhist���`a(���`fvalues���`a,���`a ���`hhisttype���aoa=���bs2a"���bs2jstepfilled���bs2a"���`a,���`a ���`dbins���aoa=���bmib30���`a,���`a
���`p                ���`ealpha���aoa=���bmfc0.8���`a,���`a ���`gdensity���aoa=���bkcdTrue���`a)���`a
���`d    ���bc1x# Add a small annotation.���`a
���`d    ���`bax���aoa.���`hannotate���`a(���bs1a'���bs1jAnnotation���bs1a'���`a,���`a ���`bxy���aoa=���`a(���bmfd0.25���`a,���`a ���bmfd4.25���`a)���`a,���`a
���`p                ���`fxytext���aoa=���`a(���bmfc0.9���`a,���`a ���bmfc0.9���`a)���`a,���`a ���`jtextcoords���aoa=���`bax���aoa.���`itransAxes���`a,���`a
���`p                ���`bva���aoa=���bs2a"���bs2ctop���bs2a"���`a,���`a ���`bha���aoa=���bs2a"���bs2eright���bs2a"���`a,���`a
���`p                ���`dbbox���aoa=���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2eround���bs2a"���`a,���`a ���`ealpha���aoa=���bmfc0.2���`a)���`a,���`a
���`p                ���`jarrowprops���aoa=���bnbddict���`a(���`a
���`x                          ���`jarrowstyle���aoa=���bs2a"���bs2b->���bs2a"���`a,���`a
���`x                          ���`oconnectionstyle���aoa=���bs2a"���bs2x!angle,angleA=-95,angleB=35,rad=10���bs2a"���`a)���`a,���`a
���`p                ���`a)���`a
���`d    ���akfreturn���`a ���`bax���`a
���`a
���`a
���akcdef���`a ���bnfkplot_figure���`a(���`kstyle_label���aoa=���bs2a"���bs2a"���`a)���`a:���`a
���`d    ���bsdxA"""Setup and plot the demonstration figure with a given style."""���`a
���`d    ���bc1xG# Use a dedicated RandomState instance to draw the same "random" values���`a
���`d    ���bc1x# across the different figures.���`a
���`d    ���`dprng���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`kRandomState���`a(���bmih96917002���`a)���`a
���`a
���`d    ���bc1xH# Tweak the figure size to be better suited for a row of numerous plots:���`a
���`d    ���bc1xI# double the width and halve the height. NB: use relative changes because���`a
���`d    ���bc1xD# some styles may have a figure size different from the default one.���`a
���`d    ���`a(���`ifig_width���`a,���`a ���`jfig_height���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1nfigure.figsize���bs1a'���`a]���`a
���`d    ���`hfig_size���`a ���aoa=���`a ���`a[���`ifig_width���`a ���aoa*���`a ���bmia2���`a,���`a ���`jfig_height���`a ���aoa/���`a ���bmia2���`a]���`a
���`a
���`d    ���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`encols���aoa=���bmia6���`a,���`a ���`enrows���aoa=���bmia1���`a,���`a ���`cnum���aoa=���`kstyle_label���`a,���`a
���`x                            ���`gfigsize���aoa=���`hfig_size���`a,���`a ���`gsqueeze���aoa=���bkcdTrue���`a)���`a
���`d    ���`caxs���`a[���bmia0���`a]���aoa.���`jset_ylabel���`a(���`kstyle_label���`a)���`a
���`a
���`d    ���`lplot_scatter���`a(���`caxs���`a[���bmia0���`a]���`a,���`a ���`dprng���`a)���`a
���`d    ���`tplot_image_and_patch���`a(���`caxs���`a[���bmia1���`a]���`a,���`a ���`dprng���`a)���`a
���`d    ���`oplot_bar_graphs���`a(���`caxs���`a[���bmia2���`a]���`a,���`a ���`dprng���`a)���`a
���`d    ���`tplot_colored_circles���`a(���`caxs���`a[���bmia3���`a]���`a,���`a ���`dprng���`a)���`a
���`d    ���`xplot_colored_sinusoidal_lines���`a(���`caxs���`a[���bmia4���`a]���`a)���`a
���`d    ���`oplot_histograms���`a(���`caxs���`a[���bmia5���`a]���`a,���`a ���`dprng���`a)���`a
���`a
���`d    ���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`a
���`d    ���akfreturn���`a ���`cfig���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs2a"���bs2h__main__���bs2a"���`a:���`a
���`a
���`d    ���bc1xA# Setup a list of all available styles, in alphabetical order but���`a
���`d    ���bc1xA# the `default` and `classic` ones, which will be forced resp. in���`a
���`d    ���bc1x# first and second position.���`a
���`d    ���`jstyle_list���`a ���aoa=���`a ���`a[���bs1a'���bs1gdefault���bs1a'���`a,���`a ���bs1a'���bs1gclassic���bs1a'���`a]���`a ���aoa+���`a ���bnbfsorted���`a(���`a
���`h        ���`estyle���`a ���akcfor���`a ���`estyle���`a ���bowbin���`a ���`cplt���aoa.���`estyle���aoa.���`iavailable���`a ���akbif���`a ���`estyle���`a ���aob!=���`a ���bs1a'���bs1gclassic���bs1a'���`a)���`a
���`a
���`d    ���bc1x># Plot a demonstration figure for every available style sheet.���`a
���`d    ���akcfor���`a ���`kstyle_label���`a ���bowbin���`a ���`jstyle_list���`a:���`a
���`h        ���akdwith���`a ���`cplt���aoa.���`jrc_context���`a(���`a{���bs2a"���bs2wfigure.max_open_warning���bs2a"���`a:���`a ���bnbclen���`a(���`jstyle_list���`a)���`a}���`a)���`a:���`a
���`l            ���akdwith���`a ���`cplt���aoa.���`estyle���aoa.���`gcontext���`a(���`kstyle_label���`a)���`a:���`a
���`p                ���`cfig���`a ���aoa=���`a ���`kplot_figure���`a(���`kstyle_label���aoa=���`kstyle_label���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�