��������c���bsdy�"""
======================
Text annotations in 3D
======================

Demonstrates the placement of text annotations on a 3D plot.

Functionality shown:

- Using the text function with three types of 'zdir' values: None, an axis
  name (ex. 'x'), or a direction tuple (ex. (1, 1, 0)).
- Using the text function with the color keyword.
- Using the text2D function to place text on a fixed position on the ax
  object.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���bc1n# Demo 1: zdir���`a
���`ezdirs���`a ���aoa=���`a ���`a(���bkcdNone���`a,���`a ���bs1a'���bs1ax���bs1a'���`a,���`a ���bs1a'���bs1ay���bs1a'���`a,���`a ���bs1a'���bs1az���bs1a'���`a,���`a ���`a(���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia0���`a)���`a,���`a ���`a(���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a)���`a)���`a
���`bxs���`a ���aoa=���`a ���`a(���bmia1���`a,���`a ���bmia4���`a,���`a ���bmia4���`a,���`a ���bmia9���`a,���`a ���bmia4���`a,���`a ���bmia1���`a)���`a
���`bys���`a ���aoa=���`a ���`a(���bmia2���`a,���`a ���bmia5���`a,���`a ���bmia8���`a,���`a ���bmib10���`a,���`a ���bmia1���`a,���`a ���bmia2���`a)���`a
���`bzs���`a ���aoa=���`a ���`a(���bmib10���`a,���`a ���bmia3���`a,���`a ���bmia8���`a,���`a ���bmia9���`a,���`a ���bmia1���`a,���`a ���bmia8���`a)���`a
���`a
���akcfor���`a ���`dzdir���`a,���`a ���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a ���bowbin���`a ���bnbczip���`a(���`ezdirs���`a,���`a ���`bxs���`a,���`a ���`bys���`a,���`a ���`bzs���`a)���`a:���`a
���`d    ���`elabel���`a ���aoa=���`a ���bs1a'���bs1a(���bsib%d���bs1b, ���bsib%d���bs1b, ���bsib%d���bs1g), dir=���bsib%s���bs1a'���`a ���aoa%���`a ���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`dzdir���`a)���`a
���`d    ���`bax���aoa.���`dtext���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`elabel���`a,���`a ���`dzdir���`a)���`a
���`a
���bc1o# Demo 2: color���`a
���`bax���aoa.���`dtext���`a(���bmia9���`a,���`a ���bmia0���`a,���`a ���bmia0���`a,���`a ���bs2a"���bs2cred���bs2a"���`a,���`a ���`ecolor���aoa=���bs1a'���bs1cred���bs1a'���`a)���`a
���`a
���bc1p# Demo 3: text2D���`a
���bc1xG# Placement 0, 0 would be the bottom left, 1, 1 would be the top right.���`a
���`bax���aoa.���`ftext2D���`a(���bmfd0.05���`a,���`a ���bmfd0.95���`a,���`a ���bs2a"���bs2g2D Text���bs2a"���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`a
���bc1x$# Tweaking display region and labels���`a
���`bax���aoa.���`hset_xlim���`a(���bmia0���`a,���`a ���bmib10���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���bmia0���`a,���`a ���bmib10���`a)���`a
���`bax���aoa.���`hset_zlim���`a(���bmia0���`a,���`a ���bmib10���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1fX axis���bs1a'���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1fY axis���bs1a'���`a)���`a
���`bax���aoa.���`jset_zlabel���`a(���bs1a'���bs1fZ axis���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�