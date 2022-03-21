��������q���bsaar���bsdy�"""
=========================================
The difference between \\dfrac and \\frac
=========================================

In this example, the differences between the \\dfrac and \\frac TeX macros are
illustrated; in particular, the difference between display style and text style
fractions when using Mathtex.

.. versionadded:: 2.1

.. note::
    To use \\dfrac with the LaTeX engine (text.usetex : True), you need to
    import the amsmath package with the text.latex.preamble rc, which is
    an unsupported feature; therefore, it is probably a better idea to just
    use the \\displaystyle option before the \\frac macro to get this behavior
    with the LaTeX engine.

"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmfd5.25���`a,���`a ���bmfd0.75���`a)���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.3���`a,���`a ���bsaar���bs1a'���bs1a\���bs1hdfrac: $���bs1a\���bs1edfrac���bsic{a}���bsic{b}���bs1a$���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.7���`a,���`a ���bsaar���bs1a'���bs1a\���bs1gfrac: $���bs1a\���bs1dfrac���bsic{a}���bsic{b}���bs1a$���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�