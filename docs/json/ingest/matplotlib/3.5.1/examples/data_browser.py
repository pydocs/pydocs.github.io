��������$���bsdy"""
============
Data Browser
============

Connecting data between multiple canvases.

This example covers how to interact data with multiple canvases. This
let's you select and highlight a point on one axis, and generating the
data of that point on the other axis.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akeclass���`a ���bnclPointBrowser���`a:���`a
���`d    ���bsdx�"""
    Click on a point to select and highlight it -- the data that
    generated the point will be shown in the lower axes.  Use the 'n'
    and 'p' keys to browse through the next and previous points
    """���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`glastind���`a ���aoa=���`a ���bmia0���`a
���`a
���`h        ���bbpdself���aoa.���`dtext���`a ���aoa=���`a ���`bax���aoa.���`dtext���`a(���bmfd0.05���`a,���`a ���bmfd0.95���`a,���`a ���bs1a'���bs1nselected: none���bs1a'���`a,���`a
���`x                            ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a,���`a ���`bva���aoa=���bs1a'���bs1ctop���bs1a'���`a)���`a
���`h        ���bbpdself���aoa.���`hselected���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`a[���`bxs���`a[���bmia0���`a]���`a]���`a,���`a ���`a[���`bys���`a[���bmia0���`a]���`a]���`a,���`a ���bs1a'���bs1ao���bs1a'���`a,���`a ���`bms���aoa=���bmib12���`a,���`a ���`ealpha���aoa=���bmfc0.4���`a,���`a
���`x!                                 ���`ecolor���aoa=���bs1a'���bs1fyellow���bs1a'���`a,���`a ���`gvisible���aoa=���bkceFalse���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfhon_press���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`glastind���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���akfreturn���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���bowcnot���`a ���bowbin���`a ���`a(���bs1a'���bs1an���bs1a'���`a,���`a ���bs1a'���bs1ap���bs1a'���`a)���`a:���`a
���`l            ���akfreturn���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1an���bs1a'���`a:���`a
���`l            ���`cinc���`a ���aoa=���`a ���bmia1���`a
���`h        ���akdelse���`a:���`a
���`l            ���`cinc���`a ���aoa=���`a ���aoa-���bmia1���`a
���`a
���`h        ���bbpdself���aoa.���`glastind���`a ���aoa+���aoa=���`a ���`cinc���`a
���`h        ���bbpdself���aoa.���`glastind���`a ���aoa=���`a ���`bnp���aoa.���`dclip���`a(���bbpdself���aoa.���`glastind���`a,���`a ���bmia0���`a,���`a ���bnbclen���`a(���`bxs���`a)���`a ���aoa-���`a ���bmia1���`a)���`a
���`h        ���bbpdself���aoa.���`fupdate���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfgon_pick���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`a
���`h        ���akbif���`a ���`eevent���aoa.���`fartist���`a ���aob!=���`a ���`dline���`a:���`a
���`l            ���akfreturn���`a ���bkcdTrue���`a
���`a
���`h        ���`aN���`a ���aoa=���`a ���bnbclen���`a(���`eevent���aoa.���`cind���`a)���`a
���`h        ���akbif���`a ���bowcnot���`a ���`aN���`a:���`a
���`l            ���akfreturn���`a ���bkcdTrue���`a
���`a
���`h        ���bc1u# the click locations���`a
���`h        ���`ax���`a ���aoa=���`a ���`eevent���aoa.���`jmouseevent���aoa.���`exdata���`a
���`h        ���`ay���`a ���aoa=���`a ���`eevent���aoa.���`jmouseevent���aoa.���`eydata���`a
���`a
���`h        ���`idistances���`a ���aoa=���`a ���`bnp���aoa.���`ehypot���`a(���`ax���`a ���aoa-���`a ���`bxs���`a[���`eevent���aoa.���`cind���`a]���`a,���`a ���`ay���`a ���aoa-���`a ���`bys���`a[���`eevent���aoa.���`cind���`a]���`a)���`a
���`h        ���`findmin���`a ���aoa=���`a ���`idistances���aoa.���`fargmin���`a(���`a)���`a
���`h        ���`gdataind���`a ���aoa=���`a ���`eevent���aoa.���`cind���`a[���`findmin���`a]���`a
���`a
���`h        ���bbpdself���aoa.���`glastind���`a ���aoa=���`a ���`gdataind���`a
���`h        ���bbpdself���aoa.���`fupdate���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnffupdate���`a(���bbpdself���`a)���`a:���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`glastind���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���akfreturn���`a
���`a
���`h        ���`gdataind���`a ���aoa=���`a ���bbpdself���aoa.���`glastind���`a
���`a
���`h        ���`cax2���aoa.���`ccla���`a(���`a)���`a
���`h        ���`cax2���aoa.���`dplot���`a(���`aX���`a[���`gdataind���`a]���`a)���`a
���`a
���`h        ���`cax2���aoa.���`dtext���`a(���bmfd0.05���`a,���`a ���bmfc0.9���`a,���`a ���bsaaf���bs1a'���bs1cmu=���bsia{���`bxs���`a[���`gdataind���`a]���bsia:���bs1d1.3f���bsia}���bseb\n���bs1fsigma=���bsia{���`bys���`a[���`gdataind���`a]���bsia:���bs1d1.3f���bsia}���bs1a'���`a,���`a
���`q                 ���`itransform���aoa=���`cax2���aoa.���`itransAxes���`a,���`a ���`bva���aoa=���bs1a'���bs1ctop���bs1a'���`a)���`a
���`h        ���`cax2���aoa.���`hset_ylim���`a(���aoa-���bmfc0.5���`a,���`a ���bmfc1.5���`a)���`a
���`h        ���bbpdself���aoa.���`hselected���aoa.���`kset_visible���`a(���bkcdTrue���`a)���`a
���`h        ���bbpdself���aoa.���`hselected���aoa.���`hset_data���`a(���`bxs���`a[���`gdataind���`a]���`a,���`a ���`bys���`a[���`gdataind���`a]���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`dtext���aoa.���`hset_text���`a(���bs1a'���bs1jselected: ���bsib%d���bs1a'���`a ���aoa%���`a ���`gdataind���`a)���`a
���`h        ���`cfig���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs1a'���bs1h__main__���bs1a'���`a:���`a
���`d    ���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`d    ���bc1x)# Fixing random state for reproducibility���`a
���`d    ���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`d    ���`aX���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmic100���`a,���`a ���bmic200���`a)���`a
���`d    ���`bxs���`a ���aoa=���`a ���`bnp���aoa.���`dmean���`a(���`aX���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`d    ���`bys���`a ���aoa=���`a ���`bnp���aoa.���`cstd���`a(���`aX���`a,���`a ���`daxis���aoa=���bmia1���`a)���`a
���`a
���`d    ���`cfig���`a,���`a ���`a(���`bax���`a,���`a ���`cax2���`a)���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x"click on point to plot time series���bs1a'���`a)���`a
���`d    ���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`bxs���`a,���`a ���`bys���`a,���`a ���bs1a'���bs1ao���bs1a'���`a,���`a ���`fpicker���aoa=���bkcdTrue���`a,���`a ���`jpickradius���aoa=���bmia5���`a)���`a
���`a
���`d    ���`gbrowser���`a ���aoa=���`a ���`lPointBrowser���`a(���`a)���`a
���`a
���`d    ���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1jpick_event���bs1a'���`a,���`a ���`gbrowser���aoa.���`gon_pick���`a)���`a
���`d    ���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1okey_press_event���bs1a'���`a,���`a ���`gbrowser���aoa.���`hon_press���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�