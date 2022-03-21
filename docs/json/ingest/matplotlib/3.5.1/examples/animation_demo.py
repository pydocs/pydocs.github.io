Ù¯‚Ù´ƒ˜Ù±‚bsdy†"""
================
pyplot animation
================

Generating an animation by calling `~.pyplot.pause` between plotting commands.

The method shown here is only suitable for simple, low-performance use.  For
more demanding applications, look at the :mod:`.animation` module and the
examples that use it.

Note that calling `time.sleep` instead of `~.pyplot.pause` would *not* work.
"""Ù±‚`a
Ù±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„jmatplotlibÙ „jmatplotlibe3.5.1fmodulejmatplotlibfmoduleõÙ±‚bnna.Ù±‚bnnfpyplotÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnncpltÙ±‚`a
Ù±‚bknfimportÙ±‚`a Ù±‚bnnÙ¢„enumpyÙ „enumpyf1.22.3fmoduleenumpyfmoduleõÙ±‚`a Ù±‚akbasÙ±‚`a Ù±‚bnnbnpÙ±‚`a
Ù±‚`a
Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`dseedÙ±‚`a(Ù±‚bmih19680801Ù±‚`a)Ù±‚`a
Ù±‚`ddataÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`bnpÙ±‚aoa.Ù±‚`frandomÙ±‚aoa.Ù±‚`frandomÙ±‚`a(Ù±‚`a(Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a,Ù±‚`a Ù±‚bmib50Ù±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚`cfigÙ±‚`a,Ù±‚`a Ù±‚`baxÙ±‚`a Ù±‚aoa=Ù±‚`a Ù±‚`cpltÙ±‚aoa.Ù±‚`hsubplotsÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`a
Ù±‚akcforÙ±‚`a Ù±‚`aiÙ±‚`a Ù±‚bowbinÙ±‚`a Ù±‚bnberangeÙ±‚`a(Ù±‚bnbclenÙ±‚`a(Ù±‚`ddataÙ±‚`a)Ù±‚`a)Ù±‚`a:Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`cclaÙ±‚`a(Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`fimshowÙ±‚`a(Ù±‚`ddataÙ±‚`a[Ù±‚`aiÙ±‚`a]Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚`baxÙ±‚aoa.Ù±‚`iset_titleÙ±‚`a(Ù±‚bs2a"Ù±‚bs2fframe Ù±‚bsib{}Ù±‚bs2a"Ù±‚aoa.Ù±‚`fformatÙ±‚`a(Ù±‚`aiÙ±‚`a)Ù±‚`a)Ù±‚`a
Ù±‚`d    Ù±‚bc1x2# Note that using time.sleep does *not* work here!Ù±‚`a
Ù±‚`d    Ù±‚`cpltÙ±‚aoa.Ù±‚`epauseÙ±‚`a(Ù±‚bmfc0.1Ù±‚`a)Ù±‚`a
`dNoneö