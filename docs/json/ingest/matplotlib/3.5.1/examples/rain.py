��������s���bsdx�"""
===============
Rain simulation
===============

Simulates rain drops on a surface by animating the scale and opacity
of 50 scatter points.

Author: Nicolas P. Rougier
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnianimation���`a ���bknfimport���`a ���`mFuncAnimation���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���bc1x/# Create new Figure and an Axes which fills it.���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia7���`a,���`a ���bmia7���`a)���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���`gframeon���aoa=���bkceFalse���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`bax���aoa.���`jset_xticks���`a(���`a[���`a]���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`bax���aoa.���`jset_yticks���`a(���`a[���`a]���`a)���`a
���`a
���bc1r# Create rain data���`a
���`gn_drops���`a ���aoa=���`a ���bmib50���`a
���`jrain_drops���`a ���aoa=���`a ���`bnp���aoa.���`ezeros���`a(���`gn_drops���`a,���`a ���`edtype���aoa=���`a[���`a(���bs1a'���bs1hposition���bs1a'���`a,���`a ���bnbefloat���`a,���`a ���`a(���bmia2���`a,���`a)���`a)���`a,���`a
���`x&                                      ���`a(���bs1a'���bs1dsize���bs1a'���`a,���`e     ���bnbefloat���`a)���`a,���`a
���`x&                                      ���`a(���bs1a'���bs1fgrowth���bs1a'���`a,���`c   ���bnbefloat���`a)���`a,���`a
���`x&                                      ���`a(���bs1a'���bs1ecolor���bs1a'���`a,���`d    ���bnbefloat���`a,���`a ���`a(���bmia4���`a,���`a)���`a)���`a]���`a)���`a
���`a
���bc1x7# Initialize the raindrops in random positions and with���`a
���bc1v# random growth rates.���`a
���`jrain_drops���`a[���bs1a'���bs1hposition���bs1a'���`a]���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`guniform���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���`a(���`gn_drops���`a,���`a ���bmia2���`a)���`a)���`a
���`jrain_drops���`a[���bs1a'���bs1fgrowth���bs1a'���`a]���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`guniform���`a(���bmib50���`a,���`a ���bmic200���`a,���`a ���`gn_drops���`a)���`a
���`a
���bc1x=# Construct the scatter which we will update during animation���`a
���bc1x# as the raindrops develop.���`a
���`dscat���`a ���aoa=���`a ���`bax���aoa.���`gscatter���`a(���`jrain_drops���`a[���bs1a'���bs1hposition���bs1a'���`a]���`a[���`a:���`a,���`a ���bmia0���`a]���`a,���`a ���`jrain_drops���`a[���bs1a'���bs1hposition���bs1a'���`a]���`a[���`a:���`a,���`a ���bmia1���`a]���`a,���`a
���`r                  ���`as���aoa=���`jrain_drops���`a[���bs1a'���bs1dsize���bs1a'���`a]���`a,���`a ���`blw���aoa=���bmfc0.5���`a,���`a ���`jedgecolors���aoa=���`jrain_drops���`a[���bs1a'���bs1ecolor���bs1a'���`a]���`a,���`a
���`r                  ���`jfacecolors���aoa=���bs1a'���bs1dnone���bs1a'���`a)���`a
���`a
���`a
���akcdef���`a ���bnffupdate���`a(���`lframe_number���`a)���`a:���`a
���`d    ���bc1x@# Get an index which we can use to re-spawn the oldest raindrop.���`a
���`d    ���`mcurrent_index���`a ���aoa=���`a ���`lframe_number���`a ���aoa%���`a ���`gn_drops���`a
���`a
���`d    ���bc1x6# Make all colors more transparent as time progresses.���`a
���`d    ���`jrain_drops���`a[���bs1a'���bs1ecolor���bs1a'���`a]���`a[���`a:���`a,���`a ���bmia3���`a]���`a ���aoa-���aoa=���`a ���bmfc1.0���aoa/���bnbclen���`a(���`jrain_drops���`a)���`a
���`d    ���`jrain_drops���`a[���bs1a'���bs1ecolor���bs1a'���`a]���`a[���`a:���`a,���`a ���bmia3���`a]���`a ���aoa=���`a ���`bnp���aoa.���`dclip���`a(���`jrain_drops���`a[���bs1a'���bs1ecolor���bs1a'���`a]���`a[���`a:���`a,���`a ���bmia3���`a]���`a,���`a ���bmia0���`a,���`a ���bmia1���`a)���`a
���`a
���`d    ���bc1x# Make all circles bigger.���`a
���`d    ���`jrain_drops���`a[���bs1a'���bs1dsize���bs1a'���`a]���`a ���aoa+���aoa=���`a ���`jrain_drops���`a[���bs1a'���bs1fgrowth���bs1a'���`a]���`a
���`a
���`d    ���bc1x?# Pick a new position for oldest rain drop, resetting its size,���`a
���`d    ���bc1x# color and growth factor.���`a
���`d    ���`jrain_drops���`a[���bs1a'���bs1hposition���bs1a'���`a]���`a[���`mcurrent_index���`a]���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`guniform���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia2���`a)���`a
���`d    ���`jrain_drops���`a[���bs1a'���bs1dsize���bs1a'���`a]���`a[���`mcurrent_index���`a]���`a ���aoa=���`a ���bmia5���`a
���`d    ���`jrain_drops���`a[���bs1a'���bs1ecolor���bs1a'���`a]���`a[���`mcurrent_index���`a]���`a ���aoa=���`a ���`a(���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a)���`a
���`d    ���`jrain_drops���`a[���bs1a'���bs1fgrowth���bs1a'���`a]���`a[���`mcurrent_index���`a]���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`guniform���`a(���bmib50���`a,���`a ���bmic200���`a)���`a
���`a
���`d    ���bc1xJ# Update the scatter collection, with the new colors, sizes and positions.���`a
���`d    ���`dscat���aoa.���`nset_edgecolors���`a(���`jrain_drops���`a[���bs1a'���bs1ecolor���bs1a'���`a]���`a)���`a
���`d    ���`dscat���aoa.���`iset_sizes���`a(���`jrain_drops���`a[���bs1a'���bs1dsize���bs1a'���`a]���`a)���`a
���`d    ���`dscat���aoa.���`kset_offsets���`a(���`jrain_drops���`a[���bs1a'���bs1hposition���bs1a'���`a]���`a)���`a
���`a
���`a
���bc1xO# Construct the animation, using the update function as the animation director.���`a
���`ianimation���`a ���aoa=���`a ���`mFuncAnimation���`a(���`cfig���`a,���`a ���`fupdate���`a,���`a ���`hinterval���aoa=���bmib10���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�