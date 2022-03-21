������������bsdx�"""
=========
Pie Demo2
=========

Make a pie charts using `~.axes.Axes.pie`.

This example demonstrates some pie chart features like labels, varying size,
autolabeling the percentage, offsetting a slice and adding a shadow.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1k# Some data���`a
���`flabels���`a ���aoa=���`a ���bs1a'���bs1eFrogs���bs1a'���`a,���`a ���bs1a'���bs1dHogs���bs1a'���`a,���`a ���bs1a'���bs1dDogs���bs1a'���`a,���`a ���bs1a'���bs1dLogs���bs1a'���`a
���`efracs���`a ���aoa=���`a ���`a[���bmib15���`a,���`a ���bmib30���`a,���`a ���bmib45���`a,���`a ���bmib10���`a]���`a
���`a
���bc1v# Make figure and axes���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia2���`a)���`a
���`a
���bc1u# A standard pie plot���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���aoa.���`cpie���`a(���`efracs���`a,���`a ���`flabels���aoa=���`flabels���`a,���`a ���`gautopct���aoa=���bs1a'���bsie%1.1f���bsib%%���bs1a'���`a,���`a ���`fshadow���aoa=���bkcdTrue���`a)���`a
���`a
���bc1x&# Shift the second slice using explode���`a
���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`cpie���`a(���`efracs���`a,���`a ���`flabels���aoa=���`flabels���`a,���`a ���`gautopct���aoa=���bs1a'���bsid%.0f���bsib%%���bs1a'���`a,���`a ���`fshadow���aoa=���bkcdTrue���`a,���`a
���`n              ���`gexplode���aoa=���`a(���bmia0���`a,���`a ���bmfc0.1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a)���`a)���`a
���`a
���bc1x.# Adapt radius and text size for a smaller pie���`a
���`gpatches���`a,���`a ���`etexts���`a,���`a ���`iautotexts���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia0���`a]���aoa.���`cpie���`a(���`efracs���`a,���`a ���`flabels���aoa=���`flabels���`a,���`a
���`x*                                          ���`gautopct���aoa=���bs1a'���bsid%.0f���bsib%%���bs1a'���`a,���`a
���`x*                                          ���`itextprops���aoa=���`a{���bs1a'���bs1dsize���bs1a'���`a:���`a ���bs1a'���bs1gsmaller���bs1a'���`a}���`a,���`a
���`x*                                          ���`fshadow���aoa=���bkcdTrue���`a,���`a ���`fradius���aoa=���bmfc0.5���`a)���`a
���bc1x!# Make percent texts even smaller���`a
���`cplt���aoa.���`dsetp���`a(���`iautotexts���`a,���`a ���`dsize���aoa=���bs1a'���bs1gx-small���bs1a'���`a)���`a
���`iautotexts���`a[���bmia0���`a]���aoa.���`iset_color���`a(���bs1a'���bs1ewhite���bs1a'���`a)���`a
���`a
���bc1xD# Use a smaller explode and turn of the shadow for better visibility���`a
���`gpatches���`a,���`a ���`etexts���`a,���`a ���`iautotexts���`a ���aoa=���`a ���`caxs���`a[���bmia1���`a,���`a ���bmia1���`a]���aoa.���`cpie���`a(���`efracs���`a,���`a ���`flabels���aoa=���`flabels���`a,���`a
���`x*                                          ���`gautopct���aoa=���bs1a'���bsid%.0f���bsib%%���bs1a'���`a,���`a
���`x*                                          ���`itextprops���aoa=���`a{���bs1a'���bs1dsize���bs1a'���`a:���`a ���bs1a'���bs1gsmaller���bs1a'���`a}���`a,���`a
���`x*                                          ���`fshadow���aoa=���bkceFalse���`a,���`a ���`fradius���aoa=���bmfc0.5���`a,���`a
���`x*                                          ���`gexplode���aoa=���`a(���bmia0���`a,���`a ���bmfd0.05���`a,���`a ���bmia0���`a,���`a ���bmia0���`a)���`a)���`a
���`cplt���aoa.���`dsetp���`a(���`iautotexts���`a,���`a ���`dsize���aoa=���bs1a'���bs1gx-small���bs1a'���`a)���`a
���`iautotexts���`a[���bmia0���`a]���aoa.���`iset_color���`a(���bs1a'���bs1ewhite���bs1a'���`a)���`a
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
���bc1x;#    - `matplotlib.axes.Axes.pie` / `matplotlib.pyplot.pie`���`a
`dNone�