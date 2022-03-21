��������O���bsdyB"""
==============================================
Including upper and lower limits in error bars
==============================================

In matplotlib, errors bars can have "limits". Applying limits to the
error bars essentially makes the error unidirectional. Because of that,
upper and lower limits can be applied in both the y- and x-directions
via the ``uplims``, ``lolims``, ``xuplims``, and ``xlolims`` parameters,
respectively. These parameters can be scalar or boolean arrays.

For example, if ``xlolims`` is ``True``, the x-error bars will only
extend from the data towards increasing values. If ``uplims`` is an
array filled with ``False`` except for the 4th and 7th values, all of the
y-error bars will be bidirectional, except the 4th and 7th bars, which
will extend from the data towards decreasing y-values.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1n# example data���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmfc0.5���`a,���`a ���bmfc1.0���`a,���`a ���bmfc1.5���`a,���`a ���bmfc2.0���`a,���`a ���bmfc2.5���`a,���`a ���bmfc3.0���`a,���`a ���bmfc3.5���`a,���`a ���bmfc4.0���`a,���`a ���bmfc4.5���`a,���`a ���bmfc5.0���`a]���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`ax���`a)���`a
���`dxerr���`a ���aoa=���`a ���bmfc0.1���`a
���`dyerr���`a ���aoa=���`a ���bmfc0.2���`a
���`a
���bc1x## lower & upper limits of the error���`a
���`flolims���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a]���`a,���`a ���`edtype���aoa=���bnbdbool���`a)���`a
���`fuplims���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���`a[���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bmia1���`a]���`a,���`a ���`edtype���aoa=���bnbdbool���`a)���`a
���`bls���`a ���aoa=���`a ���bs1a'���bs1fdotted���bs1a'���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia7���`a,���`a ���bmia4���`a)���`a)���`a
���`a
���bc1u# standard error bars���`a
���`bax���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`dxerr���aoa=���`dxerr���`a,���`a ���`dyerr���aoa=���`dyerr���`a,���`a ���`ilinestyle���aoa=���`bls���`a)���`a
���`a
���bc1x# including upper limits���`a
���`bax���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmfc0.5���`a,���`a ���`dxerr���aoa=���`dxerr���`a,���`a ���`dyerr���aoa=���`dyerr���`a,���`a ���`fuplims���aoa=���`fuplims���`a,���`a
���`l            ���`ilinestyle���aoa=���`bls���`a)���`a
���`a
���bc1x# including lower limits���`a
���`bax���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmfc1.0���`a,���`a ���`dxerr���aoa=���`dxerr���`a,���`a ���`dyerr���aoa=���`dyerr���`a,���`a ���`flolims���aoa=���`flolims���`a,���`a
���`l            ���`ilinestyle���aoa=���`bls���`a)���`a
���`a
���bc1x"# including upper and lower limits���`a
���`bax���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmfc1.5���`a,���`a ���`dxerr���aoa=���`dxerr���`a,���`a ���`dyerr���aoa=���`dyerr���`a,���`a
���`l            ���`flolims���aoa=���`flolims���`a,���`a ���`fuplims���aoa=���`fuplims���`a,���`a
���`l            ���`fmarker���aoa=���bs1a'���bs1ao���bs1a'���`a,���`a ���`jmarkersize���aoa=���bmia8���`a,���`a
���`l            ���`ilinestyle���aoa=���`bls���`a)���`a
���`a
���bc1x9# Plot a series with lower and upper limits in both x & y���`a
���bc1x'# constant x-error with varying y-error���`a
���`dxerr���`a ���aoa=���`a ���bmfc0.2���`a
���`dyerr���`a ���aoa=���`a ���`bnp���aoa.���`ifull_like���`a(���`ax���`a,���`a ���bmfc0.2���`a)���`a
���`dyerr���`a[���`a[���bmia3���`a,���`a ���bmia6���`a]���`a]���`a ���aoa=���`a ���bmfc0.3���`a
���`a
���bc1x0# mock up some limits by modifying previous data���`a
���`gxlolims���`a ���aoa=���`a ���`flolims���`a
���`gxuplims���`a ���aoa=���`a ���`fuplims���`a
���`flolims���`a ���aoa=���`a ���`bnp���aoa.���`jzeros_like���`a(���`ax���`a)���`a
���`fuplims���`a ���aoa=���`a ���`bnp���aoa.���`jzeros_like���`a(���`ax���`a)���`a
���`flolims���`a[���`a[���bmia6���`a]���`a]���`a ���aoa=���`a ���bkcdTrue���`b  ���bc1x# only limited at this index���`a
���`fuplims���`a[���`a[���bmia3���`a]���`a]���`a ���aoa=���`a ���bkcdTrue���`b  ���bc1x# only limited at this index���`a
���`a
���bc1q# do the plotting���`a
���`bax���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmfc2.1���`a,���`a ���`dxerr���aoa=���`dxerr���`a,���`a ���`dyerr���aoa=���`dyerr���`a,���`a
���`l            ���`gxlolims���aoa=���`gxlolims���`a,���`a ���`gxuplims���aoa=���`gxuplims���`a,���`a
���`l            ���`fuplims���aoa=���`fuplims���`a,���`a ���`flolims���aoa=���`flolims���`a,���`a
���`l            ���`fmarker���aoa=���bs1a'���bs1ao���bs1a'���`a,���`a ���`jmarkersize���aoa=���bmia8���`a,���`a
���`l            ���`ilinestyle���aoa=���bs1a'���bs1dnone���bs1a'���`a)���`a
���`a
���bc1t# tidy up the figure���`a
���`bax���aoa.���`hset_xlim���`a(���`a(���bmia0���`a,���`a ���bmfc5.5���`a)���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1xErrorbar upper and lower limits���bs1a'���`a)���`a
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
`dNone�