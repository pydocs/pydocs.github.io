Ù¯‚Ù´ƒ™§Ù±‚bsdyß"""
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
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfflorenzÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`azÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚aoa=Ù±‚bmib10Ù±‚`a,Ù±‚`a Ù±‚`arÙ±‚aoa=Ù±‚bmib28Ù±‚`a,Ù±‚`a Ù±‚`abÙ±‚aoa=Ù±‚bmfe2.667Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdy"""
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    """Ù±‚`a
Ù±‚`d    Ù±‚`ex_dotÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`asÙ±‚aoa*Ù±‚`a(Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`axÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`ey_dotÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`arÙ±‚aoa*Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`axÙ±‚aoa*Ù±‚`azÙ±‚`a
Ù±‚`d    Ù±‚`ez_dotÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`axÙ±‚aoa*Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`abÙ±‚aoa*Ù±‚`azÙ±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`ex_dotÙ±‚`a,Ù±‚`a Ù±‚`ey_dotÙ±‚`a,Ù±‚`a Ù±‚`ez_dotÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`bdtÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfd0.01Ù±‚`a
Ù±‚`inum_stepsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmie10000Ù±‚`a
Ù±‚`a
Ù±‚bc1x&# Need one more for the initial valuesÙ±‚`a
Ù±‚`bxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`eemptyÙ±‚`a(Ù±‚`inum_stepsÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`bysÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`eemptyÙ±‚`a(Ù±‚`inum_stepsÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`bzsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`eemptyÙ±‚`a(Ù±‚`inum_stepsÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1t# Set initial valuesÙ±‚`a
Ù±‚`bxsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`bysÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`bzsÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmfb0.Ù±‚`a,Ù±‚`a Ù±‚bmfb1.Ù±‚`a,Ù±‚`a Ù±‚bmfd1.05Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xO# Step through "time", calculating the partial derivatives at the current pointÙ±‚`a
Ù±‚bc1x+# and using them to estimate the next pointÙ±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚`inum_stepsÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`ex_dotÙ±‚`a,Ù±‚`a Ù±‚`ey_dotÙ±‚`a,Ù±‚`a Ù±‚`ez_dotÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`florenzÙ±‚`a(Ù±‚`bxsÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`bysÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`bzsÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bxsÙ±‚`a[Ù±‚`aiÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bxsÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`a(Ù±‚`ex_dotÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bdtÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bysÙ±‚`a[Ù±‚`aiÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bysÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`a(Ù±‚`ey_dotÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bdtÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`bzsÙ±‚`a[Ù±‚`aiÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bzsÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`a(Ù±‚`ez_dotÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`bdtÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1f# PlotÙ±‚`a
Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`ffigureÙ±‚`a(Ù±‚`a)Ù±‚aoa.Ù±‚`kadd_subplotÙ±‚`a(Ù±‚`jprojectionÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1b3dÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bxsÙ±‚`a,Ù±‚`a Ù±‚`bysÙ±‚`a,Ù±‚`a Ù±‚`bzsÙ±‚`a,Ù±‚`a Ù±‚`blwÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bs2a"Ù±‚bs2fX AxisÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs2a"Ù±‚bs2fY AxisÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_zlabelÙ±‚`a(Ù±‚bs2a"Ù±‚bs2fZ AxisÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2pLorenz AttractorÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö