����jAttributes�����pExtended Summary�����������nEquivalent to ����qdataframe / other���xk, but with support to substitute a fill_value for missing data in one of the inputs. With reverse version, ���hrtruediv���fpandase1.4.1fmodulexpandas.core.roperator.rtruedivfmodule����a.��������xAmong flexible wrappers (���cadd�����b, ���csub�����b, ���cmul�����b, ���cdiv�����b, ���cmod�����b, ���cpow�����x) to arithmetic operators: ���a+�����b, ���a-�����b, ���a*�����b, ���a/�����b, ���b//�����b, ���a%�����b, ���b**�����a.��gMethods�����eNotes�����������x,Mismatched indices will be unioned together.��pOther Parameters�����jParameters�������eotherx&scalar, sequence, Series, or DataFrame��������xCAny single or multiple element data structure, or list-like object.����daxisx{0 or 'index', 1 or 'columns'}��������x|Whether to compare by the index (0 or 'index') or columns (1 or 'columns'). For Series input, axis to match Series index on.����elevellint or label��������xOBroadcast across a level, matching Index values on the passed MultiIndex level.����jfill_valuexfloat or None, default None��������x�Fill existing missing (NaN) values, and any new element needed for successful DataFrame alignment, with this value before computation. If data in both corresponding DataFrame locations is missing the result will be missing.��fRaises�����hReceives�����gReturns�������`iDataFrame��������x#Result of the arithmetic operation.��gSummary�����������xLGet Floating division of dataframe and other, element-wise (binary operator ���gtruediv�����b).��hWarnings�����eWarns�����fYields������gSummarypExtended SummaryjParametersgReturnshSee AlsoeNoteshExamplesx/pandas/core/ops/__init__.py�r<class 'function'>�tpandas.DataFrame.addupandas.DataFrame.raddtpandas.DataFrame.subtpandas.DataFrame.mulxpandas.DataFrame.truedivxpandas.DataFrame.floordivtpandas.DataFrame.modtpandas.DataFrame.powupandas.DataFrame.rmulupandas.DataFrame.rsubxpandas.DataFrame.rtruedivxpandas.DataFrame.rfloordivupandas.DataFrame.rpowupandas.DataFrame.rmodtpandas.DataFrame.divupandas.DataFrame.rdivxpandas.DataFrame.multiplyxpandas.DataFrame.subtractwpandas.DataFrame.divide��������@���`bdf���`a ���aoa=���`a ���`bpd���aoa.���`���iDataFrame���fpandase1.4.1fmodulexpandas.core.frame.DataFramefmodule����`a(���`a{���bs1a'���bs1fangles���bs1a'���`a:���`a ���`a[���bmia0���`a,���`a ���bmia3���`a,���`a ���bmia4���`a]���`a,���`a
���`s                   ���bs1a'���bs1gdegrees���bs1a'���`a:���`a ���`a[���bmic360���`a,���`a ���bmic180���`a,���`a ���bmic360���`a]���`a}���`a,���`a
���`r                  ���`eindex���aoa=���`a[���bs1a'���bs1fcircle���bs1a'���`a,���`a ���bs1a'���bs1htriangle���bs1a'���`a,���`a ���bs1a'���bs1irectangle���bs1a'���`a]���`a)���`a
���`bdfxk           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360hcompiled�������xAAdd a scalar with operator version which return the same results.��������`bdf���`a ���aoa+���`a ���bmia1xk           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361hcompiled�������`bdf���aoa.���`cadd���`a(���bmia1���`a)xk           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361hcompiled�������x(Divide by constant with reverse version.��������`bdf���aoa.���`cdiv���`a(���bmib10���`a)xk           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0hcompiled�������`bdf���aoa.���`���drdiv���fpandase1.4.1fmodulexpandas.core.roperator.rdivfmodule����`a(���bmib10���`a)xw             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778hcompiled�������x9Subtract a list and Series by axis with operator version.��������`bdf���`a ���aoa-���`a ���`a[���bmia1���`a,���`a ���bmia2���`a]xk           angles  degrees
circle         -1      358
triangle        2      178
rectangle       3      358hcompiled�������`bdf���aoa.���`csub���`a(���`a[���bmia1���`a,���`a ���bmia2���`a]���`a,���`a ���`daxis���aoa=���bs1a'���bs1gcolumns���bs1a'���`a)xk           angles  degrees
circle         -1      358
triangle        2      178
rectangle       3      358hcompiled����.���`bdf���aoa.���`csub���`a(���`bpd���aoa.���`���fSeries���fpandase1.4.1fmodulexpandas.core.series.Seriesfmodule����`a(���`a[���bmia1���`a,���`a ���bmia1���`a,���`a ���bmia1���`a]���`a,���`a ���`eindex���aoa=���`a[���bs1a'���bs1fcircle���bs1a'���`a,���`a ���bs1a'���bs1htriangle���bs1a'���`a,���`a ���bs1a'���bs1irectangle���bs1a'���`a]���`a)���`a,���`a
���`g       ���`daxis���aoa=���bs1a'���bs1eindex���bs1a'���`a)xk           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359hcompiled�������x>Multiply a DataFrame of different shape with operator version.�����/���`���eother���fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmodule����`a ���aoa=���`a ���`bpd���aoa.���`���iDataFrame���fpandase1.4.1fmodulexpandas.core.frame.DataFramefmodule����`a(���`a{���bs1a'���bs1fangles���bs1a'���`a:���`a ���`a[���bmia0���`a,���`a ���bmia3���`a,���`a ���bmia4���`a]���`a}���`a,���`a
���`u                     ���`eindex���aoa=���`a[���bs1a'���bs1fcircle���bs1a'���`a,���`a ���bs1a'���bs1htriangle���bs1a'���`a,���`a ���bs1a'���bs1irectangle���bs1a'���`a]���`a)���`a
���`���eother���fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmodule�xG           angles
circle          0
triangle        3
rectangle       4hcompiled�������`bdf���`a ���aoa*���`a ���`���eother���fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmodule�xk           angles  degrees
circle          0      NaN
triangle        9      NaN
rectangle      16      NaNhcompiled�������`bdf���aoa.���`cmul���`a(���`���eother���fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmodule����`a,���`a ���`jfill_value���aoa=���bmia0���`a)xk           angles  degrees
circle          0      0.0
triangle        9      0.0
rectangle      16      0.0hcompiled�������x Divide by a MultiIndex by level.���������`ldf_multindex���`a ���aoa=���`a ���`bpd���aoa.���`���iDataFrame���fpandase1.4.1fmodulexpandas.core.frame.DataFramefmodule����`a(���`a{���bs1a'���bs1fangles���bs1a'���`a:���`a ���`a[���bmia0���`a,���`a ���bmia3���`a,���`a ���bmia4���`a,���`a ���bmia4���`a,���`a ���bmia5���`a,���`a ���bmia6���`a]���`a,���`a
���`x                             ���bs1a'���bs1gdegrees���bs1a'���`a:���`a ���`a[���bmic360���`a,���`a ���bmic180���`a,���`a ���bmic360���`a,���`a ���bmic360���`a,���`a ���bmic540���`a,���`a ���bmic720���`a]���`a}���`a,���`a
���`x                            ���`eindex���aoa=���`a[���`a[���bs1a'���bs1aA���bs1a'���`a,���`a ���bs1a'���bs1aA���bs1a'���`a,���`a ���bs1a'���bs1aA���bs1a'���`a,���`a ���bs1a'���bs1aB���bs1a'���`a,���`a ���bs1a'���bs1aB���bs1a'���`a,���`a ���bs1a'���bs1aB���bs1a'���`a]���`a,���`a
���`x#                                   ���`a[���bs1a'���bs1fcircle���bs1a'���`a,���`a ���bs1a'���bs1htriangle���bs1a'���`a,���`a ���bs1a'���bs1irectangle���bs1a'���`a,���`a
���`x$                                    ���bs1a'���bs1fsquare���bs1a'���`a,���`a ���bs1a'���bs1hpentagon���bs1a'���`a,���`a ���bs1a'���bs1ghexagon���bs1a'���`a]���`a]���`a)���`a
���`ldf_multindexx�             angles  degrees
A circle          0      360
  triangle        3      180
  rectangle       4      360
B square          4      360
  pentagon        5      540
  hexagon         6      720hcompiled�������`bdf���aoa.���`cdiv���`a(���`ldf_multindex���`a,���`a ���`elevel���aoa=���bmia1���`a,���`a ���`jfill_value���aoa=���bmia0���`a)x�             angles  degrees
A circle        NaN      1.0
  triangle      1.0      1.0
  rectangle     1.0      1.0
B square        0.0      0.0
  pentagon      0.0      0.0
  hexagon       0.0      0.0hcompiled��������mDataFrame.add����������oAdd DataFrames.��������mDataFrame.div����������x#Divide DataFrames (float division).��������rDataFrame.floordiv����������x%Divide DataFrames (integer division).��������mDataFrame.modx pandas.core.frame.DataFrame.mode���������x,Calculate modulo (remainder after division).��������mDataFrame.mul����������tMultiply DataFrames.��������mDataFrame.pow����������xCalculate exponential power.��������mDataFrame.sub����������tSubtract DataFrames.��������qDataFrame.truediv����������x#Divide DataFrames (float division).��e1.4.1���x;f(self, other, axis='columns', level=None, fill_value=None)�x2pandas.core.ops.flex_arith_method_FRAME.<locals>.f�