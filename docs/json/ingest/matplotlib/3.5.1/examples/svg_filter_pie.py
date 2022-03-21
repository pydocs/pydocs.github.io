������������bsdy	"""
==============
SVG Filter Pie
==============

Demonstrate SVG filtering effects which might be used with Matplotlib.
The pie chart drawing code is borrowed from pie_demo.py

Note that the filtering effects are only effective if your SVG renderer
support it.
"""���`a
���`a
���bknfimport���`a ���bnnbio���`a
���bknfimport���`a ���bnncxml���bnna.���bnneetree���bnna.���bnnkElementTree���`a ���akbas���`a ���bnnbET���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`fShadow���`a
���`a
���bc1x# make a square figure and axes���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmfc0.1���`a,���`a ���bmfc0.1���`a,���`a ���bmfc0.8���`a,���`a ���bmfc0.8���`a]���`a)���`a
���`a
���`flabels���`a ���aoa=���`a ���bs1a'���bs1eFrogs���bs1a'���`a,���`a ���bs1a'���bs1dHogs���bs1a'���`a,���`a ���bs1a'���bs1dDogs���bs1a'���`a,���`a ���bs1a'���bs1dLogs���bs1a'���`a
���`efracs���`a ���aoa=���`a ���`a[���bmib15���`a,���`a ���bmib30���`a,���`a ���bmib45���`a,���`a ���bmib10���`a]���`a
���`a
���`gexplode���`a ���aoa=���`a ���`a(���bmia0���`a,���`a ���bmfd0.05���`a,���`a ���bmia0���`a,���`a ���bmia0���`a)���`a
���`a
���bc1xF# We want to draw the shadow for each pie but we will not use "shadow"���`a
���bc1xA# option as it doesn't save the references to the shadow patches.���`a
���`dpies���`a ���aoa=���`a ���`bax���aoa.���`cpie���`a(���`efracs���`a,���`a ���`gexplode���aoa=���`gexplode���`a,���`a ���`flabels���aoa=���`flabels���`a,���`a ���`gautopct���aoa=���bs1a'���bsie%1.1f���bsib%%���bs1a'���`a)���`a
���`a
���akcfor���`a ���`aw���`a ���bowbin���`a ���`dpies���`a[���bmia0���`a]���`a:���`a
���`d    ���bc1x# set the id with the label.���`a
���`d    ���`aw���aoa.���`gset_gid���`a(���`aw���aoa.���`iget_label���`a(���`a)���`a)���`a
���`a
���`d    ���bc1x+# we don't want to draw the edge of the pie���`a
���`d    ���`aw���aoa.���`mset_edgecolor���`a(���bs2a"���bs2dnone���bs2a"���`a)���`a
���`a
���akcfor���`a ���`aw���`a ���bowbin���`a ���`dpies���`a[���bmia0���`a]���`a:���`a
���`d    ���bc1u# create shadow patch���`a
���`d    ���`as���`a ���aoa=���`a ���`fShadow���`a(���`aw���`a,���`a ���aoa-���bmfd0.01���`a,���`a ���aoa-���bmfd0.01���`a)���`a
���`d    ���`as���aoa.���`gset_gid���`a(���`aw���aoa.���`gget_gid���`a(���`a)���`a ���aoa+���`a ���bs2a"���bs2g_shadow���bs2a"���`a)���`a
���`d    ���`as���aoa.���`jset_zorder���`a(���`aw���aoa.���`jget_zorder���`a(���`a)���`a ���aoa-���`a ���bmfc0.1���`a)���`a
���`d    ���`bax���aoa.���`iadd_patch���`a(���`as���`a)���`a
���`a
���`a
���bc1f# save���`a
���`af���`a ���aoa=���`a ���`bio���aoa.���`gBytesIO���`a(���`a)���`a
���`cplt���aoa.���`gsavefig���`a(���`af���`a,���`a ���bnbfformat���aoa=���bs2a"���bs2csvg���bs2a"���`a)���`a
���`a
���`a
���bc1xI# Filter definition for shadow using a gaussian blur and lighting effect.���`a
���bc1xJ# The lighting filter is copied from http://www.w3.org/TR/SVG/filters.html���`a
���`a
���bc1xF# I tested it with Inkscape and Firefox3. "Gaussian blur" is supported���`a
���bc1x># in both, but the lighting effect only in Inkscape. Also note���`a
���bc1x5# that, Inkscape's exporting also may not support it.���`a
���`a
���`jfilter_def���`a ���aoa=���`a ���bs2c"""���bs2a
���bs2n  <defs xmlns=���bs2a'���bs2xhttp://www.w3.org/2000/svg���bs2a'���bs2a
���bs2t        xmlns:xlink=���bs2a'���bs2xhttp://www.w3.org/1999/xlink���bs2a'���bs2a>���bs2a
���bs2o    <filter id=���bs2a'���bs2jdropshadow���bs2a'���bs2h height=���bs2a'���bs2c1.2���bs2a'���bs2g width=���bs2a'���bs2c1.2���bs2a'���bs2a>���bs2a
���bs2x      <feGaussianBlur result=���bs2a'���bs2dblur���bs2a'���bs2n stdDeviation=���bs2a'���bs2a2���bs2a'���bs2b/>���bs2a
���bs2m    </filter>���bs2a
���bs2a
���bs2o    <filter id=���bs2a'���bs2hMyFilter���bs2a'���bs2m filterUnits=���bs2a'���bs2qobjectBoundingBox���bs2a'���bs2a
���bs2n            x=���bs2a'���bs2a0���bs2a'���bs2c y=���bs2a'���bs2a0���bs2a'���bs2g width=���bs2a'���bs2a1���bs2a'���bs2h height=���bs2a'���bs2a1���bs2a'���bs2a>���bs2a
���bs2x      <feGaussianBlur in=���bs2a'���bs2kSourceAlpha���bs2a'���bs2n stdDeviation=���bs2a'���bs2a4���bs2a%���bs2a'���bs2h result=���bs2a'���bs2dblur���bs2a'���bs2b/>���bs2a
���bs2s      <feOffset in=���bs2a'���bs2dblur���bs2a'���bs2d dx=���bs2a'���bs2a4���bs2a%���bs2a'���bs2d dy=���bs2a'���bs2a4���bs2a%���bs2a'���bs2h result=���bs2a'���bs2joffsetBlur���bs2a'���bs2b/>���bs2a
���bs2x      <feSpecularLighting in=���bs2a'���bs2dblur���bs2a'���bs2n surfaceScale=���bs2a'���bs2a5���bs2a'���bs2r specularConstant=���bs2a'���bs2c.75���bs2a'���bs2a
���bs2x           specularExponent=���bs2a'���bs2b20���bs2a'���bs2p lighting-color=���bs2a'���bs2g#bbbbbb���bs2a'���bs2h result=���bs2a'���bs2gspecOut���bs2a'���bs2a>���bs2a
���bs2x        <fePointLight x=���bs2a'���bs2e-5000���bs2a%���bs2a'���bs2c y=���bs2a'���bs2f-10000���bs2a%���bs2a'���bs2c z=���bs2a'���bs2e20000���bs2a%���bs2a'���bs2b/>���bs2a
���bs2x      </feSpecularLighting>���bs2a
���bs2v      <feComposite in=���bs2a'���bs2gspecOut���bs2a'���bs2e in2=���bs2a'���bs2kSourceAlpha���bs2a'���bs2a
���bs2x                   operator=���bs2a'���bs2bin���bs2a'���bs2h result=���bs2a'���bs2gspecOut���bs2a'���bs2b/>���bs2a
���bs2v      <feComposite in=���bs2a'���bs2mSourceGraphic���bs2a'���bs2e in2=���bs2a'���bs2gspecOut���bs2a'���bs2j operator=���bs2a'���bs2jarithmetic���bs2a'���bs2a
���bs2g    k1=���bs2a'���bs2a0���bs2a'���bs2d k2=���bs2a'���bs2a1���bs2a'���bs2d k3=���bs2a'���bs2a1���bs2a'���bs2d k4=���bs2a'���bs2a0���bs2a'���bs2b/>���bs2a
���bs2m    </filter>���bs2a
���bs2i  </defs>���bs2a
���bs2c"""���`a
���`a
���`a
���`dtree���`a,���`a ���`exmlid���`a ���aoa=���`a ���`bET���aoa.���`eXMLID���`a(���`af���aoa.���`hgetvalue���`a(���`a)���`a)���`a
���`a
���bc1x3# insert the filter definition in the svg dom tree.���`a
���`dtree���aoa.���`finsert���`a(���bmia0���`a,���`a ���`bET���aoa.���`cXML���`a(���`jfilter_def���`a)���`a)���`a
���`a
���akcfor���`a ���`ai���`a,���`a ���`hpie_name���`a ���bowbin���`a ���bnbienumerate���`a(���`flabels���`a)���`a:���`a
���`d    ���`cpie���`a ���aoa=���`a ���`exmlid���`a[���`hpie_name���`a]���`a
���`d    ���`cpie���aoa.���`cset���`a(���bs2a"���bs2ffilter���bs2a"���`a,���`a ���bs1a'���bs1nurl(#MyFilter)���bs1a'���`a)���`a
���`a
���`d    ���`fshadow���`a ���aoa=���`a ���`exmlid���`a[���`hpie_name���`a ���aoa+���`a ���bs2a"���bs2g_shadow���bs2a"���`a]���`a
���`d    ���`fshadow���aoa.���`cset���`a(���bs2a"���bs2ffilter���bs2a"���`a,���`a ���bs1a'���bs1purl(#dropshadow)���bs1a'���`a)���`a
���`a
���`bfn���`a ���aoa=���`a ���bs2a"���bs2rsvg_filter_pie.svg���bs2a"���`a
���bnbeprint���`a(���bsaaf���bs2a"���bs2gSaving ���bs2a'���bsia{���`bfn���bsia}���bs2a'���bs2a"���`a)���`a
���`bET���aoa.���`kElementTree���`a(���`dtree���`a)���aoa.���`ewrite���`a(���`bfn���`a)���`a
`dNone�