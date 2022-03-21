Ù¯‚Ù´ƒ™lÙ±‚bsdxÚ"""
===================
Precise text layout
===================

You can precisely layout text in data or axes coordinates.  This example shows
you some of the alignment and rotation specifications for text layout.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1x"# Build a rectangle in axes coordsÙ±‚`a
Ù±‚`dleftÙ±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc.25Ù±‚`a,Ù±‚`a Ù±‚bmfb.5Ù±‚`a
Ù±‚`fbottomÙ±‚`a,Ù±‚`a Ù±‚`fheightÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bmfc.25Ù±‚`a,Ù±‚`a Ù±‚bmfb.5Ù±‚`a
Ù±‚`erightÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dleftÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ewidthÙ±‚`a
Ù±‚`ctopÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`fbottomÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`fheightÙ±‚`a
Ù±‚`apÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`iRectangleÙ±‚`a(Ù±‚`a(Ù±‚`dleftÙ±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`ewidthÙ±‚`a,Ù±‚`a Ù±‚`fheightÙ±‚`a,Ù±‚`a Ù±‚`dfillÙ±‚aoa=Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`apÙ±‚aoa.Ù±‚`mset_transformÙ±‚`a(Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`apÙ±‚aoa.Ù±‚`kset_clip_onÙ±‚`a(Ù±‚bkceFalseÙ±‚`a)Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`iadd_patchÙ±‚`a(Ù±‚`apÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚`dleftÙ±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1hleft topÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`shorizontalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚`dleftÙ±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1kleft bottomÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`shorizontalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚`erightÙ±‚`a,Ù±‚`a Ù±‚`ctopÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1lright bottomÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`shorizontalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1erightÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fbottomÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚`erightÙ±‚`a,Ù±‚`a Ù±‚`ctopÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1iright topÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`shorizontalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1erightÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚`erightÙ±‚`a,Ù±‚`a Ù±‚`fbottomÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1jcenter topÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`shorizontalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1ctopÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚`dleftÙ±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`a(Ù±‚`fbottomÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ctopÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1lright centerÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`shorizontalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1erightÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`hrotationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hverticalÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚`dleftÙ±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`a(Ù±‚`fbottomÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ctopÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1kleft centerÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`shorizontalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1dleftÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`hrotationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hverticalÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`a(Ù±‚`dleftÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`erightÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`a(Ù±‚`fbottomÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ctopÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1fmiddleÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`shorizontalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚`erightÙ±‚`a,Ù±‚`a Ù±‚bmfc0.5Ù±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`a(Ù±‚`fbottomÙ±‚`a Ù±‚aoa+Ù±‚`a Ù±‚`ctopÙ±‚`a)Ù±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1hcenteredÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`shorizontalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`hrotationÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1hverticalÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`dtextÙ±‚`a(Ù±‚`dleftÙ±‚`a,Ù±‚`a Ù±‚`ctopÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1grotatedÙ±‚bseb\nÙ±‚bs1mwith newlinesÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`shorizontalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`qverticalalignmentÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1fcenterÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`hrotationÙ±‚aoa=Ù±‚bmib45Ù±‚`a,Ù±‚`a
Ù±‚`h        Ù±‚`itransformÙ±‚aoa=Ù±‚`baxÙ±‚aoa.Ù±‚`itransAxesÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`baxÙ±‚aoa.Ù±‚`lset_axis_offÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö