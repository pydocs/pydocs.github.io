������������bsdxO"""
=======================
Convert texts to images
=======================
"""���`a
���`a
���bkndfrom���`a ���bnnbio���`a ���bknfimport���`a ���`gBytesIO���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnffigure���`a ���bknfimport���`a ���`fFigure���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnjtransforms���`a ���bknfimport���`a ���`qIdentityTransform���`a
���`a
���`a
���akcdef���`a ���bnfltext_to_rgba���`a(���`as���`a,���`a ���aoa*���`a,���`a ���`cdpi���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`d    ���bc1x/# To convert a text string to an image, we can:���`a
���`d    ���bc1x/# - draw it on an empty and transparent figure;���`a
���`d    ���bc1xF# - save the figure to a temporary buffer using ``bbox_inches="tight",���`a
���`d    ���bc1x<#   pad_inches=0`` which will pick the correct area to save;���`a
���`d    ���bc1x)# - load the buffer using ``plt.imread``.���`a
���`d    ���bc1a#���`a
���`d    ���bc1xG# (If desired, one can also directly save the image to the filesystem.)���`a
���`d    ���`cfig���`a ���aoa=���`a ���`fFigure���`a(���`ifacecolor���aoa=���bs2a"���bs2dnone���bs2a"���`a)���`a
���`d    ���`cfig���aoa.���`dtext���`a(���bmia0���`a,���`a ���bmia0���`a,���`a ���`as���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a
���`d    ���akdwith���`a ���`gBytesIO���`a(���`a)���`a ���akbas���`a ���`cbuf���`a:���`a
���`h        ���`cfig���aoa.���`gsavefig���`a(���`cbuf���`a,���`a ���`cdpi���aoa=���`cdpi���`a,���`a ���bnbfformat���aoa=���bs2a"���bs2cpng���bs2a"���`a,���`a ���`kbbox_inches���aoa=���bs2a"���bs2etight���bs2a"���`a,���`a
���`t                    ���`jpad_inches���aoa=���bmia0���`a)���`a
���`h        ���`cbuf���aoa.���`dseek���`a(���bmia0���`a)���`a
���`h        ���`drgba���`a ���aoa=���`a ���`cplt���aoa.���`fimread���`a(���`cbuf���`a)���`a
���`d    ���akfreturn���`a ���`drgba���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`ergba1���`a ���aoa=���`a ���`ltext_to_rgba���`a(���bsaar���bs2a"���bs2eIQ: $���bs2a\���bs2ksigma_i=15$���bs2a"���`a,���`a ���`ecolor���aoa=���bs2a"���bs2dblue���bs2a"���`a,���`a ���`hfontsize���aoa=���bmib20���`a,���`a ���`cdpi���aoa=���bmic200���`a)���`a
���`ergba2���`a ���aoa=���`a ���`ltext_to_rgba���`a(���bsaar���bs2a"���bs2qsome other string���bs2a"���`a,���`a ���`ecolor���aoa=���bs2a"���bs2cred���bs2a"���`a,���`a ���`hfontsize���aoa=���bmib20���`a,���`a ���`cdpi���aoa=���bmic200���`a)���`a
���bc1xJ# One can then draw such text images to a Figure using `.Figure.figimage`.���`a
���`cfig���aoa.���`hfigimage���`a(���`ergba1���`a,���`a ���bmic100���`a,���`a ���bmib50���`a)���`a
���`cfig���aoa.���`hfigimage���`a(���`ergba2���`a,���`a ���bmic100���`a,���`a ���bmic150���`a)���`a
���`a
���bc1x?# One can also directly draw texts to a figure with positioning���`a
���bc1x<# in pixel coordinates by using `.Figure.text` together with���`a
���bc1x"# `.transforms.IdentityTransform`.���`a
���`cfig���aoa.���`dtext���`a(���bmic100���`a,���`a ���bmic250���`a,���`a ���bsaar���bs2a"���bs2eIQ: $���bs2a\���bs2ksigma_i=15$���bs2a"���`a,���`a ���`ecolor���aoa=���bs2a"���bs2dblue���bs2a"���`a,���`a ���`hfontsize���aoa=���bmib20���`a,���`a
���`i         ���`itransform���aoa=���`qIdentityTransform���`a(���`a)���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmic100���`a,���`a ���bmic350���`a,���`a ���bsaar���bs2a"���bs2qsome other string���bs2a"���`a,���`a ���`ecolor���aoa=���bs2a"���bs2cred���bs2a"���`a,���`a ���`hfontsize���aoa=���bmib20���`a,���`a
���`i         ���`itransform���aoa=���`qIdentityTransform���`a(���`a)���`a)���`a
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
���bc1x*#    - `matplotlib.figure.Figure.figimage`���`a
���bc1x&#    - `matplotlib.figure.Figure.text`���`a
���bc1x0#    - `matplotlib.transforms.IdentityTransform`���`a
���bc1x #    - `matplotlib.image.imread`���`a
`dNone�