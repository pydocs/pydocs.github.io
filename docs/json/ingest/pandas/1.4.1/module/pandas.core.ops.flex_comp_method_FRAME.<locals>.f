Ùª­jAttributesÙ¯‚€öpExtended SummaryÙ¯‚‚Ù¹‚Ù§xAmong flexible wrappers (Ù£ƒbeqööÙ§b, Ù£ƒbneööÙ§b, Ù£ƒbleööÙ§b, Ù£ƒbltööÙ§b, Ù£ƒbgeööÙ§b, Ù£ƒbgtööÙ§x) to comparison operators.€Ù¹‚Ù§nEquivalent to Ù£ƒb==ööÙ§b, Ù£ƒb!=ööÙ§b, Ù£ƒb<=ööÙ§b, Ù£ƒa<ööÙ§b, Ù£ƒb>=ööÙ§b, Ù£ƒa>ööÙ§xH with support to choose axis (rows or columns) and level for comparison.€ögMethodsÙ¯‚€öeNotesÙ¯‚Ù¹‚‡Ù§x-Mismatched indices will be unioned together. Ù¢„cNaNÙ „fpandase1.4.1fmodulex pandas.errors.IntCastingNaNErrorfmoduleõÙ§x' values are considered different (i.e. Ù¢„cNaNÙ „fpandase1.4.1fmodulex pandas.errors.IntCastingNaNErrorfmoduleõÙ§d != Ù¢„cNaNÙ „fpandase1.4.1fmodulex pandas.errors.IntCastingNaNErrorfmoduleõÙ§b).€öpOther ParametersÙ¯‚€öjParametersÙ¯‚ƒÙ°ƒeotherx&scalar, sequence, Series, or DataFrameÙ¹‚Ù§xCAny single or multiple element data structure, or list-like object.€Ù°ƒdaxisx1{0 or 'index', 1 or 'columns'}, default 'columns'Ù¹‚Ù§xKWhether to compare by the index (0 or 'index') or columns (1 or 'columns').€Ù°ƒelevellint or labelÙ¹‚Ù§xOBroadcast across a level, matching Index values on the passed MultiIndex level.€öfRaisesÙ¯‚€öhReceivesÙ¯‚€ögReturnsÙ¯‚Ù°ƒ`qDataFrame of boolÙ¹‚Ù§xResult of the comparison.€ögSummaryÙ¯‚Ù¹‚ƒÙ§xSGet Greater than or equal to of dataframe and other, element-wise (binary operator Ù£ƒbgeööÙ§b).€öhWarningsÙ¯‚€öeWarnsÙ¯‚€öfYieldsÙ¯‚€ö‡gSummarypExtended SummaryjParametersgReturnshSee AlsoeNoteshExamplesx/pandas/core/ops/__init__.pyĞr<class 'function'>†spandas.DataFrame.eqspandas.DataFrame.nespandas.DataFrame.ltspandas.DataFrame.gtspandas.DataFrame.lespandas.DataFrame.geÙ¯‚’Ù´ƒ˜@Ù±‚`bdfÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bpdÙ±‚aoa.Ù±‚`Ù¢„iDataFrameÙ „fpandase1.4.1fmodulexpandas.core.frame.DataFramefmoduleõÙ±‚`a(Ù±‚`a{Ù±‚bs1a'Ù±‚bs1dcostÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`a[Ù±‚bmic250Ù±‚`a,Ù±‚`a Ù±‚bmic150Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`s                   Ù±‚bs1a'Ù±‚bs1grevenueÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`a[Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic250Ù±‚`a,Ù±‚`a Ù±‚bmic300Ù±‚`a]Ù±‚`a}Ù±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚`eindexÙ±‚aoa=Ù±‚`a[Ù±‚bs1a'Ù±‚bs1aAÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aBÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aCÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`bdfxC   cost  revenue
A   250      100
B   150      250
C   100      300hcompiledÙ¹‚Ù§x>Comparison with a scalar, using either the operator or method:€Ù´ƒ…Ù±‚`bdfÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmic100xG    cost  revenue
A  False     True
B  False    False
C   True    FalsehcompiledÙ´ƒ†Ù±‚`bdfÙ±‚aoa.Ù±‚`beqÙ±‚`a(Ù±‚bmic100Ù±‚`a)xG    cost  revenue
A  False     True
B  False    False
C   True    FalsehcompiledÙ¹‚‡Ù§eWhen Ù¢„eotherÙ „ööelocaleotherelocalõÙ§f is a Ù¢„fSeriesÙ „fpandase1.4.1fmodulexpandas.core.series.SeriesfmoduleõÙ§x;, the columns of a DataFrame are aligned with the index of Ù¢„eotherÙ „ööelocaleotherelocalõÙ§o and broadcast:€Ù´ƒ˜Ù±‚`bdfÙ±‚`a Ù±‚aob!=Ù±‚`a Ù±‚`bpdÙ±‚aoa.Ù±‚`Ù¢„fSeriesÙ „fpandase1.4.1fmodulexpandas.core.series.SeriesfmoduleõÙ±‚`a(Ù±‚`a[Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic250Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`eindexÙ±‚aoa=Ù±‚`a[Ù±‚bs2a"Ù±‚bs2dcostÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2grevenueÙ±‚bs2a"Ù±‚`a]Ù±‚`a)xG    cost  revenue
A   True     True
B   True    False
C  False     TruehcompiledÙ¹‚Ù§x-Use the method to control the broadcast axis:€Ù´ƒ˜%Ù±‚`bdfÙ±‚aoa.Ù±‚`bneÙ±‚`a(Ù±‚`bpdÙ±‚aoa.Ù±‚`Ù¢„fSeriesÙ „fpandase1.4.1fmodulexpandas.core.series.SeriesfmoduleõÙ±‚`a(Ù±‚`a[Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic300Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`eindexÙ±‚aoa=Ù±‚`a[Ù±‚bs2a"Ù±‚bs2aAÙ±‚bs2a"Ù±‚`a,Ù±‚`a Ù±‚bs2a"Ù±‚bs2aDÙ±‚bs2a"Ù±‚`a]Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eindexÙ±‚bs1a'Ù±‚`a)xT   cost  revenue
A  True    False
B  True     True
C  True     True
D  True     TruehcompiledÙ¹‚ƒÙ§xaWhen comparing to an arbitrary sequence, the number of columns must match the number elements in Ù¢„eotherÙ „ööelocaleotherelocalõÙ§a:€Ù´ƒŠÙ±‚`bdfÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚`a[Ù±‚bmic250Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a]xG    cost  revenue
A   True     True
B  False    False
C  False    FalsehcompiledÙ¹‚Ù§x#Use the method to control the axis:€Ù´ƒ•Ù±‚`bdfÙ±‚aoa.Ù±‚`beqÙ±‚`a(Ù±‚`a[Ù±‚bmic250Ù±‚`a,Ù±‚`a Ù±‚bmic250Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eindexÙ±‚bs1a'Ù±‚`a)xG    cost  revenue
A   True    False
B  False     True
C   True    FalsehcompiledÙ¹‚Ù§x*Compare to a DataFrame of different shape.€Ù´ƒ˜7Ù±‚`Ù¢„eotherÙ „fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmoduleõÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bpdÙ±‚aoa.Ù±‚`Ù¢„iDataFrameÙ „fpandase1.4.1fmodulexpandas.core.frame.DataFramefmoduleõÙ±‚`a(Ù±‚`a{Ù±‚bs1a'Ù±‚bs1grevenueÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`a[Ù±‚bmic300Ù±‚`a,Ù±‚`a Ù±‚bmic250Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic150Ù±‚`a]Ù±‚`a}Ù±‚`a,Ù±‚`a
Ù±‚`u                     Ù±‚`eindexÙ±‚aoa=Ù±‚`a[Ù±‚bs1a'Ù±‚bs1aAÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aBÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aCÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aDÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`Ù¢„eotherÙ „fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmoduleõx6   revenue
A      300
B      250
C      100
D      150hcompiledÙ´ƒ†Ù±‚`bdfÙ±‚aoa.Ù±‚`bgtÙ±‚`a(Ù±‚`Ù¢„eotherÙ „fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmoduleõÙ±‚`a)xY    cost  revenue
A  False    False
B  False    False
C  False     True
D  False    FalsehcompiledÙ¹‚Ù§x!Compare to a MultiIndex by level.€Ù´ƒ˜„Ù±‚`ldf_multindexÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bpdÙ±‚aoa.Ù±‚`Ù¢„iDataFrameÙ „fpandase1.4.1fmodulexpandas.core.frame.DataFramefmoduleõÙ±‚`a(Ù±‚`a{Ù±‚bs1a'Ù±‚bs1dcostÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`a[Ù±‚bmic250Ù±‚`a,Ù±‚`a Ù±‚bmic150Ù±‚`a,Ù±‚`a Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic150Ù±‚`a,Ù±‚`a Ù±‚bmic300Ù±‚`a,Ù±‚`a Ù±‚bmic220Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x                             Ù±‚bs1a'Ù±‚bs1grevenueÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`a[Ù±‚bmic100Ù±‚`a,Ù±‚`a Ù±‚bmic250Ù±‚`a,Ù±‚`a Ù±‚bmic300Ù±‚`a,Ù±‚`a Ù±‚bmic200Ù±‚`a,Ù±‚`a Ù±‚bmic175Ù±‚`a,Ù±‚`a Ù±‚bmic225Ù±‚`a]Ù±‚`a}Ù±‚`a,Ù±‚`a
Ù±‚`x                            Ù±‚`eindexÙ±‚aoa=Ù±‚`a[Ù±‚`a[Ù±‚bs1a'Ù±‚bs1bQ1Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bQ1Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bQ1Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bQ2Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bQ2Ù±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1bQ2Ù±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x#                                   Ù±‚`a[Ù±‚bs1a'Ù±‚bs1aAÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aBÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aCÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aAÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aBÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aCÙ±‚bs1a'Ù±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`ldf_multindexx‹      cost  revenue
Q1 A   250      100
   B   150      250
   C   100      300
Q2 A   150      200
   B   300      175
   C   220      225hcompiledÙ´ƒ‹Ù±‚`bdfÙ±‚aoa.Ù±‚`bleÙ±‚`a(Ù±‚`ldf_multindexÙ±‚`a,Ù±‚`a Ù±‚`elevelÙ±‚aoa=Ù±‚bmia1Ù±‚`a)x’       cost  revenue
Q1 A   True     True
   B   True     True
   C   True     True
Q2 A  False     True
   B   True    False
   C   True    Falsehcompiledö†Ù¼ƒÙ»ƒlDataFrame.eqööÙ¹‚Ù§x,Compare DataFrames for equality elementwise.€öÙ¼ƒÙ»ƒlDataFrame.geööÙ¹‚Ù§xGCompare DataFrames for greater than inequality or equality elementwise.€öÙ¼ƒÙ»ƒlDataFrame.gtööÙ¹‚Ù§xDCompare DataFrames for strictly greater than inequality elementwise.€öÙ¼ƒÙ»ƒlDataFrame.leööÙ¹‚Ù§xDCompare DataFrames for less than inequality or equality elementwise.€öÙ¼ƒÙ»ƒlDataFrame.ltööÙ¹‚Ù§xACompare DataFrames for strictly less than inequality elementwise.€öÙ¼ƒÙ»ƒlDataFrame.neööÙ¹‚Ù§x.Compare DataFrames for inequality elementwise.€öe1.4.1Ù«x*f(self, other, axis='columns', level=None)öx1pandas.core.ops.flex_comp_method_FRAME.<locals>.f€