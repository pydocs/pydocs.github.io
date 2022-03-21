������������bsdxr"""
===================
Image Slices Viewer
===================

Scroll through 2D image slices of a 3D array.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���akeclass���`a ���bnclIndexTracker���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`bax���`a,���`a ���`aX���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`bax���`a ���aoa=���`a ���`bax���`a
���`h        ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x#use scroll wheel to navigate images���bs1a'���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`aX���`a ���aoa=���`a ���`aX���`a
���`h        ���`drows���`a,���`a ���`dcols���`a,���`a ���bbpdself���aoa.���`fslices���`a ���aoa=���`a ���`aX���aoa.���`eshape���`a
���`h        ���bbpdself���aoa.���`cind���`a ���aoa=���`a ���bbpdself���aoa.���`fslices���aoa/���aoa/���bmia2���`a
���`a
���`h        ���bbpdself���aoa.���`bim���`a ���aoa=���`a ���`bax���aoa.���`fimshow���`a(���bbpdself���aoa.���`aX���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bbpdself���aoa.���`cind���`a]���`a)���`a
���`h        ���bbpdself���aoa.���`fupdate���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfion_scroll���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bnbeprint���`a(���bs2a"���bsib%s���bs2a ���bsib%s���bs2a"���`a ���aoa%���`a ���`a(���`eevent���aoa.���`fbutton���`a,���`a ���`eevent���aoa.���`dstep���`a)���`a)���`a
���`h        ���akbif���`a ���`eevent���aoa.���`fbutton���`a ���aob==���`a ���bs1a'���bs1bup���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`cind���`a ���aoa=���`a ���`a(���bbpdself���aoa.���`cind���`a ���aoa+���`a ���bmia1���`a)���`a ���aoa%���`a ���bbpdself���aoa.���`fslices���`a
���`h        ���akdelse���`a:���`a
���`l            ���bbpdself���aoa.���`cind���`a ���aoa=���`a ���`a(���bbpdself���aoa.���`cind���`a ���aoa-���`a ���bmia1���`a)���`a ���aoa%���`a ���bbpdself���aoa.���`fslices���`a
���`h        ���bbpdself���aoa.���`fupdate���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnffupdate���`a(���bbpdself���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`bim���aoa.���`hset_data���`a(���bbpdself���aoa.���`aX���`a[���`a:���`a,���`a ���`a:���`a,���`a ���bbpdself���aoa.���`cind���`a]���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`jset_ylabel���`a(���bs1a'���bs1fslice ���bsib%s���bs1a'���`a ���aoa%���`a ���bbpdself���aoa.���`cind���`a)���`a
���`h        ���bbpdself���aoa.���`bim���aoa.���`daxes���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia1���`a,���`a ���bmia1���`a)���`a
���`a
���`aX���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib20���`a,���`a ���bmib20���`a,���`a ���bmib40���`a)���`a
���`a
���`gtracker���`a ���aoa=���`a ���`lIndexTracker���`a(���`bax���`a,���`a ���`aX���`a)���`a
���`a
���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1lscroll_event���bs1a'���`a,���`a ���`gtracker���aoa.���`ion_scroll���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�