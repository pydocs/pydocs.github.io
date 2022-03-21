Ùª­jAttributesÙ¯‚€öpExtended SummaryÙ¯‚‚Ù¹‚…Ù§nEquivalent to Ù¡qdataframe / otherÙ§xk, but with support to substitute a fill_value for missing data in one of the inputs. With reverse version, Ù¢„hrtruedivÙ „fpandase1.4.1fmodulexpandas.core.roperator.rtruedivfmoduleõÙ§a.€Ù¹‚˜Ù§xAmong flexible wrappers (Ù£ƒcaddööÙ§b, Ù£ƒcsubööÙ§b, Ù£ƒcmulööÙ§b, Ù£ƒcdivööÙ§b, Ù£ƒcmodööÙ§b, Ù£ƒcpowööÙ§x) to arithmetic operators: Ù£ƒa+ööÙ§b, Ù£ƒa-ööÙ§b, Ù£ƒa*ööÙ§b, Ù£ƒa/ööÙ§b, Ù£ƒb//ööÙ§b, Ù£ƒa%ööÙ§b, Ù£ƒb**ööÙ§a.€ögMethodsÙ¯‚€öeNotesÙ¯‚Ù¹‚Ù§x,Mismatched indices will be unioned together.€öpOther ParametersÙ¯‚€öjParametersÙ¯‚„Ù°ƒeotherx&scalar, sequence, Series, or DataFrameÙ¹‚Ù§xCAny single or multiple element data structure, or list-like object.€Ù°ƒdaxisx{0 or 'index', 1 or 'columns'}Ù¹‚Ù§x|Whether to compare by the index (0 or 'index') or columns (1 or 'columns'). For Series input, axis to match Series index on.€Ù°ƒelevellint or labelÙ¹‚Ù§xOBroadcast across a level, matching Index values on the passed MultiIndex level.€Ù°ƒjfill_valuexfloat or None, default NoneÙ¹‚Ù§xßFill existing missing (NaN) values, and any new element needed for successful DataFrame alignment, with this value before computation. If data in both corresponding DataFrame locations is missing the result will be missing.€öfRaisesÙ¯‚€öhReceivesÙ¯‚€ögReturnsÙ¯‚Ù°ƒ`iDataFrameÙ¹‚Ù§x#Result of the arithmetic operation.€ögSummaryÙ¯‚Ù¹‚ƒÙ§xLGet Floating division of dataframe and other, element-wise (binary operator Ù£ƒgtruedivööÙ§b).€öhWarningsÙ¯‚€öeWarnsÙ¯‚€öfYieldsÙ¯‚€ö‡gSummarypExtended SummaryjParametersgReturnshSee AlsoeNoteshExamplesx/pandas/core/ops/__init__.py¢r<class 'function'>“tpandas.DataFrame.addupandas.DataFrame.raddtpandas.DataFrame.subtpandas.DataFrame.mulxpandas.DataFrame.truedivxpandas.DataFrame.floordivtpandas.DataFrame.modtpandas.DataFrame.powupandas.DataFrame.rmulupandas.DataFrame.rsubxpandas.DataFrame.rtruedivxpandas.DataFrame.rfloordivupandas.DataFrame.rpowupandas.DataFrame.rmodtpandas.DataFrame.divupandas.DataFrame.rdivxpandas.DataFrame.multiplyxpandas.DataFrame.subtractwpandas.DataFrame.divideÙ¯‚’Ù´ƒ˜@Ù±‚`bdfÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bpdÙ±‚aoa.Ù±‚`Ù¢„iDataFrameÙ „fpandase1.4.1fmodulexpandas.core.frame.DataFramefmoduleõÙ±‚`a(Ù±‚`a{Ù±‚bs1a'Ù±‚bs1fanglesÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`s                   Ù±‚bs1a'Ù±‚bs1gdegreesÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`a[Ù±‚bmic360Ù±‚`a,Ù±‚`a Ù±‚bmic180Ù±‚`a,Ù±‚`a Ù±‚bmic360Ù±‚`a]Ù±‚`a}Ù±‚`a,Ù±‚`a
Ù±‚`r                  Ù±‚`eindexÙ±‚aoa=Ù±‚`a[Ù±‚bs1a'Ù±‚bs1fcircleÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1htriangleÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1irectangleÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`bdfxk           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360hcompiledÙ¹‚Ù§xAAdd a scalar with operator version which return the same results.€Ù´ƒ…Ù±‚`bdfÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚bmia1xk           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361hcompiledÙ´ƒ†Ù±‚`bdfÙ±‚aoa.Ù±‚`caddÙ±‚`a(Ù±‚bmia1Ù±‚`a)xk           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361hcompiledÙ¹‚Ù§x(Divide by constant with reverse version.€Ù´ƒ†Ù±‚`bdfÙ±‚aoa.Ù±‚`cdivÙ±‚`a(Ù±‚bmib10Ù±‚`a)xk           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0hcompiledÙ´ƒ†Ù±‚`bdfÙ±‚aoa.Ù±‚`Ù¢„drdivÙ „fpandase1.4.1fmodulexpandas.core.roperator.rdivfmoduleõÙ±‚`a(Ù±‚bmib10Ù±‚`a)xw             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778hcompiledÙ¹‚Ù§x9Subtract a list and Series by axis with operator version.€Ù´ƒŠÙ±‚`bdfÙ±‚`a Ù±‚aoa-Ù±‚`a Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]xk           angles  degrees
circle         -1      358
triangle        2      178
rectangle       3      358hcompiledÙ´ƒ’Ù±‚`bdfÙ±‚aoa.Ù±‚`csubÙ±‚`a(Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1gcolumnsÙ±‚bs1a'Ù±‚`a)xk           angles  degrees
circle         -1      358
triangle        2      178
rectangle       3      358hcompiledÙ´ƒ˜.Ù±‚`bdfÙ±‚aoa.Ù±‚`csubÙ±‚`a(Ù±‚`bpdÙ±‚aoa.Ù±‚`Ù¢„fSeriesÙ „fpandase1.4.1fmodulexpandas.core.series.SeriesfmoduleõÙ±‚`a(Ù±‚`a[Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a]Ù±‚`a,Ù±‚`a Ù±‚`eindexÙ±‚aoa=Ù±‚`a[Ù±‚bs1a'Ù±‚bs1fcircleÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1htriangleÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1irectangleÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`g       Ù±‚`daxisÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1eindexÙ±‚bs1a'Ù±‚`a)xk           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359hcompiledÙ¹‚Ù§x>Multiply a DataFrame of different shape with operator version.€Ù´ƒ˜/Ù±‚`Ù¢„eotherÙ „fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmoduleõÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bpdÙ±‚aoa.Ù±‚`Ù¢„iDataFrameÙ „fpandase1.4.1fmodulexpandas.core.frame.DataFramefmoduleõÙ±‚`a(Ù±‚`a{Ù±‚bs1a'Ù±‚bs1fanglesÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a]Ù±‚`a}Ù±‚`a,Ù±‚`a
Ù±‚`u                     Ù±‚`eindexÙ±‚aoa=Ù±‚`a[Ù±‚bs1a'Ù±‚bs1fcircleÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1htriangleÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1irectangleÙ±‚bs1a'Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`Ù¢„eotherÙ „fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmoduleõxG           angles
circle          0
triangle        3
rectangle       4hcompiledÙ´ƒ…Ù±‚`bdfÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`Ù¢„eotherÙ „fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmoduleõxk           angles  degrees
circle          0      NaN
triangle        9      NaN
rectangle      16      NaNhcompiledÙ´ƒ‹Ù±‚`bdfÙ±‚aoa.Ù±‚`cmulÙ±‚`a(Ù±‚`Ù¢„eotherÙ „fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmoduleõÙ±‚`a,Ù±‚`a Ù±‚`jfill_valueÙ±‚aoa=Ù±‚bmia0Ù±‚`a)xk           angles  degrees
circle          0      0.0
triangle        9      0.0
rectangle      16      0.0hcompiledÙ¹‚Ù§x Divide by a MultiIndex by level.€Ù´ƒ˜…Ù±‚`ldf_multindexÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bpdÙ±‚aoa.Ù±‚`Ù¢„iDataFrameÙ „fpandase1.4.1fmodulexpandas.core.frame.DataFramefmoduleõÙ±‚`a(Ù±‚`a{Ù±‚bs1a'Ù±‚bs1fanglesÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`a[Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmia3Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmia4Ù±‚`a,Ù±‚`a Ù±‚bmia5Ù±‚`a,Ù±‚`a Ù±‚bmia6Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x                             Ù±‚bs1a'Ù±‚bs1gdegreesÙ±‚bs1a'Ù±‚`a:Ù±‚`a Ù±‚`a[Ù±‚bmic360Ù±‚`a,Ù±‚`a Ù±‚bmic180Ù±‚`a,Ù±‚`a Ù±‚bmic360Ù±‚`a,Ù±‚`a Ù±‚bmic360Ù±‚`a,Ù±‚`a Ù±‚bmic540Ù±‚`a,Ù±‚`a Ù±‚bmic720Ù±‚`a]Ù±‚`a}Ù±‚`a,Ù±‚`a
Ù±‚`x                            Ù±‚`eindexÙ±‚aoa=Ù±‚`a[Ù±‚`a[Ù±‚bs1a'Ù±‚bs1aAÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aAÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aAÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aBÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aBÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aBÙ±‚bs1a'Ù±‚`a]Ù±‚`a,Ù±‚`a
Ù±‚`x#                                   Ù±‚`a[Ù±‚bs1a'Ù±‚bs1fcircleÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1htriangleÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1irectangleÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`x$                                    Ù±‚bs1a'Ù±‚bs1fsquareÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1hpentagonÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1ghexagonÙ±‚bs1a'Ù±‚`a]Ù±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`ldf_multindexxÊ             angles  degrees
A circle          0      360
  triangle        3      180
  rectangle       4      360
B square          4      360
  pentagon        5      540
  hexagon         6      720hcompiledÙ´ƒÙ±‚`bdfÙ±‚aoa.Ù±‚`cdivÙ±‚`a(Ù±‚`ldf_multindexÙ±‚`a,Ù±‚`a Ù±‚`elevelÙ±‚aoa=Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚`jfill_valueÙ±‚aoa=Ù±‚bmia0Ù±‚`a)xÊ             angles  degrees
A circle        NaN      1.0
  triangle      1.0      1.0
  rectangle     1.0      1.0
B square        0.0      0.0
  pentagon      0.0      0.0
  hexagon       0.0      0.0hcompiledöˆÙ¼ƒÙ»ƒmDataFrame.addööÙ¹‚Ù§oAdd DataFrames.€öÙ¼ƒÙ»ƒmDataFrame.divööÙ¹‚Ù§x#Divide DataFrames (float division).€öÙ¼ƒÙ»ƒrDataFrame.floordivööÙ¹‚Ù§x%Divide DataFrames (integer division).€öÙ¼ƒÙ»ƒmDataFrame.modx pandas.core.frame.DataFrame.modeõÙ¹‚Ù§x,Calculate modulo (remainder after division).€öÙ¼ƒÙ»ƒmDataFrame.mulööÙ¹‚Ù§tMultiply DataFrames.€öÙ¼ƒÙ»ƒmDataFrame.powööÙ¹‚Ù§xCalculate exponential power.€öÙ¼ƒÙ»ƒmDataFrame.subööÙ¹‚Ù§tSubtract DataFrames.€öÙ¼ƒÙ»ƒqDataFrame.truedivööÙ¹‚Ù§x#Divide DataFrames (float division).€öe1.4.1Ù«x;f(self, other, axis='columns', level=None, fill_value=None)öx2pandas.core.ops.flex_arith_method_FRAME.<locals>.f€