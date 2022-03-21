������������bsdxy"""
=====================
Simple Axes Divider 1
=====================

See also :doc:`/tutorials/toolkits/axes_grid`.
"""���`a
���`a
���bkndfrom���`a ���bnnlmpl_toolkits���bnna.���bnnjaxes_grid1���`a ���bknfimport���`a ���`dSize���`a,���`a ���`gDivider���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfjlabel_axes���`a(���`bax���`a,���`a ���`dtext���`a)���`a:���`a
���`d    ���bsdxH"""Place a label at the center of an axes, and remove the axis ticks."""���`a
���`d    ���`bax���aoa.���`dtext���`a(���bmfb.5���`a,���`a ���bmfb.5���`a,���`a ���`dtext���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a
���`l            ���`shorizontalalignment���aoa=���bs2a"���bs2fcenter���bs2a"���`a,���`a ���`qverticalalignment���aoa=���bs2a"���bs2fcenter���bs2a"���`a)���`a
���`d    ���`bax���aoa.���`ktick_params���`a(���`fbottom���aoa=���bkceFalse���`a,���`a ���`klabelbottom���aoa=���bkceFalse���`a,���`a
���`s                   ���`dleft���aoa=���bkceFalse���`a,���`a ���`ilabelleft���aoa=���bkceFalse���`a)���`a
���`a
���`a
���bc1xN##############################################################################���`a
���bc1x## Fixed axes sizes; fixed paddings.���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs2a"���bs2x Fixed axes sizes, fixed paddings���bs2a"���`a)���`a
���`a
���bc1v# Sizes are in inches.���`a
���`ehoriz���`a ���aoa=���`a ���`a[���`dSize���aoa.���`eFixed���`a(���bmfb1.���`a)���`a,���`a ���`dSize���aoa.���`eFixed���`a(���bmfb.5���`a)���`a,���`a ���`dSize���aoa.���`eFixed���`a(���bmfc1.5���`a)���`a,���`a ���`dSize���aoa.���`eFixed���`a(���bmfb.5���`a)���`a]���`a
���`dvert���`a ���aoa=���`a ���`a[���`dSize���aoa.���`eFixed���`a(���bmfc1.5���`a)���`a,���`a ���`dSize���aoa.���`eFixed���`a(���bmfb.5���`a)���`a,���`a ���`dSize���aoa.���`eFixed���`a(���bmfb1.���`a)���`a]���`a
���`a
���`drect���`a ���aoa=���`a ���`a(���bmfc0.1���`a,���`a ���bmfc0.1���`a,���`a ���bmfc0.8���`a,���`a ���bmfc0.8���`a)���`a
���bc1xM# Divide the axes rectangle into a grid with sizes specified by horiz * vert.���`a
���`cdiv���`a ���aoa=���`a ���`gDivider���`a(���`cfig���`a,���`a ���`drect���`a,���`a ���`ehoriz���`a,���`a ���`dvert���`a,���`a ���`faspect���aoa=���bkceFalse���`a)���`a
���`a
���bc1xM# The rect parameter will actually be ignored and overridden by axes_locator.���`a
���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`drect���`a,���`a ���`laxes_locator���aoa=���`cdiv���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia0���`a,���`a ���`bny���aoa=���bmia0���`a)���`a)���`a
���`jlabel_axes���`a(���`cax1���`a,���`a ���bs2a"���bs2jnx=0, ny=0���bs2a"���`a)���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`drect���`a,���`a ���`laxes_locator���aoa=���`cdiv���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia0���`a,���`a ���`bny���aoa=���bmia2���`a)���`a)���`a
���`jlabel_axes���`a(���`cax2���`a,���`a ���bs2a"���bs2jnx=0, ny=2���bs2a"���`a)���`a
���`cax3���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`drect���`a,���`a ���`laxes_locator���aoa=���`cdiv���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia2���`a,���`a ���`bny���aoa=���bmia2���`a)���`a)���`a
���`jlabel_axes���`a(���`cax3���`a,���`a ���bs2a"���bs2jnx=2, ny=2���bs2a"���`a)���`a
���`cax4���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`drect���`a,���`a ���`laxes_locator���aoa=���`cdiv���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia2���`a,���`a ���`cnx1���aoa=���bmia4���`a,���`a ���`bny���aoa=���bmia0���`a)���`a)���`a
���`jlabel_axes���`a(���`cax4���`a,���`a ���bs2a"���bs2qnx=2, nx1=4, ny=0���bs2a"���`a)���`a
���`a
���bc1xN##############################################################################���`a
���bc1x=# Axes sizes that scale with the figure size; fixed paddings.���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia6���`a,���`a ���bmia6���`a)���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs2a"���bs2x#Scalable axes sizes, fixed paddings���bs2a"���`a)���`a
���`a
���`ehoriz���`a ���aoa=���`a ���`a[���`dSize���aoa.���`fScaled���`a(���bmfc1.5���`a)���`a,���`a ���`dSize���aoa.���`eFixed���`a(���bmfb.5���`a)���`a,���`a ���`dSize���aoa.���`fScaled���`a(���bmfb1.���`a)���`a,���`a ���`dSize���aoa.���`fScaled���`a(���bmfb.5���`a)���`a]���`a
���`dvert���`a ���aoa=���`a ���`a[���`dSize���aoa.���`fScaled���`a(���bmfb1.���`a)���`a,���`a ���`dSize���aoa.���`eFixed���`a(���bmfb.5���`a)���`a,���`a ���`dSize���aoa.���`fScaled���`a(���bmfc1.5���`a)���`a]���`a
���`a
���`drect���`a ���aoa=���`a ���`a(���bmfc0.1���`a,���`a ���bmfc0.1���`a,���`a ���bmfc0.8���`a,���`a ���bmfc0.8���`a)���`a
���bc1xM# Divide the axes rectangle into a grid with sizes specified by horiz * vert.���`a
���`cdiv���`a ���aoa=���`a ���`gDivider���`a(���`cfig���`a,���`a ���`drect���`a,���`a ���`ehoriz���`a,���`a ���`dvert���`a,���`a ���`faspect���aoa=���bkceFalse���`a)���`a
���`a
���bc1xM# The rect parameter will actually be ignored and overridden by axes_locator.���`a
���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`drect���`a,���`a ���`laxes_locator���aoa=���`cdiv���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia0���`a,���`a ���`bny���aoa=���bmia0���`a)���`a)���`a
���`jlabel_axes���`a(���`cax1���`a,���`a ���bs2a"���bs2jnx=0, ny=0���bs2a"���`a)���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`drect���`a,���`a ���`laxes_locator���aoa=���`cdiv���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia0���`a,���`a ���`bny���aoa=���bmia2���`a)���`a)���`a
���`jlabel_axes���`a(���`cax2���`a,���`a ���bs2a"���bs2jnx=0, ny=2���bs2a"���`a)���`a
���`cax3���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`drect���`a,���`a ���`laxes_locator���aoa=���`cdiv���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia2���`a,���`a ���`bny���aoa=���bmia2���`a)���`a)���`a
���`jlabel_axes���`a(���`cax3���`a,���`a ���bs2a"���bs2jnx=2, ny=2���bs2a"���`a)���`a
���`cax4���`a ���aoa=���`a ���`cfig���aoa.���`hadd_axes���`a(���`drect���`a,���`a ���`laxes_locator���aoa=���`cdiv���aoa.���`knew_locator���`a(���`bnx���aoa=���bmia2���`a,���`a ���`cnx1���aoa=���bmia4���`a,���`a ���`bny���aoa=���bmia0���`a)���`a)���`a
���`jlabel_axes���`a(���`cax4���`a,���`a ���bs2a"���bs2qnx=2, nx1=4, ny=0���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�