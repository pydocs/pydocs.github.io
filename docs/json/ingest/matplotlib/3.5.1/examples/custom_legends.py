������������bsdy_"""
========================
Composing Custom Legends
========================

Composing custom legends piece-by-piece.

.. note::

   For more information on creating and customizing legends, see the following
   pages:

   * :doc:`/tutorials/intermediate/legend_guide`
   * :doc:`/gallery/text_labels_and_annotations/legend_demo`

Sometimes you don't want a legend that is explicitly tied to data that
you have plotted. For example, say you have plotted 10 lines, but don't
want a legend item to show up for each one. If you simply plot the lines
and call ``ax.legend()``, you will get the following:
"""���`a
���bc1x%# sphinx_gallery_thumbnail_number = 2���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`hrcParams���`a,���`a ���`fcycler���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`aN���`a ���aoa=���`a ���bmib10���`a
���`ddata���`a ���aoa=���`a ���`a(���`bnp���aoa.���`igeomspace���`a(���bmia1���`a,���`a ���bmib10���`a,���`a ���bmic100���`a)���`a ���aoa+���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���`aN���`a,���`a ���bmic100���`a)���`a)���aoa.���`aT���`a
���`dcmap���`a ���aoa=���`a ���`cplt���aoa.���`bcm���aoa.���`hcoolwarm���`a
���`hrcParams���`a[���bs1a'���bs1oaxes.prop_cycle���bs1a'���`a]���`a ���aoa=���`a ���`fcycler���`a(���`ecolor���aoa=���`dcmap���`a(���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���`aN���`a)���`a)���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`elines���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`ddata���`a)���`a
���`bax���aoa.���`flegend���`a(���`a)���`a
���`a
���bc1xN##############################################################################���`a
���bc1x+# Note that no legend entries were created.���`a
���bc1xL# In this case, we can compose a legend using Matplotlib objects that aren't���`a
���bc1x<# explicitly tied to the data that was plotted. For example:���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnelines���`a ���bknfimport���`a ���`fLine2D���`a
���`lcustom_lines���`a ���aoa=���`a ���`a[���`fLine2D���`a(���`a[���bmia0���`a]���`a,���`a ���`a[���bmia0���`a]���`a,���`a ���`ecolor���aoa=���`dcmap���`a(���bmfb0.���`a)���`a,���`a ���`blw���aoa=���bmia4���`a)���`a,���`a
���`p                ���`fLine2D���`a(���`a[���bmia0���`a]���`a,���`a ���`a[���bmia0���`a]���`a,���`a ���`ecolor���aoa=���`dcmap���`a(���bmfb.5���`a)���`a,���`a ���`blw���aoa=���bmia4���`a)���`a,���`a
���`p                ���`fLine2D���`a(���`a[���bmia0���`a]���`a,���`a ���`a[���bmia0���`a]���`a,���`a ���`ecolor���aoa=���`dcmap���`a(���bmfb1.���`a)���`a,���`a ���`blw���aoa=���bmia4���`a)���`a]���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`elines���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`ddata���`a)���`a
���`bax���aoa.���`flegend���`a(���`lcustom_lines���`a,���`a ���`a[���bs1a'���bs1dCold���bs1a'���`a,���`a ���bs1a'���bs1fMedium���bs1a'���`a,���`a ���bs1a'���bs1cHot���bs1a'���`a]���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1xN# There are many other Matplotlib objects that can be used in this way. In the���`a
���bc1x,# code below we've listed a few common ones.���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`ePatch���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnelines���`a ���bknfimport���`a ���`fLine2D���`a
���`a
���`olegend_elements���`a ���aoa=���`a ���`a[���`fLine2D���`a(���`a[���bmia0���`a]���`a,���`a ���`a[���bmia0���`a]���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ab���bs1a'���`a,���`a ���`blw���aoa=���bmia4���`a,���`a ���`elabel���aoa=���bs1a'���bs1dLine���bs1a'���`a)���`a,���`a
���`s                   ���`fLine2D���`a(���`a[���bmia0���`a]���`a,���`a ���`a[���bmia0���`a]���`a,���`a ���`fmarker���aoa=���bs1a'���bs1ao���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1aw���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1gScatter���bs1a'���`a,���`a
���`x                          ���`omarkerfacecolor���aoa=���bs1a'���bs1ag���bs1a'���`a,���`a ���`jmarkersize���aoa=���bmib15���`a)���`a,���`a
���`s                   ���`ePatch���`a(���`ifacecolor���aoa=���bs1a'���bs1forange���bs1a'���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a
���`x                         ���`elabel���aoa=���bs1a'���bs1kColor Patch���bs1a'���`a)���`a]���`a
���`a
���bc1s# Create the figure���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`flegend���`a(���`ghandles���aoa=���`olegend_elements���`a,���`a ���`cloc���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�