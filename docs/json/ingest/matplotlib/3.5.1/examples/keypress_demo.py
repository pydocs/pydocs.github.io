������������bsdx]"""
==============
Keypress event
==============

Show how to connect to keypress events.
"""���`a
���bknfimport���`a ���bnncsys���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfhon_press���`a(���`eevent���`a)���`a:���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1epress���bs1a'���`a,���`a ���`eevent���aoa.���`ckey���`a)���`a
���`d    ���`csys���aoa.���`fstdout���aoa.���`eflush���`a(���`a)���`a
���`d    ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1ax���bs1a'���`a:���`a
���`h        ���`gvisible���`a ���aoa=���`a ���`bxl���aoa.���`kget_visible���`a(���`a)���`a
���`h        ���`bxl���aoa.���`kset_visible���`a(���bowcnot���`a ���`gvisible���`a)���`a
���`h        ���`cfig���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1okey_press_event���bs1a'���`a,���`a ���`hon_press���`a)���`a
���`a
���`bax���aoa.���`dplot���`a(���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib12���`a)���`a,���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmib12���`a)���`a,���`a ���bs1a'���bs1bgo���bs1a'���`a)���`a
���`bxl���`a ���aoa=���`a ���`bax���aoa.���`jset_xlabel���`a(���bs1a'���bs1reasy come, easy go���bs1a'���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1kPress a key���bs1a'���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�