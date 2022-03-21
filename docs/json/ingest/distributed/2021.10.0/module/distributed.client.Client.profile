����jAttributes�����pExtended Summary�����gMethods�����eNotes�����pOther Parameters�����jParameters�������ckeycstr��������xdKey prefix to select, this is typically a function name like 'inc' Leave as None to collect all data����estartdtime����dstopdtime����gworkersdlist��������x/List of workers to restrict profile information����fserverdbool��������x�If true, return the profile of the worker's administrative thread rather than the worker threads. This is useful when profiling Dask itself, rather than user code.����ischedulerdbool��������x�If true, return the profile information from the scheduler's administrative thread rather than the workers. This is useful when profiling Dask's scheduling itself.����dplotqboolean or string��������x&Whether or not to return a plot object����hfilenamecstr��������xFilename to save the plot��fRaises�����hReceives�����gReturns�����gSummary�����������x;Collect statistical profiling information about recent work��hWarnings�����eWarns�����fYields������gSummaryjParametershExamplesv/distributed/client.py
���`���fclient���kdistributedi2021.10.0fmodulerdistributed.clientfmodule����aoa.���`���gprofile���kdistributedi2021.10.0fmodulesdistributed.profilefmodule����`a(���`hfilename���aoa=���bs1a'���bs1qdask-profile.html���bs1a'���`a)���`b  ���bc1s# save to html file`hcompiled��i2021.10.0���x�profile(self, key=None, start=None, stop=None, workers=None, merge_workers=True, plot=False, filename=None, server=False, scheduler=False)�x!distributed.client.Client.profile�