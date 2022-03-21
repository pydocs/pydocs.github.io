ЩЇ‚ЃЩґѓРЩ±‚bsdx}"""
====================
Horizontal bar chart
====================

This example showcases a simple horizontal bar chart.
"""Щ±‚`a
Щ±‚bknfimportЩ±‚`a Щ±‚bnnЩў„jmatplotlibЩ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleхЩ±‚bnna.Щ±‚bnnfpyplotЩ±‚`a Щ±‚akbasЩ±‚`a Щ±‚bnncpltЩ±‚`a
Щ±‚bknfimportЩ±‚`a Щ±‚bnnЩў„enumpyЩ „enumpyf1.22.3fmoduleenumpyfmoduleхЩ±‚`a Щ±‚akbasЩ±‚`a Щ±‚bnnbnpЩ±‚`a
Щ±‚`a
Щ±‚bc1x)# Fixing random state for reproducibilityЩ±‚`a
Щ±‚`bnpЩ±‚aoa.Щ±‚`frandomЩ±‚aoa.Щ±‚`dseedЩ±‚`a(Щ±‚bmih19680801Щ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚`a
Щ±‚`cpltЩ±‚aoa.Щ±‚`jrcdefaultsЩ±‚`a(Щ±‚`a)Щ±‚`a
Щ±‚`cfigЩ±‚`a,Щ±‚`a Щ±‚`baxЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`cpltЩ±‚aoa.Щ±‚`hsubplotsЩ±‚`a(Щ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚bc1n# Example dataЩ±‚`a
Щ±‚`fpeopleЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`a(Щ±‚bs1a'Щ±‚bs1cTomЩ±‚bs1a'Щ±‚`a,Щ±‚`a Щ±‚bs1a'Щ±‚bs1dDickЩ±‚bs1a'Щ±‚`a,Щ±‚`a Щ±‚bs1a'Щ±‚bs1eHarryЩ±‚bs1a'Щ±‚`a,Щ±‚`a Щ±‚bs1a'Щ±‚bs1dSlimЩ±‚bs1a'Щ±‚`a,Щ±‚`a Щ±‚bs1a'Щ±‚bs1cJimЩ±‚bs1a'Щ±‚`a)Щ±‚`a
Щ±‚`ey_posЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`bnpЩ±‚aoa.Щ±‚`farangeЩ±‚`a(Щ±‚bnbclenЩ±‚`a(Щ±‚`fpeopleЩ±‚`a)Щ±‚`a)Щ±‚`a
Щ±‚`kperformanceЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚bmia3Щ±‚`a Щ±‚aoa+Щ±‚`a Щ±‚bmib10Щ±‚`a Щ±‚aoa*Щ±‚`a Щ±‚`bnpЩ±‚aoa.Щ±‚`frandomЩ±‚aoa.Щ±‚`drandЩ±‚`a(Щ±‚bnbclenЩ±‚`a(Щ±‚`fpeopleЩ±‚`a)Щ±‚`a)Щ±‚`a
Щ±‚`eerrorЩ±‚`a Щ±‚aoa=Щ±‚`a Щ±‚`bnpЩ±‚aoa.Щ±‚`frandomЩ±‚aoa.Щ±‚`drandЩ±‚`a(Щ±‚bnbclenЩ±‚`a(Щ±‚`fpeopleЩ±‚`a)Щ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚`baxЩ±‚aoa.Щ±‚`dbarhЩ±‚`a(Щ±‚`ey_posЩ±‚`a,Щ±‚`a Щ±‚`kperformanceЩ±‚`a,Щ±‚`a Щ±‚`dxerrЩ±‚aoa=Щ±‚`eerrorЩ±‚`a,Щ±‚`a Щ±‚`ealignЩ±‚aoa=Щ±‚bs1a'Щ±‚bs1fcenterЩ±‚bs1a'Щ±‚`a)Щ±‚`a
Щ±‚`baxЩ±‚aoa.Щ±‚`jset_yticksЩ±‚`a(Щ±‚`ey_posЩ±‚`a,Щ±‚`a Щ±‚`flabelsЩ±‚aoa=Щ±‚`fpeopleЩ±‚`a)Щ±‚`a
Щ±‚`baxЩ±‚aoa.Щ±‚`linvert_yaxisЩ±‚`a(Щ±‚`a)Щ±‚`b  Щ±‚bc1x# labels read top-to-bottomЩ±‚`a
Щ±‚`baxЩ±‚aoa.Щ±‚`jset_xlabelЩ±‚`a(Щ±‚bs1a'Щ±‚bs1kPerformanceЩ±‚bs1a'Щ±‚`a)Щ±‚`a
Щ±‚`baxЩ±‚aoa.Щ±‚`iset_titleЩ±‚`a(Щ±‚bs1a'Щ±‚bs1x!How fast do you want to go today?Щ±‚bs1a'Щ±‚`a)Щ±‚`a
Щ±‚`a
Щ±‚`cpltЩ±‚aoa.Щ±‚`dshowЩ±‚`a(Щ±‚`a)Щ±‚`a
`dNoneц