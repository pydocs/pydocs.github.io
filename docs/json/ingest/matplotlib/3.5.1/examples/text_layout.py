�����������bsdx_"""
===========
Text Layout
===========

Create text with different alignment and rotation.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���akbas���`a ���bnngpatches���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`a
���`dleft���`a,���`a ���`ewidth���`a ���aoa=���`a ���bmfc.25���`a,���`a ���bmfb.5���`a
���`fbottom���`a,���`a ���`fheight���`a ���aoa=���`a ���bmfc.25���`a,���`a ���bmfb.5���`a
���`eright���`a ���aoa=���`a ���`dleft���`a ���aoa+���`a ���`ewidth���`a
���`ctop���`a ���aoa=���`a ���`fbottom���`a ���aoa+���`a ���`fheight���`a
���`a
���bc1xM# Draw a rectangle in figure coordinates ((0, 0) is bottom left and (1, 1) is���`a
���bc1o# upper right).���`a
���`ap���`a ���aoa=���`a ���`gpatches���aoa.���`iRectangle���`a(���`a(���`dleft���`a,���`a ���`fbottom���`a)���`a,���`a ���`ewidth���`a,���`a ���`fheight���`a,���`a ���`dfill���aoa=���bkceFalse���`a)���`a
���`cfig���aoa.���`jadd_artist���`a(���`ap���`a)���`a
���`a
���bc1xM# Figure.text (aka. plt.figtext) behaves like Axes.text (aka. plt.text), with���`a
���bc1xO# the sole exception that the coordinates are relative to the figure ((0, 0) is���`a
���bc1x)# bottom left and (1, 1) is upper right).���`a
���`cfig���aoa.���`dtext���`a(���`dleft���`a,���`a ���`fbottom���`a,���`a ���bs1a'���bs1hleft top���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1dleft���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1ctop���bs1a'���`a)���`a
���`cfig���aoa.���`dtext���`a(���`dleft���`a,���`a ���`fbottom���`a,���`a ���bs1a'���bs1kleft bottom���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1dleft���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`cfig���aoa.���`dtext���`a(���`eright���`a,���`a ���`ctop���`a,���`a ���bs1a'���bs1lright bottom���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`cfig���aoa.���`dtext���`a(���`eright���`a,���`a ���`ctop���`a,���`a ���bs1a'���bs1iright top���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1ctop���bs1a'���`a)���`a
���`cfig���aoa.���`dtext���`a(���`eright���`a,���`a ���`fbottom���`a,���`a ���bs1a'���bs1jcenter top���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1ctop���bs1a'���`a)���`a
���`cfig���aoa.���`dtext���`a(���`dleft���`a,���`a ���bmfc0.5���aoa*���`a(���`fbottom���aoa+���`ctop���`a)���`a,���`a ���bs1a'���bs1lright center���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`i         ���`hrotation���aoa=���bs1a'���bs1hvertical���bs1a'���`a)���`a
���`cfig���aoa.���`dtext���`a(���`dleft���`a,���`a ���bmfc0.5���aoa*���`a(���`fbottom���aoa+���`ctop���`a)���`a,���`a ���bs1a'���bs1kleft center���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1dleft���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`i         ���`hrotation���aoa=���bs1a'���bs1hvertical���bs1a'���`a)���`a
���`cfig���aoa.���`dtext���`a(���bmfc0.5���aoa*���`a(���`dleft���aoa+���`eright���`a)���`a,���`a ���bmfc0.5���aoa*���`a(���`fbottom���aoa+���`ctop���`a)���`a,���`a ���bs1a'���bs1fmiddle���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`i         ���`hfontsize���aoa=���bmib20���`a,���`a ���`ecolor���aoa=���bs1a'���bs1cred���bs1a'���`a)���`a
���`cfig���aoa.���`dtext���`a(���`eright���`a,���`a ���bmfc0.5���aoa*���`a(���`fbottom���aoa+���`ctop���`a)���`a,���`a ���bs1a'���bs1hcentered���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`i         ���`hrotation���aoa=���bs1a'���bs1hvertical���bs1a'���`a)���`a
���`cfig���aoa.���`dtext���`a(���`dleft���`a,���`a ���`ctop���`a,���`a ���bs1a'���bs1grotated���bseb\n���bs1mwith newlines���bs1a'���`a,���`a
���`i         ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`i         ���`hrotation���aoa=���bmib45���`a)���`a
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
���bc1x,#    - `matplotlib.figure.Figure.add_artist`���`a
���bc1x&#    - `matplotlib.figure.Figure.text`���`a
`dNone�