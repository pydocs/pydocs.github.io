��������R���bsdxp"""
=============
Font indexing
=============

This example shows how the font tables relate to one another.
"""���`a
���`a
���bknfimport���`a ���bnnbos���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngft2font���`a ���bknfimport���`a ���`a(���`a
���`d    ���`gFT2Font���`a,���`a ���`oKERNING_DEFAULT���`a,���`a ���`pKERNING_UNFITTED���`a,���`a ���`pKERNING_UNSCALED���`a)���`a
���`a
���`a
���`dfont���`a ���aoa=���`a ���`gFT2Font���`a(���`a
���`d    ���`bos���aoa.���`dpath���aoa.���`djoin���`a(���`���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����aoa.���`mget_data_path���`a(���`a)���`a,���`a ���bs1a'���bs1xfonts/ttf/DejaVuSans.ttf���bs1a'���`a)���`a)���`a
���`dfont���aoa.���`kset_charmap���`a(���bmia0���`a)���`a
���`a
���`ecodes���`a ���aoa=���`a ���`dfont���aoa.���`kget_charmap���`a(���`a)���aoa.���`eitems���`a(���`a)���`a
���`a
���bc1x5# make a charname to charcode and glyphind dictionary���`a
���`ecoded���`a ���aoa=���`a ���`a{���`a}���`a
���`fglyphd���`a ���aoa=���`a ���`a{���`a}���`a
���akcfor���`a ���`eccode���`a,���`a ���`hglyphind���`a ���bowbin���`a ���`ecodes���`a:���`a
���`d    ���`dname���`a ���aoa=���`a ���`dfont���aoa.���`nget_glyph_name���`a(���`hglyphind���`a)���`a
���`d    ���`ecoded���`a[���`dname���`a]���`a ���aoa=���`a ���`eccode���`a
���`d    ���`fglyphd���`a[���`dname���`a]���`a ���aoa=���`a ���`hglyphind���`a
���`d    ���bc1x/# print(glyphind, ccode, hex(int(ccode)), name)���`a
���`a
���`dcode���`a ���aoa=���`a ���`ecoded���`a[���bs1a'���bs1aA���bs1a'���`a]���`a
���`eglyph���`a ���aoa=���`a ���`dfont���aoa.���`iload_char���`a(���`dcode���`a)���`a
���bnbeprint���`a(���`eglyph���aoa.���`dbbox���`a)���`a
���bnbeprint���`a(���`fglyphd���`a[���bs1a'���bs1aA���bs1a'���`a]���`a,���`a ���`fglyphd���`a[���bs1a'���bs1aV���bs1a'���`a]���`a,���`a ���`ecoded���`a[���bs1a'���bs1aA���bs1a'���`a]���`a,���`a ���`ecoded���`a[���bs1a'���bs1aV���bs1a'���`a]���`a)���`a
���bnbeprint���`a(���bs1a'���bs1bAV���bs1a'���`a,���`a ���`dfont���aoa.���`kget_kerning���`a(���`fglyphd���`a[���bs1a'���bs1aA���bs1a'���`a]���`a,���`a ���`fglyphd���`a[���bs1a'���bs1aV���bs1a'���`a]���`a,���`a ���`oKERNING_DEFAULT���`a)���`a)���`a
���bnbeprint���`a(���bs1a'���bs1bAV���bs1a'���`a,���`a ���`dfont���aoa.���`kget_kerning���`a(���`fglyphd���`a[���bs1a'���bs1aA���bs1a'���`a]���`a,���`a ���`fglyphd���`a[���bs1a'���bs1aV���bs1a'���`a]���`a,���`a ���`pKERNING_UNFITTED���`a)���`a)���`a
���bnbeprint���`a(���bs1a'���bs1bAV���bs1a'���`a,���`a ���`dfont���aoa.���`kget_kerning���`a(���`fglyphd���`a[���bs1a'���bs1aA���bs1a'���`a]���`a,���`a ���`fglyphd���`a[���bs1a'���bs1aV���bs1a'���`a]���`a,���`a ���`pKERNING_UNSCALED���`a)���`a)���`a
���bnbeprint���`a(���bs1a'���bs1bAT���bs1a'���`a,���`a ���`dfont���aoa.���`kget_kerning���`a(���`fglyphd���`a[���bs1a'���bs1aA���bs1a'���`a]���`a,���`a ���`fglyphd���`a[���bs1a'���bs1aT���bs1a'���`a]���`a,���`a ���`pKERNING_UNSCALED���`a)���`a)���`a
`dNone�