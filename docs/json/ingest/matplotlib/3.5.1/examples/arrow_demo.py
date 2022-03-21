�����������bsdx�"""
==========
Arrow Demo
==========

Three ways of drawing arrows to encode arrow "strength" (e.g., transition
probabilities in a Markov model) using arrow length, width, or alpha (opacity).
"""���`a
���`a
���bknfimport���`a ���bnniitertools���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akcdef���`a ���bnfpmake_arrow_graph���`a(���`bax���`a,���`a ���`ddata���`a,���`a ���`dsize���aoa=���bmia4���`a,���`a ���`gdisplay���aoa=���bs1a'���bs1flength���bs1a'���`a,���`a ���`eshape���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a
���`u                     ���`omax_arrow_width���aoa=���bmfd0.03���`a,���`a ���`iarrow_sep���aoa=���bmfd0.02���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a,���`a
���`u                     ���`nnormalize_data���aoa=���bkceFalse���`a,���`a ���`bec���aoa=���bkcdNone���`a,���`a ���`jlabelcolor���aoa=���bkcdNone���`a,���`a
���`u                     ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`d    ���bsdy�"""
    Makes an arrow plot.

    Parameters
    ----------
    ax
        The axes where the graph is drawn.
    data
        Dict with probabilities for the bases and pair transitions.
    size
        Size of the plot, in inches.
    display : {'length', 'width', 'alpha'}
        The arrow property to change.
    shape : {'full', 'left', 'right'}
        For full or half arrows.
    max_arrow_width : float
        Maximum width of an arrow, in data coordinates.
    arrow_sep : float
        Separation between arrows in a pair, in data coordinates.
    alpha : float
        Maximum opacity of arrows.
    **kwargs
        `.FancyArrow` properties, e.g. *linewidth* or *edgecolor*.
    """���`a
���`a
���`d    ���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���aoa-���bmfc0.5���`a,���`a ���bmfc1.5���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���bmfc0.5���`a,���`a ���bmfc1.5���`a)���`a,���`a ���`fxticks���aoa=���`a[���`a]���`a,���`a ���`fyticks���aoa=���`a[���`a]���`a)���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfc.01���`a,���`a ���bmfc.01���`a,���`a ���bsaaf���bs1a'���bs1vflux encoded as arrow ���bsia{���`gdisplay���bsia}���bs1a'���`a,���`a
���`l            ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`d    ���`mmax_text_size���`a ���aoa=���`a ���`dsize���`a ���aoa*���`a ���bmib12���`a
���`d    ���`mmin_text_size���`a ���aoa=���`a ���`dsize���`a
���`d    ���`olabel_text_size���`a ���aoa=���`a ���`dsize���`a ���aoa*���`a ���bmfc2.5���`a
���`a
���`d    ���`ebases���`a ���aoa=���`a ���bs1a'���bs1dATGC���bs1a'���`a
���`d    ���`fcoords���`a ���aoa=���`a ���`a{���`a
���`h        ���bs1a'���bs1aA���bs1a'���`a:���`a ���`bnp���aoa.���`earray���`a(���`a[���bmia0���`a,���`a ���bmia1���`a]���`a)���`a,���`a
���`h        ���bs1a'���bs1aT���bs1a'���`a:���`a ���`bnp���aoa.���`earray���`a(���`a[���bmia1���`a,���`a ���bmia1���`a]���`a)���`a,���`a
���`h        ���bs1a'���bs1aG���bs1a'���`a:���`a ���`bnp���aoa.���`earray���`a(���`a[���bmia0���`a,���`a ���bmia0���`a]���`a)���`a,���`a
���`h        ���bs1a'���bs1aC���bs1a'���`a:���`a ���`bnp���aoa.���`earray���`a(���`a[���bmia1���`a,���`a ���bmia0���`a]���`a)���`a,���`a
���`d    ���`a}���`a
���`d    ���`fcolors���`a ���aoa=���`a ���`a{���bs1a'���bs1aA���bs1a'���`a:���`a ���bs1a'���bs1ar���bs1a'���`a,���`a ���bs1a'���bs1aT���bs1a'���`a:���`a ���bs1a'���bs1ak���bs1a'���`a,���`a ���bs1a'���bs1aG���bs1a'���`a:���`a ���bs1a'���bs1ag���bs1a'���`a,���`a ���bs1a'���bs1aC���bs1a'���`a:���`a ���bs1a'���bs1ab���bs1a'���`a}���`a
���`a
���`d    ���akcfor���`a ���`dbase���`a ���bowbin���`a ���`ebases���`a:���`a
���`h        ���`hfontsize���`a ���aoa=���`a ���`bnp���aoa.���`dclip���`a(���`mmax_text_size���`a ���aoa*���`a ���`ddata���`a[���`dbase���`a]���aoa*���aoa*���`a(���bmia1���aoa/���bmia2���`a)���`a,���`a
���`x                           ���`mmin_text_size���`a,���`a ���`mmax_text_size���`a)���`a
���`h        ���`bax���aoa.���`dtext���`a(���aoa*���`fcoords���`a[���`dbase���`a]���`a,���`a ���bsaaf���bs1a'���bs1a$���bsia{���`dbase���bsia}���bs1c_3$���bs1a'���`a,���`a
���`p                ���`ecolor���aoa=���`fcolors���`a[���`dbase���`a]���`a,���`a ���`dsize���aoa=���`hfontsize���`a,���`a
���`p                ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`p                ���`fweight���aoa=���bs1a'���bs1dbold���bs1a'���`a)���`a
���`a
���`d    ���`narrow_h_offset���`a ���aoa=���`a ���bmfd0.25���`b  ���bc1x*# data coordinates, empirically determined���`a
���`d    ���`pmax_arrow_length���`a ���aoa=���`a ���bmia1���`a ���aoa-���`a ���bmia2���`a ���aoa*���`a ���`narrow_h_offset���`a
���`d    ���`nmax_head_width���`a ���aoa=���`a ���bmfc2.5���`a ���aoa*���`a ���`omax_arrow_width���`a
���`d    ���`omax_head_length���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���`omax_arrow_width���`a
���`d    ���`bsf���`a ���aoa=���`a ���bmfc0.6���`b  ���bc1x/# max arrow size represents this in data coords���`a
���`a
���`d    ���akbif���`a ���`nnormalize_data���`a:���`a
���`h        ���bc1x@# find maximum value for rates, i.e. where keys are 2 chars long���`a
���`h        ���`gmax_val���`a ���aoa=���`a ���bnbcmax���`a(���`a(���`av���`a ���akcfor���`a ���`ak���`a,���`a ���`av���`a ���bowbin���`a ���`ddata���aoa.���`eitems���`a(���`a)���`a ���akbif���`a ���bnbclen���`a(���`ak���`a)���`a ���aob==���`a ���bmia2���`a)���`a,���`a ���`gdefault���aoa=���bmia0���`a)���`a
���`h        ���bc1x9# divide rates by max val, multiply by arrow scale factor���`a
���`h        ���akcfor���`a ���`ak���`a,���`a ���`av���`a ���bowbin���`a ���`ddata���aoa.���`eitems���`a(���`a)���`a:���`a
���`l            ���`ddata���`a[���`ak���`a]���`a ���aoa=���`a ���`av���`a ���aoa/���`a ���`gmax_val���`a ���aoa*���`a ���`bsf���`a
���`a
���`d    ���bc1x3# iterate over strings 'AT', 'TA', 'AG', 'GA', etc.���`a
���`d    ���akcfor���`a ���`dpair���`a ���bowbin���`a ���bnbcmap���`a(���bs1a'���bs1a'���aoa.���`djoin���`a,���`a ���`iitertools���aoa.���`lpermutations���`a(���`ebases���`a,���`a ���bmia2���`a)���`a)���`a:���`a
���`h        ���bc1x# set the length of the arrow���`a
���`h        ���akbif���`a ���`gdisplay���`a ���aob==���`a ���bs1a'���bs1flength���bs1a'���`a:���`a
���`l            ���`flength���`a ���aoa=���`a ���`a(���`omax_head_length���`a
���`v                      ���aoa+���`a ���`ddata���`a[���`dpair���`a]���`a ���aoa/���`a ���`bsf���`a ���aoa*���`a ���`a(���`pmax_arrow_length���`a ���aoa-���`a ���`omax_head_length���`a)���`a)���`a
���`h        ���akdelse���`a:���`a
���`l            ���`flength���`a ���aoa=���`a ���`pmax_arrow_length���`a
���`h        ���bc1x## set the transparency of the arrow���`a
���`h        ���akbif���`a ���`gdisplay���`a ���aob==���`a ���bs1a'���bs1ealpha���bs1a'���`a:���`a
���`l            ���`ealpha���`a ���aoa=���`a ���bnbcmin���`a(���`ddata���`a[���`dpair���`a]���`a ���aoa/���`a ���`bsf���`a,���`a ���`ealpha���`a)���`a
���`h        ���bc1x# set the width of the arrow���`a
���`h        ���akbif���`a ���`gdisplay���`a ���aob==���`a ���bs1a'���bs1ewidth���bs1a'���`a:���`a
���`l            ���`escale���`a ���aoa=���`a ���`ddata���`a[���`dpair���`a]���`a ���aoa/���`a ���`bsf���`a
���`l            ���`ewidth���`a ���aoa=���`a ���`omax_arrow_width���`a ���aoa*���`a ���`escale���`a
���`l            ���`jhead_width���`a ���aoa=���`a ���`nmax_head_width���`a ���aoa*���`a ���`escale���`a
���`l            ���`khead_length���`a ���aoa=���`a ���`omax_head_length���`a ���aoa*���`a ���`escale���`a
���`h        ���akdelse���`a:���`a
���`l            ���`ewidth���`a ���aoa=���`a ���`omax_arrow_width���`a
���`l            ���`jhead_width���`a ���aoa=���`a ���`nmax_head_width���`a
���`l            ���`khead_length���`a ���aoa=���`a ���`omax_head_length���`a
���`a
���`h        ���`bfc���`a ���aoa=���`a ���`fcolors���`a[���`dpair���`a[���bmia0���`a]���`a]���`a
���`a
���`h        ���`ccp0���`a ���aoa=���`a ���`fcoords���`a[���`dpair���`a[���bmia0���`a]���`a]���`a
���`h        ���`ccp1���`a ���aoa=���`a ���`fcoords���`a[���`dpair���`a[���bmia1���`a]���`a]���`a
���`h        ���bc1x # unit vector in arrow direction���`a
���`h        ���`edelta���`a ���aoa=���`a ���`ccos���`a,���`a ���`csin���`a ���aoa=���`a ���`a(���`ccp1���`a ���aoa-���`a ���`ccp0���`a)���`a ���aoa/���`a ���`bnp���aoa.���`ehypot���`a(���aoa*���`a(���`ccp1���`a ���aoa-���`a ���`ccp0���`a)���`a)���`a
���`h        ���`ex_pos���`a,���`a ���`ey_pos���`a ���aoa=���`a ���`a(���`a
���`l            ���`a(���`ccp0���`a ���aoa+���`a ���`ccp1���`a)���`a ���aoa/���`a ���bmia2���`b  ���bc1j# midpoint���`a
���`l            ���aoa-���`a ���`edelta���`a ���aoa*���`a ���`flength���`a ���aoa/���`a ���bmia2���`b  ���bc1w# half the arrow length���`a
���`l            ���aoa+���`a ���`bnp���aoa.���`earray���`a(���`a[���aoa-���`csin���`a,���`a ���`ccos���`a]���`a)���`a ���aoa*���`a ���`iarrow_sep���`b  ���bc1x# shift outwards by arrow_sep���`a
���`h        ���`a)���`a
���`h        ���`bax���aoa.���`earrow���`a(���`a
���`l            ���`ex_pos���`a,���`a ���`ey_pos���`a,���`a ���`ccos���`a ���aoa*���`a ���`flength���`a,���`a ���`csin���`a ���aoa*���`a ���`flength���`a,���`a
���`l            ���`bfc���aoa=���`bfc���`a,���`a ���`bec���aoa=���`bec���`a ���bowbor���`a ���`bfc���`a,���`a ���`ealpha���aoa=���`ealpha���`a,���`a ���`ewidth���aoa=���`ewidth���`a,���`a
���`l            ���`jhead_width���aoa=���`jhead_width���`a,���`a ���`khead_length���aoa=���`khead_length���`a,���`a ���`eshape���aoa=���`eshape���`a,���`a
���`l            ���`tlength_includes_head���aoa=���bkcdTrue���`a,���`a
���`h        ���`a)���`a
���`a
���`h        ���bc1x"# figure out coordinates for text:���`a
���`h        ���bc1x<# if drawing relative to base: x and y are same as for arrow���`a
���`h        ���bc1x+# dx and dy are one arrow width left and up���`a
���`h        ���`norig_positions���`a ���aoa=���`a ���`a{���`a
���`l            ���bs1a'���bs1dbase���bs1a'���`a:���`a ���`a[���bmia3���`a ���aoa*���`a ���`omax_arrow_width���`a,���`a ���bmia3���`a ���aoa*���`a ���`omax_arrow_width���`a]���`a,���`a
���`l            ���bs1a'���bs1fcenter���bs1a'���`a:���`a ���`a[���`flength���`a ���aoa/���`a ���bmia2���`a,���`a ���bmia3���`a ���aoa*���`a ���`omax_arrow_width���`a]���`a,���`a
���`l            ���bs1a'���bs1ctip���bs1a'���`a:���`a ���`a[���`flength���`a ���aoa-���`a ���bmia3���`a ���aoa*���`a ���`omax_arrow_width���`a,���`a ���bmia3���`a ���aoa*���`a ���`omax_arrow_width���`a]���`a,���`a
���`h        ���`a}���`a
���`h        ���bc1x6# for diagonal arrows, put the label at the arrow base���`a
���`h        ���bc1x5# for vertical or horizontal arrows, center the label���`a
���`h        ���`ewhere���`a ���aoa=���`a ���bs1a'���bs1dbase���bs1a'���`a ���akbif���`a ���`a(���`ccp0���`a ���aob!=���`a ���`ccp1���`a)���aoa.���`call���`a(���`a)���`a ���akdelse���`a ���bs1a'���bs1fcenter���bs1a'���`a
���`h        ���bc1x/# rotate based on direction of arrow (cos, sin)���`a
���`h        ���`aM���`a ���aoa=���`a ���`a[���`a[���`ccos���`a,���`a ���aoa-���`csin���`a]���`a,���`a ���`a[���`csin���`a,���`a ���`ccos���`a]���`a]���`a
���`h        ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`cdot���`a(���`aM���`a,���`a ���`norig_positions���`a[���`ewhere���`a]���`a)���`a ���aoa+���`a ���`a[���`ex_pos���`a,���`a ���`ey_pos���`a]���`a
���`h        ���`elabel���`a ���aoa=���`a ���bsaar���bs1a'���bs1c$r_���bs1a{���bs1a_���bs1a{���bs1a\���bs1fmathrm���bs1a{���bsib%s���bs1d}}}$���bs1a'���`a ���aoa%���`a ���`a(���`dpair���`a,���`a)���`a
���`h        ���`bax���aoa.���`dtext���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`elabel���`a,���`a ���`dsize���aoa=���`olabel_text_size���`a,���`a ���`bha���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`bva���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`p                ���`ecolor���aoa=���`jlabelcolor���`a ���bowbor���`a ���`bfc���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs1a'���bs1h__main__���bs1a'���`a:���`a
���`d    ���`ddata���`a ���aoa=���`a ���`a{���`b  ���bc1k# test data���`a
���`h        ���bs1a'���bs1aA���bs1a'���`a:���`a ���bmfc0.4���`a,���`a ���bs1a'���bs1aT���bs1a'���`a:���`a ���bmfc0.3���`a,���`a ���bs1a'���bs1aG���bs1a'���`a:���`a ���bmfc0.6���`a,���`a ���bs1a'���bs1aC���bs1a'���`a:���`a ���bmfc0.2���`a,���`a
���`h        ���bs1a'���bs1bAT���bs1a'���`a:���`a ���bmfc0.4���`a,���`a ���bs1a'���bs1bAC���bs1a'���`a:���`a ���bmfc0.3���`a,���`a ���bs1a'���bs1bAG���bs1a'���`a:���`a ���bmfc0.2���`a,���`a
���`h        ���bs1a'���bs1bTA���bs1a'���`a:���`a ���bmfc0.2���`a,���`a ���bs1a'���bs1bTC���bs1a'���`a:���`a ���bmfc0.3���`a,���`a ���bs1a'���bs1bTG���bs1a'���`a:���`a ���bmfc0.4���`a,���`a
���`h        ���bs1a'���bs1bCT���bs1a'���`a:���`a ���bmfc0.2���`a,���`a ���bs1a'���bs1bCG���bs1a'���`a:���`a ���bmfc0.3���`a,���`a ���bs1a'���bs1bCA���bs1a'���`a:���`a ���bmfc0.2���`a,���`a
���`h        ���bs1a'���bs1bGA���bs1a'���`a:���`a ���bmfc0.1���`a,���`a ���bs1a'���bs1bGT���bs1a'���`a:���`a ���bmfc0.4���`a,���`a ���bs1a'���bs1bGC���bs1a'���`a:���`a ���bmfc0.1���`a,���`a
���`d    ���`a}���`a
���`a
���`d    ���`dsize���`a ���aoa=���`a ���bmia4���`a
���`d    ���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia3���`a ���aoa*���`a ���`dsize���`a,���`a ���`dsize���`a)���`a,���`a ���`rconstrained_layout���aoa=���bkcdTrue���`a)���`a
���`d    ���`caxs���`a ���aoa=���`a ���`cfig���aoa.���`nsubplot_mosaic���`a(���`a[���`a[���bs2a"���bs2flength���bs2a"���`a,���`a ���bs2a"���bs2ewidth���bs2a"���`a,���`a ���bs2a"���bs2ealpha���bs2a"���`a]���`a]���`a)���`a
���`a
���`d    ���akcfor���`a ���`gdisplay���`a,���`a ���`bax���`a ���bowbin���`a ���`caxs���aoa.���`eitems���`a(���`a)���`a:���`a
���`h        ���`pmake_arrow_graph���`a(���`a
���`l            ���`bax���`a,���`a ���`ddata���`a,���`a ���`gdisplay���aoa=���`gdisplay���`a,���`a ���`ilinewidth���aoa=���bmfe0.001���`a,���`a ���`iedgecolor���aoa=���bkcdNone���`a,���`a
���`l            ���`nnormalize_data���aoa=���bkcdTrue���`a,���`a ���`dsize���aoa=���`dsize���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�