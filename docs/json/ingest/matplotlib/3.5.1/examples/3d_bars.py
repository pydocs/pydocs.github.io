������������bsdx�"""
=====================
Demo of 3D bar charts
=====================

A basic demo of how to plot 3D bars with and without shading.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���bc1x# setup the figure and axes���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia8���`a,���`a ���bmia3���`a)���`a)���`a
���`cax1���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmic121���`a,���`a ���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`cax2���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmic122���`a,���`a ���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���bc1k# fake data���`a
���`b_x���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia4���`a)���`a
���`b_y���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia5���`a)���`a
���`c_xx���`a,���`a ���`c_yy���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`b_x���`a,���`a ���`b_y���`a)���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`c_xx���aoa.���`eravel���`a(���`a)���`a,���`a ���`c_yy���aoa.���`eravel���`a(���`a)���`a
���`a
���`ctop���`a ���aoa=���`a ���`ax���`a ���aoa+���`a ���`ay���`a
���`fbottom���`a ���aoa=���`a ���`bnp���aoa.���`jzeros_like���`a(���`ctop���`a)���`a
���`ewidth���`a ���aoa=���`a ���`edepth���`a ���aoa=���`a ���bmia1���`a
���`a
���`cax1���aoa.���`ebar3d���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`fbottom���`a,���`a ���`ewidth���`a,���`a ���`edepth���`a,���`a ���`ctop���`a,���`a ���`eshade���aoa=���bkcdTrue���`a)���`a
���`cax1���aoa.���`iset_title���`a(���bs1a'���bs1fShaded���bs1a'���`a)���`a
���`a
���`cax2���aoa.���`ebar3d���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`fbottom���`a,���`a ���`ewidth���`a,���`a ���`edepth���`a,���`a ���`ctop���`a,���`a ���`eshade���aoa=���bkceFalse���`a)���`a
���`cax2���aoa.���`iset_title���`a(���bs1a'���bs1jNot Shaded���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�