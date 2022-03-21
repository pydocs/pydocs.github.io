������������bsdy�"""
=============
Unicode minus
=============

By default, tick labels at negative values are rendered using a `Unicode
minus`__ (U+2212) rather than an ASCII hyphen (U+002D).  This can be controlled
by setting :rc:`axes.unicode_minus`.

__ https://en.wikipedia.org/wiki/Plus_and_minus_signs#Character_codes

The replacement is performed at draw time of the tick labels (usually during a
`.pyplot.show()` or `.pyplot.savefig()` call). Therefore, all tick labels of
the figure follow the same setting and we cannot demonstrate both glyphs on
real tick labels of the same figure simultaneously.

Instead, this example simply showcases the difference between the two glyphs
in a magnified font.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia4���`a,���`a ���bmia2���`a)���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmfc.15���`a,���`a ���bmfb.6���`a,���`a ���bs2a"���bs2nUnicode minus:���bs2a"���`a,���`a ���`hfontsize���aoa=���bmib20���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmfc.85���`a,���`a ���bmfb.6���`a,���`a ���bs2a"���bsen\N{MINUS SIGN}���bs2a1���bs2a"���`a,���`a ���`bha���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib20���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmfc.15���`a,���`a ���bmfb.3���`a,���`a ���bs2a"���bs2mASCII hyphen:���bs2a"���`a,���`a ���`hfontsize���aoa=���bmib20���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmfc.85���`a,���`a ���bmfb.3���`a,���`a ���bs2a"���bs2b-1���bs2a"���`a,���`a ���`bha���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib20���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�