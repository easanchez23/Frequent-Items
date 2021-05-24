# Frequent-Items
Uses both an exact and sampling based algorithm to calculate frequent items in a dataset.

My code can be run from the commandline as follows:

For exact.py:
python3 Exact.py threshold "filepath"
For sampling.py
python3 Sampling.py sampleSize DatasetSize failureProbability threshold "file/path"


Output should appear as follows (for Sampling.py):
0.005991664354740023.
(17, 0.54596)
(12, 0.54514)
(18, 0.54438)
(16, 0.53369)
(31, 0.51078)
(21, 0.48609)
