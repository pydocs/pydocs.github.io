������������bsdx�"""
===========
Path Editor
===========

Sharing events across GUIs.

This example demonstrates a cross-GUI application using Matplotlib event
handling to interact with and modify objects on the canvas.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnmbackend_bases���`a ���bknfimport���`a ���`kMouseButton���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnndpath���`a ���bknfimport���`a ���`dPath���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`iPathPatch���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`a
���`hpathdata���`a ���aoa=���`a ���`a[���`a
���`d    ���`a(���`dPath���aoa.���`fMOVETO���`a,���`a ���`a(���bmfd1.58���`a,���`a ���aoa-���bmfd2.57���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a(���bmfd0.35���`a,���`a ���aoa-���bmfc1.1���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a(���aoa-���bmfd1.75���`a,���`a ���bmfc2.0���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a(���bmfe0.375���`a,���`a ���bmfc2.0���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fLINETO���`a,���`a ���`a(���bmfd0.85���`a,���`a ���bmfd1.15���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a(���bmfc2.2���`a,���`a ���bmfc3.2���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a(���bmia3���`a,���`a ���bmfd0.05���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`fCURVE4���`a,���`a ���`a(���bmfc2.0���`a,���`a ���aoa-���bmfc0.5���`a)���`a)���`a,���`a
���`d    ���`a(���`dPath���aoa.���`iCLOSEPOLY���`a,���`a ���`a(���bmfd1.58���`a,���`a ���aoa-���bmfd2.57���`a)���`a)���`a,���`a
���`a]���`a
���`a
���`ecodes���`a,���`a ���`everts���`a ���aoa=���`a ���bnbczip���`a(���aoa*���`hpathdata���`a)���`a
���`dpath���`a ���aoa=���`a ���`dPath���`a(���`everts���`a,���`a ���`ecodes���`a)���`a
���`epatch���`a ���aoa=���`a ���`iPathPatch���`a(���`a
���`d    ���`dpath���`a,���`a ���`ifacecolor���aoa=���bs1a'���bs1egreen���bs1a'���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1fyellow���bs1a'���`a,���`a ���`ealpha���aoa=���bmfc0.5���`a)���`a
���`bax���aoa.���`iadd_patch���`a(���`epatch���`a)���`a
���`a
���`a
���akeclass���`a ���bncnPathInteractor���`a:���`a
���`d    ���bsdx�"""
    An path editor.

    Press 't' to toggle vertex markers on and off.  When vertex markers are on,
    they can be dragged with the mouse.
    """���`a
���`a
���`d    ���`ishowverts���`a ���aoa=���`a ���bkcdTrue���`a
���`d    ���`gepsilon���`a ���aoa=���`a ���bmia5���`b  ���bc1x-# max pixel distance to count as a vertex hit���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`ipathpatch���`a)���`a:���`a
���`a
���`h        ���bbpdself���aoa.���`bax���`a ���aoa=���`a ���`ipathpatch���aoa.���`daxes���`a
���`h        ���`fcanvas���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���`a
���`h        ���bbpdself���aoa.���`ipathpatch���`a ���aoa=���`a ���`ipathpatch���`a
���`h        ���bbpdself���aoa.���`ipathpatch���aoa.���`lset_animated���`a(���bkcdTrue���`a)���`a
���`a
���`h        ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���bnbczip���`a(���aoa*���bbpdself���aoa.���`ipathpatch���aoa.���`hget_path���`a(���`a)���aoa.���`hvertices���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`a
���`l            ���`ax���`a,���`a ���`ay���`a,���`a ���`fmarker���aoa=���bs1a'���bs1ao���bs1a'���`a,���`a ���`omarkerfacecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`hanimated���aoa=���bkcdTrue���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`d_ind���`a ���aoa=���`a ���bkcdNone���`b  ���bc1s# the active vertex���`a
���`a
���`h        ���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1jdraw_event���bs1a'���`a,���`a ���bbpdself���aoa.���`gon_draw���`a)���`a
���`h        ���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1rbutton_press_event���bs1a'���`a,���`a ���bbpdself���aoa.���`oon_button_press���`a)���`a
���`h        ���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1okey_press_event���bs1a'���`a,���`a ���bbpdself���aoa.���`lon_key_press���`a)���`a
���`h        ���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1tbutton_release_event���bs1a'���`a,���`a ���bbpdself���aoa.���`qon_button_release���`a)���`a
���`h        ���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1smotion_notify_event���bs1a'���`a,���`a ���bbpdself���aoa.���`mon_mouse_move���`a)���`a
���`h        ���bbpdself���aoa.���`fcanvas���`a ���aoa=���`a ���`fcanvas���`a
���`a
���`d    ���akcdef���`a ���bnfsget_ind_under_point���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bsdx�"""
        Return the index of the point closest to the event position or *None*
        if no point is within ``self.epsilon`` to the event position.
        """���`a
���`h        ���bc1p# display coords���`a
���`h        ���`bxy���`a ���aoa=���`a ���`bnp���aoa.���`gasarray���`a(���bbpdself���aoa.���`ipathpatch���aoa.���`hget_path���`a(���`a)���aoa.���`hvertices���`a)���`a
���`h        ���`cxyt���`a ���aoa=���`a ���bbpdself���aoa.���`ipathpatch���aoa.���`mget_transform���`a(���`a)���aoa.���`itransform���`a(���`bxy���`a)���`a
���`h        ���`bxt���`a,���`a ���`byt���`a ���aoa=���`a ���`cxyt���`a[���`a:���`a,���`a ���bmia0���`a]���`a,���`a ���`cxyt���`a[���`a:���`a,���`a ���bmia1���`a]���`a
���`h        ���`ad���`a ���aoa=���`a ���`bnp���aoa.���`dsqrt���`a(���`a(���`bxt���`a ���aoa-���`a ���`eevent���aoa.���`ax���`a)���aoa*���aoa*���bmia2���`a ���aoa+���`a ���`a(���`byt���`a ���aoa-���`a ���`eevent���aoa.���`ay���`a)���aoa*���aoa*���bmia2���`a)���`a
���`h        ���`cind���`a ���aoa=���`a ���`ad���aoa.���`fargmin���`a(���`a)���`a
���`a
���`h        ���akbif���`a ���`ad���`a[���`cind���`a]���`a ���aoa>���aoa=���`a ���bbpdself���aoa.���`gepsilon���`a:���`a
���`l            ���`cind���`a ���aoa=���`a ���bkcdNone���`a
���`a
���`h        ���akfreturn���`a ���`cind���`a
���`a
���`d    ���akcdef���`a ���bnfgon_draw���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bsdx"""Callback for draws."""���`a
���`h        ���bbpdself���aoa.���`jbackground���`a ���aoa=���`a ���bbpdself���aoa.���`fcanvas���aoa.���`ncopy_from_bbox���`a(���bbpdself���aoa.���`bax���aoa.���`dbbox���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���bbpdself���aoa.���`ipathpatch���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���bbpdself���aoa.���`dline���`a)���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`dblit���`a(���bbpdself���aoa.���`bax���aoa.���`dbbox���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfoon_button_press���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bsdx("""Callback for mouse button presses."""���`a
���`h        ���akbif���`a ���`a(���`eevent���aoa.���`finaxes���`a ���bowbis���`a ���bkcdNone���`a
���`p                ���bowbor���`a ���`eevent���aoa.���`fbutton���`a ���aob!=���`a ���`kMouseButton���aoa.���`dLEFT���`a
���`p                ���bowbor���`a ���bowcnot���`a ���bbpdself���aoa.���`ishowverts���`a)���`a:���`a
���`l            ���akfreturn���`a
���`h        ���bbpdself���aoa.���`d_ind���`a ���aoa=���`a ���bbpdself���aoa.���`sget_ind_under_point���`a(���`eevent���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfqon_button_release���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bsdx)"""Callback for mouse button releases."""���`a
���`h        ���akbif���`a ���`a(���`eevent���aoa.���`fbutton���`a ���aob!=���`a ���`kMouseButton���aoa.���`dLEFT���`a
���`p                ���bowbor���`a ���bowcnot���`a ���bbpdself���aoa.���`ishowverts���`a)���`a:���`a
���`l            ���akfreturn���`a
���`h        ���bbpdself���aoa.���`d_ind���`a ���aoa=���`a ���bkcdNone���`a
���`a
���`d    ���akcdef���`a ���bnflon_key_press���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bsdx"""Callback for key presses."""���`a
���`h        ���akbif���`a ���bowcnot���`a ���`eevent���aoa.���`finaxes���`a:���`a
���`l            ���akfreturn���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1at���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`ishowverts���`a ���aoa=���`a ���bowcnot���`a ���bbpdself���aoa.���`ishowverts���`a
���`l            ���bbpdself���aoa.���`dline���aoa.���`kset_visible���`a(���bbpdself���aoa.���`ishowverts���`a)���`a
���`l            ���akbif���`a ���bowcnot���`a ���bbpdself���aoa.���`ishowverts���`a:���`a
���`p                ���bbpdself���aoa.���`d_ind���`a ���aoa=���`a ���bkcdNone���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfmon_mouse_move���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bsdx#"""Callback for mouse movements."""���`a
���`h        ���akbif���`a ���`a(���bbpdself���aoa.���`d_ind���`a ���bowbis���`a ���bkcdNone���`a
���`p                ���bowbor���`a ���`eevent���aoa.���`finaxes���`a ���bowbis���`a ���bkcdNone���`a
���`p                ���bowbor���`a ���`eevent���aoa.���`fbutton���`a ���aob!=���`a ���`kMouseButton���aoa.���`dLEFT���`a
���`p                ���bowbor���`a ���bowcnot���`a ���bbpdself���aoa.���`ishowverts���`a)���`a:���`a
���`l            ���akfreturn���`a
���`a
���`h        ���`hvertices���`a ���aoa=���`a ���bbpdself���aoa.���`ipathpatch���aoa.���`hget_path���`a(���`a)���aoa.���`hvertices���`a
���`a
���`h        ���`hvertices���`a[���bbpdself���aoa.���`d_ind���`a]���`a ���aoa=���`a ���`eevent���aoa.���`exdata���`a,���`a ���`eevent���aoa.���`eydata���`a
���`h        ���bbpdself���aoa.���`dline���aoa.���`hset_data���`a(���bnbczip���`a(���aoa*���`hvertices���`a)���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`nrestore_region���`a(���bbpdself���aoa.���`jbackground���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���bbpdself���aoa.���`ipathpatch���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���bbpdself���aoa.���`dline���`a)���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`dblit���`a(���bbpdself���aoa.���`bax���aoa.���`dbbox���`a)���`a
���`a
���`a
���`jinteractor���`a ���aoa=���`a ���`nPathInteractor���`a(���`epatch���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1xdrag vertices to update path���bs1a'���`a)���`a
���`bax���aoa.���`hset_xlim���`a(���aoa-���bmia3���`a,���`a ���bmia4���`a)���`a
���`bax���aoa.���`hset_ylim���`a(���aoa-���bmia3���`a,���`a ���bmia4���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�