������������bsdx�"""
===============
Font properties
===============

This example lists the attributes of an `.FT2Font` object, which describe
global font properties.  For individual character metrics, use the `.Glyph`
object, as returned by `.load_char`.
"""���`a
���`a
���bknfimport���`a ���bnnbos���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngft2font���`a ���akbas���`a ���bnnbft���`a
���`a
���`a
���`dfont���`a ���aoa=���`a ���`bft���aoa.���`gFT2Font���`a(���`a
���`d    ���bc1x%# Use a font shipped with Matplotlib.���`a
���`d    ���`bos���aoa.���`dpath���aoa.���`djoin���`a(���`���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����aoa.���`mget_data_path���`a(���`a)���`a,���`a
���`q                 ���bs1a'���bs1x fonts/ttf/DejaVuSans-Oblique.ttf���bs1a'���`a)���`a)���`a
���`a
���bnbeprint���`a(���bs1a'���bs1lNum faces:  ���bs1a'���`a,���`a ���`dfont���aoa.���`inum_faces���`a)���`h        ���bc1x# number of faces in file���`a
���bnbeprint���`a(���bs1a'���bs1lNum glyphs: ���bs1a'���`a,���`a ���`dfont���aoa.���`jnum_glyphs���`a)���`g       ���bc1x# number of glyphs in the face���`a
���bnbeprint���`a(���bs1a'���bs1lFamily name:���bs1a'���`a,���`a ���`dfont���aoa.���`kfamily_name���`a)���`f      ���bc1r# face family name���`a
���bnbeprint���`a(���bs1a'���bs1lStyle name: ���bs1a'���`a,���`a ���`dfont���aoa.���`jstyle_name���`a)���`g       ���bc1q# face style name���`a
���bnbeprint���`a(���bs1a'���bs1lPS name:    ���bs1a'���`a,���`a ���`dfont���aoa.���`opostscript_name���`a)���`b  ���bc1u# the postscript name���`a
���bnbeprint���`a(���bs1a'���bs1lNum fixed:  ���bs1a'���`a,���`a ���`dfont���aoa.���`onum_fixed_sizes���`a)���`b  ���bc1x# number of embedded bitmaps���`a
���`a
���bc1x3# the following are only available if face.scalable���`a
���akbif���`a ���`dfont���aoa.���`hscalable���`a:���`a
���`d    ���bc1x7# the face global bounding box (xmin, ymin, xmax, ymax)���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1tBbox:               ���bs1a'���`a,���`a ���`dfont���aoa.���`dbbox���`a)���`a
���`d    ���bc1x(# number of font units covered by the EM���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1tEM:                 ���bs1a'���`a,���`a ���`dfont���aoa.���`lunits_per_EM���`a)���`a
���`d    ���bc1x# the ascender in 26.6 units���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1tAscender:           ���bs1a'���`a,���`a ���`dfont���aoa.���`hascender���`a)���`a
���`d    ���bc1x# the descender in 26.6 units���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1tDescender:          ���bs1a'���`a,���`a ���`dfont���aoa.���`idescender���`a)���`a
���`d    ���bc1x# the height in 26.6 units���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1tHeight:             ���bs1a'���`a,���`a ���`dfont���aoa.���`fheight���`a)���`a
���`d    ���bc1x## maximum horizontal cursor advance���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1tMax adv width:      ���bs1a'���`a,���`a ���`dfont���aoa.���`qmax_advance_width���`a)���`a
���`d    ���bc1x# same for vertical layout���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1tMax adv height:     ���bs1a'���`a,���`a ���`dfont���aoa.���`rmax_advance_height���`a)���`a
���`d    ���bc1x(# vertical position of the underline bar���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1tUnderline pos:      ���bs1a'���`a,���`a ���`dfont���aoa.���`runderline_position���`a)���`a
���`d    ���bc1x%# vertical thickness of the underline���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1tUnderline thickness:���bs1a'���`a,���`a ���`dfont���aoa.���`sunderline_thickness���`a)���`a
���`a
���akcfor���`a ���`estyle���`a ���bowbin���`a ���`a(���bs1a'���bs1fItalic���bs1a'���`a,���`a
���`n              ���bs1a'���bs1dBold���bs1a'���`a,���`a
���`n              ���bs1a'���bs1hScalable���bs1a'���`a,���`a
���`n              ���bs1a'���bs1kFixed sizes���bs1a'���`a,���`a
���`n              ���bs1a'���bs1kFixed width���bs1a'���`a,���`a
���`n              ���bs1a'���bs1dSFNT���bs1a'���`a,���`a
���`n              ���bs1a'���bs1jHorizontal���bs1a'���`a,���`a
���`n              ���bs1a'���bs1hVertical���bs1a'���`a,���`a
���`n              ���bs1a'���bs1gKerning���bs1a'���`a,���`a
���`n              ���bs1a'���bs1kFast glyphs���bs1a'���`a,���`a
���`n              ���bs1a'���bs1pMultiple masters���bs1a'���`a,���`a
���`n              ���bs1a'���bs1kGlyph names���bs1a'���`a,���`a
���`n              ���bs1a'���bs1oExternal stream���bs1a'���`a)���`a:���`a
���`d    ���`fbitpos���`a ���aoa=���`a ���bnbggetattr���`a(���`bft���`a,���`a ���`estyle���aoa.���`greplace���`a(���bs1a'���bs1a ���bs1a'���`a,���`a ���bs1a'���bs1a_���bs1a'���`a)���aoa.���`eupper���`a(���`a)���`a)���`a ���aoa-���`a ���bmia1���`a
���`d    ���bnbeprint���`a(���bsaaf���bs2a"���bsia{���`estyle���aoa+���bs1a'���bs1a:���bs1a'���bsia:���bs2b17���bsia}���bs2a"���`a,���`a ���bnbdbool���`a(���`dfont���aoa.���`kstyle_flags���`a ���aoa&���`a ���`a(���bmia1���`a ���aob<<���`a ���`fbitpos���`a)���`a)���`a)���`a
`dNone�