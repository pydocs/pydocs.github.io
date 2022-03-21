ŸØÇÅŸ¥Éò¸Ÿ±ÇbsdyÀ"""
============================
Colorbar with `.AxesDivider`
============================

The `.axes_divider.make_axes_locatable` function takes an existing axes, adds
it to a new `.AxesDivider` and returns the `.AxesDivider`.  The `.append_axes`
method of the `.AxesDivider` can then be used to create a new axes on a given
side ("top", "right", "bottom", or "left") of the original axes. This example
uses `.append_axes` to add colorbars next to axes.
"""Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±ÇbknfimportŸ±Ç`a Ÿ±ÇbnnŸ¢ÑjmatplotlibŸ†Ñjmatplotlibe3.5.1fmodulejmatplotlibfmoduleıŸ±Çbnna.Ÿ±ÇbnnfpyplotŸ±Ç`a Ÿ±ÇakbasŸ±Ç`a Ÿ±ÇbnncpltŸ±Ç`a
Ÿ±ÇbkndfromŸ±Ç`a Ÿ±Çbnnlmpl_toolkitsŸ±Çbnna.Ÿ±Çbnnjaxes_grid1Ÿ±Çbnna.Ÿ±Çbnnlaxes_dividerŸ±Ç`a Ÿ±ÇbknfimportŸ±Ç`a Ÿ±Ç`smake_axes_locatableŸ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`hsubplotsŸ±Ç`a(Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`osubplots_adjustŸ±Ç`a(Ÿ±Ç`fwspaceŸ±Çaoa=Ÿ±Çbmfc0.5Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cim1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax1Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`kax1_dividerŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`smake_axes_locatableŸ±Ç`a(Ÿ±Ç`cax1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x,# Add an axes to the right of the main axes.Ÿ±Ç`a
Ÿ±Ç`dcax1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kax1_dividerŸ±Çaoa.Ÿ±Ç`kappend_axesŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2erightŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a7Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cpadŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a2Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ccb1Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cim1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccaxŸ±Çaoa=Ÿ±Ç`dcax1Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cim2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cax2Ÿ±Çaoa.Ÿ±Ç`fimshowŸ±Ç`a(Ÿ±Ç`a[Ÿ±Ç`a[Ÿ±Çbmia1Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia2Ÿ±Ç`a]Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`a[Ÿ±Çbmia3Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Çbmia4Ÿ±Ç`a]Ÿ±Ç`a]Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`kax2_dividerŸ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`smake_axes_locatableŸ±Ç`a(Ÿ±Ç`cax2Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1x"# Add an axes above the main axes.Ÿ±Ç`a
Ÿ±Ç`dcax2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`kax2_dividerŸ±Çaoa.Ÿ±Ç`kappend_axesŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2ctopŸ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`dsizeŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a7Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`cpadŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2a2Ÿ±Çbs2a%Ÿ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`ccb2Ÿ±Ç`a Ÿ±Çaoa=Ÿ±Ç`a Ÿ±Ç`cfigŸ±Çaoa.Ÿ±Ç`hcolorbarŸ±Ç`a(Ÿ±Ç`cim2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`ccaxŸ±Çaoa=Ÿ±Ç`dcax2Ÿ±Ç`a,Ÿ±Ç`a Ÿ±Ç`korientationŸ±Çaoa=Ÿ±Çbs2a"Ÿ±Çbs2jhorizontalŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Çbc1xM# Change tick position to top (with the default tick position "bottom", ticksŸ±Ç`a
Ÿ±Çbc1u# overlap the image).Ÿ±Ç`a
Ÿ±Ç`dcax2Ÿ±Çaoa.Ÿ±Ç`exaxisŸ±Çaoa.Ÿ±Ç`rset_ticks_positionŸ±Ç`a(Ÿ±Çbs2a"Ÿ±Çbs2ctopŸ±Çbs2a"Ÿ±Ç`a)Ÿ±Ç`a
Ÿ±Ç`a
Ÿ±Ç`cpltŸ±Çaoa.Ÿ±Ç`dshowŸ±Ç`a(Ÿ±Ç`a)Ÿ±Ç`a
`dNoneˆ