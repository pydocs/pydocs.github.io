��������_���bsaar���bsdy�"""
==================
Text Rotation Mode
==================

This example illustrates the effect of ``rotation_mode`` on the positioning
of rotated text.

Rotated `.Text`\s are created by passing the parameter ``rotation`` to
the constructor or the axes' method `~.axes.Axes.text`.

The actual positioning depends on the additional parameters
``horizontalalignment``, ``verticalalignment`` and ``rotation_mode``.
``rotation_mode`` determines the order of rotation and alignment:

- ``rotation_mode='default'`` (or None) first rotates the text and then aligns
  the bounding box of the rotated text.
- ``rotation_mode='anchor'`` aligns the unrotated text and then rotates the
  text around the point of alignment.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfrtest_rotation_mode���`a(���`cfig���`a,���`a ���`dmode���`a,���`a ���`psubplot_location���`a)���`a:���`a
���`d    ���`gha_list���`a ���aoa=���`a ���`a[���bs2a"���bs2dleft���bs2a"���`a,���`a ���bs2a"���bs2fcenter���bs2a"���`a,���`a ���bs2a"���bs2eright���bs2a"���`a]���`a
���`d    ���`gva_list���`a ���aoa=���`a ���`a[���bs2a"���bs2ctop���bs2a"���`a,���`a ���bs2a"���bs2fcenter���bs2a"���`a,���`a ���bs2a"���bs2hbaseline���bs2a"���`a,���`a ���bs2a"���bs2fbottom���bs2a"���`a]���`a
���`d    ���`caxs���`a ���aoa=���`a ���`bnp���aoa.���`eempty���`a(���`a(���bnbclen���`a(���`gva_list���`a)���`a,���`a ���bnbclen���`a(���`gha_list���`a)���`a)���`a,���`a ���bnbfobject���`a)���`a
���`d    ���`bgs���`a ���aoa=���`a ���`psubplot_location���aoa.���`ksubgridspec���`a(���aoa*���`caxs���aoa.���`eshape���`a,���`a ���`fhspace���aoa=���bmia0���`a,���`a ���`fwspace���aoa=���bmia0���`a)���`a
���`d    ���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`bgs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a)���`a
���`d    ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`gva_list���`a)���`a)���`a:���`a
���`h        ���akcfor���`a ���`aj���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`gha_list���`a)���`a)���`a:���`a
���`l            ���akbif���`a ���`a(���`ai���`a,���`a ���`aj���`a)���`a ���aob==���`a ���`a(���bmia0���`a,���`a ���bmia0���`a)���`a:���`a
���`p                ���akhcontinue���`b  ���bc1n# Already set.���`a
���`l            ���`caxs���`a[���`ai���`a,���`a ���`aj���`a]���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`a
���`p                ���`bgs���`a[���`ai���`a,���`a ���`aj���`a]���`a,���`a ���`fsharex���aoa=���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a,���`a ���`fsharey���aoa=���`caxs���`a[���bmia0���`a,���`a ���bmia0���`a]���`a)���`a
���`d    ���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`h        ���`bax���aoa.���`cset���`a(���`faspect���aoa=���bmia1���`a)���`a
���`a
���`d    ���bc1r# labels and title���`a
���`d    ���akcfor���`a ���`bha���`a,���`a ���`bax���`a ���bowbin���`a ���bnbczip���`a(���`gha_list���`a,���`a ���`caxs���`a[���aoa-���bmia1���`a,���`a ���`a:���`a]���`a)���`a:���`a
���`h        ���`bax���aoa.���`jset_xlabel���`a(���`bha���`a)���`a
���`d    ���akcfor���`a ���`bva���`a,���`a ���`bax���`a ���bowbin���`a ���bnbczip���`a(���`gva_list���`a,���`a ���`caxs���`a[���`a:���`a,���`a ���bmia0���`a]���`a)���`a:���`a
���`h        ���`bax���aoa.���`jset_ylabel���`a(���`bva���`a)���`a
���`d    ���`caxs���`a[���bmia0���`a,���`a ���bmia1���`a]���aoa.���`iset_title���`a(���bsaaf���bs2a"���bs2nrotation_mode=���bs2a'���bsia{���`dmode���bsia}���bs2a'���bs2a"���`a,���`a ���`dsize���aoa=���bs2a"���bs2elarge���bs2a"���`a)���`a
���`a
���`d    ���`bkw���`a ���aoa=���`a ���`a(���`a
���`h        ���`a{���`a}���`a ���akbif���`a ���`dmode���`a ���aob==���`a ���bs2a"���bs2gdefault���bs2a"���`a ���akdelse���`a
���`h        ���`a{���bs2a"���bs2dbbox���bs2a"���`a:���`a ���bnbddict���`a(���`hboxstyle���aoa=���bs2a"���bs2msquare,pad=0.���bs2a"���`a,���`a ���`bec���aoa=���bs2a"���bs2dnone���bs2a"���`a,���`a ���`bfc���aoa=���bs2a"���bs2bC1���bs2a"���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a)���`a}���`a
���`d    ���`a)���`a
���`a
���`d    ���bc1x-# use a different text alignment in each axes���`a
���`d    ���akcfor���`a ���`ai���`a,���`a ���`bva���`a ���bowbin���`a ���bnbienumerate���`a(���`gva_list���`a)���`a:���`a
���`h        ���akcfor���`a ���`aj���`a,���`a ���`bha���`a ���bowbin���`a ���bnbienumerate���`a(���`gha_list���`a)���`a:���`a
���`l            ���`bax���`a ���aoa=���`a ���`caxs���`a[���`ai���`a,���`a ���`aj���`a]���`a
���`l            ���bc1u# prepare axes layout���`a
���`l            ���`bax���aoa.���`cset���`a(���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a)���`a
���`l            ���`bax���aoa.���`gaxvline���`a(���bmfc0.5���`a,���`a ���`ecolor���aoa=���bs2a"���bs2gskyblue���bs2a"���`a,���`a ���`fzorder���aoa=���bmia0���`a)���`a
���`l            ���`bax���aoa.���`gaxhline���`a(���bmfc0.5���`a,���`a ���`ecolor���aoa=���bs2a"���bs2gskyblue���bs2a"���`a,���`a ���`fzorder���aoa=���bmia0���`a)���`a
���`l            ���`bax���aoa.���`dplot���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���`ecolor���aoa=���bs2a"���bs2bC0���bs2a"���`a,���`a ���`fmarker���aoa=���bs2a"���bs2ao���bs2a"���`a,���`a ���`fzorder���aoa=���bmia1���`a)���`a
���`l            ���bc1x/# add text with rotation and alignment settings���`a
���`l            ���`btx���`a ���aoa=���`a ���`bax���aoa.���`dtext���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a,���`a ���bs2a"���bs2cTpg���bs2a"���`a,���`a
���`x                         ���`dsize���aoa=���bs2a"���bs2gx-large���bs2a"���`a,���`a ���`hrotation���aoa=���bmib40���`a,���`a
���`x                         ���`shorizontalalignment���aoa=���`bha���`a,���`a ���`qverticalalignment���aoa=���`bva���`a,���`a
���`x                         ���`mrotation_mode���aoa=���`dmode���`a,���`a ���aoa*���aoa*���`bkw���`a)���`a
���`a
���`d    ���akbif���`a ���`dmode���`a ���aob==���`a ���bs2a"���bs2gdefault���bs2a"���`a:���`a
���`h        ���bc1p# highlight bbox���`a
���`h        ���`cfig���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`h        ���akcfor���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`dflat���`a:���`a
���`l            ���`dtext���`a,���`a ���aoa=���`a ���`bax���aoa.���`etexts���`a
���`l            ���`bbb���`a ���aoa=���`a ���`dtext���aoa.���`qget_window_extent���`a(���`a)���aoa.���`ktransformed���`a(���`bax���aoa.���`itransData���aoa.���`hinverted���`a(���`a)���`a)���`a
���`l            ���`drect���`a ���aoa=���`a ���`cplt���aoa.���`iRectangle���`a(���`a(���`bbb���aoa.���`bx0���`a,���`a ���`bbb���aoa.���`by0���`a)���`a,���`a ���`bbb���aoa.���`ewidth���`a,���`a ���`bbb���aoa.���`fheight���`a,���`a
���`x!                                 ���`ifacecolor���aoa=���bs2a"���bs2bC1���bs2a"���`a,���`a ���`ealpha���aoa=���bmfc0.3���`a,���`a ���`fzorder���aoa=���bmia2���`a)���`a
���`l            ���`bax���aoa.���`iadd_patch���`a(���`drect���`a)���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia5���`a)���`a)���`a
���`bgs���`a ���aoa=���`a ���`cfig���aoa.���`ladd_gridspec���`a(���bmia1���`a,���`a ���bmia2���`a)���`a
���`rtest_rotation_mode���`a(���`cfig���`a,���`a ���bs2a"���bs2gdefault���bs2a"���`a,���`a ���`bgs���`a[���bmia0���`a]���`a)���`a
���`rtest_rotation_mode���`a(���`cfig���`a,���`a ���bs2a"���bs2fanchor���bs2a"���`a,���`a ���`bgs���`a[���bmia1���`a]���`a)���`a
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
���bc1x=#    - `matplotlib.axes.Axes.text` / `matplotlib.pyplot.text`���`a
`dNone�