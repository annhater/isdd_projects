import numpy as np
import scipy as sc
image = np.array([[1, 0, 0, 0, 0, 1],
                   [0, 1, 1, 1, 0, 0],
                   [0, 1, 1, 1, 0, 0],
                   [1, 1, 1, 1, 1, 1],
                   [0, 0, 1, 1, 0 ,0],
                   [1, 0, 1, 1, 0, 1]])

kernel = np.array(
    [[1/9, 1/9, 1/9],
     [1/9, 1/9, 1/9],
     [1/9, 1/9, 1/9]
    ]
)

res = sc.signal.convolve2d(image, kernel, mode='valid')
print(np.count_nonzero(res == 5/9))

