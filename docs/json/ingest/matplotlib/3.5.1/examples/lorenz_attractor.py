������������bsdy�"""
================
Lorenz Attractor
================

This is an example of plotting Edward Lorenz's 1963 `"Deterministic Nonperiodic
Flow"`_ in a 3-dimensional space using mplot3d.

.. _"Deterministic Nonperiodic Flow":
   https://journals.ametsoc.org/view/journals/atsc/20/2/1520-0469_1963_020_0130_dnf_2_0_co_2.xml

.. note::
   Because this is a simple non-linear ODE, it would be more easily done using
   SciPy's ODE solver, but this approach depends only upon NumPy.
"""���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfpyplot���`a ���akbas���`a ���bnncplt���`a
���`a
���`a
���akcdef���`a ���bnfflorenz���`a(���`ax���`a,���`a ���`ay���`a,���`a ���`az���`a,���`a ���`as���aoa=���bmib10���`a,���`a ���`ar���aoa=���bmib28���`a,���`a ���`ab���aoa=���bmfe2.667���`a)���`a:���`a
���`d    ���bsdy"""
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    """���`a
���`d    ���`ex_dot���`a ���aoa=���`a ���`as���aoa*���`a(���`ay���`a ���aoa-���`a ���`ax���`a)���`a
���`d    ���`ey_dot���`a ���aoa=���`a ���`ar���aoa*���`ax���`a ���aoa-���`a ���`ay���`a ���aoa-���`a ���`ax���aoa*���`az���`a
���`d    ���`ez_dot���`a ���aoa=���`a ���`ax���aoa*���`ay���`a ���aoa-���`a ���`ab���aoa*���`az���`a
���`d    ���akfreturn���`a ���`ex_dot���`a,���`a ���`ey_dot���`a,���`a ���`ez_dot���`a
���`a
���`a
���`bdt���`a ���aoa=���`a ���bmfd0.01���`a
���`inum_steps���`a ���aoa=���`a ���bmie10000���`a
���`a
���bc1x&# Need one more for the initial values���`a
���`bxs���`a ���aoa=���`a ���`bnp���aoa.���`eempty���`a(���`inum_steps���`a ���aoa+���`a ���bmia1���`a)���`a
���`bys���`a ���aoa=���`a ���`bnp���aoa.���`eempty���`a(���`inum_steps���`a ���aoa+���`a ���bmia1���`a)���`a
���`bzs���`a ���aoa=���`a ���`bnp���aoa.���`eempty���`a(���`inum_steps���`a ���aoa+���`a ���bmia1���`a)���`a
���`a
���bc1t# Set initial values���`a
���`bxs���`a[���bmia0���`a]���`a,���`a ���`bys���`a[���bmia0���`a]���`a,���`a ���`bzs���`a[���bmia0���`a]���`a ���aoa=���`a ���`a(���bmfb0.���`a,���`a ���bmfb1.���`a,���`a ���bmfd1.05���`a)���`a
���`a
���bc1xO# Step through "time", calculating the partial derivatives at the current point���`a
���bc1x+# and using them to estimate the next point���`a
���akcfor���`a ���`ai���`a ���bowbin���`a ���bnberange���`a(���`inum_steps���`a)���`a:���`a
���`d    ���`ex_dot���`a,���`a ���`ey_dot���`a,���`a ���`ez_dot���`a ���aoa=���`a ���`florenz���`a(���`bxs���`a[���`ai���`a]���`a,���`a ���`bys���`a[���`ai���`a]���`a,���`a ���`bzs���`a[���`ai���`a]���`a)���`a
���`d    ���`bxs���`a[���`ai���`a ���aoa+���`a ���bmia1���`a]���`a ���aoa=���`a ���`bxs���`a[���`ai���`a]���`a ���aoa+���`a ���`a(���`ex_dot���`a ���aoa*���`a ���`bdt���`a)���`a
���`d    ���`bys���`a[���`ai���`a ���aoa+���`a ���bmia1���`a]���`a ���aoa=���`a ���`bys���`a[���`ai���`a]���`a ���aoa+���`a ���`a(���`ey_dot���`a ���aoa*���`a ���`bdt���`a)���`a
���`d    ���`bzs���`a[���`ai���`a ���aoa+���`a ���bmia1���`a]���`a ���aoa=���`a ���`bzs���`a[���`ai���`a]���`a ���aoa+���`a ���`a(���`ez_dot���`a ���aoa*���`a ���`bdt���`a)���`a
���`a
���`a
���bc1f# Plot���`a
���`bax���`a ���aoa=���`a ���`cplt���aoa.���`ffigure���`a(���`a)���aoa.���`kadd_subplot���`a(���`jprojection���aoa=���bs1a'���bs1b3d���bs1a'���`a)���`a
���`a
���`bax���aoa.���`dplot���`a(���`bxs���`a,���`a ���`bys���`a,���`a ���`bzs���`a,���`a ���`blw���aoa=���bmfc0.5���`a)���`a
���`bax���aoa.���`jset_xlabel���`a(���bs2a"���bs2fX Axis���bs2a"���`a)���`a
���`bax���aoa.���`jset_ylabel���`a(���bs2a"���bs2fY Axis���bs2a"���`a)���`a
���`bax���aoa.���`jset_zlabel���`a(���bs2a"���bs2fZ Axis���bs2a"���`a)���`a
���`bax���aoa.���`iset_title���`a(���bs2a"���bs2pLorenz Attractor���bs2a"���`a)���`a
���`a
���`cplt���aoa.���`dshow���`a(���`a)���`a
`dNone�