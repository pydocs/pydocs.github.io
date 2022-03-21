��������N���bsdxD"""
============
Boxplot Demo
============

Example boxplot code
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���bc1s# fake up some data���`a
���`fspread���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib50���`a)���`a ���aoa*���`a ���bmic100���`a
���`fcenter���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���bmib25���`a)���`a ���aoa*���`a ���bmib50���`a
���`jflier_high���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a ���aoa*���`a ���bmic100���`a ���aoa+���`a ���bmic100���`a
���`iflier_low���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a ���aoa*���`a ���aoa-���bmic100���`a
���`ddata���`a ���aoa=���`a ���`bnp���aoa.���`kconcatenate���`a(���`a(���`fspread���`a,���`a ���`fcenter���`a,���`a ���`jflier_high���`a,���`a ���`iflier_low���`a)���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`dfig1���`a,���`a ���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1jBasic Plot���bs1a'���`a)���`a
���`cax1���aoa.���`gboxplot���`a(���`ddata���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`dfig2���`a,���`a ���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1mNotched boxes���bs1a'���`a)���`a
���`cax2���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`enotch���aoa=���bkcdTrue���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`mgreen_diamond���`a ���aoa=���`a ���bnbddict���`a(���`omarkerfacecolor���aoa=���bs1a'���bs1ag���bs1a'���`a,���`a ���`fmarker���aoa=���bs1a'���bs1aD���bs1a'���`a)���`a
���`dfig3���`a,���`a ���`cax3���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax3���aoa.���`iset_title���`a(���bs1a'���bs1wChanged Outlier Symbols���bs1a'���`a)���`a
���`cax3���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`jflierprops���aoa=���`mgreen_diamond���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`dfig4���`a,���`a ���`cax4���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax4���aoa.���`iset_title���`a(���bs1a'���bs1sHide Outlier Points���bs1a'���`a)���`a
���`cax4���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`jshowfliers���aoa=���bkceFalse���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`jred_square���`a ���aoa=���`a ���bnbddict���`a(���`omarkerfacecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`fmarker���aoa=���bs1a'���bs1as���bs1a'���`a)���`a
���`dfig5���`a,���`a ���`cax5���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax5���aoa.���`iset_title���`a(���bs1a'���bs1pHorizontal Boxes���bs1a'���`a)���`a
���`cax5���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`dvert���aoa=���bkceFalse���`a,���`a ���`jflierprops���aoa=���`jred_square���`a)���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`dfig6���`a,���`a ���`cax6���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax6���aoa.���`iset_title���`a(���bs1a'���bs1vShorter Whisker Length���bs1a'���`a)���`a
���`cax6���aoa.���`gboxplot���`a(���`ddata���`a,���`a ���`jflierprops���aoa=���`jred_square���`a,���`a ���`dvert���aoa=���bkceFalse���`a,���`a ���`dwhis���aoa=���bmfd0.75���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x# Fake up some more data���`a
���`a
���`fspread���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib50���`a)���`a ���aoa*���`a ���bmic100���`a
���`fcenter���`a ���aoa=���`a ���`bnp���aoa.���`dones���`a(���bmib25���`a)���`a ���aoa*���`a ���bmib40���`a
���`jflier_high���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a ���aoa*���`a ���bmic100���`a ���aoa+���`a ���bmic100���`a
���`iflier_low���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib10���`a)���`a ���aoa*���`a ���aoa-���bmic100���`a
���`bd2���`a ���aoa=���`a ���`bnp���aoa.���`kconcatenate���`a(���`a(���`fspread���`a,���`a ���`fcenter���`a,���`a ���`jflier_high���`a,���`a ���`iflier_low���`a)���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x:# Making a 2-D array only works if all the columns are the���`a
���bc1x9# same length.  If they are not, then use a list instead.���`a
���bc1x:# This is actually more efficient because boxplot converts���`a
���bc1x7# a 2-D array into a list of vectors internally anyway.���`a
���`a
���`ddata���`a ���aoa=���`a ���`a[���`ddata���`a,���`a ���`bd2���`a,���`a ���`bd2���`a[���`a:���`a:���bmia2���`a]���`a]���`a
���`dfig7���`a,���`a ���`cax7���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`cax7���aoa.���`iset_title���`a(���bs1a'���bs1x%Multiple Samples with Different sizes���bs1a'���`a)���`a
���`cax7���aoa.���`gboxplot���`a(���`ddata���`a)���`a
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
���bc1xC#    - `matplotlib.axes.Axes.boxplot` / `matplotlib.pyplot.boxplot`���`a
`dNone�