import numpy as np
from numbapro import vectorize

@vectorize(['float32(float32, float32)'], target='gpu')
def Add(a, b):
  return a + b

# Initialize arrays
A = np.ones(N, dtype=np.float32)
B = np.ones(A.shape, dtype=A.dtype)
C = np.empty_like(A, dtype=A.dtype)

# Add arrays on GPU
C = Add(A, B)
