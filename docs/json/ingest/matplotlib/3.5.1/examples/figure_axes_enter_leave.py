Ù¯‚Ù´ƒ™(Ù±‚bsdxØ"""
==================================
Figure/Axes enter and leave events
==================================

Illustrate the figure and Axes enter and leave events by changing the
frame colors on enter and leave.
"""Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfmon_enter_axesÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jenter_axesÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚aoa.Ù±‚`epatchÙ±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1fyellowÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`eeventÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfmon_leave_axesÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1jleave_axesÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`eeventÙ±‚aoa.Ù±‚`finaxesÙ±‚aoa.Ù±‚`epatchÙ±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1ewhiteÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`eeventÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfoon_enter_figureÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lenter_figureÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ffigureÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`eeventÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`epatchÙ±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1credÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`eeventÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akcdefÙ±‚`a Ù±‚bnfoon_leave_figureÙ±‚`a(Ù±‚`eeventÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bnbeprintÙ±‚`a(Ù±‚bs1a'Ù±‚bs1lleave_figureÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`eeventÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ffigureÙ±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`eeventÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ffigureÙ±‚aoa.Ù±‚`epatchÙ±‚aoa.Ù±‚`mset_facecolorÙ±‚`a(Ù±‚bs1a'Ù±‚bs1dgreyÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`eeventÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`ddrawÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`caxsÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia2Ù±‚`a,Ù±‚`a Ù±‚bmia1Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1x1mouse hover over figure or axes to trigger eventsÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1rfigure_enter_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`oon_enter_figureÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1rfigure_leave_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`oon_leave_figureÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1paxes_enter_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`mon_enter_axesÙ±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`fcanvasÙ±‚aoa.Ù±‚`kmpl_connectÙ±‚`a(Ù±‚bs1a'Ù±‚bs1paxes_leave_eventÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`mon_leave_axesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö