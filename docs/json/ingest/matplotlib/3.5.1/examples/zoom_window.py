Ù¯‚Ù´ƒ™7Ù±‚bsdyØ"""
===========
Zoom Window
===========

This example shows how to connect events in one window, for example, a mouse
press, to another figure window.

If you click on a point in the first window, the z and y limits of the second
will be adjusted so that the center of the zoom in the second window will be
the (x, y) coordinates of the clicked point.

Note the diameter of the circles in the scatter are defined in points**2, so
their size is independent of the zoom.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚bc1x)# Fixing random state for reproducibilityÙ±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ffigsrcÙ±‚`a,Ù±‚`a Ù±‚`eaxsrcÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`gfigzoomÙ±‚`a,Ù±‚`a Ù±‚`faxzoomÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`eaxsrcÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`dxlimÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dylimÙ±‚aoa=Ù±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`lautoscale_onÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a,Ù±‚`a
Ù±‚`j          Ù±‚`etitleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1mClick to zoomÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`faxzoomÙ±‚aoa.Ù±‚`csetÙ±‚`a(Ù±‚`dxlimÙ±‚aoa=Ù±‚`a(Ù±‚bmfd0.45Ù±‚`a,Ù±‚`a Ù±‚bmfd0.55Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`dylimÙ±‚aoa=Ù±‚`a(Ù±‚bmfc0.4Ù±‚`a,Ù±‚`a Ù±‚bmfc0.6Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`lautoscale_onÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a,Ù±‚`a
Ù±‚`k           Ù±‚`etitleÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1kZoom windowÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚`acÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`drandÙ±‚`a(Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmic200Ù±‚`a)Ù±‚`a
Ù±‚`asÙ±‚`a Ù±‚aoa*Ù±‚aoa=Ù±‚`a Ù±‚bmic200Ù±‚`a
Ù±‚`a
Ù±‚`eaxsrcÙ±‚aoa.Ù±‚`gscatterÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚`acÙ±‚`a)Ù±‚`a
Ù±‚`faxzoomÙ±‚aoa.Ù±‚`gscatterÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚`a,Ù±‚`a Ù±‚`acÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfhon_pressÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akbifÙ±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fbuttonÙ±‚`a Ù±‚aob!=Ù±‚`a Ù±‚bmia1Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a
Ù±‚`d    Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`exdataÙ±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`eydataÙ±‚`a
Ù±‚`d    Ù±‚`faxzoomÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚`axÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`axÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`faxzoomÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`ayÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmfc0.1Ù±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`gfigzoomÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`ffigsrcÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1rbutton_press_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hon_pressÙ±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö