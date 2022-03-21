�����������bsdy("""
==============================
Plotting masked and NaN values
==============================

Sometimes you need to plot data with missing values.

One possibility is to simply remove undesired data points. The line plotted
through the remaining data will be continuous, and not indicate where the
missing data is located.

If it is useful to have gaps in the line where the data is missing, then the
undesired points can be indicated using a `masked array`_ or by setting their
values to NaN. No marker will be drawn where either x or y are masked and, if
plotting with a line, it will be broken there.

.. _masked array:
   https://numpy.org/doc/stable/reference/maskedarray.generic.html

The following example illustrates the three cases:

1) Removing points.
2) Masking points.
3) Setting to NaN.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���`bnp���aoa.���`bpi���aoa/���bmia2���`a,���`a ���`bnp���aoa.���`bpi���aoa/���bmia2���`a,���`a ���bmib31���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`ccos���`a(���`ax���`a)���aoa*���aoa*���bmia3���`a
���`a
���bc1x # 1) remove points where y > 0.7���`a
���`bx2���`a ���aoa=���`a ���`ax���`a[���`ay���`a ���aoa<���aoa=���`a ���bmfc0.7���`a]���`a
���`by2���`a ���aoa=���`a ���`ay���`a[���`ay���`a ���aoa<���aoa=���`a ���bmfc0.7���`a]���`a
���`a
���bc1x# 2) mask points where y > 0.7���`a
���`by3���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`lmasked_where���`a(���`ay���`a ���aoa>���`a ���bmfc0.7���`a,���`a ���`ay���`a)���`a
���`a
���bc1x# 3) set to NaN where y > 0.7���`a
���`by4���`a ���aoa=���`a ���`ay���aoa.���`dcopy���`a(���`a)���`a
���`by4���`a[���`by3���`a ���aoa>���`a ���bmfc0.7���`a]���`a ���aoa=���`a ���`bnp���aoa.���`cnan���`a
���`a
���`cplt���aoa.���`dplot���`a(���`ax���aoa*���bmfc0.1���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1bo-���bs1a'���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ilightgrey���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1gNo mask���bs1a'���`a)���`a
���`cplt���aoa.���`dplot���`a(���`bx2���aoa*���bmfc0.4���`a,���`a ���`by2���`a,���`a ���bs1a'���bs1bo-���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1nPoints removed���bs1a'���`a)���`a
���`cplt���aoa.���`dplot���`a(���`ax���aoa*���bmfc0.7���`a,���`a ���`by3���`a,���`a ���bs1a'���bs1bo-���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1mMasked values���bs1a'���`a)���`a
���`cplt���aoa.���`dplot���`a(���`ax���aoa*���bmfc1.0���`a,���`a ���`by4���`a,���`a ���bs1a'���bs1bo-���bs1a'���`a,���`a ���`elabel���aoa=���bs1a'���bs1jNaN values���bs1a'���`a)���`a
���`cplt���aoa.���`flegend���`a(���`a)���`a
���`cplt���aoa.���`etitle���`a(���bs1a'���bs1sMasked and NaN data���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�