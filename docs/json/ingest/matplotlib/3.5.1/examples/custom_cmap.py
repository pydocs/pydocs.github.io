��������x���bsdy
�"""
=========================================
Creating a colormap from a list of colors
=========================================

For more detail on creating and manipulating colormaps see
:doc:`/tutorials/colors/colormap-manipulation`.

Creating a :doc:`colormap </tutorials/colors/colormaps>` from a list of colors
can be done with the `.LinearSegmentedColormap.from_list` method.  You must
pass a list of RGB tuples that define the mixture of colors from 0 to 1.


Creating custom colormaps
-------------------------
It is also possible to create a custom mapping for a colormap. This is
accomplished by creating dictionary that specifies how the RGB channels
change from one end of the cmap to the other.

Example: suppose you want red to increase from 0 to 1 over the bottom
half, green to do the same over the middle half, and blue over the top
half.  Then you would use::

  cdict = {'red':   ((0.0,  0.0, 0.0),
                     (0.5,  1.0, 1.0),
                     (1.0,  1.0, 1.0)),

           'green': ((0.0,  0.0, 0.0),
                     (0.25, 0.0, 0.0),
                     (0.75, 1.0, 1.0),
                     (1.0,  1.0, 1.0)),

           'blue':  ((0.0,  0.0, 0.0),
                     (0.5,  0.0, 0.0),
                     (1.0,  1.0, 1.0))}

If, as in this example, there are no discontinuities in the r, g, and b
components, then it is quite simple: the second and third element of
each tuple, above, is the same--call it "y".  The first element ("x")
defines interpolation intervals over the full range of 0 to 1, and it
must span that whole range.  In other words, the values of x divide the
0-to-1 range into a set of segments, and y gives the end-point color
values for each segment.

Now consider the green. cdict['green'] is saying that for
0 <= x <= 0.25, y is zero; no green.
0.25 < x <= 0.75, y varies linearly from 0 to 1.
x > 0.75, y remains at 1, full green.

If there are discontinuities, then it is a little more complicated.
Label the 3 elements in each row in the cdict entry for a given color as
(x, y0, y1).  Then for values of x between x[i] and x[i+1] the color
value is interpolated between y1[i] and y0[i+1].

Going back to the cookbook example, look at cdict['red']; because y0 !=
y1, it is saying that for x from 0 to 0.5, red increases from 0 to 1,
but then it jumps down, so that for x from 0.5 to 1, red increases from
0.7 to 1.  Green ramps from 0 to 1 as x goes from 0 to 0.5, then jumps
back to 0, and ramps back to 1 as x goes from 0.5 to 1.::

  row i:   x  y0  y1
                  /
                 /
  row i+1: x  y0  y1

Above is an attempt to show that for x in the range x[i] to x[i+1], the
interpolation is between y1[i] and y0[i+1].  So, y0[0] and y1[-1] are
never used.

"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���akbas���`a ���bnncmpl���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfcolors���`a ���bknfimport���`a ���`wLinearSegmentedColormap���`a
���`a
���bc1x## Make some illustrative fake data:���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmfc0.1���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmfc0.1���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`aZ���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���`aX���`a)���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`aY���`a)���`a ���aoa*���`a ���bmib10���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# --- Colormaps from a list ---���`a
���`a
���`fcolors���`a ���aoa=���`a ���`a[���`a(���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a)���`a,���`a ���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a)���`a,���`a ���`a(���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a)���`a]���`b  ���bc1m# R -> G -> B���`a
���`fn_bins���`a ���aoa=���`a ���`a[���bmia3���`a,���`a ���bmia6���`a,���`a ���bmib10���`a,���`a ���bmic100���`a]���`b  ���bc1x)# Discretizes the interpolation into bins���`a
���`icmap_name���`a ���aoa=���`a ���bs1a'���bs1gmy_list���bs1a'���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia9���`a)���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfd0.02���`a,���`a ���`fbottom���aoa=���bmfd0.06���`a,���`a ���`eright���aoa=���bmfd0.95���`a,���`a ���`ctop���aoa=���bmfd0.94���`a,���`a ���`fwspace���aoa=���bmfd0.05���`a)���`a
���akcfor���`a ���`en_bin���`a,���`a ���`bax���`a ���bowbin���`a ���bnbczip���`a(���`fn_bins���`a,���`a ���`caxs���aoa.���`dflat���`a)���`a:���`a
���`d    ���bc1u# Create the colormap���`a
���`d    ���`dcmap���`a ���aoa=���`a ���`wLinearSegmentedColormap���aoa.���`ifrom_list���`a(���`icmap_name���`a,���`a ���`fcolors���`a,���`a ���`aN���aoa=���`en_bin���`a)���`a
���`d    ���bc1x;# Fewer bins will result in "coarser" colomap interpolation���`a
���`d    ���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`forigin���aoa=���bs1a'���bs1elower���bs1a'���`a,���`a ���`dcmap���aoa=���`dcmap���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs2a"���bs2hN bins: ���bsib%s���bs2a"���`a ���aoa%���`a ���`en_bin���`a)���`a
���`d    ���`cfig���aoa.���`hcolorbar���`a(���`bim���`a,���`a ���`bax���aoa=���`bax���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# --- Custom colormaps ---���`a
���`a
���`fcdict1���`a ���aoa=���`a ���`a{���bs1a'���bs1cred���bs1a'���`a:���`c   ���`a(���`a(���bmfc0.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a,���`a
���`t                    ���`a(���bmfc0.5���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.1���`a)���`a,���`a
���`t                    ���`a(���bmfc1.0���`a,���`a ���bmfc1.0���`a,���`a ���bmfc1.0���`a)���`a)���`a,���`a
���`a
���`j          ���bs1a'���bs1egreen���bs1a'���`a:���`a ���`a(���`a(���bmfc0.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a,���`a
���`t                    ���`a(���bmfc1.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a)���`a,���`a
���`a
���`j          ���bs1a'���bs1dblue���bs1a'���`a:���`b  ���`a(���`a(���bmfc0.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc1.0���`a)���`a,���`a
���`t                    ���`a(���bmfc0.5���`a,���`a ���bmfc0.1���`a,���`a ���bmfc0.0���`a)���`a,���`a
���`t                    ���`a(���bmfc1.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a)���`a
���`j          ���`a}���`a
���`a
���`fcdict2���`a ���aoa=���`a ���`a{���bs1a'���bs1cred���bs1a'���`a:���`c   ���`a(���`a(���bmfc0.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a,���`a
���`t                    ���`a(���bmfc0.5���`a,���`a ���bmfc0.0���`a,���`a ���bmfc1.0���`a)���`a,���`a
���`t                    ���`a(���bmfc1.0���`a,���`a ���bmfc0.1���`a,���`a ���bmfc1.0���`a)���`a)���`a,���`a
���`a
���`j          ���bs1a'���bs1egreen���bs1a'���`a:���`a ���`a(���`a(���bmfc0.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a,���`a
���`t                    ���`a(���bmfc1.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a)���`a,���`a
���`a
���`j          ���bs1a'���bs1dblue���bs1a'���`a:���`b  ���`a(���`a(���bmfc0.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.1���`a)���`a,���`a
���`t                    ���`a(���bmfc0.5���`a,���`a ���bmfc1.0���`a,���`a ���bmfc0.0���`a)���`a,���`a
���`t                    ���`a(���bmfc1.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a)���`a
���`j          ���`a}���`a
���`a
���`fcdict3���`a ���aoa=���`a ���`a{���bs1a'���bs1cred���bs1a'���`a:���`b  ���`a(���`a(���bmfc0.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a,���`a
���`s                   ���`a(���bmfd0.25���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a,���`a
���`s                   ���`a(���bmfc0.5���`a,���`a ���bmfc0.8���`a,���`a ���bmfc1.0���`a)���`a,���`a
���`s                   ���`a(���bmfd0.75���`a,���`a ���bmfc1.0���`a,���`a ���bmfc1.0���`a)���`a,���`a
���`s                   ���`a(���bmfc1.0���`a,���`a ���bmfc0.4���`a,���`a ���bmfc1.0���`a)���`a)���`a,���`a
���`a
���`j          ���bs1a'���bs1egreen���bs1a'���`a:���`a ���`a(���`a(���bmfc0.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a,���`a
���`t                    ���`a(���bmfd0.25���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a,���`a
���`t                    ���`a(���bmfc0.5���`a,���`a ���bmfc0.9���`a,���`a ���bmfc0.9���`a)���`a,���`a
���`t                    ���`a(���bmfd0.75���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a,���`a
���`t                    ���`a(���bmfc1.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a)���`a,���`a
���`a
���`j          ���bs1a'���bs1dblue���bs1a'���`a:���`b  ���`a(���`a(���bmfc0.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.4���`a)���`a,���`a
���`t                    ���`a(���bmfd0.25���`a,���`a ���bmfc1.0���`a,���`a ���bmfc1.0���`a)���`a,���`a
���`t                    ���`a(���bmfc0.5���`a,���`a ���bmfc1.0���`a,���`a ���bmfc0.8���`a)���`a,���`a
���`t                    ���`a(���bmfd0.75���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a,���`a
���`t                    ���`a(���bmfc1.0���`a,���`a ���bmfc0.0���`a,���`a ���bmfc0.0���`a)���`a)���`a
���`j          ���`a}���`a
���`a
���bc1x:# Make a modified version of cdict3 with some transparency���`a
���bc1x# in the middle of the range.���`a
���`fcdict4���`a ���aoa=���`a ���`a{���aoa*���aoa*���`fcdict3���`a,���`a
���`j          ���bs1a'���bs1ealpha���bs1a'���`a:���`a ���`a(���`a(���bmfc0.0���`a,���`a ���bmfc1.0���`a,���`a ���bmfc1.0���`a)���`a,���`a
���`t                    ���bc1s# (0.25, 1.0, 1.0),���`a
���`t                    ���`a(���bmfc0.5���`a,���`a ���bmfc0.3���`a,���`a ���bmfc0.3���`a)���`a,���`a
���`t                    ���bc1s# (0.75, 1.0, 1.0),���`a
���`t                    ���`a(���bmfc1.0���`a,���`a ���bmfc1.0���`a,���`a ���bmfc1.0���`a)���`a)���`a,���`a
���`j          ���`a}���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x6# Now we will use this example to illustrate 2 ways of���`a
���bc1x# handling custom colormaps.���`a
���bc1x&# First, the most direct and explicit:���`a
���`a
���`iblue_red1���`a ���aoa=���`a ���`wLinearSegmentedColormap���`a(���bs1a'���bs1hBlueRed1���bs1a'���`a,���`a ���`fcdict1���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x4# Second, create the map explicitly and register it.���`a
���bc1x8# Like the first method, this method works with any kind���`a
���bc1w# of Colormap, not just���`a
���bc1x# a LinearSegmentedColormap:���`a
���`a
���`cmpl���aoa.���`icolormaps���aoa.���`hregister���`a(���`wLinearSegmentedColormap���`a(���bs1a'���bs1hBlueRed2���bs1a'���`a,���`a ���`fcdict2���`a)���`a)���`a
���`cmpl���aoa.���`icolormaps���aoa.���`hregister���`a(���`wLinearSegmentedColormap���`a(���bs1a'���bs1hBlueRed3���bs1a'���`a,���`a ���`fcdict3���`a)���`a)���`a
���`cmpl���aoa.���`icolormaps���aoa.���`hregister���`a(���`wLinearSegmentedColormap���`a(���bs1a'���bs1lBlueRedAlpha���bs1a'���`a,���`a ���`fcdict4���`a)���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1r# Make the figure:���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia9���`a)���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`dleft���aoa=���bmfd0.02���`a,���`a ���`fbottom���aoa=���bmfd0.06���`a,���`a ���`eright���aoa=���bmfd0.95���`a,���`a ���`ctop���aoa=���bmfd0.94���`a,���`a ���`fwspace���aoa=���bmfd0.05���`a)���`a
���`a
���bc1r# Make 4 subplots:���`a
���`a
���`cim1���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`dcmap���aoa=���`iblue_red1���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cim1���`a,���`a ���`bax���aoa=���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a)���`a
���`a
���`cim2���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`fimshow���`a(���`aZ���`a,���`a ���`dcmap���aoa=���bs1a'���bs1hBlueRed2���bs1a'���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cim2���`a,���`a ���`bax���aoa=���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���`a)���`a
���`a
���bc1x;# Now we will set the third cmap as the default.  One would���`a
���bc1x;# not normally do this in the middle of a script like this;���`a
���bc1x0# it is done here just to illustrate the method.���`a
���`a
���`cplt���aoa.���`hrcParams���`a[���bs1a'���bs1jimage.cmap���bs1a'���`a]���`a ���aoa=���`a ���bs1a'���bs1hBlueRed3���bs1a'���`a
���`a
���`cim3���`a ���aoa=���`a ���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`fimshow���`a(���`aZ���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cim3���`a,���`a ���`bax���aoa=���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���`a)���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs2a"���bs2iAlpha = 1���bs2a"���`a)���`a
���`a
���bc1x:# Or as yet another variation, we can replace the rcParams���`a
���bc1x># specification *before* the imshow with the following *after*���`a
���bc1i# imshow.���`a
���bc1x?# This sets the new default *and* sets the colormap of the last���`a
���bc1x-# image-like item plotted via pyplot, if any.���`a
���bc1a#���`a
���`a
���bc1x=# Draw a line with low zorder so it will be behind the image.���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`dplot���`a(���`a[���bmia0���`a,���`a ���bmib10���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmib20���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a]���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ac���bs1a'���`a,���`a ���`blw���aoa=���bmib20���`a,���`a ���`fzorder���aoa=���aoa-���bmia1���`a)���`a
���`a
���`cim4���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`fimshow���`a(���`aZ���`a)���`a
���`cfig���aoa.���`hcolorbar���`a(���`cim4���`a,���`a ���`bax���aoa=���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���`a)���`a
���`a
���bc1xA# Here it is: changing the colormap for the current image and its���`a
���bc1x(# colorbar after they have been plotted.���`a
���`cim4���aoa.���`hset_cmap���`a(���bs1a'���bs1lBlueRedAlpha���bs1a'���`a)���`a
���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bs2a"���bs2mVarying alpha���bs2a"���`a)���`a
���bc1a#���`a
���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1xCustom Blue-Red colormaps���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib16���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`ctop���aoa=���bmfc0.9���`a)���`a
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
���bc1xA#    - `matplotlib.axes.Axes.imshow` / `matplotlib.pyplot.imshow`���`a
���bc1xI#    - `matplotlib.figure.Figure.colorbar` / `matplotlib.pyplot.colorbar`���`a
���bc1x#    - `matplotlib.colors`���`a
���bc1x2#    - `matplotlib.colors.LinearSegmentedColormap`���`a
���bc1x<#    - `matplotlib.colors.LinearSegmentedColormap.from_list`���`a
���bc1v#    - `matplotlib.cm`���`a
���bc1x.#    - `matplotlib.cm.ScalarMappable.set_cmap`���`a
���bc1x$#    - `matplotlib.cm.register_cmap`���`a
`dNone�