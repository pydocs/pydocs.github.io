Ù¯‚Ù´ƒ™HÙ±‚bsdy1"""
==========
Evans test
==========

A mockup "Foo" units class which supports conversion and different tick
formatting depending on the "unit".  Here the "unit" is just a scalar
conversion factor, but this example shows that Matplotlib is entirely agnostic
to what kind of units client packages use.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnneunitsÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnneunitsÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnftickerÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnftickerÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnccFooÙ±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bfmh__init__Ù±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`cvalÙ±‚`a,Ù±‚`a Ù±‚`dunitÙ±‚aoa=Ù±‚bmfc1.0Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dunitÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`dunitÙ±‚`a
Ù±‚`h        Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_valÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cvalÙ±‚`a Ù±‚aoa*Ù±‚`a Ù±‚`dunitÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfevalueÙ±‚`a(Ù±‚bbpdselfÙ±‚`a,Ù±‚`a Ù±‚`dunitÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`dunitÙ±‚`a Ù±‚bowbisÙ±‚`a Ù±‚bkcdNoneÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚`dunitÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`dunitÙ±‚`a
Ù±‚`h        Ù±‚akfreturnÙ±‚`a Ù±‚bbpdselfÙ±‚aoa.Ù±‚`d_valÙ±‚`a Ù±‚aoa/Ù±‚`a Ù±‚`dunitÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚akeclassÙ±‚`a Ù±‚bnclFooConverterÙ±‚`a(Ù±‚`eunitsÙ±‚aoa.Ù±‚`sConversionInterfaceÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚bndm@staticmethodÙ±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfhaxisinfoÙ±‚`a(Ù±‚`dunitÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx"""Return the Foo AxisInfo."""Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`dunitÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmfc1.0Ù±‚`a Ù±‚bowborÙ±‚`a Ù±‚`dunitÙ±‚`a Ù±‚aob==Ù±‚`a Ù±‚bmfc2.0Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚`eunitsÙ±‚aoa.Ù±‚`hAxisInfoÙ±‚`a(Ù±‚`a
Ù±‚`p                Ù±‚`fmajlocÙ±‚aoa=Ù±‚`ftickerÙ±‚aoa.Ù±‚`lIndexLocatorÙ±‚`a(Ù±‚bmia8Ù±‚`a,Ù±‚`a Ù±‚bmia0Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`fmajfmtÙ±‚aoa=Ù±‚`ftickerÙ±‚aoa.Ù±‚`rFormatStrFormatterÙ±‚`a(Ù±‚bs2a"Ù±‚bs2eVAL: Ù±‚bsib%sÙ±‚bs2a"Ù±‚`a)Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`elabelÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1cfooÙ±‚bs1a'Ù±‚`a,Ù±‚`a
Ù±‚`p                Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚bkcdNoneÙ±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bndm@staticmethodÙ±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfgconvertÙ±‚`a(Ù±‚`cobjÙ±‚`a,Ù±‚`a Ù±‚`dunitÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdxs"""
        Convert *obj* using *unit*.

        If *obj* is a sequence, return the converted sequence.
        """Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hiterableÙ±‚`a(Ù±‚`cobjÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚`a[Ù±‚`aoÙ±‚aoa.Ù±‚`evalueÙ±‚`a(Ù±‚`dunitÙ±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`aoÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`cobjÙ±‚`a]Ù±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚`cobjÙ±‚aoa.Ù±‚`evalueÙ±‚`a(Ù±‚`dunitÙ±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`d    Ù±‚bndm@staticmethodÙ±‚`a
Ù±‚`d    Ù±‚akcdefÙ±‚`a Ù±‚bnfmdefault_unitsÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`daxisÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`h        Ù±‚bsdx."""Return the default unit for *x* or None."""Ù±‚`a
Ù±‚`h        Ù±‚akbifÙ±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`hiterableÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akcforÙ±‚`a Ù±‚`ethisxÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚`axÙ±‚`a:Ù±‚`a
Ù±‚`p                Ù±‚akfreturnÙ±‚`a Ù±‚`ethisxÙ±‚aoa.Ù±‚`dunitÙ±‚`a
Ù±‚`h        Ù±‚akdelseÙ±‚`a:Ù±‚`a
Ù±‚`l            Ù±‚akfreturnÙ±‚`a Ù±‚`axÙ±‚aoa.Ù±‚`dunitÙ±‚`a
Ù±‚`a
Ù±‚`a
Ù±‚`eunitsÙ±‚aoa.Ù±‚`hregistryÙ±‚`a[Ù±‚`cFooÙ±‚`a]Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`lFooConverterÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1r# create some FoosÙ±‚`a
Ù±‚`axÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`cFooÙ±‚`a(Ù±‚`cvalÙ±‚`a,Ù±‚`a Ù±‚bmfc1.0Ù±‚`a)Ù±‚`a Ù±‚akcforÙ±‚`a Ù±‚`cvalÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bmia0Ù±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚bc1x# and some arbitrary y dataÙ±‚`a
Ù±‚`ayÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`a[Ù±‚`aiÙ±‚`a Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`axÙ±‚`a)Ù±‚`a)Ù±‚`a]Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`a(Ù±‚`cax1Ù±‚`a,Ù±‚`a Ù±‚`cax2Ù±‚`a)Ù±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚bmia1Ù±‚`a,Ù±‚`a Ù±‚bmia2Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`hsuptitleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2lCustom unitsÙ±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`cfigÙ±‚aoa.Ù±‚`osubplots_adjustÙ±‚`a(Ù±‚`fbottomÙ±‚aoa=Ù±‚bmfc0.2Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1w# plot specifying unitsÙ±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a,Ù±‚`a Ù±‚bs1a'Ù±‚bs1aoÙ±‚bs1a'Ù±‚`a,Ù±‚`a Ù±‚`fxunitsÙ±‚aoa=Ù±‚bmfc2.0Ù±‚`a)Ù±‚`a
Ù±‚`cax2Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2lxunits = 2.0Ù±‚bs2a"Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dsetpÙ±‚`a(Ù±‚`cax2Ù±‚aoa.Ù±‚`oget_xticklabelsÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`hrotationÙ±‚aoa=Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚`bhaÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1erightÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚bc1xF# plot without specifying units; will use the None branch for axisinfoÙ±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`dplotÙ±‚`a(Ù±‚`axÙ±‚`a,Ù±‚`a Ù±‚`ayÙ±‚`a)Ù±‚`b  Ù±‚bc1t# uses default unitsÙ±‚`a
Ù±‚`cax1Ù±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs1a'Ù±‚bs1mdefault unitsÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dsetpÙ±‚`a(Ù±‚`cax1Ù±‚aoa.Ù±‚`oget_xticklabelsÙ±‚`a(Ù±‚`a)Ù±‚`a,Ù±‚`a Ù±‚`hrotationÙ±‚aoa=Ù±‚bmib30Ù±‚`a,Ù±‚`a Ù±‚`bhaÙ±‚aoa=Ù±‚bs1a'Ù±‚bs1erightÙ±‚bs1a'Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cpltÙ±‚aoa.Ù±‚`dshowÙ±‚`a(Ù±‚`a)Ù±‚`a
`dNoneö