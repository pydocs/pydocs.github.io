��������(���bsdx�"""
==================================
Figure/Axes enter and leave events
==================================

Illustrate the figure and Axes enter and leave events by changing the
frame colors on enter and leave.
"""���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfmon_enter_axes���`a(���`eevent���`a)���`a:���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1jenter_axes���bs1a'���`a,���`a ���`eevent���aoa.���`finaxes���`a)���`a
���`d    ���`eevent���aoa.���`finaxes���aoa.���`epatch���aoa.���`mset_facecolor���`a(���bs1a'���bs1fyellow���bs1a'���`a)���`a
���`d    ���`eevent���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`a
���akcdef���`a ���bnfmon_leave_axes���`a(���`eevent���`a)���`a:���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1jleave_axes���bs1a'���`a,���`a ���`eevent���aoa.���`finaxes���`a)���`a
���`d    ���`eevent���aoa.���`finaxes���aoa.���`epatch���aoa.���`mset_facecolor���`a(���bs1a'���bs1ewhite���bs1a'���`a)���`a
���`d    ���`eevent���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`a
���akcdef���`a ���bnfoon_enter_figure���`a(���`eevent���`a)���`a:���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1lenter_figure���bs1a'���`a,���`a ���`eevent���aoa.���`fcanvas���aoa.���`ffigure���`a)���`a
���`d    ���`eevent���aoa.���`fcanvas���aoa.���`ffigure���aoa.���`epatch���aoa.���`mset_facecolor���`a(���bs1a'���bs1cred���bs1a'���`a)���`a
���`d    ���`eevent���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`a
���akcdef���`a ���bnfoon_leave_figure���`a(���`eevent���`a)���`a:���`a
���`d    ���bnbeprint���`a(���bs1a'���bs1lleave_figure���bs1a'���`a,���`a ���`eevent���aoa.���`fcanvas���aoa.���`ffigure���`a)���`a
���`d    ���`eevent���aoa.���`fcanvas���aoa.���`ffigure���aoa.���`epatch���aoa.���`mset_facecolor���`a(���bs1a'���bs1dgrey���bs1a'���`a)���`a
���`d    ���`eevent���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`a
���`cfig���`a,���`a ���`caxs���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���bmia2���`a,���`a ���bmia1���`a)���`a
���`cfig���aoa.���`hsuptitle���`a(���bs1a'���bs1x1mouse hover over figure or axes to trigger events���bs1a'���`a)���`a
���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1rfigure_enter_event���bs1a'���`a,���`a ���`oon_enter_figure���`a)���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1rfigure_leave_event���bs1a'���`a,���`a ���`oon_leave_figure���`a)���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1paxes_enter_event���bs1a'���`a,���`a ���`mon_enter_axes���`a)���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1paxes_leave_event���bs1a'���`a,���`a ���`mon_leave_axes���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�