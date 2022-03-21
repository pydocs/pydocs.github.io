������������bsdxP"""
=======================
Animated 3D random walk
=======================

"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnianimation���`a ���akbas���`a ���bnnianimation���`a
���`a
���bc1x)# Fixing random state for reproducibility���`a
���`bnp���aoa.���`frandom���aoa.���`dseed���`a(���bmih19680801���`a)���`a
���`a
���`a
���akcdef���`a ���bnfkrandom_walk���`a(���`inum_steps���`a,���`a ���`hmax_step���aoa=���bmfd0.05���`a)���`a:���`a
���`d    ���bsdx6"""Return a 3D random walk as (num_steps, 3) array."""���`a
���`d    ���`istart_pos���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`frandom���`a(���bmia3���`a)���`a
���`d    ���`esteps���`a ���aoa=���`a ���`bnp���aoa.���`frandom���aoa.���`guniform���`a(���aoa-���`hmax_step���`a,���`a ���`hmax_step���`a,���`a ���`dsize���aoa=���`a(���`inum_steps���`a,���`a ���bmia3���`a)���`a)���`a
���`d    ���`dwalk���`a ���aoa=���`a ���`istart_pos���`a ���aoa+���`a ���`bnp���aoa.���`fcumsum���`a(���`esteps���`a,���`a ���`daxis���aoa=���bmia0���`a)���`a
���`d    ���akfreturn���`a ���`dwalk���`a
���`a
���`a
���akcdef���`a ���bnflupdate_lines���`a(���`cnum���`a,���`a ���`ewalks���`a,���`a ���`elines���`a)���`a:���`a
���`d    ���akcfor���`a ���`dline���`a,���`a ���`dwalk���`a ���bowbin���`a ���bnbczip���`a(���`elines���`a,���`a ���`ewalks���`a)���`a:���`a
���`h        ���bc1x1# NOTE: there is no .set_data() for 3 dim data...���`a
���`h        ���`dline���aoa.���`hset_data���`a(���`dwalk���`a[���`a:���`cnum���`a,���`a ���`a:���bmia2���`a]���aoa.���`aT���`a)���`a
���`h        ���`dline���aoa.���`qset_3d_properties���`a(���`dwalk���`a[���`a:���`cnum���`a,���`a ���bmia2���`a]���`a)���`a
���`d    ���akfreturn���`a ���`elines���`a
���`a
���`a
���bc1x0# Data: 40 random walks as (num_steps, 3) arrays���`a
���`inum_steps���`a ���aoa=���`a ���bmib30���`a
���`ewalks���`a ���aoa=���`a ���`a[���`krandom_walk���`a(���`inum_steps���`a)���`a ���akcfor���`a ���`eindex���`a ���bowbin���`a ���bnberange���`a(���bmib40���`a)���`a]���`a
���`a
���bc1x!# Attaching 3D axis to the figure���`a
���`cfig���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���`a
���`bax���`a ���aoa=���`a ���`cfig���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs2a"���bs2b3d���bs2a"���`a)���`a
���`a
���bc1x%# Create lines initially without data���`a
���`elines���`a ���aoa=���`a ���`a[���`bax���aoa.���`dplot���`a(���`a[���`a]���`a,���`a ���`a[���`a]���`a,���`a ���`a[���`a]���`a)���`a[���bmia0���`a]���`a ���akcfor���`a ���`a_���`a ���bowbin���`a ���`ewalks���`a]���`a
���`a
���bc1x# Setting the axes properties���`a
���`bax���aoa.���`cset���`a(���`fxlim3d���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`fxlabel���aoa=���bs1a'���bs1aX���bs1a'���`a)���`a
���`bax���aoa.���`cset���`a(���`fylim3d���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`fylabel���aoa=���bs1a'���bs1aY���bs1a'���`a)���`a
���`bax���aoa.���`cset���`a(���`fzlim3d���aoa=���`a(���bmia0���`a,���`a ���bmia1���`a)���`a,���`a ���`fzlabel���aoa=���bs1a'���bs1aZ���bs1a'���`a)���`a
���`a
���bc1x# Creating the Animation object���`a
���`cani���`a ���aoa=���`a ���`ianimation���aoa.���`mFuncAnimation���`a(���`a
���`d    ���`cfig���`a,���`a ���`lupdate_lines���`a,���`a ���`inum_steps���`a,���`a ���`efargs���aoa=���`a(���`ewalks���`a,���`a ���`elines���`a)���`a,���`a ���`hinterval���aoa=���bmic100���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�