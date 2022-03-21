������������bsdy<"""
====================================================
Creating boxes from error bars using PatchCollection
====================================================

In this example, we snazz up a pretty standard error bar plot by adding
a rectangle patch defined by the limits of the bars in both the x- and
y- directions. To do this, we have to write our own custom function
called ``make_error_boxes``. Close inspection of this function will
reveal the preferred pattern in writing functions for matplotlib:

  1. an `~.axes.Axes` object is passed directly to the function
  2. the function operates on the ``Axes`` methods directly, not through
     the ``pyplot`` interface
  3. plotting keyword arguments that could be abbreviated are spelled out for
     better code readability in the future (for example we use *facecolor*
     instead of *fc*)
  4. the artists returned by the ``Axes`` plotting methods are then
     returned by the function so that, if desired, their styles
     can be modified later outside of the function (they are not
     modified in this example).
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkcollections���`a ���bknfimport���`a ���`oPatchCollection���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`iRectangle���`a
���`a
���bc1w# Number of data points���`a
���`an���`a ���aoa=���`a ���bmia5���`a
���`a
���bc1l# Dummy data���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���`an���`a,���`a ���bmia1���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���`an���`a)���`a ���aoa*���`a ���bmfb5.���`a
���`a
���bc1x # Dummy errors (above and below)���`a
���`dxerr���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia2���`a,���`a ���`an���`a)���`a ���aoa+���`a ���bmfc0.1���`a
���`dyerr���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia2���`a,���`a ���`an���`a)���`a ���aoa+���`a ���bmfc0.2���`a
���`a
���`a
���akcdef���`a ���bnfpmake_error_boxes���`a(���`bax���`a,���`a ���`exdata���`a,���`a ���`eydata���`a,���`a ���`fxerror���`a,���`a ���`fyerror���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a
���`u                     ���`iedgecolor���aoa=���bs1a'���bs1dnone���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a:���`a
���`a
���`d    ���bc1x=# Loop over data points; create box from errors at each point���`a
���`d    ���`jerrorboxes���`a ���aoa=���`a ���`a[���`iRectangle���`a(���`a(���`ax���`a ���aoa-���`a ���`bxe���`a[���bmia0���`a]���`a,���`a ���`ay���`a ���aoa-���`a ���`bye���`a[���bmia0���`a]���`a)���`a,���`a ���`bxe���aoa.���`csum���`a(���`a)���`a,���`a ���`bye���aoa.���`csum���`a(���`a)���`a)���`a
���`r                  ���akcfor���`a ���`ax���`a,���`a ���`ay���`a,���`a ���`bxe���`a,���`a ���`bye���`a ���bowbin���`a ���bnbczip���`a(���`exdata���`a,���`a ���`eydata���`a,���`a ���`fxerror���aoa.���`aT���`a,���`a ���`fyerror���aoa.���`aT���`a)���`a]���`a
���`a
���`d    ���bc1x5# Create patch collection with specified colour/alpha���`a
���`d    ���`bpc���`a ���aoa=���`a ���`oPatchCollection���`a(���`jerrorboxes���`a,���`a ���`ifacecolor���aoa=���`ifacecolor���`a,���`a ���`ealpha���aoa=���`ealpha���`a,���`a
���`x                         ���`iedgecolor���aoa=���`iedgecolor���`a)���`a
���`a
���`d    ���bc1x# Add collection to axes���`a
���`d    ���`bax���aoa.���`nadd_collection���`a(���`bpc���`a)���`a
���`a
���`d    ���bc1p# Plot errorbars���`a
���`d    ���`gartists���`a ���aoa=���`a ���`bax���aoa.���`herrorbar���`a(���`exdata���`a,���`a ���`eydata���`a,���`a ���`dxerr���aoa=���`fxerror���`a,���`a ���`dyerr���aoa=���`fyerror���`a,���`a
���`x                          ���`cfmt���aoa=���bs1a'���bs1dnone���bs1a'���`a,���`a ���`fecolor���aoa=���bs1a'���bs1ak���bs1a'���`a)���`a
���`a
���`d    ���akfreturn���`a ���`gartists���`a
���`a
���`a
���bc1x# Create figure and axes���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a)���`a
���`a
���bc1x%# Call function to create error boxes���`a
���`a_���`a ���aoa=���`a ���`pmake_error_boxes���`a(���`bax���`a,���`a ���`ax���`a,���`a ���`ay���`a,���`a ���`dxerr���`a,���`a ���`dyerr���`a)���`a
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
���bc1xE#    - `matplotlib.axes.Axes.errorbar` / `matplotlib.pyplot.errorbar`���`a
���bc1x,#    - `matplotlib.axes.Axes.add_collection`���`a
���bc1x/#    - `matplotlib.collections.PatchCollection`���`a
`dNone�