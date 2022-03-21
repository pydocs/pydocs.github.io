�����������bsdxw"""
=================
Mathtext Examples
=================

Selected features of Matplotlib's math rendering engine.
"""���`a
���bknfimport���`a ���bnnbre���`a
���bknfimport���`a ���bnnjsubprocess���`a
���bknfimport���`a ���bnncsys���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���bc1xN# Selection of features following "Writing mathematical expressions" tutorial,���`a
���bc1x # with randomly picked examples.���`a
���`nmathtext_demos���`a ���aoa=���`a ���`a{���`a
���`d    ���bs2a"���bs2kHeader demo���bs2a"���`a:���`a
���`h        ���bsaar���bs2a"���bs2c$W^���bs2a{���bs2a3���bs2a\���bs2fbeta}_���bs2a{���bs2a\���bs2hdelta_1 ���bs2a\���bs2frho_1 ���bs2a\���bs2ksigma_2} = ���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2bU^���bs2a{���bs2a3���bs2a\���bs2fbeta}_���bs2a{���bs2a\���bs2hdelta_1 ���bs2a\���bs2irho_1} + ���bs2a\���bs2dfrac���bsic{1}���bs2a{���bs2b8 ���bs2a\���bs2fpi 2} ���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2a\���bs2dint^���bs2a{���bs2a\���bs2ialpha_2}_���bs2a{���bs2a\���bs2kalpha_2} d ���bs2a\���bs2falpha^���bs2a\���bs2hprime_2 ���bs2a\���bs2eleft[���bs2a\���bs2dfrac���bs2a{���bs2a ���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2bU^���bs2a{���bs2a2���bs2a\���bs2fbeta}_���bs2a{���bs2a\���bs2hdelta_1 ���bs2a\���bs2irho_1} - ���bs2a\���bs2falpha^���bs2a\���bs2iprime_2U^���bs2a{���bs2a1���bs2a\���bs2fbeta}_���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2a{���bs2a\���bs2frho_1 ���bs2a\���bs2jsigma_2} }���bs2a{���bs2bU^���bs2a{���bs2a0���bs2a\���bs2fbeta}_���bs2a{���bs2a\���bs2frho_1 ���bs2a\���bs2isigma_2}}���bs2a\���bs2gright]$���bs2a"���`a,���`a
���`a
���`d    ���bs2a"���bs2xSubscripts and superscripts���bs2a"���`a:���`a
���`h        ���bsaar���bs2a"���bs2a$���bs2a\���bs2jalpha_i > ���bs2a\���bs2gbeta_i,���bs2a\���bs2a ���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2a\���bs2falpha_���bs2a{���bs2ii+1}^j = ���bs2a{���bs2a\���bs2irm sin}(2���bs2a\���bs2npi f_j t_i) e^���bs2a{���bs2g-5 t_i/���bs2a\���bs2etau},���bs2a\���bs2a ���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2a\���bs2fldots$���bs2a"���`a,���`a
���`a
���`d    ���bs2a"���bs2x(Fractions, binomials and stacked numbers���bs2a"���`a:���`a
���`h        ���bsaar���bs2a"���bs2a$���bs2a\���bs2dfrac���bsic{3}���bsic{4}���bs2a,���bs2a\���bs2a ���bs2a\���bs2ebinom���bsic{3}���bsic{4}���bs2a,���bs2a\���bs2a ���bs2a\���bs2ggenfrac���bsib{}���bsib{}���bsic{0}���bsib{}���bsic{3}���bsic{4}���bs2a,���bs2a\���bs2a ���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2a\���bs2eleft(���bs2a\���bs2dfrac���bs2a{���bs2d5 - ���bs2a\���bs2dfrac���bsic{1}���bsic{x}���bs2a}���bsic{4}���bs2a\���bs2gright),���bs2a\���bs2a ���bs2a\���bs2fldots$���bs2a"���`a,���`a
���`a
���`d    ���bs2a"���bs2hRadicals���bs2a"���`a:���`a
���`h        ���bsaar���bs2a"���bs2a$���bs2a\���bs2dsqrt���bsic{2}���bs2a,���bs2a\���bs2a ���bs2a\���bs2gsqrt[3]���bsic{x}���bs2a,���bs2a\���bs2a ���bs2a\���bs2fldots$���bs2a"���`a,���`a
���`a
���`d    ���bs2a"���bs2eFonts���bs2a"���`a:���`a
���`h        ���bsaar���bs2a"���bs2a$���bs2a\���bs2fmathrm���bsig{Roman}���bs2a\���bs2c , ���bs2a\���bs2a ���bs2a\���bs2fmathit���bsih{Italic}���bs2a\���bs2c , ���bs2a\���bs2a ���bs2a\���bs2fmathtt���bsil{Typewriter}���bs2a ���bs2a\���bs2a ���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2a\���bs2fmathrm���bsid{or}���bs2a\���bs2a ���bs2a\���bs2gmathcal���bsim{CALLIGRAPHY}���bs2a$���bs2a"���`a,���`a
���`a
���`d    ���bs2a"���bs2gAccents���bs2a"���`a:���`a
���`h        ���bsaar���bs2a"���bs2a$���bs2a\���bs2hacute a,���bs2a\���bs2a ���bs2a\���bs2fbar a,���bs2a\���bs2a ���bs2a\���bs2hbreve a,���bs2a\���bs2a ���bs2a\���bs2fdot a,���bs2a\���bs2a ���bs2a\���bs2hddot a, ���bs2a\���bs2a ���bs2a\���bs2igrave a, ���bs2a\���bs2a ���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2a\���bs2fhat a,���bs2a\���bs2a ���bs2a\���bs2htilde a,���bs2a\���bs2a ���bs2a\���bs2fvec a,���bs2a\���bs2a ���bs2a\���bs2gwidehat���bsie{xyz}���bs2a,���bs2a\���bs2a ���bs2a\���bs2iwidetilde���bsie{xyz}���bs2a,���bs2a\���bs2a ���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2a\���bs2fldots$���bs2a"���`a,���`a
���`a
���`d    ���bs2a"���bs2mGreek, Hebrew���bs2a"���`a:���`a
���`h        ���bsaar���bs2a"���bs2a$���bs2a\���bs2falpha,���bs2a\���bs2a ���bs2a\���bs2ebeta,���bs2a\���bs2a ���bs2a\���bs2dchi,���bs2a\���bs2a ���bs2a\���bs2fdelta,���bs2a\���bs2a ���bs2a\���bs2glambda,���bs2a\���bs2a ���bs2a\���bs2cmu,���bs2a\���bs2a ���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2a\���bs2fDelta,���bs2a\���bs2a ���bs2a\���bs2fGamma,���bs2a\���bs2a ���bs2a\���bs2fOmega,���bs2a\���bs2a ���bs2a\���bs2dPhi,���bs2a\���bs2a ���bs2a\���bs2cPi,���bs2a\���bs2a ���bs2a\���bs2hUpsilon,���bs2a\���bs2a ���bs2a\���bs2fnabla,���bs2a\���bs2a ���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2a\���bs2faleph,���bs2a\���bs2a ���bs2a\���bs2ebeth,���bs2a\���bs2a ���bs2a\���bs2gdaleth,���bs2a\���bs2a ���bs2a\���bs2fgimel,���bs2a\���bs2a ���bs2a\���bs2fldots$���bs2a"���`a,���`a
���`a
���`d    ���bs2a"���bs2x!Delimiters, functions and Symbols���bs2a"���`a:���`a
���`h        ���bsaar���bs2a"���bs2a$���bs2a\���bs2gcoprod,���bs2a\���bs2a ���bs2a\���bs2dint,���bs2a\���bs2a ���bs2a\���bs2eoint,���bs2a\���bs2a ���bs2a\���bs2eprod,���bs2a\���bs2a ���bs2a\���bs2dsum,���bs2a\���bs2a ���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2a\���bs2dlog,���bs2a\���bs2a ���bs2a\���bs2dsin,���bs2a\���bs2a ���bs2a\���bs2gapprox,���bs2a\���bs2a ���bs2a\���bs2foplus,���bs2a\���bs2a ���bs2a\���bs2estar,���bs2a\���bs2a ���bs2a\���bs2jvarpropto,���bs2a\���bs2a ���bs2a"���`a
���`h        ���bsaar���bs2a"���bs2a\���bs2finfty,���bs2a\���bs2a ���bs2a\���bs2hpartial,���bs2a\���bs2a ���bs2a\���bs2cRe,���bs2a\���bs2a ���bs2a\���bs2uleftrightsquigarrow, ���bs2a\���bs2a ���bs2a\���bs2fldots$���bs2a"���`a,���`a
���`a}���`a
���`gn_lines���`a ���aoa=���`a ���bnbclen���`a(���`nmathtext_demos���`a)���`a
���`a
���`a
���akcdef���`a ���bnfedoall���`a(���`a)���`a:���`a
���`d    ���bc1x1# Colors used in Matplotlib online documentation.���`a
���`d    ���`lmpl_grey_rgb���`a ���aoa=���`a ���`a(���bmib51���`a ���aoa/���`a ���bmic255���`a,���`a ���bmib51���`a ���aoa/���`a ���bmic255���`a,���`a ���bmib51���`a ���aoa/���`a ���bmic255���`a)���`a
���`a
���`d    ���bc1x# Creating figure and axis.���`a
���`d    ���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia7���`a,���`a ���bmia7���`a)���`a)���`a
���`d    ���`bax���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`a[���bmfd0.01���`a,���`a ���bmfd0.01���`a,���`a ���bmfd0.98���`a,���`a ���bmfd0.90���`a]���`a,���`a
���`v                      ���`ifacecolor���aoa=���bs2a"���bs2ewhite���bs2a"���`a,���`a ���`gframeon���aoa=���bkcdTrue���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmia1���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs2a"���bs2jMatplotlib���bs2a'���bs2ws math rendering engine���bs2a"���`a,���`a
���`q                 ���`ecolor���aoa=���`lmpl_grey_rgb���`a,���`a ���`hfontsize���aoa=���bmib14���`a,���`a ���`fweight���aoa=���bs1a'���bs1dbold���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`jset_xticks���`a(���`a[���`a]���`a)���`a
���`d    ���`bax���aoa.���`jset_yticks���`a(���`a[���`a]���`a)���`a
���`a
���`d    ���bc1x"# Gap between lines in axes coords���`a
���`d    ���`mline_axesfrac���`a ���aoa=���`a ���bmia1���`a ���aoa/���`a ���`gn_lines���`a
���`a
���`d    ���bc1x$# Plot header demonstration formula.���`a
���`d    ���`ifull_demo���`a ���aoa=���`a ���`nmathtext_demos���`a[���bs1a'���bs1kHeader demo���bs1a'���`a]���`a
���`d    ���`bax���aoa.���`hannotate���`a(���`ifull_demo���`a,���`a
���`p                ���`bxy���aoa=���`a(���bmfc0.5���`a,���`a ���bmfb1.���`a ���aoa-���`a ���bmfd0.59���`a ���aoa*���`a ���`mline_axesfrac���`a)���`a,���`a
���`p                ���`ecolor���aoa=���bs1a'���bs1jtab:orange���bs1a'���`a,���`a ���`bha���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib20���`a)���`a
���`a
���`d    ���bc1x&# Plot feature demonstration formulae.���`a
���`d    ���akcfor���`a ���`fi_line���`a,���`a ���`a(���`etitle���`a,���`a ���`ddemo���`a)���`a ���bowbin���`a ���bnbienumerate���`a(���`nmathtext_demos���aoa.���`eitems���`a(���`a)���`a)���`a:���`a
���`h        ���bnbeprint���`a(���`fi_line���`a,���`a ���`ddemo���`a)���`a
���`h        ���akbif���`a ���`fi_line���`a ���aob==���`a ���bmia0���`a:���`a
���`l            ���akhcontinue���`a
���`a
���`h        ���`hbaseline���`a ���aoa=���`a ���bmia1���`a ���aoa-���`a ���`fi_line���`a ���aoa*���`a ���`mline_axesfrac���`a
���`h        ���`mbaseline_next���`a ���aoa=���`a ���`hbaseline���`a ���aoa-���`a ���`mline_axesfrac���`a
���`h        ���`jfill_color���`a ���aoa=���`a ���`a[���bs1a'���bs1ewhite���bs1a'���`a,���`a ���bs1a'���bs1htab:blue���bs1a'���`a]���`a[���`fi_line���`a ���aoa%���`a ���bmia2���`a]���`a
���`h        ���`bax���aoa.���`lfill_between���`a(���`a[���bmia0���`a,���`a ���bmia1���`a]���`a,���`a ���`a[���`hbaseline���`a,���`a ���`hbaseline���`a]���`a,���`a
���`x                        ���`a[���`mbaseline_next���`a,���`a ���`mbaseline_next���`a]���`a,���`a
���`x                        ���`ecolor���aoa=���`jfill_color���`a,���`a ���`ealpha���aoa=���bmfc0.2���`a)���`a
���`h        ���`bax���aoa.���`hannotate���`a(���bsaaf���bs1a'���bsia{���`etitle���bsia}���bs1a:���bs1a'���`a,���`a
���`t                    ���`bxy���aoa=���`a(���bmfd0.06���`a,���`a ���`hbaseline���`a ���aoa-���`a ���bmfc0.3���`a ���aoa*���`a ���`mline_axesfrac���`a)���`a,���`a
���`t                    ���`ecolor���aoa=���`lmpl_grey_rgb���`a,���`a ���`fweight���aoa=���bs1a'���bs1dbold���bs1a'���`a)���`a
���`h        ���`bax���aoa.���`hannotate���`a(���`ddemo���`a,���`a
���`t                    ���`bxy���aoa=���`a(���bmfd0.04���`a,���`a ���`hbaseline���`a ���aoa-���`a ���bmfd0.75���`a ���aoa*���`a ���`mline_axesfrac���`a)���`a,���`a
���`t                    ���`ecolor���aoa=���`lmpl_grey_rgb���`a,���`a ���`hfontsize���aoa=���bmib16���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���akbif���`a ���bs1a'���bs1g--latex���bs1a'���`a ���bowbin���`a ���`csys���aoa.���`dargv���`a:���`a
���`d    ���bc1x*# Run: python mathtext_examples.py --latex���`a
���`d    ���bc1x$# Need amsmath and amssymb packages.���`a
���`d    ���akdwith���`a ���bnbdopen���`a(���bs2a"���bs2umathtext_examples.ltx���bs2a"���`a,���`a ���bs2a"���bs2aw���bs2a"���`a)���`a ���akbas���`a ���`bfd���`a:���`a
���`h        ���`bfd���aoa.���`ewrite���`a(���bs2a"���bseb\\���bs2mdocumentclass���bsii{article}���bseb\n���bs2a"���`a)���`a
���`h        ���`bfd���aoa.���`ewrite���`a(���bs2a"���bseb\\���bs2jusepackage���bs2a{���bs2qamsmath, amssymb}���bseb\n���bs2a"���`a)���`a
���`h        ���`bfd���aoa.���`ewrite���`a(���bs2a"���bseb\\���bs2ebegin���bsij{document}���bseb\n���bs2a"���`a)���`a
���`h        ���`bfd���aoa.���`ewrite���`a(���bs2a"���bseb\\���bs2ebegin���bsik{enumerate}���bseb\n���bs2a"���`a)���`a
���`a
���`h        ���akcfor���`a ���`as���`a ���bowbin���`a ���`nmathtext_demos���aoa.���`fvalues���`a(���`a)���`a:���`a
���`l            ���`as���`a ���aoa=���`a ���`bre���aoa.���`csub���`a(���bsaar���bs2a"���bs2d(?<!���bseb\\���bs2a)���bs2a\���bs2a$���bs2a"���`a,���`a ���bs2a"���bs2b$$���bs2a"���`a,���`a ���`as���`a)���`a
���`l            ���`bfd���aoa.���`ewrite���`a(���bs2a"���bseb\\���bs2eitem ���bsib%s���bseb\n���bs2a"���`a ���aoa%���`a ���`as���`a)���`a
���`a
���`h        ���`bfd���aoa.���`ewrite���`a(���bs2a"���bseb\\���bs2cend���bsik{enumerate}���bseb\n���bs2a"���`a)���`a
���`h        ���`bfd���aoa.���`ewrite���`a(���bs2a"���bseb\\���bs2cend���bsij{document}���bseb\n���bs2a"���`a)���`a
���`a
���`d    ���`jsubprocess���aoa.���`dcall���`a(���`a[���bs2a"���bs2hpdflatex���bs2a"���`a,���`a ���bs2a"���bs2umathtext_examples.ltx���bs2a"���`a]���`a)���`a
���akdelse���`a:���`a
���`d    ���`edoall���`a(���`a)���`a
`dNone�