������������bsdy9"""
========================
Errorbar limit selection
========================

Illustration of selectively drawing lower and/or upper limit symbols on
errorbars using the parameters ``uplims``, ``lolims`` of `~.pyplot.errorbar`.

Alternatively, you can use 2xN values to draw errorbars in only one direction.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmib10���`a)���`a
���`ay���`a ���aoa=���`a ���bmfc2.5���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`ax���`a ���aoa/���`a ���bmib20���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a)���`a
���`dyerr���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmfd0.05���`a,���`a ���bmfc0.2���`a,���`a ���bmib10���`a)���`a
���`a
���`cplt���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmia3���`a,���`a ���`dyerr���aoa=���`dyerr���`a,���`a ���`elabel���aoa=���bs1a'���bs1uboth limits (default)���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmia2���`a,���`a ���`dyerr���aoa=���`dyerr���`a,���`a ���`fuplims���aoa=���bkcdTrue���`a,���`a ���`elabel���aoa=���bs1a'���bs1kuplims=True���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a ���aoa+���`a ���bmia1���`a,���`a ���`dyerr���aoa=���`dyerr���`a,���`a ���`fuplims���aoa=���bkcdTrue���`a,���`a ���`flolims���aoa=���bkcdTrue���`a,���`a
���`m             ���`elabel���aoa=���bs1a'���bs1xuplims=True, lolims=True���bs1a'���`a)���`a
���`a
���`kupperlimits���`a ���aoa=���`a ���`a[���bkcdTrue���`a,���`a ���bkceFalse���`a]���`a ���aoa*���`a ���bmia5���`a
���`klowerlimits���`a ���aoa=���`a ���`a[���bkceFalse���`a,���`a ���bkcdTrue���`a]���`a ���aoa*���`a ���bmia5���`a
���`cplt���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`dyerr���aoa=���`dyerr���`a,���`a ���`fuplims���aoa=���`kupperlimits���`a,���`a ���`flolims���aoa=���`klowerlimits���`a,���`a
���`m             ���`elabel���aoa=���bs1a'���bs1xsubsets of uplims and lolims���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`flegend���`a(���`cloc���aoa=���bs1a'���bs1klower right���bs1a'���`a)���`a
���`a
���`a
���bc1xN##############################################################################���`a
���bc1xN# Similarly ``xuplims`` and ``xlolims`` can be used on the horizontal ``xerr``���`a
���bc1l# errorbars.���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmib10���`a)���`a ���aoa/���`a ���bmib10���`a
���`ay���`a ���aoa=���`a ���`a(���`ax���`a ���aoa+���`a ���bmfc0.1���`a)���aoa*���aoa*���bmia2���`a
���`a
���`cplt���aoa.���`herrorbar���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`dxerr���aoa=���bmfc0.1���`a,���`a ���`gxlolims���aoa=���bkcdTrue���`a,���`a ���`elabel���aoa=���bs1a'���bs1lxlolims=True���bs1a'���`a)���`a
���`ay���`a ���aoa=���`a ���`a(���`ax���`a ���aoa+���`a ���bmfc0.1���`a)���aoa*���aoa*���bmia3���`a
���`a
���`cplt���aoa.���`herrorbar���`a(���`ax���`a ���aoa+���`a ���bmfc0.6���`a,���`a ���`ay���`a,���`a ���`dxerr���aoa=���bmfc0.1���`a,���`a ���`gxuplims���aoa=���`kupperlimits���`a,���`a ���`gxlolims���aoa=���`klowerlimits���`a,���`a
���`m             ���`elabel���aoa=���bs1a'���bs1xsubsets of xuplims and xlolims���bs1a'���`a)���`a
���`a
���`ay���`a ���aoa=���`a ���`a(���`ax���`a ���aoa+���`a ���bmfc0.1���`a)���aoa*���aoa*���bmia4���`a
���`cplt���aoa.���`herrorbar���`a(���`ax���`a ���aoa+���`a ���bmfc1.2���`a,���`a ���`ay���`a,���`a ���`dxerr���aoa=���bmfc0.1���`a,���`a ���`gxuplims���aoa=���bkcdTrue���`a,���`a ���`elabel���aoa=���bs1a'���bs1lxuplims=True���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`flegend���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xN##############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xE#    - `matplotlib.axes.Axes.errorbar` / `matplotlib.pyplot.errorbar`���`a
`dNone�