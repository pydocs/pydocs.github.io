����jAttributes�����pExtended Summary�����gMethods�����eNotes�����pOther Parameters�����jParameters�������aNcint��������xNumber of rows in the output.����fchunkshint, str��������x;How to chunk the array. Must be one of the following forms:��ȁ��������vA blocksize like 1000.��������xPA size in bytes, like "100 MiB" which will choose a uniform     block-like shape��������xNThe word "auto" which acts like the above, but uses a configuration     value ����parray.chunk-size���s for the chunk size����aMmint, optional��������x6Number of columns in the output. If None, defaults to ���aN�����elocalaNelocal����a.����akmint, optional��������x�Index of the diagonal: 0 (the default) refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower diagonal.����edtypesdata-type, optional��������x Data-type of the returned array.��fRaises�����hReceives�����gReturns�������aItArray of shape (N,M)��������x>An array where all elements are equal to zero, except for the ���ak�����elocalakelocal����x,-th diagonal, whose values are equal to one.��gSummary�����������xAReturn a 2-D Array with ones on the diagonal and zeros elsewhere.��hWarnings�����eWarns�����fYields������gSummaryjParametersgReturnsw/dask/array/creation.py�r<class 'function'>�ndask.array.eye������i2021.10.0���x9eye(N, chunks='auto', M=None, k=0, dtype=<class 'float'>)�wdask.array.creation.eye�