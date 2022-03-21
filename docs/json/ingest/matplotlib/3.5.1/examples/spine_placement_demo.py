������������bsdx�"""
===============
Spine Placement
===============

Adjusting the location and appearance of axis spines.

Note: If you want to obtain arrow heads at the ends of the axes, also check
out the :doc:`/gallery/spines/centered_spines_with_arrows` example.
"""���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���bc1xO###############################################################################���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���aoa-���`bnp���aoa.���`bpi���`a,���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmic100���`a)���`a
���`ay���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia1���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1ocentered spines���bs1a'���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`fspines���aoa.���`dleft���aoa.���`lset_position���`a(���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`bax���aoa.���`fspines���aoa.���`eright���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`bax���aoa.���`fspines���aoa.���`fbottom���aoa.���`lset_position���`a(���bs1a'���bs1fcenter���bs1a'���`a)���`a
���`bax���aoa.���`fspines���aoa.���`ctop���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`bax���aoa.���`eyaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1dleft���bs1a'���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia2���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1mzeroed spines���bs1a'���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`fspines���aoa.���`dleft���aoa.���`lset_position���`a(���bs1a'���bs1dzero���bs1a'���`a)���`a
���`bax���aoa.���`fspines���aoa.���`eright���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`bax���aoa.���`fspines���aoa.���`fbottom���aoa.���`lset_position���`a(���bs1a'���bs1dzero���bs1a'���`a)���`a
���`bax���aoa.���`fspines���aoa.���`ctop���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`bax���aoa.���`eyaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1dleft���bs1a'���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia3���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1xspines at axes (0.6, 0.1)���bs1a'���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`fspines���aoa.���`dleft���aoa.���`lset_position���`a(���`a(���bs1a'���bs1daxes���bs1a'���`a,���`a ���bmfc0.6���`a)���`a)���`a
���`bax���aoa.���`fspines���aoa.���`eright���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`bax���aoa.���`fspines���aoa.���`fbottom���aoa.���`lset_position���`a(���`a(���bs1a'���bs1daxes���bs1a'���`a,���`a ���bmfc0.1���`a)���`a)���`a
���`bax���aoa.���`fspines���aoa.���`ctop���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`bax���aoa.���`eyaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1dleft���bs1a'���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia4���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs1a'���bs1uspines at data (1, 2)���bs1a'���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a)���`a
���`bax���aoa.���`fspines���aoa.���`dleft���aoa.���`lset_position���`a(���`a(���bs1a'���bs1ddata���bs1a'���`a,���`a ���bmia1���`a)���`a)���`a
���`bax���aoa.���`fspines���aoa.���`eright���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`bax���aoa.���`fspines���aoa.���`fbottom���aoa.���`lset_position���`a(���`a(���bs1a'���bs1ddata���bs1a'���`a,���`a ���bmia2���`a)���`a)���`a
���`bax���aoa.���`fspines���aoa.���`ctop���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`a
���`bax���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`bax���aoa.���`eyaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1dleft���bs1a'���`a)���`a
���`a
���bc1xO###############################################################################���`a
���bc1x># Define a method that adjusts the location of the axis spines���`a
���`a
���`a
���akcdef���`a ���bnfmadjust_spines���`a(���`bax���`a,���`a ���`fspines���`a)���`a:���`a
���`d    ���akcfor���`a ���`cloc���`a,���`a ���`espine���`a ���bowbin���`a ���`bax���aoa.���`fspines���aoa.���`eitems���`a(���`a)���`a:���`a
���`h        ���akbif���`a ���`cloc���`a ���bowbin���`a ���`fspines���`a:���`a
���`l            ���`espine���aoa.���`lset_position���`a(���`a(���bs1a'���bs1goutward���bs1a'���`a,���`a ���bmib10���`a)���`a)���`b  ���bc1v# outward by 10 points���`a
���`h        ���akdelse���`a:���`a
���`l            ���`espine���aoa.���`iset_color���`a(���bs1a'���bs1dnone���bs1a'���`a)���`b  ���bc1r# don't draw spine���`a
���`a
���`d    ���bc1x(# turn off ticks where there is no spine���`a
���`d    ���akbif���`a ���bs1a'���bs1dleft���bs1a'���`a ���bowbin���`a ���`fspines���`a:���`a
���`h        ���`bax���aoa.���`eyaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1dleft���bs1a'���`a)���`a
���`d    ���akdelse���`a:���`a
���`h        ���bc1p# no yaxis ticks���`a
���`h        ���`bax���aoa.���`eyaxis���aoa.���`iset_ticks���`a(���`a[���`a]���`a)���`a
���`a
���`d    ���akbif���`a ���bs1a'���bs1fbottom���bs1a'���`a ���bowbin���`a ���`fspines���`a:���`a
���`h        ���`bax���aoa.���`exaxis���aoa.���`rset_ticks_position���`a(���bs1a'���bs1fbottom���bs1a'���`a)���`a
���`d    ���akdelse���`a:���`a
���`h        ���bc1p# no xaxis ticks���`a
���`h        ���`bax���aoa.���`exaxis���aoa.���`iset_ticks���`a(���`a[���`a]���`a)���`a
���`a
���`a
���bc1xO###############################################################################���`a
���bc1x># Create another figure using our new ``adjust_spines`` method���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`a
���`ax���`a ���aoa=���`a ���`bnp���aoa.���`hlinspace���`a(���bmia0���`a,���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`bpi���`a,���`a ���bmic100���`a)���`a
���`ay���`a ���aoa=���`a ���bmia2���`a ���aoa*���`a ���`bnp���aoa.���`csin���`a(���`ax���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia1���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`gclip_on���aoa=���bkceFalse���`a)���`a
���`madjust_spines���`a(���`bax���`a,���`a ���`a[���bs1a'���bs1dleft���bs1a'���`a]���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia2���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`gclip_on���aoa=���bkceFalse���`a)���`a
���`madjust_spines���`a(���`bax���`a,���`a ���`a[���`a]���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia3���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`gclip_on���aoa=���bkceFalse���`a)���`a
���`madjust_spines���`a(���`bax���`a,���`a ���`a[���bs1a'���bs1dleft���bs1a'���`a,���`a ���bs1a'���bs1fbottom���bs1a'���`a]���`a)���`a
���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���bmia2���`a,���`a ���bmia2���`a,���`a ���bmia4���`a)���`a
���`bax���aoa.���`dplot���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`gclip_on���aoa=���bkceFalse���`a)���`a
���`madjust_spines���`a(���`bax���`a,���`a ���`a[���bs1a'���bs1fbottom���bs1a'���`a]���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�