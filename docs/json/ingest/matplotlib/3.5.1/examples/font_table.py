��������G���bsdy�"""
==========
Font table
==========

Matplotlib's font support is provided by the FreeType library.

Here, we use `~.Axes.table` to draw a table that shows the glyphs by Unicode
codepoint. For brevity, the table only contains the first 256 glyphs.

The example is a full working script. You can download it and use it to
investigate a font by running ::

    python font_table.py /path/to/font/file
"""���`a
���`a
���bknfimport���`a ���bnnbos���`a
���bkndfrom���`a ���bnngpathlib���`a ���bknfimport���`a ���`dPath���`a
���bknfimport���`a ���bnnkunicodedata���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnlfont_manager���`a ���akbas���`a ���bnnbfm���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngft2font���`a ���bknfimport���`a ���`gFT2Font���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnflprint_glyphs���`a(���`dpath���`a)���`a:���`a
���`d    ���bsdx�"""
    Print the all glyphs in the given font file to stdout.

    Parameters
    ----------
    path : str or None
        The path to the font file.  If None, use Matplotlib's default font.
    """���`a
���`d    ���akbif���`a ���`dpath���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`h        ���`dpath���`a ���aoa=���`a ���`bfm���aoa.���`hfindfont���`a(���`bfm���aoa.���`nFontProperties���`a(���`a)���`a)���`b  ���bc1s# The default font.���`a
���`a
���`d    ���`dfont���`a ���aoa=���`a ���`gFT2Font���`a(���`dpath���`a)���`a
���`a
���`d    ���`gcharmap���`a ���aoa=���`a ���`dfont���aoa.���`kget_charmap���`a(���`a)���`a
���`d    ���`omax_indices_len���`a ���aoa=���`a ���bnbclen���`a(���bnbcstr���`a(���bnbcmax���`a(���`gcharmap���aoa.���`fvalues���`a(���`a)���`a)���`a)���`a)���`a
���`a
���`d    ���bnbeprint���`a(���bs2a"���bs2x,The font face contains the following glyphs:���bs2a"���`a)���`a
���`d    ���akcfor���`a ���`ichar_code���`a,���`a ���`kglyph_index���`a ���bowbin���`a ���`gcharmap���aoa.���`eitems���`a(���`a)���`a:���`a
���`h        ���`dchar���`a ���aoa=���`a ���bnbcchr���`a(���`ichar_code���`a)���`a
���`h        ���`dname���`a ���aoa=���`a ���`kunicodedata���aoa.���`dname���`a(���`a
���`p                ���`dchar���`a,���`a
���`p                ���bsaaf���bs2a"���bsia{���`ichar_code���bsia:���bs2b#x���bsia}���bs2b (���bsia{���`dfont���aoa.���`nget_glyph_name���`a(���`kglyph_index���`a)���bsia}���bs2a)���bs2a"���`a)���`a
���`h        ���bnbeprint���`a(���bsaaf���bs2a"���bsia{���`kglyph_index���bsia:���bs2a>���bsia{���`omax_indices_len���bsia}���bsia}���bs2a ���bsia{���`dchar���bsia}���bs2a ���bsia{���`dname���bsia}���bs2a"���`a)���`a
���`a
���`a
���akcdef���`a ���bnfodraw_font_table���`a(���`dpath���`a)���`a:���`a
���`d    ���bsdx�"""
    Draw a font table of the first 255 chars of the given font.

    Parameters
    ----------
    path : str or None
        The path to the font file.  If None, use Matplotlib's default font.
    """���`a
���`d    ���akbif���`a ���`dpath���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`h        ���`dpath���`a ���aoa=���`a ���`bfm���aoa.���`hfindfont���`a(���`bfm���aoa.���`nFontProperties���`a(���`a)���`a)���`b  ���bc1s# The default font.���`a
���`a
���`d    ���`dfont���`a ���aoa=���`a ���`gFT2Font���`a(���`dpath���`a)���`a
���`d    ���bc1xJ# A charmap is a mapping of "character codes" (in the sense of a character���`a
���`d    ���bc1xK# encoding, e.g. latin-1) to glyph indices (i.e. the internal storage table���`a
���`d    ���bc1t# of the font face).���`a
���`d    ���bc1xG# In FreeType>=2.1, a Unicode charmap (i.e. mapping Unicode codepoints)���`a
���`d    ���bc1xE# is selected by default.  Moreover, recent versions of FreeType will���`a
���`d    ���bc1xJ# automatically synthesize such a charmap if the font does not include one���`a
���`d    ���bc1xF# (this behavior depends on the font format; for example it is present���`a
���`d    ���bc1xE# since FreeType 2.0 for Type 1 fonts but only since FreeType 2.8 for���`a
���`d    ���bc1x## TrueType (actually, SFNT) fonts).���`a
���`d    ���bc1xI# The code below (specifically, the ``chr(char_code)`` call) assumes that���`a
���`d    ���bc1x,# we have indeed selected a Unicode charmap.���`a
���`d    ���`ecodes���`a ���aoa=���`a ���`dfont���aoa.���`kget_charmap���`a(���`a)���aoa.���`eitems���`a(���`a)���`a
���`a
���`d    ���`flabelc���`a ���aoa=���`a ���`a[���bs2a"���bsid{:X}���bs2a"���aoa.���`fformat���`a(���`ai���`a)���`a ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmib16���`a)���`a]���`a
���`d    ���`flabelr���`a ���aoa=���`a ���`a[���bs2a"���bsif{:02X}���bs2a"���aoa.���`fformat���`a(���bmib16���`a ���aoa*���`a ���`ai���`a)���`a ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bmib16���`a)���`a]���`a
���`d    ���`echars���`a ���aoa=���`a ���`a[���`a[���bs2a"���bs2a"���`a ���akcfor���`a ���`ac���`a ���bowbin���`a ���bnberange���`a(���bmib16���`a)���`a]���`a ���akcfor���`a ���`ar���`a ���bowbin���`a ���bnberange���`a(���bmib16���`a)���`a]���`a
���`a
���`d    ���akcfor���`a ���`ichar_code���`a,���`a ���`kglyph_index���`a ���bowbin���`a ���`ecodes���`a:���`a
���`h        ���akbif���`a ���`ichar_code���`a ���aoa>���aoa=���`a ���bmic256���`a:���`a
���`l            ���akhcontinue���`a
���`h        ���`crow���`a,���`a ���`ccol���`a ���aoa=���`a ���bnbfdivmod���`a(���`ichar_code���`a,���`a ���bmib16���`a)���`a
���`h        ���`echars���`a[���`crow���`a]���`a[���`ccol���`a]���`a ���aoa=���`a ���bnbcchr���`a(���`ichar_code���`a)���`a
���`a
���`d    ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia4���`a)���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���`bos���aoa.���`dpath���aoa.���`hbasename���`a(���`dpath���`a)���`a)���`a
���`d    ���`bax���aoa.���`lset_axis_off���`a(���`a)���`a
���`a
���`d    ���`etable���`a ���aoa=���`a ���`bax���aoa.���`etable���`a(���`a
���`h        ���`hcellText���aoa=���`echars���`a,���`a
���`h        ���`irowLabels���aoa=���`flabelr���`a,���`a
���`h        ���`icolLabels���aoa=���`flabelc���`a,���`a
���`h        ���`jrowColours���aoa=���`a[���bs2a"���bs2ipalegreen���bs2a"���`a]���`a ���aoa*���`a ���bmib16���`a,���`a
���`h        ���`jcolColours���aoa=���`a[���bs2a"���bs2ipalegreen���bs2a"���`a]���`a ���aoa*���`a ���bmib16���`a,���`a
���`h        ���`kcellColours���aoa=���`a[���`a[���bs2a"���bs2c.95���bs2a"���`a ���akcfor���`a ���`ac���`a ���bowbin���`a ���bnberange���`a(���bmib16���`a)���`a]���`a ���akcfor���`a ���`ar���`a ���bowbin���`a ���bnberange���`a(���bmib16���`a)���`a]���`a,���`a
���`h        ���`gcellLoc���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`h        ���`cloc���aoa=���bs1a'���bs1jupper left���bs1a'���`a,���`a
���`d    ���`a)���`a
���`d    ���akcfor���`a ���`ckey���`a,���`a ���`dcell���`a ���bowbin���`a ���`etable���aoa.���`iget_celld���`a(���`a)���aoa.���`eitems���`a(���`a)���`a:���`a
���`h        ���`crow���`a,���`a ���`ccol���`a ���aoa=���`a ���`ckey���`a
���`h        ���akbif���`a ���`crow���`a ���aoa>���`a ���bmia0���`a ���bowcand���`a ���`ccol���`a ���aoa>���`a ���aoa-���bmia1���`a:���`b  ���bc1x-# Beware of table's idiosyncratic indexing...���`a
���`l            ���`dcell���aoa.���`nset_text_props���`a(���`dfont���aoa=���`dPath���`a(���`dpath���`a)���`a)���`a
���`a
���`d    ���`cfig���aoa.���`ltight_layout���`a(���`a)���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs2a"���bs2h__main__���bs2a"���`a:���`a
���`d    ���bkndfrom���`a ���bnnhargparse���`a ���bknfimport���`a ���`nArgumentParser���`a
���`a
���`d    ���`fparser���`a ���aoa=���`a ���`nArgumentParser���`a(���`kdescription���aoa=���bs2a"���bs2uDisplay a font table.���bs2a"���`a)���`a
���`d    ���`fparser���aoa.���`ladd_argument���`a(���bs2a"���bs2dpath���bs2a"���`a,���`a ���`enargs���aoa=���bs2a"���bs2a?���bs2a"���`a,���`a ���`dhelp���aoa=���bs2a"���bs2vPath to the font file.���bs2a"���`a)���`a
���`d    ���`fparser���aoa.���`ladd_argument���`a(���bs2a"���bs2k--print-all���bs2a"���`a,���`a ���`faction���aoa=���bs2a"���bs2jstore_true���bs2a"���`a,���`a
���`x                        ���`dhelp���aoa=���bs2a"���bs2x(Additionally, print all chars to stdout.���bs2a"���`a)���`a
���`d    ���`dargs���`a ���aoa=���`a ���`fparser���aoa.���`jparse_args���`a(���`a)���`a
���`a
���`d    ���akbif���`a ���`dargs���aoa.���`iprint_all���`a:���`a
���`h        ���`lprint_glyphs���`a(���`dargs���aoa.���`dpath���`a)���`a
���`d    ���`odraw_font_table���`a(���`dargs���aoa.���`dpath���`a)���`a
`dNone�