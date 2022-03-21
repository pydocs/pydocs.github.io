�����������bsdx�"""
==============================
Create 3D histogram of 2D data
==============================

Demo of a histogram for 2 dimensional data as a bar graph in 3D.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia2���`a,���`a ���bmic100���`a)���`a ���aoa*���`a ���bmia4���`a
���`dhist���`a,���`a ���`fxedges���`a,���`a ���`fyedges���`a ���aoa=���`a ���`bnp���aoa.���`khistogram2d���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`dbins���aoa=���bmia4���`a,���`a ���bnberange���aoa=���`a[���`a[���bmia0���`a,���`a ���bmia4���`a]���`a,���`a ���`a[���bmia0���`a,���`a ���bmia4���`a]���`a]���`a)���`a
���`a
���bc1x;# Construct arrays for the anchor positions of the 16 bars.���`a
���`dxpos���`a,���`a ���`dypos���`a ���aoa=���`a ���`bnp���aoa.���`hmeshgrid���`a(���`fxedges���`a[���`a:���aoa-���bmia1���`a]���`a ���aoa+���`a ���bmfd0.25���`a,���`a ���`fyedges���`a[���`a:���aoa-���bmia1���`a]���`a ���aoa+���`a ���bmfd0.25���`a,���`a ���`hindexing���aoa=���bs2a"���bs2bij���bs2a"���`a)���`a
���`dxpos���`a ���aoa=���`a ���`dxpos���aoa.���`eravel���`a(���`a)���`a
���`dypos���`a ���aoa=���`a ���`dypos���aoa.���`eravel���`a(���`a)���`a
���`dzpos���`a ���aoa=���`a ���bmia0���`a
���`a
���bc1x7# Construct arrays with the dimensions for the 16 bars.���`a
���`bdx���`a ���aoa=���`a ���`bdy���`a ���aoa=���`a ���bmfc0.5���`a ���aoa*���`a ���`bnp���aoa.���`iones_like���`a(���`dzpos���`a)���`a
���`bdz���`a ���aoa=���`a ���`dhist���aoa.���`eravel���`a(���`a)���`a
���`a
���`bax���aoa.���`ebar3d���`a(���`dxpos���`a,���`a ���`dypos���`a,���`a ���`dzpos���`a,���`a ���`bdx���`a,���`a ���`bdy���`a,���`a ���`bdz���`a,���`a ���`ezsort���aoa=���bs1a'���bs1gaverage���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�