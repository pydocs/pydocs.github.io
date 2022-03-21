��������@���bsdy
"""
===========================
The double pendulum problem
===========================

This animation illustrates the double pendulum problem.

Double pendulum formula translated from the C code at
http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c
"""���`a
���`a
���bkndfrom���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���bknfimport���`a ���`csin���`a,���`a ���`ccos���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���escipy���escipye1.8.0fmoduleescipyfmodule����bnna.���bnniintegrate���`a ���akbas���`a ���bnniintegrate���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnianimation���`a ���akbas���`a ���bnnianimation���`a
���bkndfrom���`a ���bnnkcollections���`a ���bknfimport���`a ���`edeque���`a
���`a
���`aG���`a ���aoa=���`a ���bmfc9.8���`b  ���bc1x'# acceleration due to gravity, in m/s^2���`a
���`bL1���`a ���aoa=���`a ���bmfc1.0���`b  ���bc1x# length of pendulum 1 in m���`a
���`bL2���`a ���aoa=���`a ���bmfc1.0���`b  ���bc1x# length of pendulum 2 in m���`a
���`aL���`a ���aoa=���`a ���`bL1���`a ���aoa+���`a ���`bL2���`b  ���bc1x)# maximal length of the combined pendulum���`a
���`bM1���`a ���aoa=���`a ���bmfc1.0���`b  ���bc1x# mass of pendulum 1 in kg���`a
���`bM2���`a ���aoa=���`a ���bmfc1.0���`b  ���bc1x# mass of pendulum 2 in kg���`a
���`ft_stop���`a ���aoa=���`a ���bmia5���`b  ���bc1x# how many seconds to simulate���`a
���`khistory_len���`a ���aoa=���`a ���bmic500���`b  ���bc1x'# how many trajectory points to display���`a
���`a
���`a
���akcdef���`a ���bnffderivs���`a(���`estate���`a,���`a ���`at���`a)���`a:���`a
���`a
���`d    ���`ddydx���`a ���aoa=���`a ���`bnp���aoa.���`jzeros_like���`a(���`estate���`a)���`a
���`d    ���`ddydx���`a[���bmia0���`a]���`a ���aoa=���`a ���`estate���`a[���bmia1���`a]���`a
���`a
���`d    ���`edelta���`a ���aoa=���`a ���`estate���`a[���bmia2���`a]���`a ���aoa-���`a ���`estate���`a[���bmia0���`a]���`a
���`d    ���`dden1���`a ���aoa=���`a ���`a(���`bM1���aoa+���`bM2���`a)���`a ���aoa*���`a ���`bL1���`a ���aoa-���`a ���`bM2���`a ���aoa*���`a ���`bL1���`a ���aoa*���`a ���`ccos���`a(���`edelta���`a)���`a ���aoa*���`a ���`ccos���`a(���`edelta���`a)���`a
���`d    ���`ddydx���`a[���bmia1���`a]���`a ���aoa=���`a ���`a(���`a(���`bM2���`a ���aoa*���`a ���`bL1���`a ���aoa*���`a ���`estate���`a[���bmia1���`a]���`a ���aoa*���`a ���`estate���`a[���bmia1���`a]���`a ���aoa*���`a ���`csin���`a(���`edelta���`a)���`a ���aoa*���`a ���`ccos���`a(���`edelta���`a)���`a
���`p                ���aoa+���`a ���`bM2���`a ���aoa*���`a ���`aG���`a ���aoa*���`a ���`csin���`a(���`estate���`a[���bmia2���`a]���`a)���`a ���aoa*���`a ���`ccos���`a(���`edelta���`a)���`a
���`p                ���aoa+���`a ���`bM2���`a ���aoa*���`a ���`bL2���`a ���aoa*���`a ���`estate���`a[���bmia3���`a]���`a ���aoa*���`a ���`estate���`a[���bmia3���`a]���`a ���aoa*���`a ���`csin���`a(���`edelta���`a)���`a
���`p                ���aoa-���`a ���`a(���`bM1���aoa+���`bM2���`a)���`a ���aoa*���`a ���`aG���`a ���aoa*���`a ���`csin���`a(���`estate���`a[���bmia0���`a]���`a)���`a)���`a
���`o               ���aoa/���`a ���`dden1���`a)���`a
���`a
���`d    ���`ddydx���`a[���bmia2���`a]���`a ���aoa=���`a ���`estate���`a[���bmia3���`a]���`a
���`a
���`d    ���`dden2���`a ���aoa=���`a ���`a(���`bL2���aoa/���`bL1���`a)���`a ���aoa*���`a ���`dden1���`a
���`d    ���`ddydx���`a[���bmia3���`a]���`a ���aoa=���`a ���`a(���`a(���aoa-���`a ���`bM2���`a ���aoa*���`a ���`bL2���`a ���aoa*���`a ���`estate���`a[���bmia3���`a]���`a ���aoa*���`a ���`estate���`a[���bmia3���`a]���`a ���aoa*���`a ���`csin���`a(���`edelta���`a)���`a ���aoa*���`a ���`ccos���`a(���`edelta���`a)���`a
���`p                ���aoa+���`a ���`a(���`bM1���aoa+���`bM2���`a)���`a ���aoa*���`a ���`aG���`a ���aoa*���`a ���`csin���`a(���`estate���`a[���bmia0���`a]���`a)���`a ���aoa*���`a ���`ccos���`a(���`edelta���`a)���`a
���`p                ���aoa-���`a ���`a(���`bM1���aoa+���`bM2���`a)���`a ���aoa*���`a ���`bL1���`a ���aoa*���`a ���`estate���`a[���bmia1���`a]���`a ���aoa*���`a ���`estate���`a[���bmia1���`a]���`a ���aoa*���`a ���`csin���`a(���`edelta���`a)���`a
���`p                ���aoa-���`a ���`a(���`bM1���aoa+���`bM2���`a)���`a ���aoa*���`a ���`aG���`a ���aoa*���`a ���`csin���`a(���`estate���`a[���bmia2���`a]���`a)���`a)���`a
���`o               ���aoa/���`a ���`dden2���`a)���`a
���`a
���`d    ���akfreturn���`a ���`ddydx���`a
���`a
���bc1xA# create a time array from 0..t_stop sampled at 0.02 second steps���`a
���`bdt���`a ���aoa=���`a ���bmfd0.02���`a
���`at���`a ���aoa=���`a ���`bnp���aoa.���`farange���`a(���bmia0���`a,���`a ���`ft_stop���`a,���`a ���`bdt���`a)���`a
���`a
���bc1x.# th1 and th2 are the initial angles (degrees)���`a
���bc1xE# w10 and w20 are the initial angular velocities (degrees per second)���`a
���`cth1���`a ���aoa=���`a ���bmfe120.0���`a
���`bw1���`a ���aoa=���`a ���bmfc0.0���`a
���`cth2���`a ���aoa=���`a ���aoa-���bmfd10.0���`a
���`bw2���`a ���aoa=���`a ���bmfc0.0���`a
���`a
���bc1o# initial state���`a
���`estate���`a ���aoa=���`a ���`bnp���aoa.���`gradians���`a(���`a[���`cth1���`a,���`a ���`bw1���`a,���`a ���`cth2���`a,���`a ���`bw2���`a]���`a)���`a
���`a
���bc1x+# integrate your ODE using scipy.integrate.���`a
���`ay���`a ���aoa=���`a ���`iintegrate���aoa.���`fodeint���`a(���`fderivs���`a,���`a ���`estate���`a,���`a ���`at���`a)���`a
���`a
���`bx1���`a ���aoa=���`a ���`bL1���aoa*���`csin���`a(���`ay���`a[���`a:���`a,���`a ���bmia0���`a]���`a)���`a
���`by1���`a ���aoa=���`a ���aoa-���`bL1���aoa*���`ccos���`a(���`ay���`a[���`a:���`a,���`a ���bmia0���`a]���`a)���`a
���`a
���`bx2���`a ���aoa=���`a ���`bL2���aoa*���`csin���`a(���`ay���`a[���`a:���`a,���`a ���bmia2���`a]���`a)���`a ���aoa+���`a ���`bx1���`a
���`by2���`a ���aoa=���`a ���aoa-���`bL2���aoa*���`ccos���`a(���`ay���`a[���`a:���`a,���`a ���bmia2���`a]���`a)���`a ���aoa+���`a ���`by1���`a
���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`gfigsize���aoa=���`a(���bmia5���`a,���`a ���bmia4���`a)���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`lautoscale_on���aoa=���bkceFalse���`a,���`a ���`dxlim���aoa=���`a(���aoa-���`aL���`a,���`a ���`aL���`a)���`a,���`a ���`dylim���aoa=���`a(���aoa-���`aL���`a,���`a ���bmfb1.���`a)���`a)���`a
���`bax���aoa.���`jset_aspect���`a(���bs1a'���bs1eequal���bs1a'���`a)���`a
���`bax���aoa.���`dgrid���`a(���`a)���`a
���`a
���`dline���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`a[���`a]���`a,���`a ���`a[���`a]���`a,���`a ���bs1a'���bs1bo-���bs1a'���`a,���`a ���`blw���aoa=���bmia2���`a)���`a
���`etrace���`a,���`a ���aoa=���`a ���`bax���aoa.���`dplot���`a(���`a[���`a]���`a,���`a ���`a[���`a]���`a,���`a ���bs1a'���bs1b.-���bs1a'���`a,���`a ���`blw���aoa=���bmia1���`a,���`a ���`bms���aoa=���bmia2���`a)���`a
���`mtime_template���`a ���aoa=���`a ���bs1a'���bs1gtime = ���bsid%.1f���bs1as���bs1a'���`a
���`itime_text���`a ���aoa=���`a ���`bax���aoa.���`dtext���`a(���bmfd0.05���`a,���`a ���bmfc0.9���`a,���`a ���bs1a'���bs1a'���`a,���`a ���`itransform���aoa=���`bax���aoa.���`itransAxes���`a)���`a
���`ihistory_x���`a,���`a ���`ihistory_y���`a ���aoa=���`a ���`edeque���`a(���`fmaxlen���aoa=���`khistory_len���`a)���`a,���`a ���`edeque���`a(���`fmaxlen���aoa=���`khistory_len���`a)���`a
���`a
���`a
���akcdef���`a ���bnfganimate���`a(���`ai���`a)���`a:���`a
���`d    ���`ethisx���`a ���aoa=���`a ���`a[���bmia0���`a,���`a ���`bx1���`a[���`ai���`a]���`a,���`a ���`bx2���`a[���`ai���`a]���`a]���`a
���`d    ���`ethisy���`a ���aoa=���`a ���`a[���bmia0���`a,���`a ���`by1���`a[���`ai���`a]���`a,���`a ���`by2���`a[���`ai���`a]���`a]���`a
���`a
���`d    ���akbif���`a ���`ai���`a ���aob==���`a ���bmia0���`a:���`a
���`h        ���`ihistory_x���aoa.���`eclear���`a(���`a)���`a
���`h        ���`ihistory_y���aoa.���`eclear���`a(���`a)���`a
���`a
���`d    ���`ihistory_x���aoa.���`jappendleft���`a(���`ethisx���`a[���bmia2���`a]���`a)���`a
���`d    ���`ihistory_y���aoa.���`jappendleft���`a(���`ethisy���`a[���bmia2���`a]���`a)���`a
���`a
���`d    ���`dline���aoa.���`hset_data���`a(���`ethisx���`a,���`a ���`ethisy���`a)���`a
���`d    ���`etrace���aoa.���`hset_data���`a(���`ihistory_x���`a,���`a ���`ihistory_y���`a)���`a
���`d    ���`itime_text���aoa.���`hset_text���`a(���`mtime_template���`a ���aoa%���`a ���`a(���`ai���aoa*���`bdt���`a)���`a)���`a
���`d    ���akfreturn���`a ���`dline���`a,���`a ���`etrace���`a,���`a ���`itime_text���`a
���`a
���`a
���`cani���`a ���aoa=���`a ���`ianimation���aoa.���`mFuncAnimation���`a(���`a
���`d    ���`cfig���`a,���`a ���`ganimate���`a,���`a ���bnbclen���`a(���`ay���`a)���`a,���`a ���`hinterval���aoa=���`bdt���aoa*���bmid1000���`a,���`a ���`dblit���aoa=���bkcdTrue���`a)���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�