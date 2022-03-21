������������bsdx~"""
=============
Looking Glass
=============

Example using mouse events to simulate a looking glass for inspecting data.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���akbas���`a ���bnngpatches���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmia2���`a,���`a ���bmic200���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`dcirc���`a ���aoa=���`a ���`gpatches���aoa.���`fCircle���`a(���`a(���bmfc0.5���`a,���`a ���bmfc0.5���`a)���`a,���`a ���bmfd0.25���`a,���`a ���`ealpha���aoa=���bmfc0.8���`a,���`a ���`bfc���aoa=���bs1a'���bs1fyellow���bs1a'���`a)���`a
���`bax���aoa.���`iadd_patch���`a(���`dcirc���`a)���`a
���`a
���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`ealpha���aoa=���bmfc0.2���`a)���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`ealpha���aoa=���bmfc1.0���`a,���`a ���`iclip_path���aoa=���`dcirc���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2x)Left click and drag to move looking glass���bs2a"���`a)���`a
���`a
���`a
���akeclass���`a ���bnclEventHandler���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a)���`a:���`a
���`h        ���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1rbutton_press_event���bs1a'���`a,���`a ���bbpdself���aoa.���`hon_press���`a)���`a
���`h        ���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1tbutton_release_event���bs1a'���`a,���`a ���bbpdself���aoa.���`jon_release���`a)���`a
���`h        ���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1smotion_notify_event���bs1a'���`a,���`a ���bbpdself���aoa.���`gon_move���`a)���`a
���`h        ���bbpdself���aoa.���`bx0���`a,���`a ���bbpdself���aoa.���`by0���`a ���aoa=���`a ���`dcirc���aoa.���`fcenter���`a
���`h        ���bbpdself���aoa.���`jpressevent���`a ���aoa=���`a ���bkcdNone���`a
���`a
���`d    ���akcdef���`a ���bnfhon_press���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���akbif���`a ���`eevent���aoa.���`finaxes���`a ���aob!=���`a ���`bax���`a:���`a
���`l            ���akfreturn���`a
���`a
���`h        ���akbif���`a ���bowcnot���`a ���`dcirc���aoa.���`hcontains���`a(���`eevent���`a)���`a[���bmia0���`a]���`a:���`a
���`l            ���akfreturn���`a
���`a
���`h        ���bbpdself���aoa.���`jpressevent���`a ���aoa=���`a ���`eevent���`a
���`a
���`d    ���akcdef���`a ���bnfjon_release���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`jpressevent���`a ���aoa=���`a ���bkcdNone���`a
���`h        ���bbpdself���aoa.���`bx0���`a,���`a ���bbpdself���aoa.���`by0���`a ���aoa=���`a ���`dcirc���aoa.���`fcenter���`a
���`a
���`d    ���akcdef���`a ���bnfgon_move���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`jpressevent���`a ���bowbis���`a ���bkcdNone���`a ���bowbor���`a ���`eevent���aoa.���`finaxes���`a ���aob!=���`a ���bbpdself���aoa.���`jpressevent���aoa.���`finaxes���`a:���`a
���`l            ���akfreturn���`a
���`a
���`h        ���`bdx���`a ���aoa=���`a ���`eevent���aoa.���`exdata���`a ���aoa-���`a ���bbpdself���aoa.���`jpressevent���aoa.���`exdata���`a
���`h        ���`bdy���`a ���aoa=���`a ���`eevent���aoa.���`eydata���`a ���aoa-���`a ���bbpdself���aoa.���`jpressevent���aoa.���`eydata���`a
���`h        ���`dcirc���aoa.���`fcenter���`a ���aoa=���`a ���bbpdself���aoa.���`bx0���`a ���aoa+���`a ���`bdx���`a,���`a ���bbpdself���aoa.���`by0���`a ���aoa+���`a ���`bdy���`a
���`h        ���`dline���aoa.���`mset_clip_path���`a(���`dcirc���`a)���`a
���`h        ���`cfig���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`ghandler���`a ���aoa=���`a ���`lEventHandler���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�