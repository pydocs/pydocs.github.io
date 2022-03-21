Ù¯‚Ù´ƒ™"Ù±‚bsdxm"""
=============
Scatter Demo2
=============

Demo of scatter plot with varying marker colors and sizes.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnecbookÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnecbookÙ±‚`a
Ù±‚`a
Ù±‚bc1xN# Load a numpy record array from yahoo csv data with fields date, open, close,Ù±‚`a
Ù±‚bc1xI# volume, adj_close from the mpl-data/example directory. The record arrayÙ±‚`a
Ù±‚bc1xO# stores the date as an np.datetime64 with a day unit ('D') in the date column.Ù±‚`a
Ù±‚`jprice_dataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚`ecbookÙ±‚aoa.Ù±‚`oget_sample_dataÙ±‚`a(Ù±‚bs1a'Ù±‚bs1hgoog.npzÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`gnp_loadÙ±‚aoa=Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a[Ù±‚bs1a'Ù±‚bs1jprice_dataÙ±‚bs1a'Ù±‚`a]Ù±‚`a
Ù±‚`n              Ù±‚aoa.Ù±‚`dviewÙ±‚`a(Ù±‚`bnpÙ±‚aoa.Ù±‚`hrecarrayÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`jprice_dataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`jprice_dataÙ±‚`a[Ù±‚aoa-Ù±‚bmic250Ù±‚`a:Ù±‚`a]Ù±‚`b  Ù±‚bc1x&# get the most recent 250 trading daysÙ±‚`a
Ù±‚`a
Ù±‚`fdelta1Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`ddiffÙ±‚`a(Ù±‚`jprice_dataÙ±‚aoa.Ù±‚`iadj_closeÙ±‚`a)Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`jprice_dataÙ±‚aoa.Ù±‚`iadj_closeÙ±‚`a[Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚bc1x"# Marker size in units of points^2Ù±‚`a
Ù±‚`fvolumeÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a(Ù±‚bmib15Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`jprice_dataÙ±‚aoa.Ù±‚`fvolumeÙ±‚`a[Ù±‚`a:Ù±‚aoa-Ù±‚bmia2Ù±‚`a]Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`jprice_dataÙ±‚aoa.Ù±‚`fvolumeÙ±‚`a[Ù±‚bmia0Ù±‚`a]Ù±‚`a)Ù±‚aoa*Ù±‚aoa*Ù±‚bmia2Ù±‚`a
Ù±‚`ecloseÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfe0.003Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`jprice_dataÙ±‚aoa.Ù±‚`ecloseÙ±‚`a[Ù±‚`a:Ù±‚aoa-Ù±‚bmia2Ù±‚`a]Ù±‚`a Ù±‚aoa/Ù±‚`a Ù±‚bmfe0.003Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`jprice_dataÙ±‚aoa.Ù±‚`dopenÙ±‚`a[Ù±‚`a:Ù±‚aoa-Ù±‚bmia2Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`gscatterÙ±‚`a(Ù±‚`fdelta1Ù±‚`a[Ù±‚`a:Ù±‚aoa-Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`fdelta1Ù±‚`a[Ù±‚bmia1Ù±‚`a:Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`acÙ±‚aoa=Ù±‚`ecloseÙ±‚`a,Ù±‚`a Ù±‚`asÙ±‚aoa=Ù±‚`fvolumeÙ±‚`a,Ù±‚`a Ù±‚`ealphaÙ±‚aoa=Ù±‚bmfc0.5Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_xlabelÙ±‚`a(Ù±‚bsaarÙ±‚bs1a'Ù±‚bs1a$Ù±‚bs1a\Ù±‚bs1hDelta_i$Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib15Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`jset_ylabelÙ±‚`a(Ù±‚bsaarÙ±‚bs1a'Ù±‚bs1a$Ù±‚bs1a\Ù±‚bs1fDelta_Ù±‚bs1a{Ù±‚bs1ei+1}$Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`hfontsizeÙ±‚aoa=Ù±‚bmib15Ù±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1xVolume and percent changeÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dgridÙ±‚`a(Ù±‚bkcdTrueÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`ltight_layoutÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö