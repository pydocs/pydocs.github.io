������������bsdy*"""
=========================================
Setting tick labels from a list of values
=========================================

Using `.Axes.set_xticks` causes the tick labels to be set on the currently
chosen ticks. However, you may want to allow matplotlib to dynamically
choose the number of ticks and their spacing.

In this case it may be better to determine the tick label from the
value at the tick. The following example shows how to do this.

NB: The `.ticker.MaxNLocator` is used here to ensure that the tick values
take integer values.

"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���bknfimport���`a ���`kMaxNLocator���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bxs���`a ���aoa=���`a ���bnberange���`a(���bmib26���`a)���`a
���`bys���`a ���aoa=���`a ���bnberange���`a(���bmib26���`a)���`a
���`flabels���`a ���aoa=���`a ���bnbdlist���`a(���bs1a'���bs1xabcdefghijklmnopqrstuvwxyz���bs1a'���`a)���`a
���`a
���`a
���akcdef���`a ���bnfiformat_fn���`a(���`htick_val���`a,���`a ���`htick_pos���`a)���`a:���`a
���`d    ���akbif���`a ���bnbcint���`a(���`htick_val���`a)���`a ���bowbin���`a ���`bxs���`a:���`a
���`h        ���akfreturn���`a ���`flabels���`a[���bnbcint���`a(���`htick_val���`a)���`a]���`a
���`d    ���akdelse���`a:���`a
���`h        ���akfreturn���`a ���bs1a'���bs1a'���`a
���`a
���`a
���bc1x+# A FuncFormatter is created automatically.���`a
���`bax���aoa.���`exaxis���aoa.���`sset_major_formatter���`a(���`iformat_fn���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`qset_major_locator���`a(���`kMaxNLocator���`a(���`ginteger���aoa=���bkcdTrue���`a)���`a)���`a
���`bax���aoa.���`dplot���`a(���`bxs���`a,���`a ���`bys���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1x##    - `matplotlib.pyplot.subplots`���`a
���bc1x1#    - `matplotlib.axis.Axis.set_major_formatter`���`a
���bc1x/#    - `matplotlib.axis.Axis.set_major_locator`���`a
���bc1x(#    - `matplotlib.ticker.FuncFormatter`���`a
���bc1x&#    - `matplotlib.ticker.MaxNLocator`���`a
`dNone�