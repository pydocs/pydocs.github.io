��������t���bsdxY"""
=============
Text Commands
=============

Plotting text of many different kinds.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1tbold figure suptitle���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib14���`a,���`a ���`jfontweight���aoa=���bs1a'���bs1dbold���bs1a'���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`a)���`a
���`cfig���aoa.���`osubplots_adjust���`a(���`ctop���aoa=���bmfd0.85���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1jaxes title���bs1a'���`a)���`a
���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1fxlabel���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1fylabel���bs1a'���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���bmia3���`a,���`a ���bmia8���`a,���`a ���bs1a'���bs1x!boxed italics text in data coords���bs1a'���`a,���`a ���`estyle���aoa=���bs1a'���bs1fitalic���bs1a'���`a,���`a
���`h        ���`dbbox���aoa=���`a{���bs1a'���bs1ifacecolor���bs1a'���`a:���`a ���bs1a'���bs1cred���bs1a'���`a,���`a ���bs1a'���bs1ealpha���bs1a'���`a:���`a ���bmfc0.5���`a,���`a ���bs1a'���bs1cpad���bs1a'���`a:���`a ���bmib10���`a}���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���bmia2���`a,���`a ���bmia6���`a,���`a ���bsaar���bs1a'���bs1uan equation: $E=mc^2$���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib15���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���bmia3���`a,���`a ���bmia2���`a,���`a ���bs1a'���bs1sunicode: Institut f���bsed\374���bs1gr Festk���bsed\366���bs1jrperphysik���bs1a'���`a)���`a
���`a
���`bax���aoa.���`dtext���`a(���bmfd0.95���`a,���`a ���bmfd0.01���`a,���`a ���bs1a'���bs1xcolored text in axes coords���bs1a'���`a,���`a
���`h        ���`qverticalalignment���aoa=���bs1a'���bs1fbottom���bs1a'���`a,���`a ���`shorizontalalignment���aoa=���bs1a'���bs1eright���bs1a'���`a,���`a
���`h        ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a
���`h        ���`ecolor���aoa=���bs1a'���bs1egreen���bs1a'���`a,���`a ���`hfontsize���aoa=���bmib15���`a)���`a
���`a
���`a
���`bax���aoa.���`dplot���`a(���`a[���bmia2���`a]���`a,���`a ���`a[���bmia1���`a]���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a
���`bax���aoa.���`hannotate���`a(���bs1a'���bs1hannotate���bs1a'���`a,���`a ���`bxy���aoa=���`a(���bmia2���`a,���`a ���bmia1���`a)���`a,���`a ���`fxytext���aoa=���`a(���bmia3���`a,���`a ���bmia4���`a)���`a,���`a
���`l            ���`jarrowprops���aoa=���bnbddict���`a(���`ifacecolor���aoa=���bs1a'���bs1eblack���bs1a'���`a,���`a ���`fshrink���aoa=���bmfd0.05���`a)���`a)���`a
���`a
���`bax���aoa.���`cset���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmib10���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia0���`a,���`a ���bmib10���`a)���`a)���`a
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
���bc1x*#    - `matplotlib.figure.Figure.suptitle`���`a
���bc1x-#    - `matplotlib.figure.Figure.add_subplot`���`a
���bc1x1#    - `matplotlib.figure.Figure.subplots_adjust`���`a
���bc1x'#    - `matplotlib.axes.Axes.set_title`���`a
���bc1x(#    - `matplotlib.axes.Axes.set_xlabel`���`a
���bc1x(#    - `matplotlib.axes.Axes.set_ylabel`���`a
���bc1x"#    - `matplotlib.axes.Axes.text`���`a
���bc1x&#    - `matplotlib.axes.Axes.annotate`���`a
`dNone�