��������A���bsdx,"""
===========
Basic Units
===========

"""���`a
���`a
���bknfimport���`a ���bnndmath���`a
���`a
���bknfimport���`a ���bnn���enumpy���enumpyf1.22.3fmoduleenumpyfmodule����`a ���akbas���`a ���bnnbnp���`a
���bkndfrom���`a ���bnnipackaging���bnna.���bnngversion���`a ���bknfimport���`a ���`eparse���`a ���akbas���`a ���`mparse_version���`a
���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnneunits���`a ���akbas���`a ���bnneunits���`a
���bknfimport���`a ���bnn���jmatplotlib���jmatplotlibe3.5.1fmodulejmatplotlibfmodule����bnna.���bnnfticker���`a ���akbas���`a ���bnnfticker���`a
���`a
���`a
���akeclass���`a ���bncmProxyDelegate���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`gfn_name���`a,���`a ���`jproxy_type���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`jproxy_type���`a ���aoa=���`a ���`jproxy_type���`a
���`h        ���bbpdself���aoa.���`gfn_name���`a ���aoa=���`a ���`gfn_name���`a
���`a
���`d    ���akcdef���`a ���bfmg__get__���`a(���bbpdself���`a,���`a ���`cobj���`a,���`a ���`gobjtype���aoa=���bkcdNone���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`jproxy_type���`a(���bbpdself���aoa.���`gfn_name���`a,���`a ���`cobj���`a)���`a
���`a
���`a
���akeclass���`a ���bncoTaggedValueMeta���`a(���bnbdtype���`a)���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`dname���`a,���`a ���`ebases���`a,���`a ���bnbddict���`a)���`a:���`a
���`h        ���akcfor���`a ���`gfn_name���`a ���bowbin���`a ���bbpdself���aoa.���`h_proxies���`a:���`a
���`l            ���akbif���`a ���bowcnot���`a ���bnbghasattr���`a(���bbpdself���`a,���`a ���`gfn_name���`a)���`a:���`a
���`p                ���bnbgsetattr���`a(���bbpdself���`a,���`a ���`gfn_name���`a,���`a
���`x                        ���`mProxyDelegate���`a(���`gfn_name���`a,���`a ���bbpdself���aoa.���`h_proxies���`a[���`gfn_name���`a]���`a)���`a)���`a
���`a
���`a
���akeclass���`a ���bncpPassThroughProxy���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`gfn_name���`a,���`a ���`cobj���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`gfn_name���`a ���aoa=���`a ���`gfn_name���`a
���`h        ���bbpdself���aoa.���`ftarget���`a ���aoa=���`a ���`cobj���aoa.���`lproxy_target���`a
���`a
���`d    ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���aoa*���`dargs���`a)���`a:���`a
���`h        ���`bfn���`a ���aoa=���`a ���bnbggetattr���`a(���bbpdself���aoa.���`ftarget���`a,���`a ���bbpdself���aoa.���`gfn_name���`a)���`a
���`h        ���`cret���`a ���aoa=���`a ���`bfn���`a(���aoa*���`dargs���`a)���`a
���`h        ���akfreturn���`a ���`cret���`a
���`a
���`a
���akeclass���`a ���bncpConvertArgsProxy���`a(���`pPassThroughProxy���`a)���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`gfn_name���`a,���`a ���`cobj���`a)���`a:���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���`gfn_name���`a,���`a ���`cobj���`a)���`a
���`h        ���bbpdself���aoa.���`dunit���`a ���aoa=���`a ���`cobj���aoa.���`dunit���`a
���`a
���`d    ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���aoa*���`dargs���`a)���`a:���`a
���`h        ���`nconverted_args���`a ���aoa=���`a ���`a[���`a]���`a
���`h        ���akcfor���`a ���`aa���`a ���bowbin���`a ���`dargs���`a:���`a
���`l            ���akctry���`a:���`a
���`p                ���`nconverted_args���aoa.���`fappend���`a(���`aa���aoa.���`jconvert_to���`a(���bbpdself���aoa.���`dunit���`a)���`a)���`a
���`l            ���akfexcept���`a ���bnenAttributeError���`a:���`a
���`p                ���`nconverted_args���aoa.���`fappend���`a(���`kTaggedValue���`a(���`aa���`a,���`a ���bbpdself���aoa.���`dunit���`a)���`a)���`a
���`h        ���`nconverted_args���`a ���aoa=���`a ���bnbetuple���`a(���`a[���`ac���aoa.���`iget_value���`a(���`a)���`a ���akcfor���`a ���`ac���`a ���bowbin���`a ���`nconverted_args���`a]���`a)���`a
���`h        ���akfreturn���`a ���bnbesuper���`a(���`a)���aoa.���bfmh__call__���`a(���aoa*���`nconverted_args���`a)���`a
���`a
���`a
���akeclass���`a ���bncrConvertReturnProxy���`a(���`pPassThroughProxy���`a)���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`gfn_name���`a,���`a ���`cobj���`a)���`a:���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���`gfn_name���`a,���`a ���`cobj���`a)���`a
���`h        ���bbpdself���aoa.���`dunit���`a ���aoa=���`a ���`cobj���aoa.���`dunit���`a
���`a
���`d    ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���aoa*���`dargs���`a)���`a:���`a
���`h        ���`cret���`a ���aoa=���`a ���bnbesuper���`a(���`a)���aoa.���bfmh__call__���`a(���aoa*���`dargs���`a)���`a
���`h        ���akfreturn���`a ���`a(���bbpnNotImplemented���`a ���akbif���`a ���`cret���`a ���bowbis���`a ���bbpnNotImplemented���`a
���`p                ���akdelse���`a ���`kTaggedValue���`a(���`cret���`a,���`a ���bbpdself���aoa.���`dunit���`a)���`a)���`a
���`a
���`a
���akeclass���`a ���bncoConvertAllProxy���`a(���`pPassThroughProxy���`a)���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`gfn_name���`a,���`a ���`cobj���`a)���`a:���`a
���`h        ���bnbesuper���`a(���`a)���aoa.���bfmh__init__���`a(���`gfn_name���`a,���`a ���`cobj���`a)���`a
���`h        ���bbpdself���aoa.���`dunit���`a ���aoa=���`a ���`cobj���aoa.���`dunit���`a
���`a
���`d    ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���aoa*���`dargs���`a)���`a:���`a
���`h        ���`nconverted_args���`a ���aoa=���`a ���`a[���`a]���`a
���`h        ���`iarg_units���`a ���aoa=���`a ���`a[���bbpdself���aoa.���`dunit���`a]���`a
���`h        ���akcfor���`a ���`aa���`a ���bowbin���`a ���`dargs���`a:���`a
���`l            ���akbif���`a ���bnbghasattr���`a(���`aa���`a,���`a ���bs1a'���bs1hget_unit���bs1a'���`a)���`a ���bowcand���`a ���bowcnot���`a ���bnbghasattr���`a(���`aa���`a,���`a ���bs1a'���bs1jconvert_to���bs1a'���`a)���`a:���`a
���`p                ���bc1x=# If this argument has a unit type but no conversion ability,���`a
���`p                ���bc1x# this operation is prohibited.���`a
���`p                ���akfreturn���`a ���bbpnNotImplemented���`a
���`a
���`l            ���akbif���`a ���bnbghasattr���`a(���`aa���`a,���`a ���bs1a'���bs1jconvert_to���bs1a'���`a)���`a:���`a
���`p                ���akctry���`a:���`a
���`t                    ���`aa���`a ���aoa=���`a ���`aa���aoa.���`jconvert_to���`a(���bbpdself���aoa.���`dunit���`a)���`a
���`p                ���akfexcept���`a ���bneiException���`a:���`a
���`t                    ���akdpass���`a
���`p                ���`iarg_units���aoa.���`fappend���`a(���`aa���aoa.���`hget_unit���`a(���`a)���`a)���`a
���`p                ���`nconverted_args���aoa.���`fappend���`a(���`aa���aoa.���`iget_value���`a(���`a)���`a)���`a
���`l            ���akdelse���`a:���`a
���`p                ���`nconverted_args���aoa.���`fappend���`a(���`aa���`a)���`a
���`p                ���akbif���`a ���bnbghasattr���`a(���`aa���`a,���`a ���bs1a'���bs1hget_unit���bs1a'���`a)���`a:���`a
���`t                    ���`iarg_units���aoa.���`fappend���`a(���`aa���aoa.���`hget_unit���`a(���`a)���`a)���`a
���`p                ���akdelse���`a:���`a
���`t                    ���`iarg_units���aoa.���`fappend���`a(���bkcdNone���`a)���`a
���`h        ���`nconverted_args���`a ���aoa=���`a ���bnbetuple���`a(���`nconverted_args���`a)���`a
���`h        ���`cret���`a ���aoa=���`a ���bnbesuper���`a(���`a)���aoa.���bfmh__call__���`a(���aoa*���`nconverted_args���`a)���`a
���`h        ���akbif���`a ���`cret���`a ���bowbis���`a ���bbpnNotImplemented���`a:���`a
���`l            ���akfreturn���`a ���bbpnNotImplemented���`a
���`h        ���`hret_unit���`a ���aoa=���`a ���`munit_resolver���`a(���bbpdself���aoa.���`gfn_name���`a,���`a ���`iarg_units���`a)���`a
���`h        ���akbif���`a ���`hret_unit���`a ���bowbis���`a ���bbpnNotImplemented���`a:���`a
���`l            ���akfreturn���`a ���bbpnNotImplemented���`a
���`h        ���akfreturn���`a ���`kTaggedValue���`a(���`cret���`a,���`a ���`hret_unit���`a)���`a
���`a
���`a
���akeclass���`a ���bnckTaggedValue���`a(���`imetaclass���aoa=���`oTaggedValueMeta���`a)���`a:���`a
���`a
���`d    ���`h_proxies���`a ���aoa=���`a ���`a{���bs1a'���bs1g__add__���bs1a'���`a:���`a ���`oConvertAllProxy���`a,���`a
���`p                ���bs1a'���bs1g__sub__���bs1a'���`a:���`a ���`oConvertAllProxy���`a,���`a
���`p                ���bs1a'���bs1g__mul__���bs1a'���`a:���`a ���`oConvertAllProxy���`a,���`a
���`p                ���bs1a'���bs1h__rmul__���bs1a'���`a:���`a ���`oConvertAllProxy���`a,���`a
���`p                ���bs1a'���bs1g__cmp__���bs1a'���`a:���`a ���`oConvertAllProxy���`a,���`a
���`p                ���bs1a'���bs1f__lt__���bs1a'���`a:���`a ���`oConvertAllProxy���`a,���`a
���`p                ���bs1a'���bs1f__gt__���bs1a'���`a:���`a ���`oConvertAllProxy���`a,���`a
���`p                ���bs1a'���bs1g__len__���bs1a'���`a:���`a ���`pPassThroughProxy���`a}���`a
���`a
���`d    ���akcdef���`a ���bfmg__new__���`a(���bbpccls���`a,���`a ���`evalue���`a,���`a ���`dunit���`a)���`a:���`a
���`h        ���bc1x## generate a new subclass for value���`a
���`h        ���`kvalue_class���`a ���aoa=���`a ���bnbdtype���`a(���`evalue���`a)���`a
���`h        ���akctry���`a:���`a
���`l            ���`fsubcls���`a ���aoa=���`a ���bnbdtype���`a(���bsaaf���bs1a'���bs1oTaggedValue_of_���bsia{���`kvalue_class���aoa.���bvmh__name__���bsia}���bs1a'���`a,���`a
���`x                          ���`a(���bbpccls���`a,���`a ���`kvalue_class���`a)���`a,���`a ���`a{���`a}���`a)���`a
���`l            ���akfreturn���`a ���bnbfobject���aoa.���bfmg__new__���`a(���`fsubcls���`a)���`a
���`h        ���akfexcept���`a ���bneiTypeError���`a:���`a
���`l            ���akfreturn���`a ���bnbfobject���aoa.���bfmg__new__���`a(���bbpccls���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`evalue���`a,���`a ���`dunit���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`evalue���`a ���aoa=���`a ���`evalue���`a
���`h        ���bbpdself���aoa.���`dunit���`a ���aoa=���`a ���`dunit���`a
���`h        ���bbpdself���aoa.���`lproxy_target���`a ���aoa=���`a ���bbpdself���aoa.���`evalue���`a
���`a
���`d    ���akcdef���`a ���bfmp__getattribute__���`a(���bbpdself���`a,���`a ���`dname���`a)���`a:���`a
���`h        ���akbif���`a ���`dname���aoa.���`jstartswith���`a(���bs1a'���bs1b__���bs1a'���`a)���`a:���`a
���`l            ���akfreturn���`a ���bnbfobject���aoa.���bfmp__getattribute__���`a(���bbpdself���`a,���`a ���`dname���`a)���`a
���`h        ���`hvariable���`a ���aoa=���`a ���bnbfobject���aoa.���bfmp__getattribute__���`a(���bbpdself���`a,���`a ���bs1a'���bs1evalue���bs1a'���`a)���`a
���`h        ���akbif���`a ���bnbghasattr���`a(���`hvariable���`a,���`a ���`dname���`a)���`a ���bowcand���`a ���`dname���`a ���bowcnot���`a ���bowbin���`a ���bbpdself���aoa.���bvmi__class__���aoa.���bvmh__dict__���`a:���`a
���`l            ���akfreturn���`a ���bnbggetattr���`a(���`hvariable���`a,���`a ���`dname���`a)���`a
���`h        ���akfreturn���`a ���bnbfobject���aoa.���bfmp__getattribute__���`a(���bbpdself���`a,���`a ���`dname���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfi__array__���`a(���bbpdself���`a,���`a ���`edtype���aoa=���bnbfobject���`a)���`a:���`a
���`h        ���akfreturn���`a ���`bnp���aoa.���`gasarray���`a(���bbpdself���aoa.���`evalue���`a)���aoa.���`fastype���`a(���`edtype���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfn__array_wrap__���`a(���bbpdself���`a,���`a ���`earray���`a,���`a ���`gcontext���`a)���`a:���`a
���`h        ���akfreturn���`a ���`kTaggedValue���`a(���`earray���`a,���`a ���bbpdself���aoa.���`dunit���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmh__repr__���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���bs1a'���bs1lTaggedValue(���bsid{!r}���bs1b, ���bsid{!r}���bs1a)���bs1a'���aoa.���`fformat���`a(���bbpdself���aoa.���`evalue���`a,���`a ���bbpdself���aoa.���`dunit���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmg__str__���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���bnbcstr���`a(���bbpdself���aoa.���`evalue���`a)���`a ���aoa+���`a ���bs1a'���bs1d in ���bs1a'���`a ���aoa+���`a ���bnbcstr���`a(���bbpdself���aoa.���`dunit���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmg__len__���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���bnbclen���`a(���bbpdself���aoa.���`evalue���`a)���`a
���`a
���`d    ���akbif���`a ���`mparse_version���`a(���`bnp���aoa.���`k__version__���`a)���`a ���aoa>���aoa=���`a ���`mparse_version���`a(���bs1a'���bs1d1.20���bs1a'���`a)���`a:���`a
���`h        ���akcdef���`a ���bfmk__getitem__���`a(���bbpdself���`a,���`a ���`ckey���`a)���`a:���`a
���`l            ���akfreturn���`a ���`kTaggedValue���`a(���bbpdself���aoa.���`evalue���`a[���`ckey���`a]���`a,���`a ���bbpdself���aoa.���`dunit���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmh__iter__���`a(���bbpdself���`a)���`a:���`a
���`h        ���bc1x@# Return a generator expression rather than use `yield`, so that���`a
���`h        ���bc1xD# TypeError is raised by iter(self) if appropriate when checking for���`a
���`h        ���bc1n# iterability.���`a
���`h        ���akfreturn���`a ���`a(���`kTaggedValue���`a(���`einner���`a,���`a ���bbpdself���aoa.���`dunit���`a)���`a ���akcfor���`a ���`einner���`a ���bowbin���`a ���bbpdself���aoa.���`evalue���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfsget_compressed_copy���`a(���bbpdself���`a,���`a ���`dmask���`a)���`a:���`a
���`h        ���`inew_value���`a ���aoa=���`a ���`bnp���aoa.���`bma���aoa.���`lmasked_array���`a(���bbpdself���aoa.���`evalue���`a,���`a ���`dmask���aoa=���`dmask���`a)���aoa.���`jcompressed���`a(���`a)���`a
���`h        ���akfreturn���`a ���`kTaggedValue���`a(���`inew_value���`a,���`a ���bbpdself���aoa.���`dunit���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfjconvert_to���`a(���bbpdself���`a,���`a ���`dunit���`a)���`a:���`a
���`h        ���akbif���`a ���`dunit���`a ���aob==���`a ���bbpdself���aoa.���`dunit���`a ���bowbor���`a ���bowcnot���`a ���`dunit���`a:���`a
���`l            ���akfreturn���`a ���bbpdself���`a
���`h        ���akctry���`a:���`a
���`l            ���`inew_value���`a ���aoa=���`a ���bbpdself���aoa.���`dunit���aoa.���`pconvert_value_to���`a(���bbpdself���aoa.���`evalue���`a,���`a ���`dunit���`a)���`a
���`h        ���akfexcept���`a ���bnenAttributeError���`a:���`a
���`l            ���`inew_value���`a ���aoa=���`a ���bbpdself���`a
���`h        ���akfreturn���`a ���`kTaggedValue���`a(���`inew_value���`a,���`a ���`dunit���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfiget_value���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`evalue���`a
���`a
���`d    ���akcdef���`a ���bnfhget_unit���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`dunit���`a
���`a
���`a
���akeclass���`a ���bnciBasicUnit���`a:���`a
���`d    ���akcdef���`a ���bfmh__init__���`a(���bbpdself���`a,���`a ���`dname���`a,���`a ���`hfullname���aoa=���bkcdNone���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`dname���`a ���aoa=���`a ���`dname���`a
���`h        ���akbif���`a ���`hfullname���`a ���bowbis���`a ���bkcdNone���`a:���`a
���`l            ���`hfullname���`a ���aoa=���`a ���`dname���`a
���`h        ���bbpdself���aoa.���`hfullname���`a ���aoa=���`a ���`hfullname���`a
���`h        ���bbpdself���aoa.���`kconversions���`a ���aoa=���`a ���bnbddict���`a(���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmh__repr__���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���bsaaf���bs1a'���bs1jBasicUnit(���bsia{���bbpdself���aoa.���`dname���bsia}���bs1a)���bs1a'���`a
���`a
���`d    ���akcdef���`a ���bfmg__str__���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`hfullname���`a
���`a
���`d    ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���`evalue���`a)���`a:���`a
���`h        ���akfreturn���`a ���`kTaggedValue���`a(���`evalue���`a,���`a ���bbpdself���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmg__mul__���`a(���bbpdself���`a,���`a ���`crhs���`a)���`a:���`a
���`h        ���`evalue���`a ���aoa=���`a ���`crhs���`a
���`h        ���`dunit���`a ���aoa=���`a ���bbpdself���`a
���`h        ���akbif���`a ���bnbghasattr���`a(���`crhs���`a,���`a ���bs1a'���bs1hget_unit���bs1a'���`a)���`a:���`a
���`l            ���`evalue���`a ���aoa=���`a ���`crhs���aoa.���`iget_value���`a(���`a)���`a
���`l            ���`dunit���`a ���aoa=���`a ���`crhs���aoa.���`hget_unit���`a(���`a)���`a
���`l            ���`dunit���`a ���aoa=���`a ���`munit_resolver���`a(���bs1a'���bs1g__mul__���bs1a'���`a,���`a ���`a(���bbpdself���`a,���`a ���`dunit���`a)���`a)���`a
���`h        ���akbif���`a ���`dunit���`a ���bowbis���`a ���bbpnNotImplemented���`a:���`a
���`l            ���akfreturn���`a ���bbpnNotImplemented���`a
���`h        ���akfreturn���`a ���`kTaggedValue���`a(���`evalue���`a,���`a ���`dunit���`a)���`a
���`a
���`d    ���akcdef���`a ���bfmh__rmul__���`a(���bbpdself���`a,���`a ���`clhs���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa*���`clhs���`a
���`a
���`d    ���akcdef���`a ���bnfn__array_wrap__���`a(���bbpdself���`a,���`a ���`earray���`a,���`a ���`gcontext���`a)���`a:���`a
���`h        ���akfreturn���`a ���`kTaggedValue���`a(���`earray���`a,���`a ���bbpdself���`a)���`a
���`a
���`d    ���akcdef���`a ���bnfi__array__���`a(���bbpdself���`a,���`a ���`at���aoa=���bkcdNone���`a,���`a ���`gcontext���aoa=���bkcdNone���`a)���`a:���`a
���`h        ���`cret���`a ���aoa=���`a ���`bnp���aoa.���`earray���`a(���bmia1���`a)���`a
���`h        ���akbif���`a ���`at���`a ���bowbis���`a ���bowcnot���`a ���bkcdNone���`a:���`a
���`l            ���akfreturn���`a ���`cret���aoa.���`fastype���`a(���`at���`a)���`a
���`h        ���akdelse���`a:���`a
���`l            ���akfreturn���`a ���`cret���`a
���`a
���`d    ���akcdef���`a ���bnfuadd_conversion_factor���`a(���bbpdself���`a,���`a ���`dunit���`a,���`a ���`ffactor���`a)���`a:���`a
���`h        ���akcdef���`a ���bnfgconvert���`a(���`ax���`a)���`a:���`a
���`l            ���akfreturn���`a ���`ax���aoa*���`ffactor���`a
���`h        ���bbpdself���aoa.���`kconversions���`a[���`dunit���`a]���`a ���aoa=���`a ���`gconvert���`a
���`a
���`d    ���akcdef���`a ���bnfqadd_conversion_fn���`a(���bbpdself���`a,���`a ���`dunit���`a,���`a ���`bfn���`a)���`a:���`a
���`h        ���bbpdself���aoa.���`kconversions���`a[���`dunit���`a]���`a ���aoa=���`a ���`bfn���`a
���`a
���`d    ���akcdef���`a ���bnfqget_conversion_fn���`a(���bbpdself���`a,���`a ���`dunit���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`kconversions���`a[���`dunit���`a]���`a
���`a
���`d    ���akcdef���`a ���bnfpconvert_value_to���`a(���bbpdself���`a,���`a ���`evalue���`a,���`a ���`dunit���`a)���`a:���`a
���`h        ���`mconversion_fn���`a ���aoa=���`a ���bbpdself���aoa.���`kconversions���`a[���`dunit���`a]���`a
���`h        ���`cret���`a ���aoa=���`a ���`mconversion_fn���`a(���`evalue���`a)���`a
���`h        ���akfreturn���`a ���`cret���`a
���`a
���`d    ���akcdef���`a ���bnfhget_unit���`a(���bbpdself���`a)���`a:���`a
���`h        ���akfreturn���`a ���bbpdself���`a
���`a
���`a
���akeclass���`a ���bnclUnitResolver���`a:���`a
���`d    ���akcdef���`a ���bnfmaddition_rule���`a(���bbpdself���`a,���`a ���`eunits���`a)���`a:���`a
���`h        ���akcfor���`a ���`funit_1���`a,���`a ���`funit_2���`a ���bowbin���`a ���bnbczip���`a(���`eunits���`a[���`a:���aoa-���bmia1���`a]���`a,���`a ���`eunits���`a[���bmia1���`a:���`a]���`a)���`a:���`a
���`l            ���akbif���`a ���`funit_1���`a ���aob!=���`a ���`funit_2���`a:���`a
���`p                ���akfreturn���`a ���bbpnNotImplemented���`a
���`h        ���akfreturn���`a ���`eunits���`a[���bmia0���`a]���`a
���`a
���`d    ���akcdef���`a ���bnfsmultiplication_rule���`a(���bbpdself���`a,���`a ���`eunits���`a)���`a:���`a
���`h        ���`hnon_null���`a ���aoa=���`a ���`a[���`au���`a ���akcfor���`a ���`au���`a ���bowbin���`a ���`eunits���`a ���akbif���`a ���`au���`a]���`a
���`h        ���akbif���`a ���bnbclen���`a(���`hnon_null���`a)���`a ���aoa>���`a ���bmia1���`a:���`a
���`l            ���akfreturn���`a ���bbpnNotImplemented���`a
���`h        ���akfreturn���`a ���`hnon_null���`a[���bmia0���`a]���`a
���`a
���`d    ���`gop_dict���`a ���aoa=���`a ���`a{���`a
���`h        ���bs1a'���bs1g__mul__���bs1a'���`a:���`a ���`smultiplication_rule���`a,���`a
���`h        ���bs1a'���bs1h__rmul__���bs1a'���`a:���`a ���`smultiplication_rule���`a,���`a
���`h        ���bs1a'���bs1g__add__���bs1a'���`a:���`a ���`maddition_rule���`a,���`a
���`h        ���bs1a'���bs1h__radd__���bs1a'���`a:���`a ���`maddition_rule���`a,���`a
���`h        ���bs1a'���bs1g__sub__���bs1a'���`a:���`a ���`maddition_rule���`a,���`a
���`h        ���bs1a'���bs1h__rsub__���bs1a'���`a:���`a ���`maddition_rule���`a}���`a
���`a
���`d    ���akcdef���`a ���bfmh__call__���`a(���bbpdself���`a,���`a ���`ioperation���`a,���`a ���`eunits���`a)���`a:���`a
���`h        ���akbif���`a ���`ioperation���`a ���bowcnot���`a ���bowbin���`a ���bbpdself���aoa.���`gop_dict���`a:���`a
���`l            ���akfreturn���`a ���bbpnNotImplemented���`a
���`a
���`h        ���akfreturn���`a ���bbpdself���aoa.���`gop_dict���`a[���`ioperation���`a]���`a(���bbpdself���`a,���`a ���`eunits���`a)���`a
���`a
���`a
���`munit_resolver���`a ���aoa=���`a ���`lUnitResolver���`a(���`a)���`a
���`a
���`bcm���`a ���aoa=���`a ���`iBasicUnit���`a(���bs1a'���bs1bcm���bs1a'���`a,���`a ���bs1a'���bs1kcentimeters���bs1a'���`a)���`a
���`dinch���`a ���aoa=���`a ���`iBasicUnit���`a(���bs1a'���bs1dinch���bs1a'���`a,���`a ���bs1a'���bs1finches���bs1a'���`a)���`a
���`dinch���aoa.���`uadd_conversion_factor���`a(���`bcm���`a,���`a ���bmfd2.54���`a)���`a
���`bcm���aoa.���`uadd_conversion_factor���`a(���`dinch���`a,���`a ���bmia1���aoa/���bmfd2.54���`a)���`a
���`a
���`gradians���`a ���aoa=���`a ���`iBasicUnit���`a(���bs1a'���bs1crad���bs1a'���`a,���`a ���bs1a'���bs1gradians���bs1a'���`a)���`a
���`gdegrees���`a ���aoa=���`a ���`iBasicUnit���`a(���bs1a'���bs1cdeg���bs1a'���`a,���`a ���bs1a'���bs1gdegrees���bs1a'���`a)���`a
���`gradians���aoa.���`uadd_conversion_factor���`a(���`gdegrees���`a,���`a ���bmfe180.0���aoa/���`bnp���aoa.���`bpi���`a)���`a
���`gdegrees���aoa.���`uadd_conversion_factor���`a(���`gradians���`a,���`a ���`bnp���aoa.���`bpi���aoa/���bmfe180.0���`a)���`a
���`a
���`dsecs���`a ���aoa=���`a ���`iBasicUnit���`a(���bs1a'���bs1as���bs1a'���`a,���`a ���bs1a'���bs1gseconds���bs1a'���`a)���`a
���`ehertz���`a ���aoa=���`a ���`iBasicUnit���`a(���bs1a'���bs1bHz���bs1a'���`a,���`a ���bs1a'���bs1eHertz���bs1a'���`a)���`a
���`gminutes���`a ���aoa=���`a ���`iBasicUnit���`a(���bs1a'���bs1cmin���bs1a'���`a,���`a ���bs1a'���bs1gminutes���bs1a'���`a)���`a
���`a
���`dsecs���aoa.���`qadd_conversion_fn���`a(���`ehertz���`a,���`a ���akflambda���`a ���`ax���`a:���`a ���bmfb1.���aoa/���`ax���`a)���`a
���`dsecs���aoa.���`uadd_conversion_factor���`a(���`gminutes���`a,���`a ���bmia1���aoa/���bmfd60.0���`a)���`a
���`a
���`a
���bc1t# radians formatting���`a
���akcdef���`a ���bnffrad_fn���`a(���`ax���`a,���`a ���`cpos���aoa=���bkcdNone���`a)���`a:���`a
���`d    ���akbif���`a ���`ax���`a ���aoa>���aoa=���`a ���bmia0���`a:���`a
���`h        ���`an���`a ���aoa=���`a ���bnbcint���`a(���`a(���`ax���`a ���aoa/���`a ���`bnp���aoa.���`bpi���`a)���`a ���aoa*���`a ���bmfc2.0���`a ���aoa+���`a ���bmfd0.25���`a)���`a
���`d    ���akdelse���`a:���`a
���`h        ���`an���`a ���aoa=���`a ���bnbcint���`a(���`a(���`ax���`a ���aoa/���`a ���`bnp���aoa.���`bpi���`a)���`a ���aoa*���`a ���bmfc2.0���`a ���aoa-���`a ���bmfd0.25���`a)���`a
���`a
���`d    ���akbif���`a ���`an���`a ���aob==���`a ���bmia0���`a:���`a
���`h        ���akfreturn���`a ���bs1a'���bs1a0���bs1a'���`a
���`d    ���akdelif���`a ���`an���`a ���aob==���`a ���bmia1���`a:���`a
���`h        ���akfreturn���`a ���bsaar���bs1a'���bs1a$���bs1a\���bs1epi/2$���bs1a'���`a
���`d    ���akdelif���`a ���`an���`a ���aob==���`a ���bmia2���`a:���`a
���`h        ���akfreturn���`a ���bsaar���bs1a'���bs1a$���bs1a\���bs1cpi$���bs1a'���`a
���`d    ���akdelif���`a ���`an���`a ���aob==���`a ���aoa-���bmia1���`a:���`a
���`h        ���akfreturn���`a ���bsaar���bs1a'���bs1b$-���bs1a\���bs1epi/2$���bs1a'���`a
���`d    ���akdelif���`a ���`an���`a ���aob==���`a ���aoa-���bmia2���`a:���`a
���`h        ���akfreturn���`a ���bsaar���bs1a'���bs1b$-���bs1a\���bs1cpi$���bs1a'���`a
���`d    ���akdelif���`a ���`an���`a ���aoa%���`a ���bmia2���`a ���aob==���`a ���bmia0���`a:���`a
���`h        ���akfreturn���`a ���bsabfr���bs1a'���bs1a$���bsia{���`an���aoa/���aoa/���bmia2���bsia}���bs1a\���bs1cpi$���bs1a'���`a
���`d    ���akdelse���`a:���`a
���`h        ���akfreturn���`a ���bsabfr���bs1a'���bs1a$���bsia{���`an���bsia}���bs1a\���bs1epi/2$���bs1a'���`a
���`a
���`a
���akeclass���`a ���bncrBasicUnitConverter���`a(���`eunits���aoa.���`sConversionInterface���`a)���`a:���`a
���`d    ���bndm@staticmethod���`a
���`d    ���akcdef���`a ���bnfhaxisinfo���`a(���`dunit���`a,���`a ���`daxis���`a)���`a:���`a
���`h        ���bsdx."""Return AxisInfo instance for x and unit."""���`a
���`a
���`h        ���akbif���`a ���`dunit���`a ���aob==���`a ���`gradians���`a:���`a
���`l            ���akfreturn���`a ���`eunits���aoa.���`hAxisInfo���`a(���`a
���`p                ���`fmajloc���aoa=���`fticker���aoa.���`oMultipleLocator���`a(���`dbase���aoa=���`bnp���aoa.���`bpi���aoa/���bmia2���`a)���`a,���`a
���`p                ���`fmajfmt���aoa=���`fticker���aoa.���`mFuncFormatter���`a(���`frad_fn���`a)���`a,���`a
���`p                ���`elabel���aoa=���`dunit���aoa.���`hfullname���`a,���`a
���`l            ���`a)���`a
���`h        ���akdelif���`a ���`dunit���`a ���aob==���`a ���`gdegrees���`a:���`a
���`l            ���akfreturn���`a ���`eunits���aoa.���`hAxisInfo���`a(���`a
���`p                ���`fmajloc���aoa=���`fticker���aoa.���`kAutoLocator���`a(���`a)���`a,���`a
���`p                ���`fmajfmt���aoa=���`fticker���aoa.���`rFormatStrFormatter���`a(���bsaar���bs1a'���bs1a$���bsib%i���bs1a^���bs1a\���bs1ecirc$���bs1a'���`a)���`a,���`a
���`p                ���`elabel���aoa=���`dunit���aoa.���`hfullname���`a,���`a
���`l            ���`a)���`a
���`h        ���akdelif���`a ���`dunit���`a ���bowbis���`a ���bowcnot���`a ���bkcdNone���`a:���`a
���`l            ���akbif���`a ���bnbghasattr���`a(���`dunit���`a,���`a ���bs1a'���bs1hfullname���bs1a'���`a)���`a:���`a
���`p                ���akfreturn���`a ���`eunits���aoa.���`hAxisInfo���`a(���`elabel���aoa=���`dunit���aoa.���`hfullname���`a)���`a
���`l            ���akdelif���`a ���bnbghasattr���`a(���`dunit���`a,���`a ���bs1a'���bs1dunit���bs1a'���`a)���`a:���`a
���`p                ���akfreturn���`a ���`eunits���aoa.���`hAxisInfo���`a(���`elabel���aoa=���`dunit���aoa.���`dunit���aoa.���`hfullname���`a)���`a
���`h        ���akfreturn���`a ���bkcdNone���`a
���`a
���`d    ���bndm@staticmethod���`a
���`d    ���akcdef���`a ���bnfgconvert���`a(���`cval���`a,���`a ���`dunit���`a,���`a ���`daxis���`a)���`a:���`a
���`h        ���akbif���`a ���`bnp���aoa.���`hiterable���`a(���`cval���`a)���`a:���`a
���`l            ���akbif���`a ���bnbjisinstance���`a(���`cval���`a,���`a ���`bnp���aoa.���`bma���aoa.���`kMaskedArray���`a)���`a:���`a
���`p                ���`cval���`a ���aoa=���`a ���`cval���aoa.���`fastype���`a(���bnbefloat���`a)���aoa.���`ffilled���`a(���`bnp���aoa.���`cnan���`a)���`a
���`l            ���`cout���`a ���aoa=���`a ���`bnp���aoa.���`eempty���`a(���bnbclen���`a(���`cval���`a)���`a)���`a
���`l            ���akcfor���`a ���`ai���`a,���`a ���`gthisval���`a ���bowbin���`a ���bnbienumerate���`a(���`cval���`a)���`a:���`a
���`p                ���akbif���`a ���`bnp���aoa.���`bma���aoa.���`iis_masked���`a(���`gthisval���`a)���`a:���`a
���`t                    ���`cout���`a[���`ai���`a]���`a ���aoa=���`a ���`bnp���aoa.���`cnan���`a
���`p                ���akdelse���`a:���`a
���`t                    ���akctry���`a:���`a
���`x                        ���`cout���`a[���`ai���`a]���`a ���aoa=���`a ���`gthisval���aoa.���`jconvert_to���`a(���`dunit���`a)���aoa.���`iget_value���`a(���`a)���`a
���`t                    ���akfexcept���`a ���bnenAttributeError���`a:���`a
���`x                        ���`cout���`a[���`ai���`a]���`a ���aoa=���`a ���`gthisval���`a
���`l            ���akfreturn���`a ���`cout���`a
���`h        ���akbif���`a ���`bnp���aoa.���`bma���aoa.���`iis_masked���`a(���`cval���`a)���`a:���`a
���`l            ���akfreturn���`a ���`bnp���aoa.���`cnan���`a
���`h        ���akdelse���`a:���`a
���`l            ���akfreturn���`a ���`cval���aoa.���`jconvert_to���`a(���`dunit���`a)���aoa.���`iget_value���`a(���`a)���`a
���`a
���`d    ���bndm@staticmethod���`a
���`d    ���akcdef���`a ���bnfmdefault_units���`a(���`ax���`a,���`a ���`daxis���`a)���`a:���`a
���`h        ���bsdx,"""Return the default unit for x or None."""���`a
���`h        ���akbif���`a ���`bnp���aoa.���`hiterable���`a(���`ax���`a)���`a:���`a
���`l            ���akcfor���`a ���`ethisx���`a ���bowbin���`a ���`ax���`a:���`a
���`p                ���akfreturn���`a ���`ethisx���aoa.���`dunit���`a
���`h        ���akfreturn���`a ���`ax���aoa.���`dunit���`a
���`a
���`a
���akcdef���`a ���bnfccos���`a(���`ax���`a)���`a:���`a
���`d    ���akbif���`a ���`bnp���aoa.���`hiterable���`a(���`ax���`a)���`a:���`a
���`h        ���akfreturn���`a ���`a[���`dmath���aoa.���`ccos���`a(���`cval���aoa.���`jconvert_to���`a(���`gradians���`a)���aoa.���`iget_value���`a(���`a)���`a)���`a ���akcfor���`a ���`cval���`a ���bowbin���`a ���`ax���`a]���`a
���`d    ���akdelse���`a:���`a
���`h        ���akfreturn���`a ���`dmath���aoa.���`ccos���`a(���`ax���aoa.���`jconvert_to���`a(���`gradians���`a)���aoa.���`iget_value���`a(���`a)���`a)���`a
���`a
���`a
���`eunits���aoa.���`hregistry���`a[���`iBasicUnit���`a]���`a ���aoa=���`a ���`eunits���aoa.���`hregistry���`a[���`kTaggedValue���`a]���`a ���aoa=���`a ���`rBasicUnitConverter���`a(���`a)���`a
`dNone�