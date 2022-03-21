����jAttributes�����pExtended Summary�����������xAmong flexible wrappers (���beq�����b, ���bne�����b, ���ble�����b, ���blt�����b, ���bge�����b, ���bgt�����x) to comparison operators.��������nEquivalent to ���b==�����b, ���b!=�����b, ���b<=�����b, ���a<�����b, ���b>=�����b, ���a>�����xH with support to choose axis (rows or columns) and level for comparison.��gMethods�����eNotes�����������x-Mismatched indices will be unioned together. ���cNaN���fpandase1.4.1fmodulex pandas.errors.IntCastingNaNErrorfmodule����x' values are considered different (i.e. ���cNaN���fpandase1.4.1fmodulex pandas.errors.IntCastingNaNErrorfmodule����d != ���cNaN���fpandase1.4.1fmodulex pandas.errors.IntCastingNaNErrorfmodule����b).��pOther Parameters�����jParameters�������eotherx&scalar, sequence, Series, or DataFrame��������xCAny single or multiple element data structure, or list-like object.����daxisx1{0 or 'index', 1 or 'columns'}, default 'columns'��������xKWhether to compare by the index (0 or 'index') or columns (1 or 'columns').����elevellint or label��������xOBroadcast across a level, matching Index values on the passed MultiIndex level.��fRaises�����hReceives�����gReturns�������`qDataFrame of bool��������xResult of the comparison.��gSummary�����������xSGet Greater than or equal to of dataframe and other, element-wise (binary operator ���bge�����b).��hWarnings�����eWarns�����fYields������gSummarypExtended SummaryjParametersgReturnshSee AlsoeNoteshExamplesx/pandas/core/ops/__init__.py�r<class 'function'>�spandas.DataFrame.eqspandas.DataFrame.nespandas.DataFrame.ltspandas.DataFrame.gtspandas.DataFrame.lespandas.DataFrame.ge��������@���`bdf���`a ���aoa=���`a ���`bpd���aoa.���`���iDataFrame���fpandase1.4.1fmodulexpandas.core.frame.DataFramefmodule����`a(���`a{���bs1a'���bs1dcost���bs1a'���`a:���`a ���`a[���bmic250���`a,���`a ���bmic150���`a,���`a ���bmic100���`a]���`a,���`a
���`s                   ���bs1a'���bs1grevenue���bs1a'���`a:���`a ���`a[���bmic100���`a,���`a ���bmic250���`a,���`a ���bmic300���`a]���`a}���`a,���`a
���`r                  ���`eindex���aoa=���`a[���bs1a'���bs1aA���bs1a'���`a,���`a ���bs1a'���bs1aB���bs1a'���`a,���`a ���bs1a'���bs1aC���bs1a'���`a]���`a)���`a
���`bdfxC   cost  revenue
A   250      100
B   150      250
C   100      300hcompiled�������x>Comparison with a scalar, using either the operator or method:��������`bdf���`a ���aob==���`a ���bmic100xG    cost  revenue
A  False     True
B  False    False
C   True    Falsehcompiled�������`bdf���aoa.���`beq���`a(���bmic100���`a)xG    cost  revenue
A  False     True
B  False    False
C   True    Falsehcompiled�������eWhen ���eother�����elocaleotherelocal����f is a ���fSeries���fpandase1.4.1fmodulexpandas.core.series.Seriesfmodule����x;, the columns of a DataFrame are aligned with the index of ���eother�����elocaleotherelocal����o and broadcast:��������`bdf���`a ���aob!=���`a ���`bpd���aoa.���`���fSeries���fpandase1.4.1fmodulexpandas.core.series.Seriesfmodule����`a(���`a[���bmic100���`a,���`a ���bmic250���`a]���`a,���`a ���`eindex���aoa=���`a[���bs2a"���bs2dcost���bs2a"���`a,���`a ���bs2a"���bs2grevenue���bs2a"���`a]���`a)xG    cost  revenue
A   True     True
B   True    False
C  False     Truehcompiled�������x-Use the method to control the broadcast axis:�����%���`bdf���aoa.���`bne���`a(���`bpd���aoa.���`���fSeries���fpandase1.4.1fmodulexpandas.core.series.Seriesfmodule����`a(���`a[���bmic100���`a,���`a ���bmic300���`a]���`a,���`a ���`eindex���aoa=���`a[���bs2a"���bs2aA���bs2a"���`a,���`a ���bs2a"���bs2aD���bs2a"���`a]���`a)���`a,���`a ���`daxis���aoa=���bs1a'���bs1eindex���bs1a'���`a)xT   cost  revenue
A  True    False
B  True     True
C  True     True
D  True     Truehcompiled�������xaWhen comparing to an arbitrary sequence, the number of columns must match the number elements in ���eother�����elocaleotherelocal����a:��������`bdf���`a ���aob==���`a ���`a[���bmic250���`a,���`a ���bmic100���`a]xG    cost  revenue
A   True     True
B  False    False
C  False    Falsehcompiled�������x#Use the method to control the axis:��������`bdf���aoa.���`beq���`a(���`a[���bmic250���`a,���`a ���bmic250���`a,���`a ���bmic100���`a]���`a,���`a ���`daxis���aoa=���bs1a'���bs1eindex���bs1a'���`a)xG    cost  revenue
A   True    False
B  False     True
C   True    Falsehcompiled�������x*Compare to a DataFrame of different shape.�����7���`���eother���fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmodule����`a ���aoa=���`a ���`bpd���aoa.���`���iDataFrame���fpandase1.4.1fmodulexpandas.core.frame.DataFramefmodule����`a(���`a{���bs1a'���bs1grevenue���bs1a'���`a:���`a ���`a[���bmic300���`a,���`a ���bmic250���`a,���`a ���bmic100���`a,���`a ���bmic150���`a]���`a}���`a,���`a
���`u                     ���`eindex���aoa=���`a[���bs1a'���bs1aA���bs1a'���`a,���`a ���bs1a'���bs1aB���bs1a'���`a,���`a ���bs1a'���bs1aC���bs1a'���`a,���`a ���bs1a'���bs1aD���bs1a'���`a]���`a)���`a
���`���eother���fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmodule�x6   revenue
A      300
B      250
C      100
D      150hcompiled�������`bdf���aoa.���`bgt���`a(���`���eother���fpandase1.4.1fmodulex5pandas.io.formats.css.CSSResolver._update_other_unitsfmodule����`a)xY    cost  revenue
A  False    False
B  False    False
C  False     True
D  False    Falsehcompiled�������x!Compare to a MultiIndex by level.���������`ldf_multindex���`a ���aoa=���`a ���`bpd���aoa.���`���iDataFrame���fpandase1.4.1fmodulexpandas.core.frame.DataFramefmodule����`a(���`a{���bs1a'���bs1dcost���bs1a'���`a:���`a ���`a[���bmic250���`a,���`a ���bmic150���`a,���`a ���bmic100���`a,���`a ���bmic150���`a,���`a ���bmic300���`a,���`a ���bmic220���`a]���`a,���`a
���`x                             ���bs1a'���bs1grevenue���bs1a'���`a:���`a ���`a[���bmic100���`a,���`a ���bmic250���`a,���`a ���bmic300���`a,���`a ���bmic200���`a,���`a ���bmic175���`a,���`a ���bmic225���`a]���`a}���`a,���`a
���`x                            ���`eindex���aoa=���`a[���`a[���bs1a'���bs1bQ1���bs1a'���`a,���`a ���bs1a'���bs1bQ1���bs1a'���`a,���`a ���bs1a'���bs1bQ1���bs1a'���`a,���`a ���bs1a'���bs1bQ2���bs1a'���`a,���`a ���bs1a'���bs1bQ2���bs1a'���`a,���`a ���bs1a'���bs1bQ2���bs1a'���`a]���`a,���`a
���`x#                                   ���`a[���bs1a'���bs1aA���bs1a'���`a,���`a ���bs1a'���bs1aB���bs1a'���`a,���`a ���bs1a'���bs1aC���bs1a'���`a,���`a ���bs1a'���bs1aA���bs1a'���`a,���`a ���bs1a'���bs1aB���bs1a'���`a,���`a ���bs1a'���bs1aC���bs1a'���`a]���`a]���`a)���`a
���`ldf_multindexx�      cost  revenue
Q1 A   250      100
   B   150      250
   C   100      300
Q2 A   150      200
   B   300      175
   C   220      225hcompiled�������`bdf���aoa.���`ble���`a(���`ldf_multindex���`a,���`a ���`elevel���aoa=���bmia1���`a)x�       cost  revenue
Q1 A   True     True
   B   True     True
   C   True     True
Q2 A  False     True
   B   True    False
   C   True    Falsehcompiled��������lDataFrame.eq����������x,Compare DataFrames for equality elementwise.��������lDataFrame.ge����������xGCompare DataFrames for greater than inequality or equality elementwise.��������lDataFrame.gt����������xDCompare DataFrames for strictly greater than inequality elementwise.��������lDataFrame.le����������xDCompare DataFrames for less than inequality or equality elementwise.��������lDataFrame.lt����������xACompare DataFrames for strictly less than inequality elementwise.��������lDataFrame.ne����������x.Compare DataFrames for inequality elementwise.��e1.4.1���x*f(self, other, axis='columns', level=None)�x1pandas.core.ops.flex_comp_method_FRAME.<locals>.f�