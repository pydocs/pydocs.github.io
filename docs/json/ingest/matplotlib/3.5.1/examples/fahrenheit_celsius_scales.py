Ù¯‚Ù´ƒ˜ñÙ±‚bsdxä"""
=================================
Different scales on the same axes
=================================

Demo of how to display two scales on the left and right y axis.

This example uses the Fahrenheit and Celsius scales.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfrfahrenheit2celsiusÙ±‚`a(Ù±‚`dtempÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bsdxL"""
    Returns temperature in Celsius given Fahrenheit temperature.
    """Ù±‚`a
Ù±‚`d    Ù±‚akfreturnÙ±‚`a Ù±‚`a(Ù±‚bmfb5.Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfb9.Ù±‚`a)Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`a(Ù±‚`dtempÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚bmib32Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfimake_plotÙ±‚`a(Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x5# Define a closure function to register as a callbackÙ±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfwconvert_ax_c_to_celsiusÙ±‚`a(Ù±‚`dax_fÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdxE"""
        Update second axis according with first axis.
        """Ù±‚`a
Ù±‚`h        Ù±‚`by1Ù±‚`a,Ù±‚`a Ù±‚`by2Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dax_fÙ±‚aoa.Ù±‚`hget_ylimÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`dax_cÙ±‚aoa.Ù±‚`hset_ylimÙ±‚`a(Ù±‚`rfahrenheit2celsiusÙ±‚`a(Ù±‚`by1Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`rfahrenheit2celsiusÙ±‚`a(Ù±‚`by2Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`h        Ù±‚`dax_cÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`dax_fÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dax_cÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dax_fÙ±‚aoa.Ù±‚`etwinxÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bc1x<# automatically update ylim of ax2 when ylim of ax1 changes.Ù±‚`a
Ù±‚`d    Ù±‚`dax_fÙ±‚aoa.Ù±‚`icallbacksÙ±‚aoa.Ù±‚`gconnectÙ±‚`a(Ù±‚bs2a"Ù±‚bs2lylim_changedÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚`wconvert_ax_c_to_celsiusÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dax_fÙ±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`hlinspaceÙ±‚`a(Ù±‚aoa-Ù±‚bmib40Ù±‚`a,Ù±‚`a Ù±‚bmic120Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dax_fÙ±‚aoa.Ù±‚`hset_xlimÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`dax_fÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x"Two scales: Fahrenheit and CelsiusÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dax_fÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jFahrenheitÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`dax_cÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bs1a'Ù±‚bs1gCelsiusÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`imake_plotÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö