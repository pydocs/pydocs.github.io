��������U���bsdx�"""
==================
Contour Label Demo
==================

Illustrate some of the more advanced things that one can do with
contour labels.

See also the :doc:`contour demo example
</gallery/images_contours_and_fields/contour_demo>`.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���akbas���`a ���bnnfticker���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���bc1xO###############################################################################���`a
���bc1t# Define our surface���`a
���`a
���`edelta���`a ���aoa=���`a ���bmfe0.025���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc3.0���`a,���`a ���bmfc3.0���`a,���`a ���`edelta���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���aoa-���bmfc2.0���`a,���`a ���bmfc2.0���`a,���`a ���`edelta���`a)���`a
���`aX���`a,���`a ���`aY���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bZ1���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`aX���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`aY���aoa*���aoa*���bmia2���`a)���`a
���`bZ2���`a ���aoa=���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`a(���`aX���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a ���aoa-���`a ���`a(���`aY���`a ���aoa-���`a ���bmia1���`a)���aoa*���aoa*���bmia2���`a)���`a
���`aZ���`a ���aoa=���`a ���`a(���`bZ1���`a ���aoa-���`a ���`bZ2���`a)���`a ���aoa*���`a ���bmia2���`a
���`a
���bc1xO###############################################################################���`a
���bc1x2# Make contour labels with custom level formatters���`a
���`a
���`a
���bc1xK# This custom formatter removes trailing zeros, e.g. "1.0" becomes "1", and���`a
���bc1x# then adds a percent sign.���`a
���akcdef���`a ���bnfcfmt���`a(���`ax���`a)���`a:���`a
���`d    ���`as���`a ���aoa=���`a ���bsaaf���bs2a"���bsia{���`ax���bsia:���bs2c.1f���bsia}���bs2a"���`a
���`d    ���akbif���`a ���`as���aoa.���`hendswith���`a(���bs2a"���bs2a0���bs2a"���`a)���`a:���`a
���`h        ���`as���`a ���aoa=���`a ���bsaaf���bs2a"���bsia{���`ax���bsia:���bs2c.0f���bsia}���bs2a"���`a
���`d    ���akfreturn���`a ���bsabrf���bs2a"���bsia{���`as���bsia}���bs2a ���bs2a\���bs2a%���bs2a"���`a ���akbif���`a ���`cplt���aoa.���`hrcParams���`a[���bs2a"���bs2ktext.usetex���bs2a"���`a]���`a ���akdelse���`a ���bsaaf���bs2a"���bsia{���`as���bsia}���bs2b %���bs2a"���`a
���`a
���`a
���bc1t# Basic contour plot���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bCS���`a ���aoa=���`a ���`bax���aoa.���`gcontour���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a)���`a
���`a
���`bax���aoa.���`fclabel���`a(���`bCS���`a,���`a ���`bCS���aoa.���`flevels���`a,���`a ���`finline���aoa=���bkcdTrue���`a,���`a ���`cfmt���aoa=���`cfmt���`a,���`a ���`hfontsize���aoa=���bmib10���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x:# Label contours with arbitrary strings using a dictionary���`a
���`a
���`dfig1���`a,���`a ���`cax1���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���bc1t# Basic contour plot���`a
���`cCS1���`a ���aoa=���`a ���`cax1���aoa.���`gcontour���`a(���`aX���`a,���`a ���`aY���`a,���`a ���`aZ���`a)���`a
���`a
���`cfmt���`a ���aoa=���`a ���`a{���`a}���`a
���`dstrs���`a ���aoa=���`a ���`a[���bs1a'���bs1efirst���bs1a'���`a,���`a ���bs1a'���bs1fsecond���bs1a'���`a,���`a ���bs1a'���bs1ethird���bs1a'���`a,���`a ���bs1a'���bs1ffourth���bs1a'���`a,���`a ���bs1a'���bs1efifth���bs1a'���`a,���`a ���bs1a'���bs1esixth���bs1a'���`a,���`a ���bs1a'���bs1gseventh���bs1a'���`a]���`a
���akcfor���`a ���`al���`a,���`a ���`as���`a ���bowbin���`a ���bnbczip���`a(���`cCS1���aoa.���`flevels���`a,���`a ���`dstrs���`a)���`a:���`a
���`d    ���`cfmt���`a[���`al���`a]���`a ���aoa=���`a ���`as���`a
���`a
���bc1x'# Label every other level using strings���`a
���`cax1���aoa.���`fclabel���`a(���`cCS1���`a,���`a ���`cCS1���aoa.���`flevels���`a[���`a:���`a:���bmia2���`a]���`a,���`a ���`finline���aoa=���bkcdTrue���`a,���`a ���`cfmt���aoa=���`cfmt���`a,���`a ���`hfontsize���aoa=���bmib10���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1q# Use a Formatter���`a
���`a
���`dfig2���`a,���`a ���`cax2���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`cCS2���`a ���aoa=���`a ���`cax2���aoa.���`gcontour���`a(���`aX���`a,���`a ���`aY���`a,���`a ���bmic100���aoa*���aoa*���`aZ���`a,���`a ���`glocator���aoa=���`cplt���aoa.���`jLogLocator���`a(���`a)���`a)���`a
���`cfmt���`a ���aoa=���`a ���`fticker���aoa.���`tLogFormatterMathtext���`a(���`a)���`a
���`cfmt���aoa.���`qcreate_dummy_axis���`a(���`a)���`a
���`cax2���aoa.���`fclabel���`a(���`cCS2���`a,���`a ���`cCS2���aoa.���`flevels���`a,���`a ���`cfmt���aoa=���`cfmt���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs2a"���bs2g$100^Z$���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
���`a
���bc1xM#############################################################################���`a
���bc1a#���`a
���bc1x# .. admonition:: References���`a
���bc1a#���`a
���bc1xN#    The use of the following functions, methods, classes and modules is shown���`a
���bc1u#    in this example:���`a
���bc1a#���`a
���bc1xC#    - `matplotlib.axes.Axes.contour` / `matplotlib.pyplot.contour`���`a
���bc1xA#    - `matplotlib.axes.Axes.clabel` / `matplotlib.pyplot.clabel`���`a
���bc1x/#    - `matplotlib.ticker.LogFormatterMathtext`���`a
���bc1x7#    - `matplotlib.ticker.TickHelper.create_dummy_axis`���`a
`dNone�