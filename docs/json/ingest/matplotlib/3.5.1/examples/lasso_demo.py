������������bsdyC"""
==========
Lasso Demo
==========

Show how to use a lasso to select a set of points and get the indices
of the selected points.  A callback is used to change the color of the
selected points

This is currently a proof-of-concept implementation (though it is
usable as is).  There will be some refinement of the API.
"""���`a
���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����`a ���bknfimport���`a ���`fcolors���`a ���akbas���`a ���`gmcolors���`a,���`a ���`dpath���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnkcollections���`a ���bknfimport���`a ���`uRegularPolyCollection���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnngwidgets���`a ���bknfimport���`a ���`eLasso���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akeclass���`a ���bnceDatum���`a:���`a
���`d    ���`gcolorin���`a ���aoa=���`a ���`gmcolors���aoa.���`gto_rgba���`a(���bs2a"���bs2cred���bs2a"���`a)���`a
���`d    ���`hcolorout���`a ���aoa=���`a ���`gmcolors���aoa.���`gto_rgba���`a(���bs2a"���bs2dblue���bs2a"���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`ax���`a,���`a ���`ay���`a,���`a ���`ginclude���aoa=���bkceFalse���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`ax���`a ���aoa=���`a ���`ax���`a
���`h        ���bbpdself���aoa.���`ay���`a ���aoa=���`a ���`ay���`a
���`h        ���akbif���`a ���`ginclude���`a:���`a
���`l            ���bbpdself���aoa.���`ecolor���`a ���aoa=���`a ���bbpdself���aoa.���`gcolorin���`a
���`h        ���akdelse���`a:���`a
���`l            ���bbpdself���aoa.���`ecolor���`a ���aoa=���`a ���bbpdself���aoa.���`hcolorout���`a
���`a
���`a
���akeclass���`a ���bnclLassoManager���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`bax���`a,���`a ���`ddata���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`daxes���`a ���aoa=���`a ���`bax���`a
���`h        ���bbpdself���aoa.���`fcanvas���`a ���aoa=���`a ���`bax���aoa.���`ffigure���aoa.���`fcanvas���`a
���`h        ���bbpdself���aoa.���`ddata���`a ���aoa=���`a ���`ddata���`a
���`a
���`h        ���bbpdself���aoa.���`cNxy���`a ���aoa=���`a ���bnbclen���`a(���`ddata���`a)���`a
���`a
���`h        ���`jfacecolors���`a ���aoa=���`a ���`a[���`ad���aoa.���`ecolor���`a ���akcfor���`a ���`ad���`a ���bowbin���`a ���`ddata���`a]���`a
���`h        ���bbpdself���aoa.���`cxys���`a ���aoa=���`a ���`a[���`a(���`ad���aoa.���`ax���`a,���`a ���`ad���aoa.���`ay���`a)���`a ���akcfor���`a ���`ad���`a ���bowbin���`a ���`ddata���`a]���`a
���`h        ���bbpdself���aoa.���`jcollection���`a ���aoa=���`a ���`uRegularPolyCollection���`a(���`a
���`l            ���bmia6���`a,���`a ���`esizes���aoa=���`a(���bmic100���`a,���`a)���`a,���`a
���`l            ���`jfacecolors���aoa=���`jfacecolors���`a,���`a
���`l            ���`goffsets���aoa=���bbpdself���aoa.���`cxys���`a,���`a
���`l            ���`ktransOffset���aoa=���`bax���aoa.���`itransData���`a)���`a
���`a
���`h        ���`bax���aoa.���`nadd_collection���`a(���bbpdself���aoa.���`jcollection���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`ccid���`a ���aoa=���`a ���bbpdself���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1rbutton_press_event���bs1a'���`a,���`a ���bbpdself���aoa.���`hon_press���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfhcallback���`a(���bbpdself���`a,���`a ���`everts���`a)���`a:���`a
���`h        ���`jfacecolors���`a ���aoa=���`a ���bbpdself���aoa.���`jcollection���aoa.���`nget_facecolors���`a(���`a)���`a
���`h        ���`ap���`a ���aoa=���`a ���`dpath���aoa.���`dPath���`a(���`everts���`a)���`a
���`h        ���`cind���`a ���aoa=���`a ���`ap���aoa.���`ocontains_points���`a(���bbpdself���aoa.���`cxys���`a)���`a
���`h        ���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���bnbclen���`a(���bbpdself���aoa.���`cxys���`a)���`a)���`a:���`a
���`l            ���akbif���`a ���`cind���`a[���`ai���`a]���`a:���`a
���`p                ���`jfacecolors���`a[���`ai���`a]���`a ���aoa=���`a ���`eDatum���aoa.���`gcolorin���`a
���`l            ���akdelse���`a:���`a
���`p                ���`jfacecolors���`a[���`ai���`a]���`a ���aoa=���`a ���`eDatum���aoa.���`hcolorout���`a
���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`jwidgetlock���aoa.���`grelease���`a(���bbpdself���aoa.���`elasso���`a)���`a
���`h        ���akcdel���`a ���bbpdself���aoa.���`elasso���`a
���`a
���`d    ���akcdef���`a ���bnfhon_press���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`fcanvas���aoa.���`jwidgetlock���aoa.���`flocked���`a(���`a)���`a:���`a
���`l            ���akfreturn���`a
���`h        ���akbif���`a ���`eevent���aoa.���`finaxes���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���akfreturn���`a
���`h        ���bbpdself���aoa.���`elasso���`a ���aoa=���`a ���`eLasso���`a(���`eevent���aoa.���`finaxes���`a,���`a
���`x                           ���`a(���`eevent���aoa.���`exdata���`a,���`a ���`eevent���aoa.���`eydata���`a)���`a,���`a
���`x                           ���bbpdself���aoa.���`hcallback���`a)���`a
���`h        ���bc1x&# acquire a lock on the widget drawing���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`jwidgetlock���`a(���bbpdself���aoa.���`elasso���`a)���`a
���`a
���`a
���akbif���`a ���bvmh__name__���`a ���aob==���`a ���bs1a'���bs1h__main__���bs1a'���`a:���`a
���`a
���`d    ���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`d    ���`ddata���`a ���aoa=���`a ���`a[���`eDatum���`a(���aoa*���`bxy���`a)���`a ���akcfor���`a ���`bxy���`a ���bowbin���`a ���`bnp���aoa.���`frandom���aoa.���`drand���`a(���bmic100���`a,���`a ���bmia2���`a)���`a]���`a
���`d    ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`daxes���`a(���`dxlim���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`dylim���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`lautoscale_on���aoa=���bkceFalse���`a)���`a
���`d    ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x$Lasso points using left mouse button���bs1a'���`a)���`a
���`a
���`d    ���`dlman���`a ���aoa=���`a ���`lLassoManager���`a(���`bax���`a,���`a ���`ddata���`a)���`a
���`a
���`d    ���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�