������������bsdx�"""
===
MRI
===

This example illustrates how to read an image (of an MRI) into a NumPy
array, and display it in greyscale using `~.axes.Axes.imshow`.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnecbook���`a ���akbas���`a ���bnnecbook���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���bc1x## Data are 256x256 16 bit integers.���`a
���akdwith���`a ���`ecbook���aoa.���`oget_sample_data���`a(���bs1a'���bs1ls1045.ima.gz���bs1a'���`a)���`a ���akbas���`a ���`edfile���`a:���`a
���`d    ���`bim���`a ���aoa=���`a ���`bnp���aoa.���`jfrombuffer���`a(���`edfile���aoa.���`dread���`a(���`a)���`a,���`a ���`bnp���aoa.���`fuint16���`a)���aoa.���`greshape���`a(���`a(���bmic256���`a,���`a ���bmic256���`a)���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`cnum���aoa=���bs2a"���bs2hMRI_demo���bs2a"���`a)���`a
���`bax���aoa.���`fimshow���`a(���`bim���`a,���`a ���`dcmap���aoa=���bs2a"���bs2dgray���bs2a"���`a)���`a
���`bax���aoa.���`daxis���`a(���bs1a'���bs1coff���bs1a'���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�