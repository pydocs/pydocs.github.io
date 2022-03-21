������������bsdy"""
=================
Cross hair cursor
=================

This example adds a cross hair as a data cursor.  The cross hair is
implemented as regular line objects that are updated on mouse move.

We show three implementations:

1) A simple cursor implementation that redraws the figure on every mouse move.
   This is a bit slow and you may notice some lag of the cross hair movement.
2) A cursor that uses blitting for speedup of the rendering.
3) A cursor that snaps to data points.

Faster cursoring is possible using native GUI drawing, as in
:doc:`/gallery/user_interfaces/wxcursor_demo_sgskip`.

The mpldatacursor__ and mplcursors__ third-party packages can be used to
achieve a similar effect.

__ https://github.com/joferkington/mpldatacursor
__ https://github.com/anntzer/mplcursors
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akeclass���`a ���bncfCursor���`a:���`a
���`d    ���bsdx$"""
    A cross hair cursor.
    """���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`bax���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`bax���`a ���aoa=���`a ���`bax���`a
���`h        ���bbpdself���aoa.���`ohorizontal_line���`a ���aoa=���`a ���`bax���aoa.���`gaxhline���`a(���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`blw���aoa=���bmfc0.8���`a,���`a ���`bls���aoa=���bs1a'���bs1b--���bs1a'���`a)���`a
���`h        ���bbpdself���aoa.���`mvertical_line���`a ���aoa=���`a ���`bax���aoa.���`gaxvline���`a(���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`blw���aoa=���bmfc0.8���`a,���`a ���`bls���aoa=���bs1a'���bs1b--���bs1a'���`a)���`a
���`h        ���bc1x## text location in axes coordinates���`a
���`h        ���bbpdself���aoa.���`dtext���`a ���aoa=���`a ���`bax���aoa.���`dtext���`a(���bmfd0.72���`a,���`a ���bmfc0.9���`a,���`a ���bs1a'���bs1a'���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfvset_cross_hair_visible���`a(���bbpdself���`a,���`a ���`gvisible���`a)���`a:���`a
���`h        ���`kneed_redraw���`a ���aoa=���`a ���bbpdself���aoa.���`ohorizontal_line���aoa.���`kget_visible���`a(���`a)���`a ���aob!=���`a ���`gvisible���`a
���`h        ���bbpdself���aoa.���`ohorizontal_line���aoa.���`kset_visible���`a(���`gvisible���`a)���`a
���`h        ���bbpdself���aoa.���`mvertical_line���aoa.���`kset_visible���`a(���`gvisible���`a)���`a
���`h        ���bbpdself���aoa.���`dtext���aoa.���`kset_visible���`a(���`gvisible���`a)���`a
���`h        ���akfreturn���`a ���`kneed_redraw���`a
���`a
���`d    ���akcdef���`a ���bnfmon_mouse_move���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���akbif���`a ���bowcnot���`a ���`eevent���aoa.���`finaxes���`a:���`a
���`l            ���`kneed_redraw���`a ���aoa=���`a ���bbpdself���aoa.���`vset_cross_hair_visible���`a(���bkceFalse���`a)���`a
���`l            ���akbif���`a ���`kneed_redraw���`a:���`a
���`p                ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`h        ���akdelse���`a:���`a
���`l            ���bbpdself���aoa.���`vset_cross_hair_visible���`a(���bkcdTrue���`a)���`a
���`l            ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`eevent���aoa.���`exdata���`a,���`a ���`eevent���aoa.���`eydata���`a
���`l            ���bc1x# update the line positions���`a
���`l            ���bbpdself���aoa.���`ohorizontal_line���aoa.���`iset_ydata���`a(���`ay���`a)���`a
���`l            ���bbpdself���aoa.���`mvertical_line���aoa.���`iset_xdata���`a(���`ax���`a)���`a
���`l            ���bbpdself���aoa.���`dtext���aoa.���`hset_text���`a(���bs1a'���bs1bx=���bsie%1.2f���bs1d, y=���bsie%1.2f���bs1a'���`a ���aoa%���`a ���`a(���`ax���`a,���`a ���`ay���`a)���`a)���`a
���`l            ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmfd0.01���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ax���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1mSimple cursor���bs1a'���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a
���`fcursor���`a ���aoa=���`a ���`fCursor���`a(���`bax���`a)���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1smotion_notify_event���bs1a'���`a,���`a ���`fcursor���aoa.���`mon_mouse_move���`a)���`a
���`a
���`a
���bc1xN##############################################################################���`a
���bc1x!# Faster redrawing using blitting���`a
���bc1x!# """""""""""""""""""""""""""""""���`a
���bc1xI# This technique stores the rendered plot as a background image. Only the���`a
���bc1xI# changed artists (cross hair lines and text) are rendered anew. They are���`a
���bc1x.# combined with the background using blitting.���`a
���bc1a#���`a
���bc1xN# This technique is significantly faster. It requires a bit more setup because���`a
���bc1xC# the background has to be stored without the cross hair lines (see���`a
���bc1xH# ``create_new_background()``). Additionally, a new background has to be���`a
���bc1xL# created whenever the figure changes. This is achieved by connecting to the���`a
���bc1s# ``'draw_event'``.���`a
���`a
���akeclass���`a ���bncmBlittedCursor���`a:���`a
���`d    ���bsdxE"""
    A cross hair cursor using blitting for faster redraw.
    """���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`bax���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`bax���`a ���aoa=���`a ���`bax���`a
���`h        ���bbpdself���aoa.���`jbackground���`a ���aoa=���`a ���bkcdNone���`a
���`h        ���bbpdself���aoa.���`ohorizontal_line���`a ���aoa=���`a ���`bax���aoa.���`gaxhline���`a(���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`blw���aoa=���bmfc0.8���`a,���`a ���`bls���aoa=���bs1a'���bs1b--���bs1a'���`a)���`a
���`h        ���bbpdself���aoa.���`mvertical_line���`a ���aoa=���`a ���`bax���aoa.���`gaxvline���`a(���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`blw���aoa=���bmfc0.8���`a,���`a ���`bls���aoa=���bs1a'���bs1b--���bs1a'���`a)���`a
���`h        ���bc1x## text location in axes coordinates���`a
���`h        ���bbpdself���aoa.���`dtext���`a ���aoa=���`a ���`bax���aoa.���`dtext���`a(���bmfd0.72���`a,���`a ���bmfc0.9���`a,���`a ���bs1a'���bs1a'���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`h        ���bbpdself���aoa.���`t_creating_background���`a ���aoa=���`a ���bkceFalse���`a
���`h        ���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1jdraw_event���bs1a'���`a,���`a ���bbpdself���aoa.���`gon_draw���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfgon_draw���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`ucreate_new_background���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfvset_cross_hair_visible���`a(���bbpdself���`a,���`a ���`gvisible���`a)���`a:���`a
���`h        ���`kneed_redraw���`a ���aoa=���`a ���bbpdself���aoa.���`ohorizontal_line���aoa.���`kget_visible���`a(���`a)���`a ���aob!=���`a ���`gvisible���`a
���`h        ���bbpdself���aoa.���`ohorizontal_line���aoa.���`kset_visible���`a(���`gvisible���`a)���`a
���`h        ���bbpdself���aoa.���`mvertical_line���aoa.���`kset_visible���`a(���`gvisible���`a)���`a
���`h        ���bbpdself���aoa.���`dtext���aoa.���`kset_visible���`a(���`gvisible���`a)���`a
���`h        ���akfreturn���`a ���`kneed_redraw���`a
���`a
���`d    ���akcdef���`a ���bnfucreate_new_background���`a(���bbpdself���`a)���`a:���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`t_creating_background���`a:���`a
���`l            ���bc1x3# discard calls triggered from within this function���`a
���`l            ���akfreturn���`a
���`h        ���bbpdself���aoa.���`t_creating_background���`a ���aoa=���`a ���bkcdTrue���`a
���`h        ���bbpdself���aoa.���`vset_cross_hair_visible���`a(���bkceFalse���`a)���`a
���`h        ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`h        ���bbpdself���aoa.���`jbackground���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`ncopy_from_bbox���`a(���bbpdself���aoa.���`bax���aoa.���`dbbox���`a)���`a
���`h        ���bbpdself���aoa.���`vset_cross_hair_visible���`a(���bkcdTrue���`a)���`a
���`h        ���bbpdself���aoa.���`t_creating_background���`a ���aoa=���`a ���bkceFalse���`a
���`a
���`d    ���akcdef���`a ���bnfmon_mouse_move���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`jbackground���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���bbpdself���aoa.���`ucreate_new_background���`a(���`a)���`a
���`h        ���akbif���`a ���bowcnot���`a ���`eevent���aoa.���`finaxes���`a:���`a
���`l            ���`kneed_redraw���`a ���aoa=���`a ���bbpdself���aoa.���`vset_cross_hair_visible���`a(���bkceFalse���`a)���`a
���`l            ���akbif���`a ���`kneed_redraw���`a:���`a
���`p                ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`nrestore_region���`a(���bbpdself���aoa.���`jbackground���`a)���`a
���`p                ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`dblit���`a(���bbpdself���aoa.���`bax���aoa.���`dbbox���`a)���`a
���`h        ���akdelse���`a:���`a
���`l            ���bbpdself���aoa.���`vset_cross_hair_visible���`a(���bkcdTrue���`a)���`a
���`l            ���bc1x# update the line positions���`a
���`l            ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`eevent���aoa.���`exdata���`a,���`a ���`eevent���aoa.���`eydata���`a
���`l            ���bbpdself���aoa.���`ohorizontal_line���aoa.���`iset_ydata���`a(���`ay���`a)���`a
���`l            ���bbpdself���aoa.���`mvertical_line���aoa.���`iset_xdata���`a(���`ax���`a)���`a
���`l            ���bbpdself���aoa.���`dtext���aoa.���`hset_text���`a(���bs1a'���bs1bx=���bsie%1.2f���bs1d, y=���bsie%1.2f���bs1a'���`a ���aoa%���`a ���`a(���`ax���`a,���`a ���`ay���`a)���`a)���`a
���`a
���`l            ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`nrestore_region���`a(���bbpdself���aoa.���`jbackground���`a)���`a
���`l            ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���bbpdself���aoa.���`ohorizontal_line���`a)���`a
���`l            ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���bbpdself���aoa.���`mvertical_line���`a)���`a
���`l            ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���bbpdself���aoa.���`dtext���`a)���`a
���`l            ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`dblit���`a(���bbpdself���aoa.���`bax���aoa.���`dbbox���`a)���`a
���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmfd0.01���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ax���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1nBlitted cursor���bs1a'���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a
���`nblitted_cursor���`a ���aoa=���`a ���`mBlittedCursor���`a(���`bax���`a)���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1smotion_notify_event���bs1a'���`a,���`a ���`nblitted_cursor���aoa.���`mon_mouse_move���`a)���`a
���`a
���`a
���bc1xN##############################################################################���`a
���bc1x# Snapping to data points���`a
���bc1x# """""""""""""""""""""""���`a
���bc1xK# The following cursor snaps its position to the data points of a `.Line2D`���`a
���bc1i# object.���`a
���bc1a#���`a
���bc1xL# To save unnecessary redraws, the index of the last indicated data point is���`a
���bc1xJ# saved in ``self._last_index``. A redraw is only triggered when the mouse���`a
���bc1xL# moves far enough so that another data point must be selected. This reduces���`a
���bc1xN# the lag due to many redraws. Of course, blitting could still be added on top���`a
���bc1x# for additional speedup.���`a
���`a
���akeclass���`a ���bncnSnappingCursor���`a:���`a
���`d    ���bsdx�"""
    A cross hair cursor that snaps to the data point of a line, which is
    closest to the *x* position of the cursor.

    For simplicity, this assumes that *x* values of the data are sorted.
    """���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`bax���`a,���`a ���`dline���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`bax���`a ���aoa=���`a ���`bax���`a
���`h        ���bbpdself���aoa.���`ohorizontal_line���`a ���aoa=���`a ���`bax���aoa.���`gaxhline���`a(���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`blw���aoa=���bmfc0.8���`a,���`a ���`bls���aoa=���bs1a'���bs1b--���bs1a'���`a)���`a
���`h        ���bbpdself���aoa.���`mvertical_line���`a ���aoa=���`a ���`bax���aoa.���`gaxvline���`a(���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`blw���aoa=���bmfc0.8���`a,���`a ���`bls���aoa=���bs1a'���bs1b--���bs1a'���`a)���`a
���`h        ���bbpdself���aoa.���`ax���`a,���`a ���bbpdself���aoa.���`ay���`a ���aoa=���`a ���`dline���aoa.���`hget_data���`a(���`a)���`a
���`h        ���bbpdself���aoa.���`k_last_index���`a ���aoa=���`a ���bkcdNone���`a
���`h        ���bc1x# text location in axes coords���`a
���`h        ���bbpdself���aoa.���`dtext���`a ���aoa=���`a ���`bax���aoa.���`dtext���`a(���bmfd0.72���`a,���`a ���bmfc0.9���`a,���`a ���bs1a'���bs1a'���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfvset_cross_hair_visible���`a(���bbpdself���`a,���`a ���`gvisible���`a)���`a:���`a
���`h        ���`kneed_redraw���`a ���aoa=���`a ���bbpdself���aoa.���`ohorizontal_line���aoa.���`kget_visible���`a(���`a)���`a ���aob!=���`a ���`gvisible���`a
���`h        ���bbpdself���aoa.���`ohorizontal_line���aoa.���`kset_visible���`a(���`gvisible���`a)���`a
���`h        ���bbpdself���aoa.���`mvertical_line���aoa.���`kset_visible���`a(���`gvisible���`a)���`a
���`h        ���bbpdself���aoa.���`dtext���aoa.���`kset_visible���`a(���`gvisible���`a)���`a
���`h        ���akfreturn���`a ���`kneed_redraw���`a
���`a
���`d    ���akcdef���`a ���bnfmon_mouse_move���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���akbif���`a ���bowcnot���`a ���`eevent���aoa.���`finaxes���`a:���`a
���`l            ���bbpdself���aoa.���`k_last_index���`a ���aoa=���`a ���bkcdNone���`a
���`l            ���`kneed_redraw���`a ���aoa=���`a ���bbpdself���aoa.���`vset_cross_hair_visible���`a(���bkceFalse���`a)���`a
���`l            ���akbif���`a ���`kneed_redraw���`a:���`a
���`p                ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`h        ���akdelse���`a:���`a
���`l            ���bbpdself���aoa.���`vset_cross_hair_visible���`a(���bkcdTrue���`a)���`a
���`l            ���`ax���`a,���`a ���`ay���`a ���aoa=���`a ���`eevent���aoa.���`exdata���`a,���`a ���`eevent���aoa.���`eydata���`a
���`l            ���`eindex���`a ���aoa=���`a ���bnbcmin���`a(���`bnp���aoa.���`lsearchsorted���`a(���bbpdself���aoa.���`ax���`a,���`a ���`ax���`a)���`a,���`a ���bnbclen���`a(���bbpdself���aoa.���`ax���`a)���`a ���aoa-���`a ���bmia1���`a)���`a
���`l            ���akbif���`a ���`eindex���`a ���aob==���`a ���bbpdself���aoa.���`k_last_index���`a:���`a
���`p                ���akfreturn���`b  ���bc1x.# still on the same data point. Nothing to do.���`a
���`l            ���bbpdself���aoa.���`k_last_index���`a ���aoa=���`a ���`eindex���`a
���`l            ���`ax���`a ���aoa=���`a ���bbpdself���aoa.���`ax���`a[���`eindex���`a]���`a
���`l            ���`ay���`a ���aoa=���`a ���bbpdself���aoa.���`ay���`a[���`eindex���`a]���`a
���`l            ���bc1x# update the line positions���`a
���`l            ���bbpdself���aoa.���`ohorizontal_line���aoa.���`iset_ydata���`a(���`ay���`a)���`a
���`l            ���bbpdself���aoa.���`mvertical_line���aoa.���`iset_xdata���`a(���`ax���`a)���`a
���`l            ���bbpdself���aoa.���`dtext���aoa.���`hset_text���`a(���bs1a'���bs1bx=���bsie%1.2f���bs1d, y=���bsie%1.2f���bs1a'���`a ���aoa%���`a ���`a(���`ax���`a,���`a ���`ay���`a)���`a)���`a
���`l            ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`ddraw���`a(���`a)���`a
���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmia1���`a,���`a ���bmfd0.01���`a)���`a
���`ay���`a ���aoa=���`a ���`bnp���aoa.���`csin���`a(���bmia2���`a ���aoa*���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���`ax���`a)���`a
���`a
���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1oSnapping cursor���bs1a'���`a)���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���bs1a'���bs1ao���bs1a'���`a)���`a
���`ksnap_cursor���`a ���aoa=���`a ���`nSnappingCursor���`a(���`bax���`a,���`a ���`dline���`a)���`a
���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1smotion_notify_event���bs1a'���`a,���`a ���`ksnap_cursor���aoa.���`mon_mouse_move���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�