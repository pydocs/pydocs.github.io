������������bsdx�"""
===========
Poly Editor
===========

This is an example to show how to build cross-GUI applications using
Matplotlib event handling to interact with objects on the canvas.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnelines���`a ���bknfimport���`a ���`fLine2D���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfartist���`a ���bknfimport���`a ���`fArtist���`a
���`a
���`a
���akcdef���`a ���bnfddist���`a(���`ax���`a,���`a ���`ay���`a)���`a:���`a
���`d    ���bsdx7"""
    Return the distance between two points.
    """���`a
���`d    ���`ad���`a ���aoa=���`a ���`ax���`a ���aoa-���`a ���`ay���`a
���`d    ���akfreturn���`a ���`bnp���aoa.���`dsqrt���`a(���`bnp���aoa.���`cdot���`a(���`ad���`a,���`a ���`ad���`a)���`a)���`a
���`a
���`a
���akcdef���`a ���bnfudist_point_to_segment���`a(���`ap���`a,���`a ���`bs0���`a,���`a ���`bs1���`a)���`a:���`a
���`d    ���bsdx�"""
    Get the distance of a point to a segment.
      *p*, *s0*, *s1* are *xy* sequences
    This algorithm from
    http://www.geomalgorithms.com/algorithms.html
    """���`a
���`d    ���`av���`a ���aoa=���`a ���`bs1���`a ���aoa-���`a ���`bs0���`a
���`d    ���`aw���`a ���aoa=���`a ���`ap���`a ���aoa-���`a ���`bs0���`a
���`d    ���`bc1���`a ���aoa=���`a ���`bnp���aoa.���`cdot���`a(���`aw���`a,���`a ���`av���`a)���`a
���`d    ���akbif���`a ���`bc1���`a ���aoa<���aoa=���`a ���bmia0���`a:���`a
���`h        ���akfreturn���`a ���`ddist���`a(���`ap���`a,���`a ���`bs0���`a)���`a
���`d    ���`bc2���`a ���aoa=���`a ���`bnp���aoa.���`cdot���`a(���`av���`a,���`a ���`av���`a)���`a
���`d    ���akbif���`a ���`bc2���`a ���aoa<���aoa=���`a ���`bc1���`a:���`a
���`h        ���akfreturn���`a ���`ddist���`a(���`ap���`a,���`a ���`bs1���`a)���`a
���`d    ���`ab���`a ���aoa=���`a ���`bc1���`a ���aoa/���`a ���`bc2���`a
���`d    ���`bpb���`a ���aoa=���`a ���`bs0���`a ���aoa+���`a ���`ab���`a ���aoa*���`a ���`av���`a
���`d    ���akfreturn���`a ���`ddist���`a(���`ap���`a,���`a ���`bpb���`a)���`a
���`a
���`a
���akeclass���`a ���bncqPolygonInteractor���`a:���`a
���`d    ���bsdyH"""
    A polygon editor.

    Key-bindings

      't' toggle vertex markers on and off.  When vertex markers are on,
          you can move them, delete them

      'd' delete the vertex under point

      'i' insert a vertex at point.  You must be within epsilon of the
          line connecting two existing vertices

    """���`a
���`a
���`d    ���`ishowverts���`a ���aoa=���`a ���bkcdTrue���`a
���`d    ���`gepsilon���`a ���aoa=���`a ���bmia5���`b  ���bc1x-# max pixel distance to count as a vertex hit���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`bax���`a,���`a ���`dpoly���`a)���`a:���`a
���`h        ���akbif���`a ���`dpoly���aoa.���`ffigure���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���akeraise���`a ���bnelRuntimeError���`a(���bs1a'���bs1x+You must first add the polygon to a figure ���bs1a'���`a
���`x                               ���bs1a'���bs1x(or canvas before defining the interactor���bs1a'���`a)���`a
���`h        ���bbpdself���aoa.���`bax���`a ���aoa=���`a ���`bax���`a
���`h        ���`fcanvas���`a ���aoa=���`a ���`dpoly���aoa.���`ffigure���aoa.���`fcanvas���`a
���`h        ���bbpdself���aoa.���`dpoly���`a ���aoa=���`a ���`dpoly���`a
���`a
���`h        ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���bnbczip���`a(���aoa*���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a)���`a
���`h        ���bbpdself���aoa.���`dline���`a ���aoa=���`a ���`fLine2D���`a(���`ax���`a,���`a ���`ay���`a,���`a
���`x                           ���`fmarker���aoa=���bs1a'���bs1ao���bs1a'���`a,���`a ���`omarkerfacecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a
���`x                           ���`hanimated���aoa=���bkcdTrue���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`hadd_line���`a(���bbpdself���aoa.���`dline���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`ccid���`a ���aoa=���`a ���bbpdself���aoa.���`dpoly���aoa.���`ladd_callback���`a(���bbpdself���aoa.���`lpoly_changed���`a)���`a
���`h        ���bbpdself���aoa.���`d_ind���`a ���aoa=���`a ���bkcdNone���`b  ���bc1q# the active vert���`a
���`a
���`h        ���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1jdraw_event���bs1a'���`a,���`a ���bbpdself���aoa.���`gon_draw���`a)���`a
���`h        ���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1rbutton_press_event���bs1a'���`a,���`a ���bbpdself���aoa.���`oon_button_press���`a)���`a
���`h        ���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1okey_press_event���bs1a'���`a,���`a ���bbpdself���aoa.���`lon_key_press���`a)���`a
���`h        ���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1tbutton_release_event���bs1a'���`a,���`a ���bbpdself���aoa.���`qon_button_release���`a)���`a
���`h        ���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1smotion_notify_event���bs1a'���`a,���`a ���bbpdself���aoa.���`mon_mouse_move���`a)���`a
���`h        ���bbpdself���aoa.���`fcanvas���`a ���aoa=���`a ���`fcanvas���`a
���`a
���`d    ���akcdef���`a ���bnfgon_draw���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`jbackground���`a ���aoa=���`a ���bbpdself���aoa.���`fcanvas���aoa.���`ncopy_from_bbox���`a(���bbpdself���aoa.���`bax���aoa.���`dbbox���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���bbpdself���aoa.���`dpoly���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���bbpdself���aoa.���`dline���`a)���`a
���`h        ���bc1x?# do not need to blit here, this will fire before the screen is���`a
���`h        ���bc1i# updated���`a
���`a
���`d    ���akcdef���`a ���bnflpoly_changed���`a(���bbpdself���`a,���`a ���`dpoly���`a)���`a:���`a
���`h        ���bsdxD"""This method is called whenever the pathpatch object is called."""���`a
���`h        ���bc1x<# only copy the artist props to the line (except visibility)���`a
���`h        ���`cvis���`a ���aoa=���`a ���bbpdself���aoa.���`dline���aoa.���`kget_visible���`a(���`a)���`a
���`h        ���`fArtist���aoa.���`kupdate_from���`a(���bbpdself���aoa.���`dline���`a,���`a ���`dpoly���`a)���`a
���`h        ���bbpdself���aoa.���`dline���aoa.���`kset_visible���`a(���`cvis���`a)���`b  ���bc1x%# don't use the poly visibility state���`a
���`a
���`d    ���akcdef���`a ���bnfsget_ind_under_point���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bsdx�"""
        Return the index of the point closest to the event position or *None*
        if no point is within ``self.epsilon`` to the event position.
        """���`a
���`h        ���bc1p# display coords���`a
���`h        ���`bxy���`a ���aoa=���`a ���`bnp���aoa.���`gasarray���`a(���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a)���`a
���`h        ���`cxyt���`a ���aoa=���`a ���bbpdself���aoa.���`dpoly���aoa.���`mget_transform���`a(���`a)���aoa.���`itransform���`a(���`bxy���`a)���`a
���`h        ���`bxt���`a,���`a ���`byt���`a ���aoa=���`a ���`cxyt���`a[���`a:���`a,���`a ���bmia0���`a]���`a,���`a ���`cxyt���`a[���`a:���`a,���`a ���bmia1���`a]���`a
���`h        ���`ad���`a ���aoa=���`a ���`bnp���aoa.���`ehypot���`a(���`bxt���`a ���aoa-���`a ���`eevent���aoa.���`ax���`a,���`a ���`byt���`a ���aoa-���`a ���`eevent���aoa.���`ay���`a)���`a
���`h        ���`findseq���`a,���`a ���aoa=���`a ���`bnp���aoa.���`gnonzero���`a(���`ad���`a ���aob==���`a ���`ad���aoa.���`cmin���`a(���`a)���`a)���`a
���`h        ���`cind���`a ���aoa=���`a ���`findseq���`a[���bmia0���`a]���`a
���`a
���`h        ���akbif���`a ���`ad���`a[���`cind���`a]���`a ���aoa>���aoa=���`a ���bbpdself���aoa.���`gepsilon���`a:���`a
���`l            ���`cind���`a ���aoa=���`a ���bkcdNone���`a
���`a
���`h        ���akfreturn���`a ���`cind���`a
���`a
���`d    ���akcdef���`a ���bnfoon_button_press���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bsdx("""Callback for mouse button presses."""���`a
���`h        ���akbif���`a ���bowcnot���`a ���bbpdself���aoa.���`ishowverts���`a:���`a
���`l            ���akfreturn���`a
���`h        ���akbif���`a ���`eevent���aoa.���`finaxes���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���akfreturn���`a
���`h        ���akbif���`a ���`eevent���aoa.���`fbutton���`a ���aob!=���`a ���bmia1���`a:���`a
���`l            ���akfreturn���`a
���`h        ���bbpdself���aoa.���`d_ind���`a ���aoa=���`a ���bbpdself���aoa.���`sget_ind_under_point���`a(���`eevent���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfqon_button_release���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bsdx)"""Callback for mouse button releases."""���`a
���`h        ���akbif���`a ���bowcnot���`a ���bbpdself���aoa.���`ishowverts���`a:���`a
���`l            ���akfreturn���`a
���`h        ���akbif���`a ���`eevent���aoa.���`fbutton���`a ���aob!=���`a ���bmia1���`a:���`a
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
���`h        ���akdelif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1ad���bs1a'���`a:���`a
���`l            ���`cind���`a ���aoa=���`a ���bbpdself���aoa.���`sget_ind_under_point���`a(���`eevent���`a)���`a
���`l            ���akbif���`a ���`cind���`a ���bowbis���`a ���bowcnot���`a ���bkcdNone���`a:���`a
���`p                ���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a ���aoa=���`a ���`bnp���aoa.���`fdelete���`a(���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a,���`a
���`x)                                         ���`cind���`a,���`a ���`daxis���aoa=���bmia0���`a)���`a
���`p                ���bbpdself���aoa.���`dline���aoa.���`hset_data���`a(���bnbczip���`a(���aoa*���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a)���`a)���`a
���`h        ���akdelif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1ai���bs1a'���`a:���`a
���`l            ���`cxys���`a ���aoa=���`a ���bbpdself���aoa.���`dpoly���aoa.���`mget_transform���`a(���`a)���aoa.���`itransform���`a(���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a)���`a
���`l            ���`ap���`a ���aoa=���`a ���`eevent���aoa.���`ax���`a,���`a ���`eevent���aoa.���`ay���`b  ���bc1p# display coords���`a
���`l            ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���`cxys���`a)���`a ���aoa-���`a ���bmia1���`a)���`a:���`a
���`p                ���`bs0���`a ���aoa=���`a ���`cxys���`a[���`ai���`a]���`a
���`p                ���`bs1���`a ���aoa=���`a ���`cxys���`a[���`ai���`a ���aoa+���`a ���bmia1���`a]���`a
���`p                ���`ad���`a ���aoa=���`a ���`udist_point_to_segment���`a(���`ap���`a,���`a ���`bs0���`a,���`a ���`bs1���`a)���`a
���`p                ���akbif���`a ���`ad���`a ���aoa<���aoa=���`a ���bbpdself���aoa.���`gepsilon���`a:���`a
���`t                    ���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a ���aoa=���`a ���`bnp���aoa.���`finsert���`a(���`a
���`x                        ���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a,���`a ���`ai���aoa+���bmia1���`a,���`a
���`x                        ���`a[���`eevent���aoa.���`exdata���`a,���`a ���`eevent���aoa.���`eydata���`a]���`a,���`a
���`x                        ���`daxis���aoa=���bmia0���`a)���`a
���`t                    ���bbpdself���aoa.���`dline���aoa.���`hset_data���`a(���bnbczip���`a(���aoa*���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a)���`a)���`a
���`t                    ���akebreak���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`dline���aoa.���`estale���`a:���`a
���`l            ���bbpdself���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfmon_mouse_move���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bsdx#"""Callback for mouse movements."""���`a
���`h        ���akbif���`a ���bowcnot���`a ���bbpdself���aoa.���`ishowverts���`a:���`a
���`l            ���akfreturn���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`d_ind���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���akfreturn���`a
���`h        ���akbif���`a ���`eevent���aoa.���`finaxes���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���akfreturn���`a
���`h        ���akbif���`a ���`eevent���aoa.���`fbutton���`a ���aob!=���`a ���bmia1���`a:���`a
���`l            ���akfreturn���`a
���`h        ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`eevent���aoa.���`exdata���`a,���`a ���`eevent���aoa.���`eydata���`a
���`a
���`h        ���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a[���bbpdself���aoa.���`d_ind���`a]���`a ���aoa=���`a ���`ax���`a,���`a ���`ay���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`d_ind���`a ���aob==���`a ���bmia0���`a:���`a
���`l            ���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a[���aoa-���bmia1���`a]���`a ���aoa=���`a ���`ax���`a,���`a ���`ay���`a
���`h        ���akdelif���`a ���bbpdself���aoa.���`d_ind���`a ���aob==���`a ���bnbclen���`a(���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a)���`a ���aoa-���`a ���bmia1���`a:���`a
���`l            ���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a[���bmia0���`a]���`a ���aoa=���`a ���`ax���`a,���`a ���`ay���`a
���`h        ���bbpdself���aoa.���`dline���aoa.���`hset_data���`a(���bnbczip���`a(���aoa*���bbpdself���aoa.���`dpoly���aoa.���`bxy���`a)���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`nrestore_region���`a(���bbpdself���aoa.���`jbackground���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���bbpdself���aoa.���`dpoly���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���bbpdself���aoa.���`dline���`a)���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`dblit���`a(���bbpdself���aoa.���`bax���aoa.���`dbbox���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs1a'���bs1h__main__���bs1a'���`a:���`a
���`d    ���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`d    ���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngpatches���`a ���bknfimport���`a ���`gPolygon���`a
���`a
���`d    ���`etheta���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia2���aoa*���`bnp���aoa.���`bpi���`a,���`a ���bmfc0.1���`a)���`a
���`d    ���`ar���`a ���aoa=���`a ���bmfc1.5���`a
���`a
���`d    ���`bxs���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`ccos���`a(���`etheta���`a)���`a
���`d    ���`bys���`a ���aoa=���`a ���`ar���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`etheta���`a)���`a
���`a
���`d    ���`dpoly���`a ���aoa=���`a ���`gPolygon���`a(���`bnp���aoa.���`lcolumn_stack���`a(���`a[���`bxs���`a,���`a ���`bys���`a]���`a)���`a,���`a ���`hanimated���aoa=���bkcdTrue���`a)���`a
���`a
���`d    ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`d    ���`bax���aoa.���`iadd_patch���`a(���`dpoly���`a)���`a
���`d    ���`ap���`a ���aoa=���`a ���`qPolygonInteractor���`a(���`bax���`a,���`a ���`dpoly���`a)���`a
���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x!Click and drag a point to move it���bs1a'���`a)���`a
���`d    ���`bax���aoa.���`hset_xlim���`a(���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a)���`a
���`d    ���`bax���aoa.���`hset_ylim���`a(���`a(���aoa-���bmia2���`a,���`a ���bmia2���`a)���`a)���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�