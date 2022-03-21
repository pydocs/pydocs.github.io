��������\���bsdx�"""
===============
SVG Filter Line
===============

Demonstrate SVG filtering effects which might be used with Matplotlib.

Note that the filtering effects are only effective if your SVG renderer
support it.
"""���`a
���`a
���bknfimport���`a ���bnnbio���`a
���bknfimport���`a ���bnncxml���bnna.���bnneetree���bnna.���bnnkElementTree���`a ���akbas���`a ���bnnbET���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���akbas���`a ���bnnkmtransforms���`a
���`a
���`dfig1���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`dfig1���aoa.���`hadd_axes���`a(���`a[���bmfc0.1���`a,���`a ���bmfc0.1���`a,���`a ���bmfc0.8���`a,���`a ���bmfc0.8���`a]���`a)���`a
���`a
���bc1l# draw lines���`a
���`bl1���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`a[���bmfc0.1���`a,���`a ���bmfc0.5���`a,���`a ���bmfc0.9���`a]���`a,���`a ���`a[���bmfc0.1���`a,���`a ���bmfc0.9���`a,���`a ���bmfc0.5���`a]���`a,���`a ���bs2a"���bs2cbo-���bs2a"���`a,���`a
���`n              ���`cmec���aoa=���bs2a"���bs2ab���bs2a"���`a,���`a ���`blw���aoa=���bmia5���`a,���`a ���`bms���aoa=���bmib10���`a,���`a ���`elabel���aoa=���bs2a"���bs2fLine 1���bs2a"���`a)���`a
���`bl2���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`a[���bmfc0.1���`a,���`a ���bmfc0.5���`a,���`a ���bmfc0.9���`a]���`a,���`a ���`a[���bmfc0.5���`a,���`a ���bmfc0.2���`a,���`a ���bmfc0.7���`a]���`a,���`a ���bs2a"���bs2crs-���bs2a"���`a,���`a
���`n              ���`cmec���aoa=���bs2a"���bs2ar���bs2a"���`a,���`a ���`blw���aoa=���bmia5���`a,���`a ���`bms���aoa=���bmib10���`a,���`a ���`elabel���aoa=���bs2a"���bs2fLine 2���bs2a"���`a)���`a
���`a
���`a
���akcfor���`a ���`al���`a ���bowbin���`a ���`a[���`bl1���`a,���`a ���`bl2���`a]���`a:���`a
���`a
���`d    ���bc1xB# draw shadows with same lines with slight offset and gray colors.���`a
���`a
���`d    ���`bxx���`a ���aoa=���`a ���`al���aoa.���`iget_xdata���`a(���`a)���`a
���`d    ���`byy���`a ���aoa=���`a ���`al���aoa.���`iget_ydata���`a(���`a)���`a
���`d    ���`fshadow���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`bxx���`a,���`a ���`byy���`a)���`a
���`d    ���`fshadow���aoa.���`kupdate_from���`a(���`al���`a)���`a
���`a
���`d    ���bc1n# adjust color���`a
���`d    ���`fshadow���aoa.���`iset_color���`a(���bs2a"���bs2c0.2���bs2a"���`a)���`a
���`d    ���bc1xA# adjust zorder of the shadow lines so that it is drawn below the���`a
���`d    ���bc1p# original lines���`a
���`d    ���`fshadow���aoa.���`jset_zorder���`a(���`al���aoa.���`jget_zorder���`a(���`a)���`a ���aoa-���`a ���bmfc0.5���`a)���`a
���`a
���`d    ���bc1r# offset transform���`a
���`d    ���`bot���`a ���aoa=���`a ���`kmtransforms���aoa.���`koffset_copy���`a(���`al���aoa.���`mget_transform���`a(���`a)���`a,���`a ���`dfig1���`a,���`a
���`x!                                 ���`ax���aoa=���bmfc4.0���`a,���`a ���`ay���aoa=���aoa-���bmfc6.0���`a,���`a ���`eunits���aoa=���bs1a'���bs1fpoints���bs1a'���`a)���`a
���`a
���`d    ���`fshadow���aoa.���`mset_transform���`a(���`bot���`a)���`a
���`a
���`d    ���bc1x# set the id for a later use���`a
���`d    ���`fshadow���aoa.���`gset_gid���`a(���`al���aoa.���`iget_label���`a(���`a)���`a ���aoa+���`a ���bs2a"���bs2g_shadow���bs2a"���`a)���`a
���`a
���`a
���`bax���aoa.���`hset_xlim���`a(���bmfb0.���`a,���`a ���bmfb1.���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���bmfb0.���`a,���`a ���bmfb1.���`a)���`a
���`a
���bc1x6# save the figure as a bytes string in the svg format.���`a
���`af���`a ���aoa=���`a ���`bio���aoa.���`gBytesIO���`a(���`a)���`a
���`cplt���aoa.���`gsavefig���`a(���`af���`a,���`a ���bnbfformat���aoa=���bs2a"���bs2csvg���bs2a"���`a)���`a
���`a
���`a
���bc1x'# filter definition for a gaussian blur���`a
���`jfilter_def���`a ���aoa=���`a ���bs2c"""���bs2a
���bs2n  <defs xmlns=���bs2a'���bs2xhttp://www.w3.org/2000/svg���bs2a'���bs2a
���bs2t        xmlns:xlink=���bs2a'���bs2xhttp://www.w3.org/1999/xlink���bs2a'���bs2a>���bs2a
���bs2o    <filter id=���bs2a'���bs2jdropshadow���bs2a'���bs2h height=���bs2a'���bs2c1.2���bs2a'���bs2g width=���bs2a'���bs2c1.2���bs2a'���bs2a>���bs2a
���bs2x      <feGaussianBlur result=���bs2a'���bs2dblur���bs2a'���bs2n stdDeviation=���bs2a'���bs2a3���bs2a'���bs2b/>���bs2a
���bs2m    </filter>���bs2a
���bs2i  </defs>���bs2a
���bs2c"""���`a
���`a
���`a
���bc1w# read in the saved svg���`a
���`dtree���`a,���`a ���`exmlid���`a ���aoa=���`a ���`bET���aoa.���`eXMLID���`a(���`af���aoa.���`hgetvalue���`a(���`a)���`a)���`a
���`a
���bc1x3# insert the filter definition in the svg dom tree.���`a
���`dtree���aoa.���`finsert���`a(���bmia0���`a,���`a ���`bET���aoa.���`cXML���`a(���`jfilter_def���`a)���`a)���`a
���`a
���akcfor���`a ���`al���`a ���bowbin���`a ���`a[���`bl1���`a,���`a ���`bl2���`a]���`a:���`a
���`d    ���bc1x'# pick up the svg element with given id���`a
���`d    ���`fshadow���`a ���aoa=���`a ���`exmlid���`a[���`al���aoa.���`iget_label���`a(���`a)���`a ���aoa+���`a ���bs2a"���bs2g_shadow���bs2a"���`a]���`a
���`d    ���bc1u# apply shadow filter���`a
���`d    ���`fshadow���aoa.���`cset���`a(���bs2a"���bs2ffilter���bs2a"���`a,���`a ���bs1a'���bs1purl(#dropshadow)���bs1a'���`a)���`a
���`a
���`bfn���`a ���aoa=���`a ���bs2a"���bs2ssvg_filter_line.svg���bs2a"���`a
���bnbeprint���`a(���bsaaf���bs2a"���bs2gSaving ���bs2a'���bsia{���`bfn���bsia}���bs2a'���bs2a"���`a)���`a
���`bET���aoa.���`kElementTree���`a(���`dtree���`a)���aoa.���`ewrite���`a(���`bfn���`a)���`a
`dNone�