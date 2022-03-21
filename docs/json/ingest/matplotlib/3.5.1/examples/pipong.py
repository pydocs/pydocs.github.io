������������bsdx�"""
======
Pipong
======

A Matplotlib based game of Pong illustrating one way to write interactive
animation which are easily ported to multiple backends
pipong.py was written by Paul Ivanov <http://pirsquared.org>
"""���`a
���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bkndfrom���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����bnna.���bnnfrandom���`a ���bknfimport���`a ���`erandn���`a,���`a ���`grandint���`a
���bkndfrom���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnlfont_manager���`a ���bknfimport���`a ���`nFontProperties���`a
���`a
���`linstructions���`a ���aoa=���`a ���bs2c"""���bs2a
���bs2xPlayer A:       Player B:���bs2a
���bs2b  ���bs2a'���bs2ae���bs2a'���bs2m      up     ���bs2a'���bs2ai���bs2a'���bs2a
���bs2b  ���bs2a'���bs2ad���bs2a'���bs2m     down    ���bs2a'���bs2ak���bs2a'���bs2a
���bs2a
���bs2fpress ���bs2a'���bs2at���bs2a'���bs2x -- close these instructions���bs2a
���bs2x+            (animation will be much faster)���bs2a
���bs2fpress ���bs2a'���bs2aa���bs2a'���bs2n -- add a puck���bs2a
���bs2fpress ���bs2a'���bs2aA���bs2a'���bs2q -- remove a puck���bs2a
���bs2fpress ���bs2a'���bs2a1���bs2a'���bs2w -- slow down all pucks���bs2a
���bs2fpress ���bs2a'���bs2a2���bs2a'���bs2v -- speed up all pucks���bs2a
���bs2fpress ���bs2a'���bs2a3���bs2a'���bs2x -- slow down distractors���bs2a
���bs2fpress ���bs2a'���bs2a4���bs2a'���bs2x -- speed up distractors���bs2a
���bs2fpress ���bs2a'���bs2a ���bs2a'���bs2x -- reset the first puck���bs2a
���bs2fpress ���bs2a'���bs2an���bs2a'���bs2x -- toggle distractors on/off���bs2a
���bs2fpress ���bs2a'���bs2ag���bs2a'���bs2x -- toggle the game on/off���bs2a
���bs2a
���bs2b  ���bs2c"""���`a
���`a
���`a
���akeclass���`a ���bnccPad���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`ddisp���`a,���`a ���`ax���`a,���`a ���`ay���`a,���`a ���bnbdtype���aoa=���bs1a'���bs1al���bs1a'���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`ddisp���`a ���aoa=���`a ���`ddisp���`a
���`h        ���bbpdself���aoa.���`ax���`a ���aoa=���`a ���`ax���`a
���`h        ���bbpdself���aoa.���`ay���`a ���aoa=���`a ���`ay���`a
���`h        ���bbpdself���aoa.���`aw���`a ���aoa=���`a ���bmfb.3���`a
���`h        ���bbpdself���aoa.���`escore���`a ���aoa=���`a ���bmia0���`a
���`h        ���bbpdself���aoa.���`gxoffset���`a ���aoa=���`a ���bmfc0.3���`a
���`h        ���bbpdself���aoa.���`gyoffset���`a ���aoa=���`a ���bmfc0.1���`a
���`h        ���akbif���`a ���bnbdtype���`a ���aob==���`a ���bs1a'���bs1ar���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`gxoffset���`a ���aoa*���aoa=���`a ���aoa-���bmfc1.0���`a
���`a
���`h        ���akbif���`a ���bnbdtype���`a ���aob==���`a ���bs1a'���bs1al���bs1a'���`a ���bowbor���`a ���bnbdtype���`a ���aob==���`a ���bs1a'���bs1ar���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`esignx���`a ���aoa=���`a ���aoa-���bmfc1.0���`a
���`l            ���bbpdself���aoa.���`esigny���`a ���aoa=���`a ���bmfc1.0���`a
���`h        ���akdelse���`a:���`a
���`l            ���bbpdself���aoa.���`esignx���`a ���aoa=���`a ���bmfc1.0���`a
���`l            ���bbpdself���aoa.���`esigny���`a ���aoa=���`a ���aoa-���bmfc1.0���`a
���`a
���`d    ���akcdef���`a ���bnfhcontains���`a(���bbpdself���`a,���`a ���`cloc���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`ddisp���aoa.���`hget_bbox���`a(���`a)���aoa.���`hcontains���`a(���`cloc���aoa.���`ax���`a,���`a ���`cloc���aoa.���`ay���`a)���`a
���`a
���`a
���akeclass���`a ���bncdPuck���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`ddisp���`a,���`a ���`cpad���`a,���`a ���`efield���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`dvmax���`a ���aoa=���`a ���bmfb.2���`a
���`h        ���bbpdself���aoa.���`ddisp���`a ���aoa=���`a ���`ddisp���`a
���`h        ���bbpdself���aoa.���`efield���`a ���aoa=���`a ���`efield���`a
���`h        ���bbpdself���aoa.���`f_reset���`a(���`cpad���`a)���`a
���`a
���`d    ���akcdef���`a ���bnff_reset���`a(���bbpdself���`a,���`a ���`cpad���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`ax���`a ���aoa=���`a ���`cpad���aoa.���`ax���`a ���aoa+���`a ���`cpad���aoa.���`gxoffset���`a
���`h        ���akbif���`a ���`cpad���aoa.���`ay���`a ���aoa<���`a ���bmia0���`a:���`a
���`l            ���bbpdself���aoa.���`ay���`a ���aoa=���`a ���`cpad���aoa.���`ay���`a ���aoa+���`a ���`cpad���aoa.���`gyoffset���`a
���`h        ���akdelse���`a:���`a
���`l            ���bbpdself���aoa.���`ay���`a ���aoa=���`a ���`cpad���aoa.���`ay���`a ���aoa-���`a ���`cpad���aoa.���`gyoffset���`a
���`h        ���bbpdself���aoa.���`bvx���`a ���aoa=���`a ���`cpad���aoa.���`ax���`a ���aoa-���`a ���bbpdself���aoa.���`ax���`a
���`h        ���bbpdself���aoa.���`bvy���`a ���aoa=���`a ���`cpad���aoa.���`ay���`a ���aoa+���`a ���`cpad���aoa.���`aw���aoa/���bmia2���`a ���aoa-���`a ���bbpdself���aoa.���`ay���`a
���`h        ���bbpdself���aoa.���`k_speedlimit���`a(���`a)���`a
���`h        ���bbpdself���aoa.���`g_slower���`a(���`a)���`a
���`h        ���bbpdself���aoa.���`g_slower���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bnffupdate���`a(���bbpdself���`a,���`a ���`dpads���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`ax���`a ���aoa+���aoa=���`a ���bbpdself���aoa.���`bvx���`a
���`h        ���bbpdself���aoa.���`ay���`a ���aoa+���aoa=���`a ���bbpdself���aoa.���`bvy���`a
���`h        ���akcfor���`a ���`cpad���`a ���bowbin���`a ���`dpads���`a:���`a
���`l            ���akbif���`a ���`cpad���aoa.���`hcontains���`a(���bbpdself���`a)���`a:���`a
���`p                ���bbpdself���aoa.���`bvx���`a ���aoa*���aoa=���`a ���bmfc1.2���`a ���aoa*���`a ���`cpad���aoa.���`esignx���`a
���`p                ���bbpdself���aoa.���`bvy���`a ���aoa*���aoa=���`a ���bmfc1.2���`a ���aoa*���`a ���`cpad���aoa.���`esigny���`a
���`h        ���`efudge���`a ���aoa=���`a ���bmfd.001���`a
���`h        ���bc1x)# probably cleaner with something like...���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`ax���`a ���aoa<���`a ���`efudge���`a:���`a
���`l            ���`dpads���`a[���bmia1���`a]���aoa.���`escore���`a ���aoa+���aoa=���`a ���bmia1���`a
���`l            ���bbpdself���aoa.���`f_reset���`a(���`dpads���`a[���bmia0���`a]���`a)���`a
���`l            ���akfreturn���`a ���bkcdTrue���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`ax���`a ���aoa>���`a ���bmia7���`a ���aoa-���`a ���`efudge���`a:���`a
���`l            ���`dpads���`a[���bmia0���`a]���aoa.���`escore���`a ���aoa+���aoa=���`a ���bmia1���`a
���`l            ���bbpdself���aoa.���`f_reset���`a(���`dpads���`a[���bmia1���`a]���`a)���`a
���`l            ���akfreturn���`a ���bkcdTrue���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`ay���`a ���aoa<���`a ���aoa-���bmia1���`a ���aoa+���`a ���`efudge���`a ���bowbor���`a ���bbpdself���aoa.���`ay���`a ���aoa>���`a ���bmia1���`a ���aoa-���`a ���`efudge���`a:���`a
���`l            ���bbpdself���aoa.���`bvy���`a ���aoa*���aoa=���`a ���aoa-���bmfc1.0���`a
���`l            ���bc1x2# add some randomness, just to make it interesting���`a
���`l            ���bbpdself���aoa.���`bvy���`a ���aoa-���aoa=���`a ���`a(���`erandn���`a(���`a)���aoa/���bmfe300.0���`a ���aoa+���`a ���bmia1���aoa/���bmfe300.0���`a)���`a ���aoa*���`a ���`bnp���aoa.���`dsign���`a(���bbpdself���aoa.���`bvy���`a)���`a
���`h        ���bbpdself���aoa.���`k_speedlimit���`a(���`a)���`a
���`h        ���akfreturn���`a ���bkceFalse���`a
���`a
���`d    ���akcdef���`a ���bnfg_slower���`a(���bbpdself���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`bvx���`a ���aoa/���aoa=���`a ���bmfc5.0���`a
���`h        ���bbpdself���aoa.���`bvy���`a ���aoa/���aoa=���`a ���bmfc5.0���`a
���`a
���`d    ���akcdef���`a ���bnfg_faster���`a(���bbpdself���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`bvx���`a ���aoa*���aoa=���`a ���bmfc5.0���`a
���`h        ���bbpdself���aoa.���`bvy���`a ���aoa*���aoa=���`a ���bmfc5.0���`a
���`a
���`d    ���akcdef���`a ���bnfk_speedlimit���`a(���bbpdself���`a)���`a:���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`bvx���`a ���aoa>���`a ���bbpdself���aoa.���`dvmax���`a:���`a
���`l            ���bbpdself���aoa.���`bvx���`a ���aoa=���`a ���bbpdself���aoa.���`dvmax���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`bvx���`a ���aoa<���`a ���aoa-���bbpdself���aoa.���`dvmax���`a:���`a
���`l            ���bbpdself���aoa.���`bvx���`a ���aoa=���`a ���aoa-���bbpdself���aoa.���`dvmax���`a
���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`bvy���`a ���aoa>���`a ���bbpdself���aoa.���`dvmax���`a:���`a
���`l            ���bbpdself���aoa.���`bvy���`a ���aoa=���`a ���bbpdself���aoa.���`dvmax���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`bvy���`a ���aoa<���`a ���aoa-���bbpdself���aoa.���`dvmax���`a:���`a
���`l            ���bbpdself���aoa.���`bvy���`a ���aoa=���`a ���aoa-���bbpdself���aoa.���`dvmax���`a
���`a
���`a
���akeclass���`a ���bncdGame���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`bax���`a)���`a:���`a
���`h        ���bc1x# create the initial line���`a
���`h        ���bbpdself���aoa.���`bax���`a ���aoa=���`a ���`bax���`a
���`h        ���`bax���aoa.���`exaxis���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`h        ���`bax���aoa.���`hset_xlim���`a(���`a[���bmia0���`a,���`a ���bmia7���`a]���`a)���`a
���`h        ���`bax���aoa.���`eyaxis���aoa.���`kset_visible���`a(���bkceFalse���`a)���`a
���`h        ���`bax���aoa.���`hset_ylim���`a(���`a[���aoa-���bmia1���`a,���`a ���bmia1���`a]���`a)���`a
���`h        ���`gpad_a_x���`a ���aoa=���`a ���bmia0���`a
���`h        ���`gpad_b_x���`a ���aoa=���`a ���bmfc.50���`a
���`h        ���`gpad_a_y���`a ���aoa=���`a ���`gpad_b_y���`a ���aoa=���`a ���bmfc.30���`a
���`h        ���`gpad_b_x���`a ���aoa+���aoa=���`a ���bmfc6.3���`a
���`a
���`h        ���bc1f# pads���`a
���`h        ���`bpA���`a,���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`dbarh���`a(���`gpad_a_y���`a,���`a ���bmfb.2���`a,���`a
���`x                           ���`fheight���aoa=���bmfb.3���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`ealpha���aoa=���bmfb.5���`a,���`a ���`iedgecolor���aoa=���bs1a'���bs1ab���bs1a'���`a,���`a
���`x                           ���`blw���aoa=���bmia2���`a,���`a ���`elabel���aoa=���bs2a"���bs2hPlayer B���bs2a"���`a,���`a
���`x                           ���`hanimated���aoa=���bkcdTrue���`a)���`a
���`h        ���`bpB���`a,���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`dbarh���`a(���`gpad_b_y���`a,���`a ���bmfb.2���`a,���`a
���`x                           ���`fheight���aoa=���bmfb.3���`a,���`a ���`dleft���aoa=���`gpad_b_x���`a,���`a ���`ecolor���aoa=���bs1a'���bs1ak���bs1a'���`a,���`a ���`ealpha���aoa=���bmfb.5���`a,���`a
���`x                           ���`iedgecolor���aoa=���bs1a'���bs1ar���bs1a'���`a,���`a ���`blw���aoa=���bmia2���`a,���`a ���`elabel���aoa=���bs2a"���bs2hPlayer A���bs2a"���`a,���`a
���`x                           ���`hanimated���aoa=���bkcdTrue���`a)���`a
���`a
���`h        ���bc1m# distractors���`a
���`h        ���bbpdself���aoa.���`ax���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���bmfd2.22���aoa*���`bnp���aoa.���`bpi���`a,���`a ���bmfd0.01���`a)���`a
���`h        ���bbpdself���aoa.���`dline���`a,���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`dplot���`a(���bbpdself���aoa.���`ax���`a,���`a ���`bnp���aoa.���`csin���`a(���bbpdself���aoa.���`ax���`a)���`a,���`a ���bs2a"���bs2ar���bs2a"���`a,���`a
���`x"                                  ���`hanimated���aoa=���bkcdTrue���`a,���`a ���`blw���aoa=���bmia4���`a)���`a
���`h        ���bbpdself���aoa.���`eline2���`a,���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`dplot���`a(���bbpdself���aoa.���`ax���`a,���`a ���`bnp���aoa.���`ccos���`a(���bbpdself���aoa.���`ax���`a)���`a,���`a ���bs2a"���bs2ag���bs2a"���`a,���`a
���`x#                                   ���`hanimated���aoa=���bkcdTrue���`a,���`a ���`blw���aoa=���bmia4���`a)���`a
���`h        ���bbpdself���aoa.���`eline3���`a,���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`dplot���`a(���bbpdself���aoa.���`ax���`a,���`a ���`bnp���aoa.���`ccos���`a(���bbpdself���aoa.���`ax���`a)���`a,���`a ���bs2a"���bs2ag���bs2a"���`a,���`a
���`x#                                   ���`hanimated���aoa=���bkcdTrue���`a,���`a ���`blw���aoa=���bmia4���`a)���`a
���`h        ���bbpdself���aoa.���`eline4���`a,���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`dplot���`a(���bbpdself���aoa.���`ax���`a,���`a ���`bnp���aoa.���`ccos���`a(���bbpdself���aoa.���`ax���`a)���`a,���`a ���bs2a"���bs2ar���bs2a"���`a,���`a
���`x#                                   ���`hanimated���aoa=���bkcdTrue���`a,���`a ���`blw���aoa=���bmia4���`a)���`a
���`a
���`h        ���bc1m# center line���`a
���`h        ���bbpdself���aoa.���`jcenterline���`a,���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`dplot���`a(���`a[���bmfc3.5���`a,���`a ���bmfc3.5���`a]���`a,���`a ���`a[���bmia1���`a,���`a ���aoa-���bmia1���`a]���`a,���`a ���bs1a'���bs1ak���bs1a'���`a,���`a
���`x(                                        ���`ealpha���aoa=���bmfb.5���`a,���`a ���`hanimated���aoa=���bkcdTrue���`a,���`a ���`blw���aoa=���bmia8���`a)���`a
���`a
���`h        ���bc1j# puck (s)���`a
���`h        ���bbpdself���aoa.���`hpuckdisp���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`gscatter���`a(���`a[���bmia1���`a]���`a,���`a ���`a[���bmia1���`a]���`a,���`a ���`elabel���aoa=���bs1a'���bs1j_nolegend_���bs1a'���`a,���`a
���`x(                                        ���`as���aoa=���bmic200���`a,���`a ���`ac���aoa=���bs1a'���bs1ag���bs1a'���`a,���`a
���`x(                                        ���`ealpha���aoa=���bmfb.9���`a,���`a ���`hanimated���aoa=���bkcdTrue���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`fcanvas���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���`a
���`h        ���bbpdself���aoa.���`jbackground���`a ���aoa=���`a ���bkcdNone���`a
���`h        ���bbpdself���aoa.���`ccnt���`a ���aoa=���`a ���bmia0���`a
���`h        ���bbpdself���aoa.���`hdistract���`a ���aoa=���`a ���bkcdTrue���`a
���`h        ���bbpdself���aoa.���`cres���`a ���aoa=���`a ���bmfe100.0���`a
���`h        ���bbpdself���aoa.���`bon���`a ���aoa=���`a ���bkceFalse���`a
���`h        ���bbpdself���aoa.���`dinst���`a ���aoa=���`a ���bkcdTrue���`d    ���bc1x&# show instructions from the beginning���`a
���`h        ���bbpdself���aoa.���`dpads���`a ���aoa=���`a ���`a[���`cPad���`a(���`bpA���`a,���`a ���`gpad_a_x���`a,���`a ���`gpad_a_y���`a)���`a,���`a
���`u                     ���`cPad���`a(���`bpB���`a,���`a ���`gpad_b_x���`a,���`a ���`gpad_b_y���`a,���`a ���bs1a'���bs1ar���bs1a'���`a)���`a]���`a
���`h        ���bbpdself���aoa.���`epucks���`a ���aoa=���`a ���`a[���`a]���`a
���`h        ���bbpdself���aoa.���`ai���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`hannotate���`a(���`linstructions���`a,���`a ���`a(���bmfb.5���`a,���`a ���bmfc0.5���`a)���`a,���`a
���`x"                                  ���`dname���aoa=���bs1a'���bs1imonospace���bs1a'���`a,���`a
���`x"                                  ���`qverticalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`x"                                  ���`shorizontalalignment���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a
���`x"                                  ���`nmultialignment���aoa=���bs1a'���bs1dleft���bs1a'���`a,���`a
���`x"                                  ���`hxycoords���aoa=���bs1a'���bs1maxes fraction���bs1a'���`a,���`a
���`x"                                  ���`hanimated���aoa=���bkceFalse���`a)���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`kmpl_connect���`a(���bs1a'���bs1okey_press_event���bs1a'���`a,���`a ���bbpdself���aoa.���`lon_key_press���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfddraw���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���`kdraw_artist���`a ���aoa=���`a ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`jbackground���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���bbpdself���aoa.���`jbackground���`a ���aoa=���`a ���bbpdself���aoa.���`fcanvas���aoa.���`ncopy_from_bbox���`a(���bbpdself���aoa.���`bax���aoa.���`dbbox���`a)���`a
���`a
���`h        ���bc1x$# restore the clean slate background���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`nrestore_region���`a(���bbpdself���aoa.���`jbackground���`a)���`a
���`a
���`h        ���bc1v# show the distractors���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`hdistract���`a:���`a
���`l            ���bbpdself���aoa.���`dline���aoa.���`iset_ydata���`a(���`bnp���aoa.���`csin���`a(���bbpdself���aoa.���`ax���`a ���aoa+���`a ���bbpdself���aoa.���`ccnt���aoa/���bbpdself���aoa.���`cres���`a)���`a)���`a
���`l            ���bbpdself���aoa.���`eline2���aoa.���`iset_ydata���`a(���`bnp���aoa.���`ccos���`a(���bbpdself���aoa.���`ax���`a ���aoa-���`a ���bbpdself���aoa.���`ccnt���aoa/���bbpdself���aoa.���`cres���`a)���`a)���`a
���`l            ���bbpdself���aoa.���`eline3���aoa.���`iset_ydata���`a(���`bnp���aoa.���`ctan���`a(���bbpdself���aoa.���`ax���`a ���aoa+���`a ���bbpdself���aoa.���`ccnt���aoa/���bbpdself���aoa.���`cres���`a)���`a)���`a
���`l            ���bbpdself���aoa.���`eline4���aoa.���`iset_ydata���`a(���`bnp���aoa.���`ctan���`a(���bbpdself���aoa.���`ax���`a ���aoa-���`a ���bbpdself���aoa.���`ccnt���aoa/���bbpdself���aoa.���`cres���`a)���`a)���`a
���`l            ���`kdraw_artist���`a(���bbpdself���aoa.���`dline���`a)���`a
���`l            ���`kdraw_artist���`a(���bbpdself���aoa.���`eline2���`a)���`a
���`l            ���`kdraw_artist���`a(���bbpdself���aoa.���`eline3���`a)���`a
���`l            ���`kdraw_artist���`a(���bbpdself���aoa.���`eline4���`a)���`a
���`a
���`h        ���bc1p# pucks and pads���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`bon���`a:���`a
���`l            ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���bbpdself���aoa.���`jcenterline���`a)���`a
���`l            ���akcfor���`a ���`cpad���`a ���bowbin���`a ���bbpdself���aoa.���`dpads���`a:���`a
���`p                ���`cpad���aoa.���`ddisp���aoa.���`eset_y���`a(���`cpad���aoa.���`ay���`a)���`a
���`p                ���`cpad���aoa.���`ddisp���aoa.���`eset_x���`a(���`cpad���aoa.���`ax���`a)���`a
���`p                ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���`cpad���aoa.���`ddisp���`a)���`a
���`a
���`l            ���akcfor���`a ���`dpuck���`a ���bowbin���`a ���bbpdself���aoa.���`epucks���`a:���`a
���`p                ���akbif���`a ���`dpuck���aoa.���`fupdate���`a(���bbpdself���aoa.���`dpads���`a)���`a:���`a
���`t                    ���bc1x$# we only get here if someone scored���`a
���`t                    ���bbpdself���aoa.���`dpads���`a[���bmia0���`a]���aoa.���`ddisp���aoa.���`iset_label���`a(���`a
���`x                        ���bs2a"���bs2c   ���bs2a"���`a ���aoa+���`a ���bnbcstr���`a(���bbpdself���aoa.���`dpads���`a[���bmia0���`a]���aoa.���`escore���`a)���`a)���`a
���`t                    ���bbpdself���aoa.���`dpads���`a[���bmia1���`a]���aoa.���`ddisp���aoa.���`iset_label���`a(���`a
���`x                        ���bs2a"���bs2c   ���bs2a"���`a ���aoa+���`a ���bnbcstr���`a(���bbpdself���aoa.���`dpads���`a[���bmia1���`a]���aoa.���`escore���`a)���`a)���`a
���`t                    ���bbpdself���aoa.���`bax���aoa.���`flegend���`a(���`cloc���aoa=���bs1a'���bs1fcenter���bs1a'���`a,���`a ���`jframealpha���aoa=���bmfb.2���`a,���`a
���`x#                                   ���`ifacecolor���aoa=���bs1a'���bs1c0.5���bs1a'���`a,���`a
���`x#                                   ���`dprop���aoa=���`nFontProperties���`a(���`dsize���aoa=���bs1a'���bs1hxx-large���bs1a'���`a,���`a
���`x7                                                       ���`fweight���aoa=���bs1a'���bs1dbold���bs1a'���`a)���`a)���`a
���`a
���`t                    ���bbpdself���aoa.���`jbackground���`a ���aoa=���`a ���bkcdNone���`a
���`t                    ���bbpdself���aoa.���`bax���aoa.���`ffigure���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`t                    ���akfreturn���`a ���bkcdTrue���`a
���`p                ���`dpuck���aoa.���`ddisp���aoa.���`kset_offsets���`a(���`a[���`a[���`dpuck���aoa.���`ax���`a,���`a ���`dpuck���aoa.���`ay���`a]���`a]���`a)���`a
���`p                ���bbpdself���aoa.���`bax���aoa.���`kdraw_artist���`a(���`dpuck���aoa.���`ddisp���`a)���`a
���`a
���`h        ���bc1x # just redraw the axes rectangle���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`dblit���`a(���bbpdself���aoa.���`bax���aoa.���`dbbox���`a)���`a
���`h        ���bbpdself���aoa.���`fcanvas���aoa.���`lflush_events���`a(���`a)���`a
���`h        ���akbif���`a ���bbpdself���aoa.���`ccnt���`a ���aob==���`a ���bmie50000���`a:���`a
���`l            ���bc1x## just so we don't get carried away���`a
���`l            ���bnbeprint���`a(���bs2a"���bs2j...and you���bs2a'���bs2xve been playing for too long!!!���bs2a"���`a)���`a
���`l            ���`cplt���aoa.���`eclose���`a(���`a)���`a
���`a
���`h        ���bbpdself���aoa.���`ccnt���`a ���aoa+���aoa=���`a ���bmia1���`a
���`h        ���akfreturn���`a ���bkcdTrue���`a
���`a
���`d    ���akcdef���`a ���bnflon_key_press���`a(���bbpdself���`a,���`a ���`eevent���`a)���`a:���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1a3���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`cres���`a ���aoa*���aoa=���`a ���bmfc5.0���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1a4���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`cres���`a ���aoa/���aoa=���`a ���bmfc5.0���`a
���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1ae���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`dpads���`a[���bmia0���`a]���aoa.���`ay���`a ���aoa+���aoa=���`a ���bmfb.1���`a
���`l            ���akbif���`a ���bbpdself���aoa.���`dpads���`a[���bmia0���`a]���aoa.���`ay���`a ���aoa>���`a ���bmia1���`a ���aoa-���`a ���bmfb.3���`a:���`a
���`p                ���bbpdself���aoa.���`dpads���`a[���bmia0���`a]���aoa.���`ay���`a ���aoa=���`a ���bmia1���`a ���aoa-���`a ���bmfb.3���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1ad���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`dpads���`a[���bmia0���`a]���aoa.���`ay���`a ���aoa-���aoa=���`a ���bmfb.1���`a
���`l            ���akbif���`a ���bbpdself���aoa.���`dpads���`a[���bmia0���`a]���aoa.���`ay���`a ���aoa<���`a ���aoa-���bmia1���`a:���`a
���`p                ���bbpdself���aoa.���`dpads���`a[���bmia0���`a]���aoa.���`ay���`a ���aoa=���`a ���aoa-���bmia1���`a
���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1ai���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`dpads���`a[���bmia1���`a]���aoa.���`ay���`a ���aoa+���aoa=���`a ���bmfb.1���`a
���`l            ���akbif���`a ���bbpdself���aoa.���`dpads���`a[���bmia1���`a]���aoa.���`ay���`a ���aoa>���`a ���bmia1���`a ���aoa-���`a ���bmfb.3���`a:���`a
���`p                ���bbpdself���aoa.���`dpads���`a[���bmia1���`a]���aoa.���`ay���`a ���aoa=���`a ���bmia1���`a ���aoa-���`a ���bmfb.3���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1ak���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`dpads���`a[���bmia1���`a]���aoa.���`ay���`a ���aoa-���aoa=���`a ���bmfb.1���`a
���`l            ���akbif���`a ���bbpdself���aoa.���`dpads���`a[���bmia1���`a]���aoa.���`ay���`a ���aoa<���`a ���aoa-���bmia1���`a:���`a
���`p                ���bbpdself���aoa.���`dpads���`a[���bmia1���`a]���aoa.���`ay���`a ���aoa=���`a ���aoa-���bmia1���`a
���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1aa���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`epucks���aoa.���`fappend���`a(���`dPuck���`a(���bbpdself���aoa.���`hpuckdisp���`a,���`a
���`x#                                   ���bbpdself���aoa.���`dpads���`a[���`grandint���`a(���bmia2���`a)���`a]���`a,���`a
���`x#                                   ���bbpdself���aoa.���`bax���aoa.���`dbbox���`a)���`a)���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1aA���bs1a'���`a ���bowcand���`a ���bnbclen���`a(���bbpdself���aoa.���`epucks���`a)���`a:���`a
���`l            ���bbpdself���aoa.���`epucks���aoa.���`cpop���`a(���`a)���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1a ���bs1a'���`a ���bowcand���`a ���bnbclen���`a(���bbpdself���aoa.���`epucks���`a)���`a:���`a
���`l            ���bbpdself���aoa.���`epucks���`a[���bmia0���`a]���aoa.���`f_reset���`a(���bbpdself���aoa.���`dpads���`a[���`grandint���`a(���bmia2���`a)���`a]���`a)���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1a1���bs1a'���`a:���`a
���`l            ���akcfor���`a ���`ap���`a ���bowbin���`a ���bbpdself���aoa.���`epucks���`a:���`a
���`p                ���`ap���aoa.���`g_slower���`a(���`a)���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1a2���bs1a'���`a:���`a
���`l            ���akcfor���`a ���`ap���`a ���bowbin���`a ���bbpdself���aoa.���`epucks���`a:���`a
���`p                ���`ap���aoa.���`g_faster���`a(���`a)���`a
���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1an���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`hdistract���`a ���aoa=���`a ���bowcnot���`a ���bbpdself���aoa.���`hdistract���`a
���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1ag���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`bon���`a ���aoa=���`a ���bowcnot���`a ���bbpdself���aoa.���`bon���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1at���bs1a'���`a:���`a
���`l            ���bbpdself���aoa.���`dinst���`a ���aoa=���`a ���bowcnot���`a ���bbpdself���aoa.���`dinst���`a
���`l            ���bbpdself���aoa.���`ai���aoa.���`kset_visible���`a(���bowcnot���`a ���bbpdself���aoa.���`ai���aoa.���`kget_visible���`a(���`a)���`a)���`a
���`l            ���bbpdself���aoa.���`jbackground���`a ���aoa=���`a ���bkcdNone���`a
���`l            ���bbpdself���aoa.���`fcanvas���aoa.���`idraw_idle���`a(���`a)���`a
���`h        ���akbif���`a ���`eevent���aoa.���`ckey���`a ���aob==���`a ���bs1a'���bs1aq���bs1a'���`a:���`a
���`l            ���`cplt���aoa.���`eclose���`a(���`a)���`a
`dNone�