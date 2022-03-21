������������bsdy*"""
==========================
Solarized Light stylesheet
==========================

This shows an example of "Solarized_Light" styling, which
tries to replicate the styles of:

- https://ethanschoonover.com/solarized/
- https://github.com/jrnold/ggthemes
- http://www.pygal.org/en/stable/documentation/builtin_styles.html#light-solarized

and work of:

- https://github.com/tonysyu/mpltools

using all 8 accents of the color palette - starting with blue

Still TODO:

- Create alpha values for bar and stacked charts. .33 or .5
- Apply Layout Rules
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmib10���`a)���`a
���akdwith���`a ���`cplt���aoa.���`estyle���aoa.���`gcontext���`a(���bs1a'���bs1oSolarize_Light2���bs1a'���`a)���`a:���`a
���`d    ���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a ���aoa+���`a ���`ax���`a ���aoa+���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmib50���`a)���`a)���`a
���`d    ���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a ���aoa+���`a ���bmia2���`a ���aoa*���`a ���`ax���`a ���aoa+���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmib50���`a)���`a)���`a
���`d    ���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a ���aoa+���`a ���bmia3���`a ���aoa*���`a ���`ax���`a ���aoa+���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmib50���`a)���`a)���`a
���`d    ���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a ���aoa+���`a ���bmia4���`a ���aoa+���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmib50���`a)���`a)���`a
���`d    ���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a ���aoa+���`a ���bmia5���`a ���aoa*���`a ���`ax���`a ���aoa+���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmib50���`a)���`a)���`a
���`d    ���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a ���aoa+���`a ���bmia6���`a ���aoa*���`a ���`ax���`a ���aoa+���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmib50���`a)���`a)���`a
���`d    ���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a ���aoa+���`a ���bmia7���`a ���aoa*���`a ���`ax���`a ���aoa+���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmib50���`a)���`a)���`a
���`d    ���`cplt���aoa.���`dplot���`a(���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a ���aoa+���`a ���bmia8���`a ���aoa*���`a ���`ax���`a ���aoa+���`a ���`bnp���aoa.���`frandom���aoa.���`erandn���`a(���bmib50���`a)���`a)���`a
���`d    ���bc1x-# Number of accent colors in the color scheme���`a
���`d    ���`cplt���aoa.���`etitle���`a(���bs1a'���bs1u8 Random Lines - Line���bs1a'���`a)���`a
���`d    ���`cplt���aoa.���`fxlabel���`a(���bs1a'���bs1gx label���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib14���`a)���`a
���`d    ���`cplt���aoa.���`fylabel���`a(���bs1a'���bs1gy label���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib14���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�