����jAttributes�����pExtended Summary�����������x�Arrays sometimes contain invalid or missing data.  When doing operations on such arrays, we wish to suppress invalid values, which is the purpose masked arrays fulfill (an example of typical use is given below).��������x)For example, examine the following array:����x4>>> x = np.array([2, 1, 3, np.nan, 5, 2, 3, np.nan])�������xJWhen we try to calculate the mean of the data, the result is undetermined:����r>>> np.mean(x)
nan�������x%The mean is calculated using roughly ����pnp.sum(x)/len(x)���x , but since any number added to ����cNaN���k  produces ����cNaN���x*, this doesn't work.  Enter masked arrays:����x�>>> m = np.ma.masked_array(x, np.isnan(x))
>>> m
masked_array(data = [2.0 1.0 3.0 -- 5.0 2.0 3.0 --],
      mask = [False False False  True False False False  True],
      fill_value=1e+20)�������x4Here, we construct a masked array that suppress all ����cNaN���xG values.  We may now proceed to calculate the mean of the other values:����x!>>> np.mean(m)
2.6666666666666665���x^.. [1] Not-a-Number, a floating point value that is the result of an
       invalid operation.hfootnote���lmoduleauthor��������xPierre Gerard - Marchant ����lmoduleauthor��������oJarrod Millman ��gMethods�����eNotes�����pOther Parameters�����jParameters�����fRaises�����hReceives�����gReturns�����gSummary����mMasked ArrayshWarnings�����eWarns�����fYields������gSummarypExtended Summaryu/numpy/ma/__init__.py p<class 'module'>�hnumpy.ma������f1.22.3�����hnumpy.ma������������x�Arrays sometimes contain invalid or missing data.  When doing operations on such arrays, we wish to suppress invalid values, which is the purpose masked arrays fulfill (an example of typical use is given below).��������x)For example, examine the following array:����x4>>> x = np.array([2, 1, 3, np.nan, 5, 2, 3, np.nan])�������xJWhen we try to calculate the mean of the data, the result is undetermined:����r>>> np.mean(x)
nan�������x%The mean is calculated using roughly ����pnp.sum(x)/len(x)���x , but since any number added to ����cNaN���k  produces ����cNaN���x*, this doesn't work.  Enter masked arrays:����x�>>> m = np.ma.masked_array(x, np.isnan(x))
>>> m
masked_array(data = [2.0 1.0 3.0 -- 5.0 2.0 3.0 --],
      mask = [False False False  True False False False  True],
      fill_value=1e+20)�������x4Here, we construct a masked array that suppress all ����cNaN���xG values.  We may now proceed to calculate the mean of the other values:����x!>>> np.mean(m)
2.6666666666666665���x^.. [1] Not-a-Number, a floating point value that is the result of an
       invalid operation.hfootnote���lmoduleauthor��������xPierre Gerard - Marchant ����lmoduleauthor��������oJarrod Millman �mMasked Arrays