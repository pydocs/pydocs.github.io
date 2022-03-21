��������[���bsdxy"""
==============
Legend Picking
==============

Enable picking on the legend to toggle the original line on and off
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`by1���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���`at���`a)���`a
���`by2���`a ���aoa=���`a ���bmia4���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���bmia2���aoa*���`bnp���aoa.���`bpi���aoa*���bmia2���aoa*���`at���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x*Click on legend line to toggle line on/off���bs1a'���`a)���`a
���`eline1���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`by1���`a,���`a ���`blw���aoa=���bmia2���`a,���`a ���`elabel���aoa=���bs1a'���bs1d1 Hz���bs1a'���`a)���`a
���`eline2���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`at���`a,���`a ���`by2���`a,���`a ���`blw���aoa=���bmia2���`a,���`a ���`elabel���aoa=���bs1a'���bs1d2 Hz���bs1a'���`a)���`a
���`cleg���`a ���aoa=���`a ���`bax���aoa.���`flegend���`a(���`hfancybox���aoa=���bkcdTrue���`a,���`a ���`fshadow���aoa=���bkcdTrue���`a)���`a
���`a
���`elines���`a ���aoa=���`a ���`a[���`eline1���`a,���`a ���`eline2���`a]���`a
���`elined���`a ���aoa=���`a ���`a{���`a}���`b  ���bc1x*# Will map legend lines to original lines.���`a
���akcfor���`a ���`glegline���`a,���`a ���`horigline���`a ���bowbin���`a ���bnbczip���`a(���`cleg���aoa.���`iget_lines���`a(���`a)���`a,���`a ���`elines���`a)���`a:���`a
���`d    ���`glegline���aoa.���`jset_picker���`a(���bkcdTrue���`a)���`b  ���bc1x$# Enable picking on the legend line.���`a
���`d    ���`elined���`a[���`glegline���`a]���`a ���aoa=���`a ���`horigline���`a
���`a
���`a
���akcdef���`a ���bnfgon_pick���`a(���`eevent���`a)���`a:���`a
���`d    ���bc1xG# On the pick event, find the original line corresponding to the legend���`a
���`d    ���bc1x(# proxy line, and toggle its visibility.���`a
���`d    ���`glegline���`a ���aoa=���`a ���`eevent���aoa.���`fartist���`a
���`d    ���`horigline���`a ���aoa=���`a ���`elined���`a[���`glegline���`a]���`a
���`d    ���`gvisible���`a ���aoa=���`a ���bowcnot���`a ���`horigline���aoa.���`kget_visible���`a(���`a)���`a
���`d    ���`horigline���aoa.���`kset_visible���`a(���`gvisible���`a)���`a
���`d    ���bc1xE# Change the alpha on the line in the legend so we can see what lines���`a
���`d    ���bc1t# have been toggled.���`a
���`d    ���`glegline���aoa.���`iset_alpha���`a(���bmfc1.0���`a ���akbif���`a ���`gvisible���`a ���akdelse���`a ���bmfc0.2���`a)���`a
���`d    ���`cfig���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1jpick_event���bs1a'���`a,���`a ���`gon_pick���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�