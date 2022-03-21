��������}���bsdy"""
=================================
Pausing and Resuming an Animation
=================================

This example showcases:

- using the Animation.pause() method to pause an animation.
- using the Animation.resume() method to resume an animation.
"""���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnianimation���`a ���akbas���`a ���bnnianimation���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���`a
���`a
���akeclass���`a ���bncnPauseAnimation���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a)���`a:���`a
���`h        ���`cfig���`a,���`a ���`bax���`a ���aoa=���`a ���`cplt���aoa.���`hsubplots���`a(���`a)���`a
���`h        ���`bax���aoa.���`iset_title���`a(���bs1a'���bs1x#Click to pause/resume the animation���bs1a'���`a)���`a
���`h        ���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���bmfc0.1���`a,���`a ���bmfc0.1���`a,���`a ���bmid1000���`a)���`a
���`a
���`h        ���bc1x"# Start with a normal distribution���`a
���`h        ���bbpdself���aoa.���`bn0���`a ���aoa=���`a ���`a(���bmfc1.0���`a ���aoa/���`a ���`a(���`a(���bmia4���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a ���aoa*���`a ���bmfd2e-4���`a ���aoa*���`a ���bmfc0.1���`a)���`a ���aoa*���aoa*���`a ���bmfc0.5���`a)���`a
���`s                   ���aoa*���`a ���`bnp���aoa.���`cexp���`a(���aoa-���`ax���`a ���aoa*���aoa*���`a ���bmia2���`a ���aoa/���`a ���`a(���bmia4���`a ���aoa*���`a ���bmfd2e-4���`a ���aoa*���`a ���bmfc0.1���`a)���`a)���`a)���`a
���`h        ���bbpdself���aoa.���`ap���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���bbpdself���aoa.���`bn0���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`ianimation���`a ���aoa=���`a ���`ianimation���aoa.���`mFuncAnimation���`a(���`a
���`l            ���`cfig���`a,���`a ���bbpdself���aoa.���`fupdate���`a,���`a ���`fframes���aoa=���bmic200���`a,���`a ���`hinterval���aoa=���bmib50���`a,���`a ���`dblit���aoa=���bkcdTrue���`a)���`a
���`h        ���bbpdself���aoa.���`fpaused���`a ���aoa=���`a ���bkceFalse���`a
���`a
���`h        ���`cfig���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1rbutton_press_event���bs1a'���`a,���`a ���bbpdself���aoa.���`ltoggle_pause���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfltoggle_pause���`a(���bbpdself���`a,���`a ���aoa*���`dargs���`a,���`a ���aoa*���aoa*���`fkwargs���`a)���`a:���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`fpaused���`a:���`a
���`l            ���bbpdself���aoa.���`ianimation���aoa.���`fresume���`a(���`a)���`a
���`h        ���akdelse���`a:���`a
���`l            ���bbpdself���aoa.���`ianimation���aoa.���`epause���`a(���`a)���`a
���`h        ���bbpdself���aoa.���`fpaused���`a ���aoa=���`a ���bowcnot���`a ���bbpdself���aoa.���`fpaused���`a
���`a
���`d    ���akcdef���`a ���bnffupdate���`a(���bbpdself���`a,���`a ���`ai���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`bn0���`a ���aoa+���aoa=���`a ���`ai���`a ���aoa/���`a ���bmic100���`a ���aoa%���`a ���bmia5���`a
���`h        ���bbpdself���aoa.���`ap���aoa.���`iset_ydata���`a(���bbpdself���aoa.���`bn0���`a ���aoa%���`a ���bmib20���`a)���`a
���`h        ���akfreturn���`a ���`a(���bbpdself���aoa.���`ap���`a,���`a)���`a
���`a
���`a
���`bpa���`a ���aoa=���`a ���`nPauseAnimation���`a(���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�