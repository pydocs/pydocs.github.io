������������bsdy�"""
==============================
Text Rotation Relative To Line
==============================

Text objects in matplotlib are normally rotated with respect to the
screen coordinate system (i.e., 45 degrees rotation plots text along a
line that is in between horizontal and vertical no matter how the axes
are changed).  However, at times one wants to rotate text with respect
to something on the plot.  In this case, the correct angle won't be
the angle of that object in the plot coordinate system, but the angle
that that object APPEARS in the screen coordinate system.  This angle
can be determined automatically by setting the parameter
*transform_rotates_text*, as shown in the example below.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���bc1x!# Plot diagonal line (45 degrees)���`a
���`ah���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���bnberange���`a(���bmia0���`a,���`a ���bmib10���`a)���`a,���`a ���bnberange���`a(���bmia0���`a,���`a ���bmib10���`a)���`a)���`a
���`a
���bc1xB# set limits so that it no longer looks on screen to be 45 degrees���`a
���`bax���aoa.���`hset_xlim���`a(���`a[���aoa-���bmib10���`a,���`a ���bmib20���`a]���`a)���`a
���`a
���bc1x# Locations to plot text���`a
���`bl1���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a(���bmia1���`a,���`a ���bmia1���`a)���`a)���`a
���`bl2���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a(���bmia5���`a,���`a ���bmia5���`a)���`a)���`a
���`a
���bc1n# Rotate angle���`a
���`eangle���`a ���aoa=���`a ���bmib45���`a
���`a
���bc1k# Plot text���`a
���`cth1���`a ���aoa=���`a ���`bax���aoa.���`dtext���`a(���aoa*���`bl1���`a,���`a ���bs1a'���bs1xtext not rotated correctly���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib16���`a,���`a
���`n              ���`hrotation���aoa=���`eangle���`a,���`a ���`mrotation_mode���aoa=���bs1a'���bs1fanchor���bs1a'���`a)���`a
���`cth2���`a ���aoa=���`a ���`bax���aoa.���`dtext���`a(���aoa*���`bl2���`a,���`a ���bs1a'���bs1vtext rotated correctly���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib16���`a,���`a
���`n              ���`hrotation���aoa=���`eangle���`a,���`a ���`mrotation_mode���aoa=���bs1a'���bs1fanchor���bs1a'���`a,���`a
���`n              ���`vtransform_rotates_text���aoa=���bkcdTrue���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�